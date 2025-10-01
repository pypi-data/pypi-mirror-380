from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Dict, Iterable, List, Mapping, Optional, Tuple, Union
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

    Sequence set names identify which collection of sequences to use (e.g., when
    using parse_plates_from_excel, these would be plate names). Set names can be
    None; if None and the input contains more than one set, validation raises
    because the target set is ambiguous. When there is a single set, that unique
    set is used automatically.
    """

    sequence1_set_name: Optional[str]
    sequence1_name: str
    sequence1_domain_ID: Optional[int]
    sequence2_set_name: Optional[str]
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


def _normalize_to_sequence_sets(
    input_data: Union[Mapping[str, Plate], Dict[str, Dict[str, str]]],
) -> Dict[str, Dict[str, str]]:
    """
    Convert input to normalized format: Dict[set_name, Dict[sequence_name, sequence]].

    Accepts either:
    - Mapping[str, Plate]: output from parse_plates_from_excel
    - Dict[str, Dict[str, str]]: direct sequence sets
    """
    # Check if it's a Plate mapping by examining the first value
    if not input_data:
        return {}

    first_value = next(iter(input_data.values()))

    # If it's a Plate object, extract sequences from wells
    if isinstance(first_value, Plate):
        result: Dict[str, Dict[str, str]] = {}
        # Type checker now knows input_data contains Plate objects
        plates: Mapping[str, Plate] = input_data  # type: ignore
        for plate_name, plate in plates.items():
            sequences: Dict[str, str] = {}
            for well in plate.wells or []:
                if well.name and well.sequence:
                    sequences[well.name.strip()] = well.sequence
            result[plate_name] = sequences
        return result

    # Otherwise, assume it's already in the Dict[str, Dict[str, str]] format
    return dict(input_data)  # type: ignore


def _resolve_sequence_set(
    sequence_sets: Dict[str, Dict[str, str]], desired: Optional[str]
) -> Tuple[str, Dict[str, str]]:
    """
    Resolve a sequence set by name. If desired is None, use the unique set if only one exists.
    Returns (set_name, sequences_dict).
    """
    if desired is not None:
        if desired not in sequence_sets:
            raise ConstraintError(f"Sequence set '{desired}' not found")
        return desired, sequence_sets[desired]
    # desired is None -> must be unique
    if len(sequence_sets) == 1:
        set_name = next(iter(sequence_sets.keys()))
        return set_name, sequence_sets[set_name]
    raise ConstraintError(
        "Ambiguous sequence set: multiple sets present but no set name specified"
    )


def _find_sequence_in_set(
    set_name: str, sequences: Dict[str, str], target_name: str
) -> str:
    """Find a sequence by name in a sequence set. Returns the DNA sequence string."""
    if target_name not in sequences:
        raise ConstraintError(
            f"Sequence named '{target_name}' not found in set '{set_name}'"
        )
    return sequences[target_name]


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
    sequence_sets: Union[Mapping[str, Plate], Dict[str, Dict[str, str]]],
    constraints: Iterable[WatsonCrickConstraint],
    verbose: bool = False,
) -> None:
    """
    Validate that all given constraints hold for the provided sequence sets.

    Args:
        sequence_sets: Either:
            - Mapping[str, Plate]: output from parse_plates_from_excel (set names are plate names)
            - Dict[str, Dict[str, str]]: dict where key is set name, value is dict mapping
              sequence names to DNA sequences
        constraints: iterable of WatsonCrickConstraint
        verbose: when True, prints each constraint check and whether it passed (✅) or failed (❌)

    Raises:
        ConstraintError: on the first failing constraint
    """
    # Normalize input to common format
    normalized_sets = _normalize_to_sequence_sets(sequence_sets)

    for c in constraints:
        set1_name, sequences1 = _resolve_sequence_set(
            normalized_sets, c.sequence1_set_name
        )
        set2_name, sequences2 = _resolve_sequence_set(
            normalized_sets, c.sequence2_set_name
        )

        s1_raw = _find_sequence_in_set(set1_name, sequences1, c.sequence1_name)
        s2_raw = _find_sequence_in_set(set2_name, sequences2, c.sequence2_name)

        seg1 = _select_segment(s1_raw, c.sequence1_domain_ID)
        seg2 = _select_segment(s2_raw, c.sequence2_domain_ID)

        t1 = _format_target(set1_name, c.sequence1_name, c.sequence1_domain_ID)
        t2 = _format_target(set2_name, c.sequence2_name, c.sequence2_domain_ID)

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
