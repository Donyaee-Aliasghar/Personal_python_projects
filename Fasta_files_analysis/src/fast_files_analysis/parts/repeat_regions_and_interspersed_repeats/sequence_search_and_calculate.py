"""Searching for known sequences in the file and calculating the repetition percentage."""

from typing import Dict

from .kmp_algorithm import kmpa
from pathes import RRAIR_OUTPUT_DIR


def aks(data: Dict[str, str], ks: Dict[str, str]) -> Dict[str, str]:
    """searching sequences operation."""
    results = {}
    for header, seq in data.items():
        results[header] = {}
        seq_len = len(seq)
        for name, pattern in ks.items():
            positions = kmpa(seq, pattern)
            count = len(positions)
            percentage = (count * len(pattern) / seq_len) * 100  # percent calculate.
            results[header][name] = (count, percentage)
    return results


def main(data: Dict[str, str], ks: Dict[str, str]) -> None:
    """Operations and create file."""
    results = aks(data, ks)
    with open(
        f"{RRAIR_OUTPUT_DIR}/repeat_regions_and_interspersed_repeats.txt",
        "w",
        encoding="utf-8",
    ) as fout:
        fout.write(f"\n{"="*20} sequence search and calculate results {"="*20}\n")
        for pattern_name, (count, perc) in results["sequence"].items():
            fout.write(f"Sequence: {pattern_name}\nNumber of repetitions: {count}\nCoverage percentage: {perc:.10f}%\n")
            fout.write(f"{"-"*30}\n")
    print(f"[✅] sequence earch and calculate operation done.")
