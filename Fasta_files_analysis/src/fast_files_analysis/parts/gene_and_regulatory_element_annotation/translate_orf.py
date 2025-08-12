"""Module for translate ORFs."""

from Bio.Seq import Seq


def torf(orf_seq: str) -> Seq:
    """Translation of ORF into amino acid sequence."""
    seq_obj = Seq(orf_seq)
    return seq_obj.translate(to_stop=True)
