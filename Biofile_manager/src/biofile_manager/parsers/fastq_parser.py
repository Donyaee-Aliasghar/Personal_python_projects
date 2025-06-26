class FastqRecord:
    def __init__(self, header: str, sequence: str, plus: str, quality: str):
        self.header = header
        self.sequence = sequence
        self.plus = plus
        self.quality = quality

    def __len__(self) -> int:
        return len(self.sequence)

    def mean_quality(self) -> float:
        return sum(ord(q) - 33 for q in self.quality) / len(self.quality)


def parse_fastq(file_path: str):
    with open(file_path, "r") as f:
        while True:
            header = f.readline().strip()
            if not header:
                break
            sequence = f.readline().strip()
            plus = f.readline().strip()
            quality = f.readline().strip()
            if not (header.startswith("@") and plus.startswith("+")):
                raise ValueError("Invalid FASTQ format")
            yield FastqRecord(header[1:], sequence, plus, quality)
