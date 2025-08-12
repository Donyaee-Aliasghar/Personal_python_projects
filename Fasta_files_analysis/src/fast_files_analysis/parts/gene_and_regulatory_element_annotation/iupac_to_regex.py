"""Module for converting iupac codes to regex data."""

from .datas.IUPAC_codes import iupac_codes

def itr(seq) -> str:
    """operation."""
    regex_seq = ''
    for base in seq:
        if base in iupac_codes:
            regex_seq += iupac_codes[base]
        else:
            regex_seq += base
    return regex_seq
