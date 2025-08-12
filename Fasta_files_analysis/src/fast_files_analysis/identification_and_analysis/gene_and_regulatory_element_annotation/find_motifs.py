"""Modules for finding motifs in sequences and print them."""

import re

from typing import Dict, List, Tuple
from Bio.Seq import Seq
from pathes import GAREA_OUTPUT_DIR


def fm(sequence: Seq, motif_dict: dict[str, re.Pattern]) -> dict[str, list[tuple[int, str]]]:
    """Find motifs operations."""
    results: Dict[str, List[Tuple[int, str]]] = {}
    for motif_name, pattern in motif_dict.items():
        matches: List[Tuple[int, str]] = []
        for match in pattern.finditer(str(sequence)):
            matches.append((match.start() + 1, match.group()))
        results[motif_name] = matches
    return results


def pmr(motif_results: Dict[str, List[Tuple[int, str]]]) -> None:
    """Print results operations."""
    with open(f"{GAREA_OUTPUT_DIR}/finding_motifs.txt", "w", encoding="utf-8") as fout:
        fout.write(f"\n{"-"*30} Show motifs {"-"*30}\n")
        for motif_name, matches in motif_results.items():
            fout.write(f"\nMotif name: {motif_name}\nLength: {len(matches)}\nFound at positions (1-based index):\n")
            if matches:
                for index, (pos, seq) in enumerate(matches, start=1):
                    fout.write(f"\tPosition({index:,}): {pos:,} - Sequence({index:,}): {seq}")
                    fout.write("\t")
            else:
                fout.write("[❌] No matches found.")
