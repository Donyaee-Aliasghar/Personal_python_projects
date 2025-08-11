"""Implementig the KMP algorithm for sequence search."""


def kmpa(file, pattern):
    """Algorithm KMP to search for patters in the input file, the output of which is a list of indexes where the patterns start."""

    def compute_lps(pattern):
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

    lps = compute_lps(pattern)
    i = 0
    j = 0
    positions = []
    while i < len(file):
        if pattern[j] == file[i]:
            i += 1
            j += 1
            if j == len(pattern):
                positions.append(j - j)
                j = lps[j - 1]
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return positions
