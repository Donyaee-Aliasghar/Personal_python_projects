def export_fastq(records, output_file: str) -> None:
    with open(output_file, "w") as f:
        for r in records:
            f.write(f"@{r.header}\n{r.sequence}\n+\n{r.quality}\n")


def export_fasta(records, output_file: str) -> None:
    with open(output_file, "w") as f:
        for r in records:
            f.write(f"@{r.header}\n{r.sequence}\n")
