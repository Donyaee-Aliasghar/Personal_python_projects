"""Module to clean the raw fasta file and remove all impurities."""

from .cleaning_sequence import cs
from .hash_seq import hs

from ..pathes import OUTPUT_DIR, LOG_DIR


def pf(input_file: str, min_len=30, allowed_bases: set[str] = set("ATGC")):
    """Main operation for file purification."""
    seen_hashes = set()
    total_seqs = 0
    removed_short = 0
    removed_dupicate = 0
    kept_seqs = 0

    with open(input_file, "r", encoding="utf-8") as fin, open(OUTPUT_DIR, "w", encoding="utf-8") as fout, open(
        LOG_DIR, "w", encoding="utf-8"
    ) as flog:
        header = None
        seq_chunks = []

        # Operation on the original file to purify it of all impurities.
        for line in fin:
            line = line.strip()
            if not line:
                continue
            if line.startswith(">"):
                if header is not None:
                    total_seqs += 1
                    full_seq = "".join(seq_chunks)
                    cleaned_seq = cs(full_seq, allowed_bases)

                    # Operation to delete sequences shorter than 30
                    if len(cleaned_seq) < min_len:
                        removed_short += 1
                        flog.write(f"[❌] Removed short sequence {header} length={len(cleaned_seq)}\n")
                    # Operation to allowed sequences longer than 31
                    else:
                        seq_hash = hs(cleaned_seq)
                        if seq_hash in seen_hashes:
                            removed_dupicate += 1
                            flog.write(f"[❌] Removed duplicate sequence {header}\n")
                        else:
                            seen_hashes.add(seq_hash)
                            fout.write(f"{header}\n")

                            for i in range(0, len(cleaned_seq), 80):
                                fout.write(cleaned_seq[i : i + 80] + "\n")
                                kept_seqs += 1
                                header = line.split()[0]
                                seq_chunks = []
            else:
                seq_chunks.append(line)

        if header is not None:
            total_seqs += 1
            full_seq = "".join(seq_chunks)
            cleaned_seq = cleaned_seq(full_seq, allowed_bases)

            # Operation to delete sequences shorter than 30
            if len(cleaned_seq) < min_len:
                removed_short += 1
                flog.write(f"[❌] Removed duplicate sequence {header} length={len(cleaned_seq)}\n")
            # Operation to allowed sequences longer than 31
            else:
                seq_hash = hs(cleaned_seq)
                if seq_hash in seen_hashes:
                    removed_dupicate += 1
                    flog.write(f"[❌] Removed duplicate sequence {header}\n")
                else:
                    seen_hashes.add(seq_hash)
                    fout.write(f"{header}\n")
                    for i in range(0, len(cleaned_seq), 80):
                        fout.write(cleaned_seq[i : i + 80] + "\n")
                        kept_seqs += 1

        # Create all deleted operations in sequence in the log file.
        flog.write("\n========== Summary ==========\n")
        flog.write(f"Total sequences processed: {total_seqs}\n")
        flog.write(f"Sequences kept: {kept_seqs}\n")
        flog.write(f"Removed short sequnces (<{min_len}): {removed_short}\n")
        flog.write(f"Removed duplicate sequnces: {removed_dupicate}\n")

        print("[✅] Cleaning done. Check log file for details.")
