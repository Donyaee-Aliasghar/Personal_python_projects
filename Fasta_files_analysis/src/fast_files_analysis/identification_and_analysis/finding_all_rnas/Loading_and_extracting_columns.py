"""The task of this module is to lead and extract important columns from the main gtf file."""

import pandas as pd

from typing import List


def get_gtf_attribute_field(attribute_str: str, filed_name: str) -> None:
    """Geting attributes filed from gtf file."""
    attrs = attribute_str.strip().split(";")
    for attr in attrs:
        attr = attr.strip()
        if attr.startswith(filed_name):
            parts = attr.split(" ")
            if len(parts) >= 2:
                return parts[1].strip('"')
    return None


def get_gene_id(attribute_str) -> None:
    """Send data to get_gtf_attribute_field function."""
    return get_gtf_attribute_field(attribute_str, "gene_id")


def get_gene_name(attribute_str) -> None:
    """Send data to get_gtf_attribute_field function."""
    return get_gtf_attribute_field(attribute_str, "gene_name")


def get_gene_biotype(attribute_str) -> None:
    """Send data to get_gtf_attribute_field function."""
    return get_gtf_attribute_field(attribute_str, "gene_biotype")


def get_transcript_id(attribute_str) -> None:
    """Send data to get_gtf_attribute_field function."""
    return get_gtf_attribute_field(attribute_str, "transcript_id")


def load_gtf(gtf_path: str) -> pd.DataFrame:
    """load gtf file with attributes."""
    gtf_cols: List[str] = ["seqname", "source", "feature", "start", "end", "score", "strand", "frame", "attribute"]
    df = pd.read_csv(gtf_path, sep="\t", comment="#", names=gtf_cols, dtype=str)
    df["start"] = df["start"].astype(int)
    df["end"] = df["end"].astype(int)
    df["gene_id"] = df["attribute"].apply(get_gene_id)
    df["gene_name"] = df["attribute"].apply(get_gene_name)
    df["gene_biotype"] = df["attribute"].apply(get_gene_biotype)
    df["transcript_id"] = df["attribute"].apply(get_transcript_id)

    print("[✅] Load GTF and processings done.")

    return df
