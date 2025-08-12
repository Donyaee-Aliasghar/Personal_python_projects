"""This module is for executing different parts of the program in sequences."""

from pathes import MAIN_RAW_FASTA_FILE, PS_FILE, MAIN_RAW_GTF_FILE
from raw_file_purification.process_fasta import pf
from identification_and_analysis.repeat_regions_and_interspersed_repeats.runner import rn as rrn
from identification_and_analysis.gene_and_regulatory_element_annotation.runner import rn as grn
from identification_and_analysis.finding_all_rnas.runner import rn as gtfrn


def mrn() -> None:
    """This does something."""
    # Fasta file purification operation.
    # pf(MAIN_RAW_FASTA_FILE)

    # Repeat regions and interspersed repeats operations.
    # rrn(PS_FILE)

    # Gene_and_regulatory_element_annotation operations.
    # grn(PS_FILE)

    # Operation with GTF for type of RNAs.
    # gtfrn(MAIN_RAW_GTF_FILE, PS_FILE)
