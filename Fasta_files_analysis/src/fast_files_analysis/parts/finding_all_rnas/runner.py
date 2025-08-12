"""This module is for executing different parts of the program in sequences."""

from .Loading_and_extracting_columns import load_gtf as lg
from .read_fasta import lcf
from .extract_and_save_all_rnas import easa_rnas


def rn(gtf_file: str, pure_fasta_file: str) -> None:
    """This does something."""
    # Load and extracting file.
    df = lg(gtf_file)

    # Read fasta file.
    data = lcf(pure_fasta_file)

    # Extracting all RNAs.
    easa_rnas(df, data)
