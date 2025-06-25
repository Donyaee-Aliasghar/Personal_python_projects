from typing import List, Tuple
from Bio.SeqRecord import SeqRecord


def gc_content(seq: str) -> float:
    gc = sum(base in "GCgc" for base in seq)
    return (gc / len(seq)) * 100 if seq else 0


def sliding_gc_calculator(sequence: str, window_size: int = 100, step_size: int = 100) -> List[Tuple[int, float]]:
    gc_values = []
    for i in range(0, len(sequence) - window_size + 1, step_size):
        window = sequence[i : i + window_size]
        gc_count = window.upper().count("G") + window.upper().count("C")
        gc_percent = (gc_count / window_size) * 100
        gc_values.append((i, gc_percent))
    return gc_values
