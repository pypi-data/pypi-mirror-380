from __future__ import annotations

from typing import Dict, Iterable, List, Mapping, Optional
from collections import OrderedDict

import pandas as pd
from .models import Sequence, Plate, PlateWell


def _normalize_columns(columns: Iterable[str]) -> Dict[str, str]:
    """
    Build a mapping of lowercased/stripped column names to the original names.

    This lets us match columns case-insensitively while still using
    the original column names to access DataFrame data safely.
    """
    normalized: Dict[str, str] = {}
    for col in columns:
        key = str(col).strip().lower()
        if key and key not in normalized:
            normalized[key] = col
    return normalized


def _resolve_key(
    normalized_map: Mapping[str, str],
    desired_keys: Iterable[str],
) -> Optional[str]:
    """
    From a normalized column map, find the first existing column matching any of
    the provided desired keys (case/space-insensitive). Returns the original
    column name if found, otherwise None.
    """
    for key in desired_keys:
        norm = key.strip().lower()
        if norm in normalized_map:
            return normalized_map[norm]
    return None


def parse_sequences_from_csv(
    path: str,
    *,
    name_keys: Iterable[str] | None = None,
    sequence_keys: Iterable[str] | None = None,
    pandas_read_csv_kwargs: Optional[Dict] = None,
) -> List[Sequence]:
    """
    Parse sequences from a CSV file. Assumes there are columns for name and sequence,
    but matches column names case-insensitively and allows custom key aliases.

    - Returns: list of Sequence objects (rows with non-empty sequence values)
    - name_keys: aliases to recognize the name column (default: ["name"])
    - sequence_keys: aliases for the sequence column (default: ["sequence", "seq"])
    - pandas_read_csv_kwargs: forwarded to pandas.read_csv for flexibility
    """
    if name_keys is None:
        name_keys = ["name"]
    if sequence_keys is None:
        sequence_keys = ["sequence", "seq"]
    if pandas_read_csv_kwargs is None:
        pandas_read_csv_kwargs = {}

    df = pd.read_csv(path, **pandas_read_csv_kwargs)

    norm = _normalize_columns(df.columns)
    name_col = _resolve_key(norm, name_keys)
    seq_col = _resolve_key(norm, sequence_keys)

    if seq_col is None:
        # If no sequence column, nothing to return
        return []

    # Filter rows with non-null, non-empty sequences and build Sequence objects
    results: List[Sequence] = []
    for _, row in df.iterrows():
        seq_val = row.get(seq_col)
        if isinstance(seq_val, str):
            seq_str = seq_val.strip()
        elif bool(pd.notna(seq_val)):
            seq_str = str(seq_val).strip()
        else:
            seq_str = ""
        if not seq_str:
            continue

        name_str = ""
        if name_col is not None:
            name_val = row.get(name_col)
            if isinstance(name_val, str):
                name_str = name_val.strip()
            elif bool(pd.notna(name_val)):
                name_str = str(name_val).strip()

        results.append(Sequence(name=name_str, sequence=seq_str))

    return results


def parse_sequences_from_excel(
    path: str,
    *,
    name_keys: Iterable[str] | None = None,
    sequence_keys: Iterable[str] | None = None,
    sheet_name: str | int | None = None,
    pandas_read_excel_kwargs: Optional[Dict] = None,
) -> Dict[str, List[Sequence]]:
    """
    Parse sequences from an Excel file (XLS/XLSX).

    - Returns: dict mapping sheet name -> list of Sequence objects
    - name_keys: aliases to recognize the name column (default: ["name"])
    - sequence_keys: aliases for the sequence column (default: ["sequence", "seq"])
    - sheet_name: passed to pandas.read_excel; None means all sheets
    - pandas_read_excel_kwargs: forwarded to pandas.read_excel
    """
    if name_keys is None:
        name_keys = ["name"]
    if sequence_keys is None:
        sequence_keys = ["sequence", "seq"]
    if pandas_read_excel_kwargs is None:
        pandas_read_excel_kwargs = {}

    # Read all sheets by default
    if sheet_name is None:
        pandas_read_excel_kwargs.setdefault("sheet_name", None)  # all sheets
    else:
        pandas_read_excel_kwargs.setdefault("sheet_name", sheet_name)

    xls = pd.read_excel(path, **pandas_read_excel_kwargs)

    # pandas returns a dict when sheet_name=None or a single DataFrame otherwise
    if isinstance(xls, dict):
        sheets = xls
    else:
        # Single sheet, synthesize a name
        sheets = {str(sheet_name if sheet_name is not None else "Sheet1"): xls}

    result: Dict[str, List[Sequence]] = {}
    for sheet, df in sheets.items():
        # Skip empty frames
        if df is None or df.empty:
            result[str(sheet)] = []
            continue

        norm = _normalize_columns(df.columns)
        name_col = _resolve_key(norm, name_keys)
        seq_col = _resolve_key(norm, sequence_keys)
        if seq_col is None:
            result[str(sheet)] = []
            continue

        seqs: List[Sequence] = []
        for _, row in df.iterrows():
            seq_val = row.get(seq_col)
            if isinstance(seq_val, str):
                seq_str = seq_val.strip()
            elif bool(pd.notna(seq_val)):
                seq_str = str(seq_val).strip()
            else:
                seq_str = ""
            if not seq_str:
                continue
            name_str = ""
            if name_col is not None:
                name_val = row.get(name_col)
                if isinstance(name_val, str):
                    name_str = name_val.strip()
                elif bool(pd.notna(name_val)):
                    name_str = str(name_val).strip()
            seqs.append(Sequence(name=name_str, sequence=seq_str))

        result[str(sheet)] = seqs

    return result


def _parse_well_code(raw: object) -> tuple[int, int]:
    """
    Parse a well code like "A1" or "b12" into row (1-based) and column (int).
    Returns (0, 0) when parsing fails.
    """
    try:
        if raw is None:
            return 0, 0
        s = str(raw).strip()
        if not s:
            return 0, 0
        # Split into leading letters and trailing digits
        i = 0
        while i < len(s) and s[i].isalpha():
            i += 1
        letters = s[:i].upper()
        digits = s[i:]
        if not letters or not digits or not digits.isdigit():
            return 0, 0
        # Only the first letter is used for row index (A=1)
        row = (ord(letters[0]) - ord("A")) + 1
        col = int(digits)
        return (row if row > 0 else 0), (col if col > 0 else 0)
    except Exception:
        return 0, 0


def parse_plates_from_excel(
    path: str,
    *,
    well_keys: Iterable[str] | None = None,
    name_keys: Iterable[str] | None = None,
    sequence_keys: Iterable[str] | None = None,
    sheet_name: str | int | None = None,
    pandas_read_excel_kwargs: Optional[Dict] = None,
) -> OrderedDict[str, Plate]:
    """
    Parse plate layouts from an Excel (xls/xlsx) workbook.

    - Each sheet becomes a Plate where the plate name is the sheet name
    - Default expected columns (case-insensitive):
        well_keys: ["Well Position", "well", "well id", "well_position"]
        name_keys: ["Name"]
        sequence_keys: ["Sequence", "Seq"]
    - Rows where both name and sequence are empty are ignored
    - Sheets that don't contain a well column or any of the name/sequence
      columns are ignored

    Returns a dict mapping { sheet_name: Plate }
    """
    if well_keys is None:
        well_keys = ["well position", "well", "well id", "well_position"]
    if name_keys is None:
        name_keys = ["name"]
    if sequence_keys is None:
        sequence_keys = ["sequence", "seq"]
    if pandas_read_excel_kwargs is None:
        pandas_read_excel_kwargs = {}

    # Read desired sheets (default all)
    if sheet_name is None:
        pandas_read_excel_kwargs.setdefault("sheet_name", None)
    else:
        pandas_read_excel_kwargs.setdefault("sheet_name", sheet_name)

    xls = pd.read_excel(path, **pandas_read_excel_kwargs)

    # Build an ordered mapping of sheet name -> DataFrame, preserving Excel order
    if isinstance(xls, dict):
        sheets: OrderedDict[str, pd.DataFrame] = OrderedDict(xls)
    else:
        sheets = OrderedDict(
            [(str(sheet_name if sheet_name is not None else "Sheet1"), xls)]
        )

    # Preserve insertion order of sheets in the returned mapping
    result: OrderedDict[str, Plate] = OrderedDict()
    for sheet, df in sheets.items():
        if df is None or df.empty:
            continue

        norm = _normalize_columns(df.columns)
        well_col = _resolve_key(norm, well_keys)
        name_col = _resolve_key(norm, name_keys)
        seq_col = _resolve_key(norm, sequence_keys)

        # Require wells, and at least one of name/sequence to be present
        if not well_col or (not name_col and not seq_col):
            continue

        wells: List[PlateWell] = []
        max_row = 0
        max_col = 0

        for _, row in df.iterrows():
            well_raw = row.get(well_col)
            r_idx, c_idx = _parse_well_code(well_raw)
            if r_idx <= 0 or c_idx <= 0:
                continue

            nm = ""
            if name_col is not None:
                v = row.get(name_col)
                if isinstance(v, str):
                    nm = v.strip()
                elif bool(pd.notna(v)):
                    nm = str(v).strip()

            seq = ""
            if seq_col is not None:
                v = row.get(seq_col)
                if isinstance(v, str):
                    seq = v.strip()
                elif bool(pd.notna(v)):
                    seq = str(v).strip()

            # Skip rows with no data
            if not nm and not seq:
                continue

            code = f"{chr(ord('A') + (r_idx - 1))}{c_idx}"
            wells.append(
                PlateWell(well=code.upper(), name=nm or None, sequence=seq or None)
            )
            max_row = max(max_row, r_idx)
            max_col = max(max_col, c_idx)

        if not wells:
            # Nothing meaningful on this sheet
            continue

        plate = Plate(
            name=str(sheet),
            num_rows=max_row,
            num_cols=max_col,
            wells=wells,
        )
        result[str(sheet)] = plate

    return result
