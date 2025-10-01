from __future__ import annotations

from typing import Iterable, List, Dict, Any, Sequence as TypingSequence

import io
import importlib

from .models import Sequence, Plate, PlateWell


def _rows_from_sequences(records: Iterable[Sequence]) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    for r in records:
        rows.append(
            {
                "Name": r.name or "",
                "Sequence": r.sequence or "",
                "Project": r.project or "",
                "Group": r.group or "",
            }
        )
    return rows


def export_sequences_to_csv(
    records: Iterable[Sequence], *, only_name_sequence: bool = False
) -> bytes:
    pd = importlib.import_module("pandas")
    rows = _rows_from_sequences(records)
    df = pd.DataFrame(rows)
    columns = (
        ["Name", "Sequence"]
        if only_name_sequence
        else [
            "Name",
            "Sequence",
            "Project",
            "Group",
        ]
    )
    df = df.loc[:, columns]
    buf = io.StringIO()
    df.to_csv(buf, index=False)
    return buf.getvalue().encode("utf-8")


def export_sequences_to_xlsx(
    records: Iterable[Sequence],
    *,
    only_name_sequence: bool = False,
    sheet_name: str = "sequences",
) -> bytes:
    pd = importlib.import_module("pandas")
    rows = _rows_from_sequences(records)
    df = pd.DataFrame(rows)
    columns = (
        ["Name", "Sequence"]
        if only_name_sequence
        else [
            "Name",
            "Sequence",
            "Project",
            "Group",
        ]
    )
    df = df.loc[:, columns]
    bufb = io.BytesIO()
    with pd.ExcelWriter(bufb, engine="openpyxl") as writer:
        df.to_excel(writer, index=False, sheet_name=sheet_name)
        ws = writer.sheets.get(sheet_name)
        if ws is not None:
            styles = importlib.import_module("openpyxl.styles")
            Alignment = getattr(styles, "Alignment")
            for row in ws.iter_rows(
                min_row=1, max_row=ws.max_row, min_col=1, max_col=ws.max_column
            ):
                for cell in row:
                    cell.alignment = Alignment(horizontal="left")
    return bufb.getvalue()


def _rows_from_plate(plate: Plate) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    for w in plate.wells or []:
        rows.append(
            {
                "Well Position": (w.well or "").upper(),
                "Name": w.name or "",
                "Sequence": w.sequence or "",
            }
        )
    return rows


def export_plates_to_xlsx(
    plates: TypingSequence[Plate] | Plate,
) -> bytes:
    """
    Export one or many Plate objects to an XLSX workbook.

    - One worksheet per plate
    - Worksheet name = plate.name (falls back to "Plate" if blank)
    - Columns: Well Position, Name, Sequence
    """
    pd = importlib.import_module("pandas")
    bufb = io.BytesIO()

    # Normalize input to list
    plate_list: List[Plate] = [plates] if isinstance(plates, Plate) else list(plates)

    if not plate_list:
        # Create an empty workbook
        with pd.ExcelWriter(bufb, engine="openpyxl"):
            pass
        return bufb.getvalue()

    with pd.ExcelWriter(bufb, engine="openpyxl") as writer:
        for p in plate_list:
            sheet = (p.name or "Plate")[:31]  # Excel sheet name limit
            df = pd.DataFrame(_rows_from_plate(p))
            # Ensure consistent column order even if no rows
            if df.empty:
                df = pd.DataFrame(columns=["Well Position", "Name", "Sequence"])
            else:
                df = df.loc[:, ["Well Position", "Name", "Sequence"]]
            df.to_excel(writer, index=False, sheet_name=sheet)

            # Basic formatting: left align only; also clear default header bold/border
            ws = writer.sheets.get(sheet)
            if ws is not None:
                styles = importlib.import_module("openpyxl.styles")
                Alignment = getattr(styles, "Alignment")
                Font = getattr(styles, "Font")
                Border = getattr(styles, "Border")
                for row in ws.iter_rows(
                    min_row=1, max_row=ws.max_row, min_col=1, max_col=ws.max_column
                ):
                    for cell in row:
                        cell.alignment = Alignment(horizontal="left")
                try:
                    for cell in ws[1]:
                        cell.font = Font(bold=False)
                        cell.border = Border()
                except Exception:
                    pass

    return bufb.getvalue()
