"""This module is for executing different parts of the program in sequences."""

from pathes import PS_FILE
from raw_file_purification.process_fasta import pf
from identification_and_analysis.repeat_regions_and_interspersed_repeats.runner import rn as rrn
from identification_and_analysis.gene_and_regulatory_element_annotation.runner import rn as grn


def mrn():
    """This does something."""
    # Fasta file purification operation.
    pf()

    # repeat regions and interspersed repeats operations.
    # rrn(PS_FILE)

    # gene_and_regulatory_element_annotation operations.
    # grn(PS_FILE)
