# Show statistical summary


def summarize_fasta(records):
    total = len(records)
    total_length = sum(len(r) for r in records)
    avg_length = total_length / total if total > 0 else 0
    print(f"Sequence: {total}")
    print(f"Total length: {total_length}")
    print(f"Average length: {avg_length:.2f}")


def summarize_fastq(records):
    total = len(records)
    total_length = sum(len(r) for r in records)
    avg_length = total_length / total if total > 0 else 0
    avg_quality = sum(r.Mean_quality() for r in records) / total if total > 0 else 0
    print(f"Sequences: {total}")
    print(f"Total Length: {total_length}")
    print(f"Average Length: {avg_length:.2f}")
    print(f"Average Quality: {avg_quality:.2f}")
