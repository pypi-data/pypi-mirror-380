from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Any, Dict, Optional, List, Iterable


@dataclass(slots=True)
class Sequence:
    name: str
    sequence: str
    id: Optional[int] = None
    project: Optional[str] = None
    group: Optional[str] = None
    date_added: Optional[datetime] = None

    @staticmethod
    def from_dict(payload: Dict[str, Any]) -> "Sequence":
        date_value = payload.get("date_added")
        parsed_date: Optional[datetime]
        if isinstance(date_value, str):
            try:
                parsed_date = datetime.fromisoformat(date_value)
            except Exception:
                parsed_date = None
        elif isinstance(date_value, datetime):
            parsed_date = date_value
        else:
            parsed_date = None

        return Sequence(
            id=payload.get("id"),
            name=payload.get("name", ""),
            sequence=payload.get("sequence", ""),
            project=payload.get("project"),
            group=payload.get("group"),
            date_added=parsed_date,
        )

    @staticmethod
    def from_orm(rec: Any) -> "Sequence":
        return Sequence(
            id=getattr(rec, "id", None),
            name=getattr(rec, "name", ""),
            sequence=getattr(rec, "sequence", ""),
            project=getattr(rec, "project", None),
            group=getattr(rec, "group", None),
            date_added=getattr(rec, "date_added", None),
        )

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "sequence": self.sequence,
            "project": self.project,
            "group": self.group,
            "date_added": self.date_added.isoformat() if self.date_added else None,
        }

    def __str__(self) -> str:
        return f"{self.name}: {self.sequence}"


# --- Plates ---


@dataclass(slots=True)
class PlateWell:
    well: str
    name: Optional[str] = None
    sequence: Optional[str] = None

    @staticmethod
    def from_dict(payload: Dict[str, Any]) -> "PlateWell":
        return PlateWell(
            well=(payload.get("well") or "").upper(),
            name=(payload.get("name") or None),
            sequence=(payload.get("sequence") or None),
        )

    @staticmethod
    def from_orm(rec: Any) -> "PlateWell":
        return PlateWell(
            well=getattr(rec, "well", "").upper(),
            name=getattr(rec, "name", None),
            sequence=getattr(rec, "sequence", None),
        )

    def to_dict(self) -> Dict[str, Any]:
        return {
            "well": (self.well or "").upper(),
            "name": self.name or "",
            "sequence": self.sequence or "",
        }


@dataclass(slots=True)
class Plate:
    name: str
    num_rows: int
    num_cols: int
    id: Optional[int] = None
    project: Optional[str] = None
    plate_type: Optional[str] = None
    is_source: Optional[bool] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    wells: Optional[List[PlateWell]] = None

    @staticmethod
    def from_dict(payload: Dict[str, Any]) -> "Plate":
        date_created = payload.get("created_at")
        date_updated = payload.get("updated_at")

        def _parse(dt: Any) -> Optional[datetime]:
            if isinstance(dt, datetime):
                return dt
            if isinstance(dt, str):
                try:
                    return datetime.fromisoformat(dt)
                except Exception:
                    return None
            return None

        wells_payload = payload.get("wells") or []
        wells_list: List[PlateWell] = [
            PlateWell.from_dict(w) for w in wells_payload if isinstance(w, dict)
        ]

        return Plate(
            id=payload.get("id"),
            name=payload.get("name", ""),
            num_rows=int(payload.get("num_rows") or 0),
            num_cols=int(payload.get("num_cols") or 0),
            project=payload.get("project"),
            plate_type=payload.get("plate_type"),
            is_source=payload.get("is_source"),
            created_at=_parse(date_created),
            updated_at=_parse(date_updated),
            wells=wells_list or None,
        )

    @staticmethod
    def from_orm(
        rec: Any, include_wells: bool = True, sort_wells: bool = True
    ) -> "Plate":
        wells_list: Optional[List[PlateWell]] = None
        try:
            if include_wells:
                wells = list(getattr(rec, "wells", []) or [])
                if sort_wells:

                    def _row_idx(code: str) -> int:
                        return ord((code or "A")[0].upper()) - ord("A")

                    def _col_idx(code: str) -> int:
                        try:
                            return int((code or "")[1:] or 0)
                        except Exception:
                            return 0

                    wells = sorted(
                        wells,
                        key=lambda w: (
                            _row_idx(getattr(w, "well", "A1")),
                            _col_idx(getattr(w, "well", "A1")),
                        ),
                    )
                wells_list = [PlateWell.from_orm(w) for w in wells]
        except Exception:
            wells_list = None

        return Plate(
            id=getattr(rec, "id", None),
            name=getattr(rec, "name", ""),
            num_rows=int(getattr(rec, "num_rows", 0) or 0),
            num_cols=int(getattr(rec, "num_cols", 0) or 0),
            project=getattr(rec, "project", None),
            plate_type=getattr(rec, "plate_type", None),
            is_source=getattr(rec, "is_source", None),
            created_at=getattr(rec, "created_at", None),
            updated_at=getattr(rec, "updated_at", None),
            wells=wells_list,
        )

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "num_rows": self.num_rows,
            "num_cols": self.num_cols,
            "project": self.project,
            "plate_type": self.plate_type,
            "is_source": self.is_source,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
            "wells": [w.to_dict() for w in (self.wells or [])],
        }

    # --- Utilities ---

    def layout_dict(self) -> Dict[str, str]:
        """
        Return a mapping from well code (e.g., "A1") to name for wells that have
        a non-empty name. Wells with no name are omitted.
        """
        mapping: Dict[str, str] = {}
        for w in self.wells or []:
            well_code = (w.well or "").upper()
            name = (w.name or "").strip()
            if well_code and name:
                mapping[well_code] = name
        return mapping

    def to_qslib(self):
        """
        Convert to a qslib PlateSetup using the grouping expected by qslib:
        keys are well names, values are lists of well positions.
        """
        try:
            from qslib import PlateSetup  # type: ignore
        except Exception as exc:  # pragma: no cover
            raise ImportError(
                "qslib is required for Plate.to_qslib(); ensure it is installed"
            ) from exc
        groups: Dict[str, list[str]] = {}
        for w in self.wells or []:
            well_code = (w.well or "").upper()
            name = (w.name or "").strip()
            if not well_code or not name:
                continue
            groups.setdefault(name, []).append(well_code)
        return PlateSetup(groups)

    def well_by_position(self, position: str) -> Optional[PlateWell]:
        """
        Return the PlateWell at the given position (e.g., "A1"), or None if unset.
        Position matching is case-insensitive and normalized to uppercase.
        """
        code = (position or "").strip().upper()
        if not code:
            return None
        for w in self.wells or []:
            if (w.well or "").upper() == code:
                # Return the first matching well
                return w
        return None

    def wells_by_positions(
        self, positions: Iterable[str]
    ) -> Dict[str, Optional[PlateWell]]:
        """
        Return a mapping from requested positions to PlateWell (or None when unset).
        Input positions are normalized to uppercase keys in the returned dict.
        """
        # Build an index for efficient lookups
        index: Dict[str, PlateWell] = {}
        for w in self.wells or []:
            key = (w.well or "").upper()
            if key and key not in index:
                index[key] = w
        result: Dict[str, Optional[PlateWell]] = {}
        for p in positions:
            key = (str(p) or "").strip().upper()
            result[key] = index.get(key)
        return result
