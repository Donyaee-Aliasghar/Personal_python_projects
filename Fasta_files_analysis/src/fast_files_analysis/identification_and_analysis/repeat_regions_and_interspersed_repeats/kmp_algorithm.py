"""Implementig the KMP algorithm for sequence search."""

from typing import List, Dict

from pathes import RRAIR_OUTPUT_DIR


def kmpa(text: str, pattern: Dict[str, str]) -> List[str]:
    """Algorithm KMP to search for patters in the input file, the output of which is a list of indexes where the patterns start."""

    # Create table LPS.
    def build_lps(pattern):
        lps = [0] * len(pattern)
        length = 0
        i = 1
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    lps = build_lps(pattern)
    positions = []
    i = j = 0
    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == len(pattern):
            positions.append(i - j)
            j = lps[j - 1]
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return positions


def main(seq_lines: str, ks: dict[str, str]) -> None:
    """Searching all sequences."""

    with open(
        f"{RRAIR_OUTPUT_DIR}/search_patterns_with_algorithm.txt",
        "w",
        encoding="utf-8",
    ) as fout:
        fout.write(f"\n{"="*30} Search patterns results {"="*30}\n")
        for name, pattern in ks.items():
            positions = kmpa(seq_lines, pattern)

            fout.write(
                f"\nName: {name}\nPattern: {pattern}\nNumber: {len(positions)}\nPositions: {positions[:5]}\n[⚠]For heavy processing, 5 is enough.\n"
            )
            fout.write(f"{"-"*30}\n")

    print(f"[✅] Search for patters operation done.")
