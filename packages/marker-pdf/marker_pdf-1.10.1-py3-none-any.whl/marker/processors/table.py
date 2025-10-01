import re
from collections import defaultdict
from copy import deepcopy
from typing import Annotated, List
from collections import Counter
from PIL import Image

from ftfy import fix_text
from surya.detection import DetectionPredictor, TextDetectionResult
from surya.recognition import RecognitionPredictor, TextLine
from surya.table_rec import TableRecPredictor
from surya.table_rec.schema import TableResult, TableCell as SuryaTableCell
from pdftext.extraction import table_output

from marker.processors import BaseProcessor
from marker.schema import BlockTypes
from marker.schema.blocks.tablecell import TableCell
from marker.schema.document import Document
from marker.schema.polygon import PolygonBox
from marker.settings import settings
from marker.util import matrix_intersection_area, unwrap_math
from marker.utils.image import is_blank_image
from marker.logger import get_logger

logger = get_logger()


class TableProcessor(BaseProcessor):
    """
    A processor for recognizing tables in the document.
    """

    block_types = (BlockTypes.Table, BlockTypes.TableOfContents, BlockTypes.Form)
    table_rec_batch_size: Annotated[
        int,
        "The batch size to use for the table recognition model.",
        "Default is None, which will use the default batch size for the model.",
    ] = None
    detection_batch_size: Annotated[
        int,
        "The batch size to use for the table detection model.",
        "Default is None, which will use the default batch size for the model.",
    ] = None
    recognition_batch_size: Annotated[
        int,
        "The batch size to use for the table recognition model.",
        "Default is None, which will use the default batch size for the model.",
    ] = None
    contained_block_types: Annotated[
        List[BlockTypes],
        "Block types to remove if they're contained inside the tables.",
    ] = (BlockTypes.Text, BlockTypes.TextInlineMath)
    row_split_threshold: Annotated[
        float,
        "The percentage of rows that need to be split across the table before row splitting is active.",
    ] = 0.5
    pdftext_workers: Annotated[
        int,
        "The number of workers to use for pdftext.",
    ] = 1
    disable_tqdm: Annotated[
        bool,
        "Whether to disable the tqdm progress bar.",
    ] = False
    drop_repeated_table_text: Annotated[bool, "Drop repeated text in OCR results."] = (
        False
    )
    filter_tag_list = ["p", "table", "td", "tr", "th", "tbody"]
    disable_ocr_math: Annotated[bool, "Disable inline math recognition in OCR"] = False
    disable_ocr: Annotated[bool, "Disable OCR entirely."] = False

    def __init__(
        self,
        recognition_model: RecognitionPredictor,
        table_rec_model: TableRecPredictor,
        detection_model: DetectionPredictor,
        config=None,
    ):
        super().__init__(config)

        self.recognition_model = recognition_model
        self.table_rec_model = table_rec_model
        self.detection_model = detection_model

    def __call__(self, document: Document):
        filepath = document.filepath  # Path to original pdf file

        table_data = []
        for page in document.pages:
            for block in page.contained_blocks(document, self.block_types):
                if block.block_type == BlockTypes.Table:
                    block.polygon = block.polygon.expand(0.01, 0.01)
                image = block.get_image(document, highres=True)
                image_poly = block.polygon.rescale(
                    (page.polygon.width, page.polygon.height),
                    page.get_image(highres=True).size,
                )

                table_data.append(
                    {
                        "block_id": block.id,
                        "page_id": page.page_id,
                        "table_image": image,
                        "table_bbox": image_poly.bbox,
                        "img_size": page.get_image(highres=True).size,
                        "ocr_block": any(
                            [
                                page.text_extraction_method in ["surya"],
                                page.ocr_errors_detected,
                            ]
                        ),
                    }
                )

        # Detect tables and cells
        self.table_rec_model.disable_tqdm = self.disable_tqdm
        tables: List[TableResult] = self.table_rec_model(
            [t["table_image"] for t in table_data],
            batch_size=self.get_table_rec_batch_size(),
        )
        assert len(tables) == len(table_data), (
            "Number of table results should match the number of tables"
        )

        # Assign cell text if we don't need OCR
        # We do this at a line level
        extract_blocks = [t for t in table_data if not t["ocr_block"]]
        self.assign_pdftext_lines(
            extract_blocks, filepath
        )  # Handle tables where good text exists in the PDF
        self.assign_text_to_cells(tables, table_data)

        # Assign OCR lines if needed - we do this at a cell level
        self.assign_ocr_lines(tables, table_data)

        self.split_combined_rows(tables)  # Split up rows that were combined
        self.combine_dollar_column(tables)  # Combine columns that are just dollar signs

        # Assign table cells to the table
        table_idx = 0
        for page in document.pages:
            for block in page.contained_blocks(document, self.block_types):
                block.structure = []  # Remove any existing lines, spans, etc.
                cells: List[SuryaTableCell] = tables[table_idx].cells
                for cell in cells:
                    # Rescale the cell polygon to the page size
                    cell_polygon = PolygonBox(polygon=cell.polygon).rescale(
                        page.get_image(highres=True).size, page.polygon.size
                    )

                    # Rescale cell polygon to be relative to the page instead of the table
                    for corner in cell_polygon.polygon:
                        corner[0] += block.polygon.bbox[0]
                        corner[1] += block.polygon.bbox[1]

                    cell_block = TableCell(
                        polygon=cell_polygon,
                        text_lines=self.finalize_cell_text(cell),
                        rowspan=cell.rowspan,
                        colspan=cell.colspan,
                        row_id=cell.row_id,
                        col_id=cell.col_id,
                        is_header=bool(cell.is_header),
                        page_id=page.page_id,
                    )
                    page.add_full_block(cell_block)
                    block.add_structure(cell_block)
                table_idx += 1

        # Clean out other blocks inside the table
        # This can happen with stray text blocks inside the table post-merging
        for page in document.pages:
            child_contained_blocks = page.contained_blocks(
                document, self.contained_block_types
            )
            for block in page.contained_blocks(document, self.block_types):
                intersections = matrix_intersection_area(
                    [c.polygon.bbox for c in child_contained_blocks],
                    [block.polygon.bbox],
                )
                for child, intersection in zip(child_contained_blocks, intersections):
                    # Adjust this to percentage of the child block that is enclosed by the table
                    intersection_pct = intersection / max(child.polygon.area, 1)
                    if intersection_pct > 0.95 and child.id in page.structure:
                        page.structure.remove(child.id)

    def finalize_cell_text(self, cell: SuryaTableCell):
        fixed_text = []
        text_lines = cell.text_lines if cell.text_lines else []
        for line in text_lines:
            text = line["text"].strip()
            if not text or text == ".":
                continue
            # Spaced sequences: ". . .", "- - -", "_ _ _", "… … …"
            text = re.sub(r"(\s?[.\-_…]){2,}", "", text)
            # Unspaced sequences: "...", "---", "___", "……"
            text = re.sub(r"[.\-_…]{2,}", "", text)
            # Remove mathbf formatting if there is only digits with decimals/commas/currency symbols inside
            text = re.sub(r"\\mathbf\{([0-9.,$€£]+)\}", r"<b>\1</b>", text)
            # Drop empty tags like \overline{}
            text = re.sub(r"\\[a-zA-Z]+\{\s*\}", "", text)
            # Drop \phantom{...} (remove contents too)
            text = re.sub(r"\\phantom\{.*?\}", "", text)
            # Drop \quad
            text = re.sub(r"\\quad", "", text)
            # Drop \,
            text = re.sub(r"\\,", "", text)
            # Unwrap \mathsf{...}
            text = re.sub(r"\\mathsf\{([^}]*)\}", r"\1", text)
            # Handle unclosed tags: keep contents, drop the command
            text = re.sub(r"\\[a-zA-Z]+\{([^}]*)$", r"\1", text)
            # If the whole string is \text{...} → unwrap
            text = re.sub(r"^\s*\\text\{([^}]*)\}\s*$", r"\1", text)

            # In case the above steps left no more latex math - We can unwrap
            text = unwrap_math(text)
            text = self.normalize_spaces(fix_text(text))
            fixed_text.append(text)
        return fixed_text

    @staticmethod
    def normalize_spaces(text):
        space_chars = [
            "\u2003",  # em space
            "\u2002",  # en space
            "\u00a0",  # non-breaking space
            "\u200b",  # zero-width space
            "\u3000",  # ideographic space
        ]
        for space in space_chars:
            text = text.replace(space, " ")
        return text

    def combine_dollar_column(self, tables: List[TableResult]):
        for table in tables:
            if len(table.cells) == 0:
                # Skip empty tables
                continue
            unique_cols = sorted(list(set([c.col_id for c in table.cells])))
            max_col = max(unique_cols)
            dollar_cols = []
            for col in unique_cols:
                # Cells in this col
                col_cells = [c for c in table.cells if c.col_id == col]
                col_text = [
                    "\n".join(self.finalize_cell_text(c)).strip() for c in col_cells
                ]
                all_dollars = all([ct in ["", "$"] for ct in col_text])
                colspans = [c.colspan for c in col_cells]
                span_into_col = [
                    c
                    for c in table.cells
                    if c.col_id != col and c.col_id + c.colspan > col > c.col_id
                ]

                # This is a column that is entirely dollar signs
                if all(
                    [
                        all_dollars,
                        len(col_cells) > 1,
                        len(span_into_col) == 0,
                        all([c == 1 for c in colspans]),
                        col < max_col,
                    ]
                ):
                    next_col_cells = [c for c in table.cells if c.col_id == col + 1]
                    next_col_rows = [c.row_id for c in next_col_cells]
                    col_rows = [c.row_id for c in col_cells]
                    if (
                        len(next_col_cells) == len(col_cells)
                        and next_col_rows == col_rows
                    ):
                        dollar_cols.append(col)

            if len(dollar_cols) == 0:
                continue

            dollar_cols = sorted(dollar_cols)
            col_offset = 0
            for col in unique_cols:
                col_cells = [c for c in table.cells if c.col_id == col]
                if col_offset == 0 and col not in dollar_cols:
                    continue

                if col in dollar_cols:
                    col_offset += 1
                    for cell in col_cells:
                        text_lines = cell.text_lines if cell.text_lines else []
                        next_row_col = [
                            c
                            for c in table.cells
                            if c.row_id == cell.row_id and c.col_id == col + 1
                        ]

                        # Add dollar to start of the next column
                        next_text_lines = (
                            next_row_col[0].text_lines
                            if next_row_col[0].text_lines
                            else []
                        )
                        next_row_col[0].text_lines = deepcopy(text_lines) + deepcopy(
                            next_text_lines
                        )
                        table.cells = [
                            c for c in table.cells if c.cell_id != cell.cell_id
                        ]  # Remove original cell
                        next_row_col[0].col_id -= col_offset
                else:
                    for cell in col_cells:
                        cell.col_id -= col_offset

    def split_combined_rows(self, tables: List[TableResult]):
        for table in tables:
            if len(table.cells) == 0:
                # Skip empty tables
                continue
            unique_rows = sorted(list(set([c.row_id for c in table.cells])))
            row_info = []
            for row in unique_rows:
                # Cells in this row
                # Deepcopy is because we do an in-place mutation later, and that can cause rows to shift to match rows in unique_rows
                # making them be processed twice
                row_cells = deepcopy([c for c in table.cells if c.row_id == row])
                rowspans = [c.rowspan for c in row_cells]
                line_lens = [
                    len(c.text_lines) if isinstance(c.text_lines, list) else 1
                    for c in row_cells
                ]

                # Other cells that span into this row
                rowspan_cells = [
                    c
                    for c in table.cells
                    if c.row_id != row and c.row_id + c.rowspan > row > c.row_id
                ]
                should_split_entire_row = all(
                    [
                        len(row_cells) > 1,
                        len(rowspan_cells) == 0,
                        all([rowspan == 1 for rowspan in rowspans]),
                        all([line_len > 1 for line_len in line_lens]),
                        all([line_len == line_lens[0] for line_len in line_lens]),
                    ]
                )
                line_lens_counter = Counter(line_lens)
                counter_keys = sorted(list(line_lens_counter.keys()))
                should_split_partial_row = all(
                    [
                        len(row_cells) > 3,  # Only split if there are more than 3 cells
                        len(rowspan_cells) == 0,
                        all([r == 1 for r in rowspans]),
                        len(line_lens_counter) == 2
                        and counter_keys[0] <= 1
                        and counter_keys[1] > 1
                        and line_lens_counter[counter_keys[0]]
                        == 1,  # Allow a single column with a single line - keys are the line lens, values are the counts
                    ]
                )
                should_split = should_split_entire_row or should_split_partial_row
                row_info.append(
                    {
                        "should_split": should_split,
                        "row_cells": row_cells,
                        "line_lens": line_lens,
                    }
                )

            # Don't split if we're not splitting most of the rows in the table.  This avoids splitting stray multiline rows.
            if (
                sum([r["should_split"] for r in row_info]) / len(row_info)
                < self.row_split_threshold
            ):
                continue

            new_cells = []
            shift_up = 0
            max_cell_id = max([c.cell_id for c in table.cells])
            new_cell_count = 0
            for row, item_info in zip(unique_rows, row_info):
                max_lines = max(item_info["line_lens"])
                if item_info["should_split"]:
                    for i in range(0, max_lines):
                        for cell in item_info["row_cells"]:
                            # Calculate height based on number of splits
                            split_height = cell.bbox[3] - cell.bbox[1]
                            current_bbox = [
                                cell.bbox[0],
                                cell.bbox[1] + i * split_height,
                                cell.bbox[2],
                                cell.bbox[1] + (i + 1) * split_height,
                            ]

                            line = (
                                [cell.text_lines[i]]
                                if cell.text_lines and i < len(cell.text_lines)
                                else None
                            )
                            cell_id = max_cell_id + new_cell_count
                            new_cells.append(
                                SuryaTableCell(
                                    polygon=current_bbox,
                                    text_lines=line,
                                    rowspan=1,
                                    colspan=cell.colspan,
                                    row_id=cell.row_id + shift_up + i,
                                    col_id=cell.col_id,
                                    is_header=cell.is_header
                                    and i == 0,  # Only first line is header
                                    within_row_id=cell.within_row_id,
                                    cell_id=cell_id,
                                )
                            )
                            new_cell_count += 1

                    # For each new row we add, shift up subsequent rows
                    # The max is to account for partial rows
                    shift_up += max_lines - 1
                else:
                    for cell in item_info["row_cells"]:
                        cell.row_id += shift_up
                        new_cells.append(cell)

            # Only update the cells if we added new cells
            if len(new_cells) > len(table.cells):
                table.cells = new_cells

    def assign_text_to_cells(self, tables: List[TableResult], table_data: list):
        for table_result, table_page_data in zip(tables, table_data):
            if table_page_data["ocr_block"]:
                continue

            table_text_lines = table_page_data["table_text_lines"]
            table_cells: List[SuryaTableCell] = table_result.cells
            text_line_bboxes = [t["bbox"] for t in table_text_lines]
            table_cell_bboxes = [c.bbox for c in table_cells]

            intersection_matrix = matrix_intersection_area(
                text_line_bboxes, table_cell_bboxes
            )

            cell_text = defaultdict(list)
            for text_line_idx, table_text_line in enumerate(table_text_lines):
                intersections = intersection_matrix[text_line_idx]
                if intersections.sum() == 0:
                    continue

                max_intersection = intersections.argmax()
                cell_text[max_intersection].append(table_text_line)

            for k in cell_text:
                # TODO: see if the text needs to be sorted (based on rotation)
                text = cell_text[k]
                assert all("text" in t for t in text), "All text lines must have text"
                assert all("bbox" in t for t in text), "All text lines must have a bbox"
                table_cells[k].text_lines = text

    def assign_pdftext_lines(self, extract_blocks: list, filepath: str):
        table_inputs = []
        unique_pages = list(set([t["page_id"] for t in extract_blocks]))
        if len(unique_pages) == 0:
            return

        for page in unique_pages:
            tables = []
            img_size = None
            for block in extract_blocks:
                if block["page_id"] == page:
                    tables.append(block["table_bbox"])
                    img_size = block["img_size"]

            table_inputs.append({"tables": tables, "img_size": img_size})
        cell_text = table_output(
            filepath,
            table_inputs,
            page_range=unique_pages,
            workers=self.pdftext_workers,
        )
        assert len(cell_text) == len(unique_pages), (
            "Number of pages and table inputs must match"
        )

        for pidx, (page_tables, pnum) in enumerate(zip(cell_text, unique_pages)):
            table_idx = 0
            for block in extract_blocks:
                if block["page_id"] == pnum:
                    table_text = page_tables[table_idx]
                    if len(table_text) == 0:
                        block["ocr_block"] = (
                            True  # Re-OCR the block if pdftext didn't find any text
                        )
                    else:
                        block["table_text_lines"] = page_tables[table_idx]
                    table_idx += 1
            assert table_idx == len(page_tables), (
                "Number of tables and table inputs must match"
            )

    def align_table_cells(
        self, table: TableResult, table_detection_result: TextDetectionResult
    ):
        table_cells = table.cells
        table_text_lines = table_detection_result.bboxes

        text_line_bboxes = [t.bbox for t in table_text_lines]
        table_cell_bboxes = [c.bbox for c in table_cells]

        intersection_matrix = matrix_intersection_area(
            text_line_bboxes, table_cell_bboxes
        )

        # Map cells -> list of assigned text lines
        cell_text = defaultdict(list)
        for text_line_idx, table_text_line in enumerate(table_text_lines):
            intersections = intersection_matrix[text_line_idx]
            if intersections.sum() == 0:
                continue
            max_intersection = intersections.argmax()
            cell_text[max_intersection].append(table_text_line)

        # Adjust cell polygons in place
        for cell_idx, cell in enumerate(table_cells):
            # all intersecting lines
            intersecting_line_indices = [
                i for i, area in enumerate(intersection_matrix[:, cell_idx]) if area > 0
            ]
            if not intersecting_line_indices:
                continue

            assigned_lines = cell_text.get(cell_idx, [])
            # Expand to fit assigned lines - **Only in the y direction**
            for assigned_line in assigned_lines:
                x1 = cell.bbox[0]
                x2 = cell.bbox[2]
                y1 = min(cell.bbox[1], assigned_line.bbox[1])
                y2 = max(cell.bbox[3], assigned_line.bbox[3])
                cell.polygon = [[x1, y1], [x2, y1], [x2, y2], [x1, y2]]

            # Clear out non-assigned lines
            non_assigned_lines = [
                table_text_lines[i]
                for i in intersecting_line_indices
                if table_text_lines[i] not in cell_text.get(cell_idx, [])
            ]
            if non_assigned_lines:
                # Find top-most and bottom-most non-assigned boxes
                top_box = min(
                    non_assigned_lines, key=lambda line: line.bbox[1]
                )  # smallest y0
                bottom_box = max(
                    non_assigned_lines, key=lambda line: line.bbox[3]
                )  # largest y1

                # Current cell bbox (from polygon)
                x0, y0, x1, y1 = cell.bbox

                # Adjust y-limits based on non-assigned boxes
                new_y0 = max(y0, top_box.bbox[3])  # top moves down
                new_y1 = min(y1, bottom_box.bbox[1])  # bottom moves up

                if new_y0 < new_y1:
                    # Replace polygon with a new shrunken rectangle
                    cell.polygon = [
                        [x0, new_y0],
                        [x1, new_y0],
                        [x1, new_y1],
                        [x0, new_y1],
                    ]

    def needs_ocr(self, tables: List[TableResult], table_blocks: List[dict]):
        ocr_tables = []
        ocr_idxs = []
        for j, (table_result, table_block) in enumerate(zip(tables, table_blocks)):
            table_cells: List[SuryaTableCell] = table_result.cells
            text_lines_need_ocr = any([tc.text_lines is None for tc in table_cells])
            if (
                table_block["ocr_block"]
                and text_lines_need_ocr
                and not self.disable_ocr
            ):
                logger.debug(
                    f"Table {j} needs OCR, info table block needs ocr: {table_block['ocr_block']}, text_lines {text_lines_need_ocr}"
                )
                ocr_tables.append(table_result)
                ocr_idxs.append(j)

        detection_results: List[TextDetectionResult] = self.detection_model(
            images=[table_blocks[i]["table_image"] for i in ocr_idxs],
            batch_size=self.get_detection_batch_size(),
        )
        assert len(detection_results) == len(ocr_idxs), (
            "Every OCRed table requires a text detection result"
        )

        for idx, table_detection_result in zip(ocr_idxs, detection_results):
            self.align_table_cells(tables[idx], table_detection_result)

        ocr_polys = []
        for ocr_idx in ocr_idxs:
            table_cells = tables[ocr_idx].cells
            polys = [tc for tc in table_cells if tc.text_lines is None]
            ocr_polys.append(polys)
        return ocr_tables, ocr_polys, ocr_idxs

    def get_ocr_results(
        self, table_images: List[Image.Image], ocr_polys: List[List[SuryaTableCell]]
    ):
        ocr_polys_bad = []

        for table_image, polys in zip(table_images, ocr_polys):
            table_polys_bad = [
                any(
                    [
                        poly.height < 6,
                        is_blank_image(table_image.crop(poly.bbox), poly.polygon),
                    ]
                )
                for poly in polys
            ]
            ocr_polys_bad.append(table_polys_bad)

        filtered_polys = []
        for table_polys, table_polys_bad in zip(ocr_polys, ocr_polys_bad):
            filtered_table_polys = []
            for p, is_bad in zip(table_polys, table_polys_bad):
                if is_bad:
                    continue
                polygon = p.polygon
                # Round the polygon
                for corner in polygon:
                    for i in range(2):
                        corner[i] = int(corner[i])

                filtered_table_polys.append(polygon)
            filtered_polys.append(filtered_table_polys)

        ocr_results = self.recognition_model(
            images=table_images,
            task_names=["ocr_with_boxes"] * len(table_images),
            recognition_batch_size=self.get_recognition_batch_size(),
            drop_repeated_text=self.drop_repeated_table_text,
            polygons=filtered_polys,
            filter_tag_list=self.filter_tag_list,
            max_tokens=2048,
            max_sliding_window=2148,
            math_mode=not self.disable_ocr_math,
        )

        # Re-align the predictions to the original length, since we skipped some predictions
        for table_ocr_result, table_polys_bad in zip(ocr_results, ocr_polys_bad):
            updated_lines = []
            idx = 0
            for is_bad in table_polys_bad:
                if is_bad:
                    updated_lines.append(
                        TextLine(
                            text="",
                            polygon=[[0, 0], [0, 0], [0, 0], [0, 0]],
                            confidence=1,
                            chars=[],
                            original_text_good=False,
                            words=None,
                        )
                    )
                else:
                    updated_lines.append(table_ocr_result.text_lines[idx])
                    idx += 1
            table_ocr_result.text_lines = updated_lines

        return ocr_results

    def assign_ocr_lines(self, tables: List[TableResult], table_blocks: list):
        ocr_tables, ocr_polys, ocr_idxs = self.needs_ocr(tables, table_blocks)
        det_images = [
            t["table_image"] for i, t in enumerate(table_blocks) if i in ocr_idxs
        ]
        assert len(det_images) == len(ocr_polys), (
            f"Number of detection images and OCR polygons must match: {len(det_images)} != {len(ocr_polys)}"
        )
        self.recognition_model.disable_tqdm = self.disable_tqdm
        ocr_results = self.get_ocr_results(table_images=det_images, ocr_polys=ocr_polys)

        for result, ocr_res in zip(ocr_tables, ocr_results):
            table_cells: List[SuryaTableCell] = result.cells
            cells_need_text = [tc for tc in table_cells if tc.text_lines is None]

            assert len(cells_need_text) == len(ocr_res.text_lines), (
                "Number of cells needing text and OCR results must match"
            )

            for cell_text, cell_needs_text in zip(ocr_res.text_lines, cells_need_text):
                # Don't need to correct back to image size
                # Table rec boxes are relative to the table
                cell_text_lines = [{"text": t} for t in cell_text.text.split("<br>")]
                cell_needs_text.text_lines = cell_text_lines

    def get_table_rec_batch_size(self):
        if self.table_rec_batch_size is not None:
            return self.table_rec_batch_size
        elif settings.TORCH_DEVICE_MODEL == "mps":
            return 6
        elif settings.TORCH_DEVICE_MODEL == "cuda":
            return 14
        return 6

    def get_recognition_batch_size(self):
        if self.recognition_batch_size is not None:
            return self.recognition_batch_size
        elif settings.TORCH_DEVICE_MODEL == "mps":
            return 32
        elif settings.TORCH_DEVICE_MODEL == "cuda":
            return 48
        return 32

    def get_detection_batch_size(self):
        if self.detection_batch_size is not None:
            return self.detection_batch_size
        elif settings.TORCH_DEVICE_MODEL == "cuda":
            return 10
        return 4
