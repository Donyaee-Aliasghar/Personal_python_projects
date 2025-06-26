import argparse
import os

from parsers.fasta_parser import parse_fasta
from parsers.fastq_parser import parse_fastq

from utils.stats import summarize_fasta, summarize_fastq
from utils.filters import filter_by_length, filter_by_quality


def main():
    parser = argparse.ArgumentParser(description="Bio file manager CLI")

    parser.add_argument("-i", "--input", required=True, help="Path to input file")
    parser.add_argument("-f", "--format", required=True, choices=["fasta", "fastq"], help="File format")
    parser.add_argument("-o", "--output", help="Path to output file (optional)")
    parser.add_argument("--minlen", type=int, help="Minimum sequence length")
    parser.add_argument("--maxlen", type=int, help="Maximum sequence length")
    parser.add_argument("--minqual", type=float, help="Minimum average quality (just FASTQ)")
    parser.add_argument("--maxqual", type=float, help="Maximum average quality (just FASTQ)")

    args = parser.parse_args()
    output_path = os.path.join("results", args.output) if args.output else None
    if args.output:
        os.makedirs("results", exist_ok=True)

    if args.format == "fasta":
        records = list(parse_fasta(args.input))
        if args.minlen is not None or args.maxlen is not None:
            filter_by_length(records, args.minlen, args.maxlen)

        summarize_fasta(records)

        if args.output:
            from utils.export import export_fasta

            export_fasta(records, output_path)
            print(f"Exported to {output_path}")
    elif args.format == "fastq":
        records = list(parse_fastq(args.input))

        if args.minlen is not None or args.maxlen is not None:
            records = filter_by_length(records, args.minlen, args.maxlen)
        if args.minqual is not None or args.maxqual is not None:
            print("\n [DEBUG] Mean qualities before filtering: ")
            for r in records:
                print(f"{r.header}: mean quality = {r.mean_quality():.2f}")
            records = filter_by_quality(records, args.minqual, args.maxqual)

        summarize_fastq(records)

        if args.output:
            from utils.export import export_fastq

            export_fastq(records, output_path)
            print(f"Exported to {output_path}")


if __name__ == "__main__":
    main()
