# Copyright (c) 2025 Yash Munnalal Gupta
# SPDX-License-Identifier: MIT

from typing import List, Tuple
from pathlib import Path
from Bio import SeqIO
from .core import compute_electrons, Result

def compute_from_fasta(
    fasta_path: str,
    *,
    double_stranded: bool = True,
    include_backbone: bool = True,
    include_phosphate_charge: bool = True,
) -> List[Tuple[str, Result]]:
    """Compute electron counts for each sequence in a FASTA file.
    Returns a list of (record_id, Result)."""
    rows: List[Tuple[str, Result]] = []
    for record in SeqIO.parse(Path(fasta_path), "fasta"):
        seq_str = str(record.seq)
        res = compute_electrons(
            seq_str,
            double_stranded=double_stranded,
            include_backbone=include_backbone,
            include_phosphate_charge=include_phosphate_charge,
        )
        rows.append((record.id, res))
    return rows
