"""Module for check correct seq with md5."""
import hashlib


def hs(seq: str) -> str:
    """Checking the correctness of sequence."""
    return hashlib.md5(seq.encode()).hexdigest()
