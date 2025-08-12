"""This module for read pure file."""

from typing import List
from Bio import SeqIO
from Bio.SeqUtils import gc_fraction
from pathes import RRAIR_OUTPUT_DIR


def rf(filepath: str) -> List[str]:
    """operation."""

    fasta_list: List[str] = []
    record = SeqIO.read(filepath, "fasta")
    seq = record.seq

    with open(filepath, "r", encoding="utf-8") as f, open(
        f"{RRAIR_OUTPUT_DIR}/read_pure_fasta.txt",
        "w",
        encoding="utf-8",
    ) as fout:
        header = None
        seq_part = []
        for line in f:
            line = line.strip()
            if line.startswith(">"):
                if header:
                    fasta_list.append({"header": header, "sequence": "".join(seq_part)})
                header = line[1:]
                seq_part = []
            else:
                seq_part.append(line)
        if header:
            fasta_list.append({"header": header, "sequence": "".join(seq_part)})

        # Create rrair text file.
        fout.write(f"\n{"="*20} Read pure file length results {"="*20}\n")
        fout.write(f"\nNumber of sequence reads: {len(seq):,} bp\n")
    print(f"[✅] Read pure sequence file operation done.")
    return fasta_list
