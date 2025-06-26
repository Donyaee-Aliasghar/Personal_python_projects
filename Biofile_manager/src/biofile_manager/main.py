import os
from src.biofile_manager.parsers.fasta_parser import parse_fasta
from src.biofile_manager.utils.stats import summarize_fasta


def main():
    path = os.path.join(os.path.dirname(__file__), "datas", "example.fasta")
    records = list(parse_fasta(path))
    summarize_fasta(records)


if __name__ == "__main__":
    main()
