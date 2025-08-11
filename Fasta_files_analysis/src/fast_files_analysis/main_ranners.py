"""This module is for executing different parts of the program in sequences."""

from raw_file_purification.process_fasta import pf
from identification_and_analysis.repeat_regions_and_interspersed_repeats.runner import rn as rrn
from pathes import PS_FILE


def mrn():
    """This does something."""
    # Fasta file purification operation.
    # pf()
    # repeat regions and interspersed repeats operations.
    with open(PS_FILE, "r", encoding="utf-8") as f:
        rrn(f.read())
