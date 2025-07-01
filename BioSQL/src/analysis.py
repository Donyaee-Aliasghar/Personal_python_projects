from Bio.Seq import Seq


def count_nucleotides(seq):
    return {
        "A": seq.upper().count("A"),
        "T": seq.upper().count("T"),
        "G": seq.upper().count("G"),
        "C": seq.upper().count("C"),
    }


def gc_content(seq):
    seq = seq.upper()
    gc = seq.count("G") + seq.count("C")
    return round((gc / len(seq)) * 100, 2) if seq else 0


def reverse_complement(seq):
    mapping = str.maketrans("ATGC", "TACG")
    return seq.upper().translate(mapping)[::-1]


def transcribe_dna_to_rna(seq):
    return seq.upper().replace("T", "U")


def get_all_orfs(seq, min_length=100):
    seq = Seq(seq.upper())
    orfs = []

    for strand, nuc in [(+1, seq), (-1, seq.reverse_complement())]:
        for frame in range(3):
            trans = nuc[frame:].translate(to_stop=False)
            aa_seq = str(trans)
            current_orf = ""
            in_orf = False
            for i, aa in enumerate(aa_seq):
                if aa == "M":
                    in_orf = True
                    current_orf = "M"
                elif aa == "*":
                    if in_orf and len(current_orf) >= min_length:
                        start_pos = frame + i * 3
                        orfs.append(
                            {
                                "frame": frame if strand == 1 else -(frame + 1),
                                "strand": "+" if strand == 1 else "-",
                                "orf_protein": current_orf,
                                "length": len(current_orf),
                            }
                        )
                    in_orf = False
                    current_orf = ""
                elif in_orf:
                    current_orf += aa
    return sorted(orfs, key=lambda x: x["length"], reverse=True)


def get_best_orf(seq):
    orfs = get_all_orfs(seq)
    return orfs[0] if orfs else None
