"""Module for analysis fasta file."""

from Bio import SeqIO
from Bio.SeqUtils import gc_fraction

from pathes import GAREA_OUTPUT_DIR
from .find_motifs import fm, pmr
from .regulatory_element_patterns import motif_patterns
from .find_orfs import forfs
from .translate_orf import torf


def af(pure_file: str) -> None:
    """Full analyze file operations."""
    record = SeqIO.read(pure_file, "fasta")
    seq = record.seq

    gc = seq.upper().count("G")
    cc = seq.upper().count("C")
    ac = seq.upper().count("A")
    tc = seq.upper().count("T")
    gcf = gc_fraction(seq) * 100

    with open(f"{GAREA_OUTPUT_DIR}/full_analysis.txt", "w", encoding="utf-8") as fout:
        fout.write(f"\n{"="*30} Summary analyze {"="*30}\n")
        fout.write(f"Sequence ID: {record.id}\n")
        fout.write(f"Sequence length: {len(seq):,} bp\n")
        fout.write(f"GC content: {gc+cc:,} bp({gcf:.10f}%) \n")
        fout.write(f"AT content: {ac+tc:,} bp({100-gcf:.10f}%) \n")
        fout.write(f"First 100 bases:\n{seq[:100]}...\n")

    # Regulatory elements searching.
    motif_results = fm(seq, motif_patterns)
    pmr(motif_results)

    # Find ORFs.
    orfs = forfs(seq, min_length=300)

    # Translate and show 10 firts motifs.
    with open(f"{GAREA_OUTPUT_DIR}/finding_ORFs.txt", "a", encoding="utf-8") as fout:
        for idx, (start, end, orf_seq) in enumerate(orfs[:10], 1):
            aa_seq = torf(orf_seq)
            fout.write(
                f"\nORF number {idx:,}\n\t+.Start: {start:,}\n\t+.End: {end:,}\n\t+.Length: {end - start + 1:,} bp\n\t+.Amino acid sequence (first 30 aa): {aa_seq[:30]}..."
            )

    print("[✅] Full analyze file operation done.")
