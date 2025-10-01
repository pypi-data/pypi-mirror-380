from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Dict, Iterable, List, Mapping, Optional, Tuple
import re

from .models import Plate, PlateWell


class ConstraintType(str, Enum):
    """
    Constraint relationship between two DNA sequences (or domains of sequences).

    - "equal": the two compared segments must be exactly equal after normalization
    - "reverse_complement": the two compared segments must be reverse complements
    """

    EQUAL = "equal"
    REVERSE_COMPLEMENT = "reverse_complement"


@dataclass(slots=True)
class WatsonCrickConstraint:
    """
    A constraint between two named sequences (optionally narrowed to domains).

    Domains are specified by zero-based IDs, left-to-right, where each domain is
    the substring between spaces in the sequence. For example, for the sequence:
    "CCATGTCCCATT AAATGCTTTAAACAGTTCAGAAAA TTTTTTACTATCTCCGCTCA"
    domain ID 0 refers to "CCATGTCCCATT", domain ID 1 refers to
    "AAATGCTTTAAACAGTTCAGAAAA", and domain ID 2 refers to
    "TTTTTTACTATCTCCGCTCA".

    If a domain ID is None, the entire sequence is used.

    Plate names can be None. If None, and the parsed orders mapping contains
    more than one plate, validation raises because the target plate is ambiguous.
    When there is a single plate, that unique plate is used.
    """

    sequence1_plate_name: Optional[str]
    sequence1_name: str
    sequence1_domain_ID: Optional[int]
    sequence2_plate_name: Optional[str]
    sequence2_name: str
    sequence2_domain_ID: Optional[int]
    constraint_type: ConstraintType


_MODIFIER_RE = re.compile(r"/[^/\n\r]*/")


def _strip_modifiers(seq: str) -> str:
    """
    Remove attached modifier tokens like "/5ATTO590N/" which are enclosed in slashes.
    These are not DNA bases and should be ignored for comparisons.
    """
    if not seq:
        return seq
    return _MODIFIER_RE.sub("", seq)


def _normalize_sequence(seq: str) -> str:
    """Strip modifiers, remove spaces, and uppercase A/T/G/C characters only."""
    s = _strip_modifiers(seq)
    # Keep spaces for domain tokenization step elsewhere; here only case-normalize
    return s.upper()


def _split_domains(seq: str) -> List[str]:
    """
    Split a sequence string into domain tokens by spaces, preserving token order.
    Empty tokens are ignored. Modifiers are stripped prior to splitting.
    """
    clean = _normalize_sequence(seq)
    tokens = [t for t in (clean.split(" ") if clean else []) if t]
    return tokens


_RC_MAP = str.maketrans({"A": "T", "T": "A", "G": "C", "C": "G"})


def reverse_complement(seq: str) -> str:
    """
    Compute the reverse complement of a DNA sequence.

    Modifiers enclosed in slashes are ignored. Non-ATGC symbols are preserved
    in-place prior to complementation mapping (i.e., they map to themselves).
    Spaces are removed during comparison logic, not in this function.
    """
    s = _normalize_sequence(seq).replace(" ", "")
    comp = s.translate(_RC_MAP)
    return comp[::-1]


class ConstraintError(ValueError):
    pass


def _resolve_plate(plates: Mapping[str, Plate], desired: Optional[str]) -> Plate:
    if desired is not None:
        try:
            return plates[desired]
        except KeyError as exc:
            raise ConstraintError(f"Plate '{desired}' not found in orders") from exc
    # desired is None -> must be unique
    if len(plates) == 1:
        return next(iter(plates.values()))
    raise ConstraintError(
        "Ambiguous plate: multiple plates present but no plate specified"
    )


def _find_sequence_in_plate(plate: Plate, target_name: str) -> PlateWell:
    for w in plate.wells or []:
        if (w.name or "").strip() == target_name:
            return w
    raise ConstraintError(
        f"Sequence named '{target_name}' not found in plate '{plate.name}'"
    )


def _select_segment(full_sequence: str, domain_id: Optional[int]) -> str:
    if domain_id is None:
        return _normalize_sequence(full_sequence).replace(" ", "")
    domains = _split_domains(full_sequence)
    if domain_id < 0 or domain_id >= len(domains):
        raise ConstraintError(
            f"Domain ID {domain_id} out of range (found {len(domains)} domains)"
        )
    return domains[domain_id]


def _format_target(
    plate_name: str, sequence_name: str, domain_id: Optional[int]
) -> str:
    """Format a human-readable target like 'Plate:Seq (domain N)' when domain is set."""
    if domain_id is None:
        return f"{plate_name}:{sequence_name}"
    return f"{plate_name}:{sequence_name} (domain {domain_id})"


def validate_constraints(
    orders: Mapping[str, Plate],
    constraints: Iterable[WatsonCrickConstraint],
    verbose: bool = False,
) -> None:
    """
    Validate that all given constraints hold for the provided orders mapping
    produced by parse_plates_from_excel.

    - orders: mapping of plate_name -> Plate
    - constraints: iterable of WatsonCrickConstraint
    - verbose: when True, prints each constraint check and whether it passed (✅) or failed (❌)

    Raises ConstraintError on the first failing constraint.
    """
    for c in constraints:
        plate1 = _resolve_plate(orders, c.sequence1_plate_name)
        plate2 = _resolve_plate(orders, c.sequence2_plate_name)

        w1 = _find_sequence_in_plate(plate1, c.sequence1_name)
        w2 = _find_sequence_in_plate(plate2, c.sequence2_name)

        s1_raw = w1.sequence or ""
        s2_raw = w2.sequence or ""

        seg1 = _select_segment(s1_raw, c.sequence1_domain_ID)
        seg2 = _select_segment(s2_raw, c.sequence2_domain_ID)

        t1 = _format_target(plate1.name, c.sequence1_name, c.sequence1_domain_ID)
        t2 = _format_target(plate2.name, c.sequence2_name, c.sequence2_domain_ID)

        if c.constraint_type == ConstraintType.EQUAL:
            left = seg1.replace(" ", "")
            right = seg2.replace(" ", "")
            ok = left == right
            if verbose:
                print(
                    ("✅ " if ok else "❌ ")
                    + f"equal: {t1} == {t2}; left='{left}', right='{right}'"
                )
            if not ok:
                raise ConstraintError(
                    f"Constraint equal failed: {t1} != {t2}; left='{left}', right='{right}'"
                )
        elif c.constraint_type == ConstraintType.REVERSE_COMPLEMENT:
            left_rc = reverse_complement(seg1)
            right = seg2.replace(" ", "")
            ok = left_rc == right
            if verbose:
                print(
                    ("✅ " if ok else "❌ ")
                    + f"reverse_complement: rc({t1}) == {t2}; left='{seg1}', right='{right}'"
                )
            if not ok:
                raise ConstraintError(
                    f"Constraint reverse_complement failed: rc({t1}) != {t2}; left_rc='{left_rc}', right='{right}'"
                )
        else:  # pragma: no cover - defensive
            raise ConstraintError(f"Unknown constraint type: {c.constraint_type}")

    # All constraints satisfied -> return None
    return None
