import sys
import os

from src.gc_content_calculator.utils.gc_calculator import sliding_gc_calculator

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


def test_gc_simple():
    seq = "GCGCGCGCGC"
    result = sliding_gc_calculator(seq, window_size=10, step_size=1)
    assert result == [(0, 100.0)]


def test_gc_partial():
    seq = "ATGCATGCAT"
    result = sliding_gc_calculator(seq, window_size=10, step_size=1)
    assert result == [(0, 40.0)]


def test_gc_multiple_windows():
    seq = "ATGCGCGCGCATATATATATAT"
    result = sliding_gc_calculator(seq, window_size=10, step_size=5)
    assert len(result) == ((len(seq) - 10) // 5 + 1)


def test_gc_empty_sequence():
    seq = ""
    result = sliding_gc_calculator(seq, window_size=10, step_size=1)
    assert result == []


def test_gc_window_larger_than_sequence():
    seq = "ATGC"
    result = sliding_gc_calculator(seq, window_size=10, step_size=1)
    assert result == []
