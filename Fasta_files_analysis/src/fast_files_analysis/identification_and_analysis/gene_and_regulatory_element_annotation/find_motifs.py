"""Modules for finding motifs in sequences and print them."""

import re

from typing import Dict, List, Tuple
from Bio.Seq import Seq


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
    for motif_name, matches in motif_results.items():
        print(f"\n[✅] {motif_name} found at positions (1-based index):")
        if matches:
            for pos, seq in matches:
                print(f"[🟢] Position: {pos}, Sequence: {seq}")
        else:
            print("[❌] No matches found.")
