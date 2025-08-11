"""This module is for executing different parts of the program in sequences."""

from .kmp_algorithm import kmpa
from .sequence_search_and_calculate import aks
from .famous_repetitive_sequences import known_sequences as ks


def rn(pure_file):
    """This does something."""
    # algoritm operations.
    positions = kmpa(pure_file, ks)
    # sequence search and calculate operation.
    aks(positions, ks)
