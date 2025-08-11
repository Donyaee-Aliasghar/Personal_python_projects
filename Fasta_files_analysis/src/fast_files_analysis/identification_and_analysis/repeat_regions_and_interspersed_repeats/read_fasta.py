"""This module for read pure file."""

from typing import List


def rf(filepath: str) -> List[str]:
    """operation."""
    seq_lines: List[str] = []
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            if not line.startswith(">"):  # ignore the header
                seq_lines.append(line.strip())
    print(f"[🟢] Number of sequence reads: {len(seq_lines):,} bp")
    return "".join(seq_lines)
