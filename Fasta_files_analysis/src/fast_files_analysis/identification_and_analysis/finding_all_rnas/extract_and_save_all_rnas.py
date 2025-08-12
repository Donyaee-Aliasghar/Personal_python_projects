"""Module for RNAs operations."""

import pandas as pd

from typing import List
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO
from Bio.Seq import Seq

from pathes import FAR_OUTPUT_DIR
from .datas.rna_types import rna_types


def filter_rna_types(df: pd.DataFrame, rna_types: List[str]) -> pd.DataFrame:
    """Filterting type of RNAs."""
    return df[(df["feature"] == "gene") & (df["gene_biotype"].isin(rna_types))]


def easa_rnas(df: pd.DataFrame, data: List[str]) -> None:
    """Extrect and save all type of RNAs in output file operation."""

    # Processing for get part of descriptoin.
    description = data.description
    parts = description.split()
    chrom_info = parts[1]
    chrom_parts = chrom_info.split(":")
    value = chrom_parts[1]

    rna_df = filter_rna_types(df, rna_types)

    for rna_type in rna_types:
        sub_df = rna_df[rna_df["gene_biotype"] == rna_type]
        if sub_df.empty:
            print(f"[❌] No {rna_type} Found.")
            continue

        records: SeqRecord = []
        for _, row in sub_df.iterrows():
            start = row["start"] - 1  # convert to 0-based
            end = row["end"]
            seq = data[start:end]
            if row["strand"] == "-":
                seq = seq.reverse_complement()
            seq_str = str(seq)

            # Create SeqRecord for save in FASTA.
            record = SeqRecord(
                seq_str,
                id=row["gene_id"],
                description=f"gene name: {row["gene_name"]}, RNA type: {rna_type} row sequence name {row["seqname"]}: {row["start"]}(start)-{row["end"]}(end) strand: ({row["strand"]})",
            )
            records.append(record)

        # save output file.
        output_file = f"{FAR_OUTPUT_DIR}/{value}_{rna_type}.fasta"
        SeqIO.write(records, output_file, "fasta")
        print(f"[✅] Saved {len(records):,} sequence of {rna_type} to {output_file}")
