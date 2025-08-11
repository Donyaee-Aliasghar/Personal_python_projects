"""Module for clean sequence."""


def cs(seq: list[str], allowed_bases: set[str] = set("ATGC")) -> str:
    """Clean sequence form all 'N' word."""
    seq = seq.upper()
    cleaned = "".join([b for b in seq if b in allowed_bases])
    return cleaned
