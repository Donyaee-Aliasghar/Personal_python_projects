import pytest
from src.analysis import (
    count_nucleotides,
    gc_content,
    reverse_complement,
    transcribe_dna_to_rna,
)


def test_count_nucleotides():
    seq = "ATGCATGC"
    result = count_nucleotides(seq)
    assert result == {"A": 2, "T": 2, "G": 2, "C": 2}


def test_gc_content():
    seq = "GGCCAAATTT"
    assert gc_content(seq) == 40.0


def test_reverse_complement():
    seq = "ATGC"
    assert reverse_complement(seq) == "GCAT"


def test_transcribe_dna_to_rna():
    seq = "ATTGC"
    assert transcribe_dna_to_rna(seq) == "AUUGC"
