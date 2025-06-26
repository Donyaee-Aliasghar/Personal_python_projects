class FastaRecord:
    def __init__(self, header: str, sequence: str):
        self.header = header
        self.sequence = sequence

    def __len__(self) -> int:
        return len(self.sequence)


def parse_fasta(file_path: str):
    with open(file_path, "r") as f:
        header = None
        sequence = []
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line.startswith(">"):
                if header:
                    yield FastaRecord(header, "".join(sequence))
                header = line[1:]  # remove ">"
                sequence = []
            else:
                sequence.append(line)
        if header:
            yield FastaRecord(header, "".join(sequence))
