"""Module for analysis fasta file."""

from Bio import SeqIO
from Bio.SeqUtils import GC

from find_motifs import fm, pmr
from regulatory_element_patterns import motif_patterns
from find_orfs import forfs
from translate_orf import torf


def af(fasta_path: str) -> None:
    """Full analyze file operations."""
    record = SeqIO.read(fasta_path, "fasta")
    seq = record.seq
    print(f"Sequence ID: {record.id}")
    print(f"Sequence length: {len(seq)}")
    print(f"GC content: {GC(seq):.3f}%")
    print(f"AT content: {(GC(seq) / len(seq)) * 100:,.3f}%")
    print(f"First 100 bases:\n{seq[:100]}\n")

    # Regulatory elements searching.
    motif_results = fm(seq, motif_patterns)
    pmr(motif_results)

    # Find ORFs.
    orfs = forfs(seq, min_length=300)

    # Translate and show 10 firts motifs.
    for idx, (start, end, orf_seq) in enumerate(orfs[:10], 1):
        aa_seq = torf(orf_seq)
        print(f"\nORF {idx}: Start={start}, End={end}, Length={end - start + 1} bp")
        print(f"Amino acid sequence (first 50 aa):\n{aa_seq[:50]}")
