"""This module is for executing different parts of the program in sequences."""

from analyze_fasta import af


def rn(pure_file: str) -> None:
    """This does something."""
    # Analysis fasta file.
    af(pure_file)
