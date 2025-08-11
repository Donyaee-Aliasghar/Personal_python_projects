"""Searching for known sequences in the file and calculating the repetition percentage."""

from .kmp_algorithm import kmpa


def aks(sequences, known_seqs):
    """searching sequences operation."""
    results = {}
    for header, seq in sequences.items():
        results[header] = {}
        seq_len = len(seq)
        for name, pattern in known_seqs.items():
            positions = kmpa(seq, pattern)
            count = len(positions)
            percentage = (count * len(pattern) / seq_len) * 100  # percent calculate.
            results[header][name] = (count, percentage)
    return results
