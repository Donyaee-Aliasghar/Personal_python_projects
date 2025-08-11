"""This module is for executing different parts of the program in sequences."""

from typing import List

from .read_fasta import rf
from .kmp_algorithm import main as kmpa_main
from .sequence_search_and_calculate import main as aks_main
from .datas.famous_repetitive_sequences import known_sequences as ks


def rn(pure_file: str) -> None:
    """This does something."""
    # convert str pure sequence fasta file to dict.
    seq_lines = rf(pure_file)
    # algoritm operations.
    kmpa_main(seq_lines, ks)
    # sequence search and calculate operation.
    aks_main(seq_lines, ks)
