def filter_by_length(records, min_len: int = None, max_len: int = None):
    result = []
    for r in records:
        l = len(r)
        if (min_len is None or l >= min_len) and (max_len is None or l <= max_len):
            result.append(r)
    return result


def filter_by_quality(records, min_qual: float = None, max_qual: float = None):
    if min_qual is None and max_qual is None:
        return records
    filtered = []
    for r in records:
        if not hasattr(r, "mean_quality"):
            continue
        mean_q = r.mean_quality()
        if (min_qual is None or mean_q >= min_qual) and (max_qual is None or mean_q <= max_qual):
            filtered.append(r)
    return filtered
