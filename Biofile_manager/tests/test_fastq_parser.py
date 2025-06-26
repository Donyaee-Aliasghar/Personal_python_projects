import os
from parsers.fastq_parser import parse_fastq


def Test_parser_fastq():
    path = os.path.join(os.path.dirname(__file__), "datas", "example.fastq")
    records = list(parse_fastq(path))
    assert len(records) > 0
    for record in records:
        assert record.header
        assert record.sequence
        assert record.plus
        assert record.quality
        print(
            f"Header: {record.header}\n Length: {len(record)}\n Other header: {record.plus}\n Quality: {record.quality}"
        )
