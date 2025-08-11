"""Module for clean sequence."""

from typing import List, Set


def cs(seq: List[str], allowed_bases: Set[str]) -> str:
    """Clean sequence form all 'N' word."""
    seq = seq.upper()
    cleaned = "".join([b for b in seq if b in allowed_bases])
    return cleaned
