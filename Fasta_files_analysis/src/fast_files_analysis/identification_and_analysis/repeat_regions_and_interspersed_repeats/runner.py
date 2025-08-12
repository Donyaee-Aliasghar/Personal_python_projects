"""This module is for executing different parts of the program in sequences."""

from .read_fasta import rf
from .kmp_algorithm import main as kmpa_main
from .sequence_search_and_calculate import main as aks_main
from .datas.famous_repetitive_sequences import known_sequences as ks


def rn(pure_file: str) -> None:
    """This does something."""
    # Read pure fasta file and save detaisl.
    data = rf(pure_file)  # data => pure fasta

    # Algoritm operations.
    kmpa_main(data[0]["sequence"], ks)

    # Sequence search and calculate operation.
    aks_main(data[0], ks)
