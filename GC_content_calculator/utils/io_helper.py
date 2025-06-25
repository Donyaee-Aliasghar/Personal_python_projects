from Bio import SeqIO
from io import StringIO


def parser_sequence_file(uploaded_file):
    name = uploaded_file.name.lower()
    if name.endswith((".fasta", ".fa")):
        fmt = "fasta"
    elif name.endswith(".fastq"):
        fmt = "fastq"
    else:
        raise ValueError("Unsupported file type (just FASTA or FASTQ).")

    content = uploaded_file.read().decode("utf-8")
    handle = StringIO(content)
    return list(SeqIO.parse(handle, fmt))
