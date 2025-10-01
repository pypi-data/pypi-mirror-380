from __future__ import annotations

from typing import Any, Dict, List, Optional, Iterable

# pyright: reportMissingTypeStubs=false
import requests

from .models import Sequence, Plate


class MajorGroove:
    """
    Simple client for the MajorGroove API.

    Example:
        mg = MajorGroove(base_url="https://your-host", token="...")
        rows = mg.get_sequences(name="M13", project="SDC")
    """

    def __init__(
        self,
        host: str = "127.0.0.1",  # hostname or full URL
        port: int = 5002,
        scheme: str = "http",
        session: requests.Session | None = None,
    ):
        self.base_url = (
            host.rstrip("/")
            if "://" in host
            else f"{scheme}://{host.rstrip('/')}:{port}"
        )
        self.port = port
        self._session = session or requests.Session()

    def _headers(self) -> Dict[str, str]:
        # Token auth removed; keep method for potential future headers
        headers: Dict[str, str] = {}
        return headers

    def _raise_for_status_with_context(self, resp: requests.Response) -> None:
        try:
            resp.raise_for_status()
        except requests.HTTPError:
            try:
                content = resp.json()
            except Exception:
                content = resp.text
            print(
                f"[MajorGroove] HTTP {resp.status_code} for {getattr(resp.request, 'method', 'REQUEST')} {resp.url}"
            )
            print(content)
            # For 400-level validation errors, raise a ValueError with details
            if resp.status_code == 400:
                message = "Bad Request"
                if isinstance(content, dict):
                    base = content.get("error") or content.get("message")
                    details = content.get("details")
                    if base:
                        message = base
                    if isinstance(details, list) and details:
                        # Format details compactly: [index] code: error
                        parts: list[str] = []
                        for d in details:
                            try:
                                idx = d.get("index")
                                code = d.get("code")
                                err = d.get("error")
                                prefix = f"[{idx}] " if idx is not None else ""
                                mid = f"{code}: " if code else ""
                                parts.append(f"{prefix}{mid}{err}")
                            except Exception:
                                parts.append(str(d))
                        if parts:
                            message = f"{message}; details: " + "; ".join(parts)
                else:
                    # Non-JSON body
                    message = f"Bad Request: {content}"
                raise ValueError(message)
            # otherwise, re-raise the original HTTP error
            raise

    def get_sequences(
        self,
        *,
        name: Optional[str] = None,
        project: Optional[str] = None,
        group: Optional[str] = None,
        timeout: float = 10.0,
    ) -> List[Sequence]:
        params: Dict[str, str] = {}
        if name:
            params["name"] = name
        if project:
            params["project"] = project
        if group:
            params["group"] = group

        url = f"{self.base_url}/api/sequences"
        resp = self._session.get(
            url, headers=self._headers(), params=params, timeout=timeout
        )
        self._raise_for_status_with_context(resp)
        data = resp.json()
        if not isinstance(data, list):
            raise ValueError(
                "Unexpected response shape from /api/sequences; expected a JSON list"
            )

        return [Sequence.from_dict(d) for d in data]

    def get_sequence(
        self,
        *,
        name: Optional[str] = None,
        project: Optional[str] = None,
        group: Optional[str] = None,
        timeout: float = 10.0,
    ) -> Sequence:
        results = self.get_sequences(
            name=name,
            project=project,
            group=group,
            timeout=timeout,
        )
        if len(results) == 0:
            raise ValueError("No sequence found")
        if len(results) > 1:
            raise ValueError(
                "More than one sequence found, use get_sequences for details"
            )
        return results[0]

    def set_sequences(
        self,
        rows: Iterable[Sequence | Dict[str, Any]],
        *,
        overwrite: bool = False,
        project_all: Optional[str] = None,
        group_all: Optional[str] = None,
        timeout: float = 10.0,
    ) -> Dict[str, Any]:
        payload_rows: List[Dict[str, Any]] = []
        for row in rows:
            if isinstance(row, Sequence):
                payload_rows.append(row.to_dict())
            else:
                payload_rows.append(dict(row))
        payload: Dict[str, Any] = {"overwrite": overwrite, "rows": payload_rows}
        if project_all is not None:
            payload["project_all"] = project_all
        if group_all is not None:
            payload["group_all"] = group_all
        url = f"{self.base_url}/api/sequences"
        resp = self._session.put(
            url, headers=self._headers(), json=payload, timeout=timeout
        )
        self._raise_for_status_with_context(resp)
        return resp.json()

    # --- Plates ---

    def get_plates(
        self,
        *,
        name: Optional[str] = None,
        projects: Optional[Iterable[str] | str] = None,
        timeout: float = 10.0,
    ) -> List[Plate]:
        # Build query parameters; support multiple project filters
        params_list: List[tuple[str, str]] = []
        if name:
            params_list.append(("name", name))
        if projects:
            if isinstance(projects, str):
                if projects.strip():
                    params_list.append(("project", projects))
            else:
                for p in projects:
                    if p and str(p).strip():
                        params_list.append(("project", str(p)))

        url = f"{self.base_url}/api/plates"
        resp = self._session.get(
            url, headers=self._headers(), params=params_list or None, timeout=timeout
        )
        self._raise_for_status_with_context(resp)
        data = resp.json()
        if not isinstance(data, list):
            raise ValueError(
                "Unexpected response shape from /api/plates; expected a JSON list"
            )
        return [Plate.from_dict(d) for d in data]

    def get_plate(
        self,
        *,
        id: Optional[int] = None,
        name: Optional[str] = None,
        projects: Optional[Iterable[str] | str] = None,
        timeout: float = 10.0,
    ) -> Plate:
        # Prefer direct fetch by id when provided
        if id is not None:
            url = f"{self.base_url}/api/plates/{id}"
            resp = self._session.get(url, headers=self._headers(), timeout=timeout)
            if resp.status_code == 404:
                raise ValueError("No plate found")
            self._raise_for_status_with_context(resp)
            data = resp.json()
            if isinstance(data, dict):
                return Plate.from_dict(data)
            if isinstance(data, list):
                if len(data) == 0:
                    raise ValueError("No plate found")
                if len(data) > 1:
                    raise ValueError("More than one plate found; query is ambiguous")
                return Plate.from_dict(data[0])
            raise ValueError("Unexpected response when fetching plate by id")

        results = self.get_plates(
            name=name,
            projects=projects,
            timeout=timeout,
        )
        if len(results) == 0:
            raise ValueError("No plate found")
        if len(results) > 1:
            raise ValueError(
                "More than one plate found, use get_plates for details or provide id"
            )
        return results[0]

    def set_plate(
        self,
        plate: Plate | Dict[str, Any],
        *,
        overwrite: bool = False,
        timeout: float = 15.0,
    ) -> Dict[str, Any]:
        """
        Upsert a single plate without the caller needing to manage IDs.
        Calls PUT /api/plates with overwrite semantics.
        """
        # Normalize input to a dict payload compatible with server expectations
        if isinstance(plate, Plate):
            wells_payload: list[dict[str, str]] = []
            for w in plate.wells or []:
                wells_payload.append(
                    {
                        "well": (w.well or "").upper(),
                        "name": (w.name or ""),
                        "sequence": (w.sequence or ""),
                    }
                )
            payload_plate: Dict[str, Any] = {
                "id": plate.id,
                "name": plate.name,
                "project": plate.project or "",
                "num_rows": int(plate.num_rows),
                "num_cols": int(plate.num_cols),
                "is_source": plate.is_source,
                "wells": wells_payload,
            }
        else:
            # Shallow copy and sanitize
            p = dict(plate)
            wells_payload = []
            for w in p.get("wells") or []:
                wells_payload.append(
                    {
                        "well": str((w.get("well") or "")).strip().upper(),
                        "name": str(w.get("name") or ""),
                        "sequence": str(w.get("sequence") or ""),
                    }
                )
            payload_plate = {
                "id": p.get("id"),
                "name": (p.get("name") or "").strip(),
                "project": (p.get("project") or "").strip(),
                "num_rows": int(p.get("num_rows") or 0),
                "num_cols": int(p.get("num_cols") or 0),
                "is_source": p.get("is_source"),
                "wells": wells_payload,
            }

        # Basic validation
        name_val = payload_plate.get("name") or ""
        if not name_val:
            raise ValueError("Plate name is required")
        if (
            int(payload_plate.get("num_rows") or 0) <= 0
            or int(payload_plate.get("num_cols") or 0) <= 0
        ):
            raise ValueError("num_rows and num_cols must be positive integers")

        # When creating, check for existing plate by name (optionally scoped by project)
        if payload_plate.get("id") is None:
            try:
                existing = self.get_plates(
                    name=name_val,
                    projects=(payload_plate.get("project") or None) or None,
                    timeout=timeout,
                )
            except Exception:
                existing = []
            if len(existing) > 1:
                raise ValueError(
                    "Multiple plates already exist with this name; provide id to update"
                )
            if len(existing) == 1:
                if not overwrite:
                    raise ValueError(
                        "Plate with this name already exists; set overwrite=True to update it"
                    )
                # Convert this operation into an update of the existing record
                payload_plate["id"] = existing[0].id

        url = f"{self.base_url}/api/plates"
        resp = self._session.put(
            url,
            headers=self._headers(),
            json={"overwrite": overwrite, "plates": [payload_plate]},
            timeout=timeout,
        )
        self._raise_for_status_with_context(resp)
        return resp.json()
