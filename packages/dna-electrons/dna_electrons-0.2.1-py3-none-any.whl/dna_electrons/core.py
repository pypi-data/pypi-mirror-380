# Copyright (c) 2025 Yash Munnalal Gupta
# SPDX-License-Identifier: MIT

from dataclasses import dataclass
from typing import Dict, List

# Per-base electron counts (bases only; no sugar/phosphate)
ELECTRONS_PER_BASE: Dict[str, int] = {
    "A": 70,  # C5H5N5
    "T": 66,  # C5H6N2O2
    "G": 78,  # C5H5N5O
    "C": 58,  # C4H5N3O
}

# Backbone per base pair: 2*(deoxyribose 70) + 2*(phosphate 49) = 238 (no charge)
BACKBONE_ELECTRONS: int = 2 * 70 + 2 * 49

# Phosphate charge per base pair
PHOSPHATE_CHARGE_ELECTRONS: int = 2

COMPLEMENT = {"A": "T", "T": "A", "G": "C", "C": "G"}

@dataclass
class Result:
    total: int
    breakdown: Dict[str, int]
    counts: Dict[str, int]
    sequence_length: int
    double_stranded: bool
    include_backbone: bool
    include_phosphate_charge: bool

def _count_bases(seq: str) -> Dict[str, int]:
    counts = {"A": 0, "T": 0, "G": 0, "C": 0}
    invalid_positions: List[int] = []
    for i, ch in enumerate(seq.upper()):
        if ch in counts:
            counts[ch] += 1
        else:
            invalid_positions.append(i)
    if invalid_positions:
        sample = ", ".join(str(i) for i in invalid_positions[:5])
        more = "" if len(invalid_positions) <= 5 else f" and {len(invalid_positions)-5} more"
        raise ValueError(f"Sequence contains non-ATGC characters at positions: {sample}{more}.")
    return counts

def _pairwise_base_electrons(counts: Dict[str, int]) -> int:
    # Any base pair contributes 136 electrons from bases: AT (70+66) or GC (78+58)
    n_pairs = sum(counts.values())
    return 136 * n_pairs

def _single_strand_base_electrons(counts: Dict[str, int]) -> int:
    return sum(ELECTRONS_PER_BASE[b] * n for b, n in counts.items())

def compute_electrons(
    sequence: str,
    *,
    double_stranded: bool = True,
    include_backbone: bool = True,
    include_phosphate_charge: bool = True,
) -> Result:
    """Compute total electrons for a DNA sequence.

    Parameters
    ----------
    sequence : str
        Nucleotide sequence (ATGC). If double_stranded=True, treated as one strand in a perfectly paired duplex.
    double_stranded : bool
        If True, includes electrons from both paired bases.
    include_backbone : bool
        If True, adds sugar-phosphate backbone electrons (per base pair if double-stranded; per nucleotide if single).
    include_phosphate_charge : bool
        If True, adds phosphate negative-charge electrons (+2 per base pair, +1 per nucleotide for single strand).
    """
    if not sequence:
        raise ValueError("Sequence must be non-empty.")
    counts = _count_bases(sequence)
    n = sum(counts.values())
    breakdown: Dict[str, int] = {}

    if double_stranded:
        base_e = _pairwise_base_electrons(counts)
        breakdown["bases"] = base_e
        backbone_e = BACKBONE_ELECTRONS * n if include_backbone else 0
        if include_backbone:
            breakdown["backbone"] = backbone_e
        charge_e = PHOSPHATE_CHARGE_ELECTRONS * n if include_phosphate_charge else 0
        if include_phosphate_charge:
            breakdown["phosphate_charge"] = charge_e
        total = base_e + backbone_e + charge_e
    else:
        base_e = _single_strand_base_electrons(counts)
        breakdown["bases"] = base_e
        single_backbone = (BACKBONE_ELECTRONS // 2) if include_backbone else 0
        backbone_e = single_backbone * n
        if include_backbone:
            breakdown["backbone"] = backbone_e
        single_charge = (PHOSPHATE_CHARGE_ELECTRONS // 2) if include_phosphate_charge else 0
        charge_e = single_charge * n
        if include_phosphate_charge:
            breakdown["phosphate_charge"] = charge_e
        total = base_e + backbone_e + charge_e

    return Result(
        total=total,
        breakdown=breakdown,
        counts=counts,
        sequence_length=n,
        double_stranded=double_stranded,
        include_backbone=include_backbone,
        include_phosphate_charge=include_phosphate_charge,
    )
