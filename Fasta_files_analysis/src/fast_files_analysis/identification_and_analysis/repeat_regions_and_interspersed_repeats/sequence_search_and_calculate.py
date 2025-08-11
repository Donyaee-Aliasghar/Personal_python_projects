"""Searching for known sequences in the file and calculating the repetition percentage."""

from typing import List, Dict

from .kmp_algorithm import kmpa


def aks(s: List[str], ks: Dict[str, str]) -> Dict[str, str]:
    """searching sequences operation."""
    results = {}
    for header, seq in s.items():
        results[header] = {}
        seq_len = len(seq)
        for name, pattern in ks.items():
            positions = kmpa(seq, pattern)
            count = len(positions)
            percentage = (count * len(pattern) / seq_len) * 100  # percent calculate.
            results[header][name] = (count, percentage)
    return results


def main(s: List[str], kss: Dict[str, str]) -> None:
    results = aks(s, kss)
    for header, data in results.items():
        print(f"\nresults for {header}\n")
        for pattern_name, (count, perc) in data.items():
            print(f"sequence {pattern_name}: Number of repetitions = {count}, Coverage percentage = {perc:.3f}%")
