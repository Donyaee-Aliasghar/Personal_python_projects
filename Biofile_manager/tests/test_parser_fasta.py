import os
from parsers.fasta_parser import parse_fasta


def test_parser_fasta():
    path = os.path.join(os.path.dirname(__file__), "datas", "example.fasta")
    records = list(parse_fasta(path))
    assert len(records) > 0
    for record in records:
        assert record.header
        assert record.sequence
        print(f"Header: {record.header}\n Length: {len(record)}\n")
