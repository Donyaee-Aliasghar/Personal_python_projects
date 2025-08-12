"""Module for finding ORFs in sequences."""

from typing import List, Tuple
from Bio.Seq import Seq
from pathes import GAREA_OUTPUT_DIR


def forfs(sequence: Seq, min_length: int = 300) -> List[Tuple[int, int, str]]:
    """Find ORFs in +1 frame."""
    orfs: List[Tuple[int, int, str]] = []
    seq_str = str(sequence)
    start_codon = "ATG"
    stop_codons = ["TAA", "TAG", "TGA"]
    seq_len = len(seq_str)

    with open(f"{GAREA_OUTPUT_DIR}/finding_ORFs.txt", "w", encoding="utf-8") as fout:
        fout.write(f"\n{"-"*20} Show ORFs {"="*20}\n")
        for i in range(seq_len):
            if seq_str[i : i + 3] == start_codon:
                for j in range(i + 3, seq_len, 3):
                    codon = seq_str[j : j + 3]
                    if codon in stop_codons:
                        orf_length = j + 3 - i
                        if orf_length >= min_length:
                            orf_seq = seq_str[i : j + 3]
                            orfs.append((i + 1, j + 3, orf_seq))  # -1 positions.
                        break
        fout.write(f"\nFound {len(orfs):,} ORFs longer than {min_length} bp.")
    return orfs
