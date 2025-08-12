"""Module to clean the raw fasta file and remove all impurities."""

from typing import List

from .cleaning_sequence import cs
from .hash_seq import hs

from pathes import PS_OUTPUT_DIR, FFPD_LOG_DIR


def pf(MAIN_RAW_FASTA_FILE) -> None:
    """Main operation for file purification."""
    allowed_bases = set("ATGC")
    min_len = 80
    seen_hashes = set()
    total_seqs = 0
    removed_short = 0
    removed_duplicate = 0
    kept_seqs = 0

    with open(MAIN_RAW_FASTA_FILE, "r", encoding="utf-8") as fin, open(
        f"{PS_OUTPUT_DIR}/pure_sequence.fasta", "w", encoding="utf-8"
    ) as fout, open(f"{FFPD_LOG_DIR}/fasta_file_purification_details.log", "w", encoding="utf-8") as flog:
        header = None
        seq_chunks: List[str] = []

        for line in fin:
            line = line.strip()
            if not line:
                continue
            if line.startswith(">"):
                # If there is a previous header, process the previous sequence.
                if header is not None:
                    total_seqs += 1
                    full_seq = "".join(seq_chunks)
                    cleaned_seq = cs(full_seq, allowed_bases)
                    if len(cleaned_seq) < min_len:
                        removed_short += 1
                        flog.write(f"[❌] Removed short sequence {header} length={len(cleaned_seq)}\n")
                    else:
                        seq_hash = hs(cleaned_seq)
                        if seq_hash in seen_hashes:
                            removed_duplicate += 1
                            flog.write(f"[❌] Removed duplicate sequence {header}\n")
                        else:
                            seen_hashes.add(seq_hash)
                            fout.write(f"{header}\n")
                            for i in range(0, len(cleaned_seq), 80):
                                fout.write(cleaned_seq[i : i + 80] + "\n")
                            kept_seqs += 1
                # Set the new header and reset seq_chunks.
                header = line
                seq_chunks: List[str] = []
            else:
                seq_chunks.append(line)

        # Process the last sequence at the end of the file.
        if header is not None and seq_chunks:
            total_seqs += 1
            full_seq = "".join(seq_chunks)
            cleaned_seq = cs(full_seq, allowed_bases)
            if len(cleaned_seq) < min_len:
                removed_short += 1
                flog.write(f"[❌] Removed short sequence {header} length={len(cleaned_seq)}\n")
            else:
                seq_hash = hs(cleaned_seq)
                if seq_hash in seen_hashes:
                    removed_duplicate += 1
                    flog.write(f"[❌] Removed duplicate sequence {header}\n")
                else:
                    seen_hashes.add(seq_hash)
                    fout.write(f"{header}\n")
                    for i in range(0, len(cleaned_seq), 80):
                        fout.write(cleaned_seq[i : i + 80] + "\n")
                    kept_seqs += 1

        # Create all deleted operations in sequence in the log file.
        flog.write(f"\n{"="*20} Summary {"="*20}\n")
        flog.write(f"Total sequences processed: {total_seqs}\n")
        flog.write(f"Sequences kept: {kept_seqs}\n")
        flog.write(f"Removed short sequences (<{min_len}): {removed_short}\n")
        flog.write(f"Removed duplicate sequences: {removed_duplicate}\n")

        print("[✅] Cleaning sequence done. Check results folder and pure_sequence.fasta file.")
