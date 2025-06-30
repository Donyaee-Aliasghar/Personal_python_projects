import click
import time
import networkx as nx

from db import (
    connect_db,
    create_tables,
    add_organism,
    add_sequence,
    add_feature,
    get_organism_by_name,
    get_sequence_by_accession,
    export_analysis_to_markdown,
)
from rich.progress import Progress
from analysis import count_nucleotides, gc_content, reverse_complement, get_all_orfs, transcribe_dna_to_rna
from graph_utils import build_bio_graph, export_graph


@click.group()
def cli():
    pass


@cli.command()
def initdb():
    con = connect_db()
    create_tables(con)
    # show colored progress
    with Progress() as progress:
        task = progress.add_task("[cyan]Creating database...", total=100)
        while not progress.finished:
            progress.update(task, advance=1)
            time.sleep(0.03)
    click.echo(click.style("Database and Tables create successfuly", fg="green", bold=True))
    con.close()


@cli.command(name="add-organism")
@click.option("--name", prompt="Organism name", help="Please enter organism name.")
@click.option("--taxonomy", prompt="Organism taxonomy", help="Please enter taxonomy.")
@click.option("--metadata", prompt="Metadata (optional)", default="", help="Optional metadata for the organism.")
def add_organism_cmd(name, taxonomy, metadata):
    conn = connect_db()
    success = add_organism(conn, name, taxonomy, metadata)
    if success:
        click.echo(click.style(f"Organism '{name}' added successfully.", fg="green", bold=True))
    else:
        click.echo(click.style(f"[Error]: Organism '{name}' already exists!", fg="red", bold=True))
    conn.close()


@cli.command(name="add-sequence")
@click.option("--organism_name", prompt="Organism name", help="The name of the organism associated with the sequence.")
@click.option("--accession", prompt="Accession", help="Accession sequence.")
@click.option("--description", prompt="Description", help="Description sequence.")
@click.option("--seq", prompt="Sequence", help="DNA/RNA/Protein sequence.")
@click.option("--alphabet", prompt="Alphabet (DNA/RNA/PROTEIN)", help="Type of sequence (DNA, RNA or PROTEIN).")
def add_sequence_cmd(organism_name, accession, description, seq, alphabet):
    conn = connect_db()
    organism = get_organism_by_name(conn, organism_name)
    if not organism:
        click.echo(click.style("Organism not found, please add organism first.", fg="yellow", bold=True))
        conn.close()
        return
    organism_id = organism[0]
    success = add_sequence(conn, organism_id, accession, description, seq, alphabet.upper())
    if success:
        click.echo(click.style(f"Sequence '{accession}' adding successfuly", fg="green", bold=True))
    else:
        click.echo("[Error] adding sequence.", fg="red", bold=True)
    conn.close()


@cli.command(name="add-feature")
@click.option("--accession", prompt="Accession sequence", help="Accession is the sequence associated with the feature.")
@click.option("--feature_type", prompt="type of Feature", help="Feature type (exon, intron, promoter, etc.).")
@click.option("--start_pos", prompt="Starting position", type=int, help="Feature start position.")
@click.option("--end_pos", prompt="End position", type=int, help="End position of the feature.")
@click.option("--strand", prompt="Strand (+/-)", help="Strand direction (+ or -).")
def add_feature_cmd(accession, feature_type, start_pos, end_pos, strand):
    conn = connect_db()
    sequence = get_sequence_by_accession(conn, accession)
    if not sequence:
        click.echo(click.style("Sequence not found, please add the sequence first.", fg="yellow", bold=True))
        conn.close()
        return
    sequence_id = sequence[0]
    success = add_feature(conn, sequence_id, feature_type, start_pos, end_pos, strand)
    if success:
        click.echo(click.style(f"Feature '{feature_type}' adding successfuly.", fg="green", bold=True))
    else:
        click.echo(click.style("[Error] adding feature.", fg="red", bold=True))
    conn.close()


@cli.command(name="analyze-sequence")
@click.option("--accession", prompt="Sequence accession", help="Accession of sequence to analyze.")
@click.option("--save", is_flag=True, help="Save analysis results in the database.")
@click.option("--export", type=click.Path(), help="Path to the Markdown output file for the report.")
def analyze_sequence_cmd(accession, save, export):
    conn = connect_db()
    seq_row = get_sequence_by_accession(conn, accession)
    if not seq_row:
        click.echo(click.style("Sequence not found.", fg="red", bold=True))
        return

    seq = seq_row[4]

    counts = count_nucleotides(seq)
    gc = gc_content(seq)
    rev_comp = reverse_complement(seq)
    rna = transcribe_dna_to_rna(seq)

    click.echo(click.style(f"\nAnalysis of sequence '{accession}':", bold=True))
    click.echo(f"Counts: {counts}")
    click.echo(f"GC Content: {gc}%")
    click.echo(f"Reverse Complement: {rev_comp}")
    click.echo(f"Transcribed RNA: {rna}")

    if save:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE sequence SET gc_content=?, rev_complement=?, transcribed_rna=? WHERE accession=?",
            (gc, rev_comp, rna, accession),
        )
        conn.commit()
        click.echo(click.style("The analysis was saved in the database.", fg="green", bold=True))

    if export:
        export_analysis_to_markdown(accession, counts, gc, rev_comp, rna, export)
        click.echo(click.style(f"Report saved in {export}.", fg="blue", bold=True))

    conn.close()


@cli.command(name="list-sequences")
def list_sequences_cmd():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT accession, description FROM sequence")
    rows = cursor.fetchall()
    if not rows:
        click.echo(click.style("No sequence recorded.", fg="yellow", bold=True))
    else:
        click.echo(click.style("\nsequence lists:\n", bold=True))
        for acc, desc in rows:
            click.echo(f"🔹 {acc}: {desc}")
    conn.close()


@cli.command(name="view-sequence")
@click.option("--accession", prompt="Sequence accession", help="The desired accession for displaying information.")
def view_sequence_cmd(accession):
    conn = connect_db()
    seq = get_sequence_by_accession(conn, accession)
    if not seq:
        click.echo(click.style("Sequence not found.", fg="red", bold=True))
        return
    click.echo(click.style(f"\nSequence information'{accession}':", bold=True))
    click.echo(f"Description: {seq[3]}")
    click.echo(f"Sequence: {seq[4]}")
    click.echo(f"Alphabet: {seq[5]}")
    click.echo(f"GC Content: {seq[6]}")
    click.echo(f"Reverse Complement: {seq[7]}")
    click.echo(f"Transcribed RNA: {seq[8]}")
    conn.close()


@cli.command(name="find-orfs")
@click.option("--accession", prompt="Sequence accession", help="Sequence accession for ORF search")
@click.option("--min-length", default=100, help="Minimum length of ORF (in amino acids)")
@click.option("--top", default=3, help="How many top ORFs to display")
def find_orfs_cmd(accession, min_length, top):
    conn = connect_db()
    seq_row = get_sequence_by_accession(conn, accession)
    if not seq_row:
        click.echo(click.style("Sequence not found.", fg="red", bold=True))
        return

    seq = seq_row[4]
    orfs = get_all_orfs(seq, min_length=min_length)
    if not orfs:
        click.echo(click.style("No valid ORF found.", fg="red", bold=True))
        return

    click.echo(click.style(f"\n🔍 Found {len(orfs)} ORFs (top {top} shown):\n", bold=True))
    for i, orf in enumerate(orfs[:top]):
        click.echo(f"{i+1}. Frame: {orf['frame']} ({orf['strand']}), Length: {orf['length']} aa")
        click.echo(f"   Protein: {orf['orf_protein'][:60]}...\n")
    conn.close()


@cli.command(name="show-graph-info")
def show_graph_info_cmd():
    conn = connect_db()
    G = build_bio_graph(conn)
    click.echo(click.style("📊 BioGraph Summary:", bold=True))
    click.echo(f"🔹 Nodes: {G.number_of_nodes()}")
    click.echo(f"🔹 Edges: {G.number_of_edges()}")

    from collections import Counter

    labels = [data.get("label", "unknown") for _, data in G.nodes(data=True)]
    counts = Counter(labels)
    for label, count in counts.items():
        click.echo(f"   - {label}: {count}")
    conn.close()


@cli.command(name="export-graph")
@click.option("--outdir", default="results", help="پوشه ذخیره فایل‌های گراف.")
def export_graph_cmd(outdir):
    """خروجی گرفتن گراف در فرمت‌های GraphML, GML, JSON"""
    conn = connect_db()
    G = build_bio_graph(conn)
    paths = export_graph(G, output_dir=outdir)
    click.echo(click.style("✅ Graph exported successfully!", fg="green", bold=True))
    for fmt, path in paths.items():
        click.echo(f"📁 {fmt.upper()}: {path}")
    conn.close()


if __name__ == "__main__":
    cli()
