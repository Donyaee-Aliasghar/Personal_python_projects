"""Module for reading fasta file for GTF file."""

from Bio.Seq import Seq
from Bio import SeqIO


def lcf(fasta_path: str) -> Seq:
    """simple Operation."""
    record = SeqIO.read(fasta_path, "fasta")

    print("[✅] Load chromosom file and processing done.")
    return record
