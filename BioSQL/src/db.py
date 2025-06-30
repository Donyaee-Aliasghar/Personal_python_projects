import sqlite3
import os


def connect_db():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "db", "bio.db")
    conn = sqlite3.connect(db_path)
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn


def create_tables(conn):
    cursor = conn.cursor()
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS organism (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE NOT NULL,
        taxonomy TEXT NOT NULL,
        metadata TEXT
    );"""
    )
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS sequence (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        organism_id INTEGER NOT NULL,
        accession TEXT UNIQUE NOT NULL,
        description TEXT,
        seq TEXT NOT NULL,
        alphabet TEXT CHECK(alphabet IN ('DNA', 'RNA', 'PROTEIN')) NOT NULL,
        FOREIGN KEY (organism_id) REFERENCES organism(id)
    );"""
    )
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS feature (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sequence_id INTEGER NOT NULL,
        feature_type TEXT NOT NULL,
        start_pos INTEGER NOT NULL,
        end_pos INTEGER NOT NULL,
        strand TEXT CHECK(strand IN ('+', '-')) NOT NULL,
        FOREIGN KEY (sequence_id) REFERENCES sequence(id)
    );"""
    )
    conn.commit()


def add_organism(conn, name, taxonomy, metadata=None):
    cursor = conn.cursor()
    try:
        cursor.execute("ALTER TABLE organism ADD COLUMN metadata TEXT")
        cursor.execute("INSERT INTO organism (name, taxonomy, metadata) VALUES (?, ?, ?)", (name, taxonomy, metadata))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False


def add_sequence(conn, organism_id, accession, description, seq, alphabet):
    cursor = conn.cursor()
    try:
        for column in ["gc_content", "rev_complement", "transcribed_rna"]:
            try:
                cursor.execute(f"ALTER TABLE sequence ADD COLUMN {column} TEXT")
            except sqlite3.OperationalError:
                pass
            conn.commit()
        cursor.execute(
            "INSERT INTO sequence (organism_id, accession, description, seq, alphabet) VALUES (?, ?, ?, ?, ?)",
            (organism_id, accession, description, seq, alphabet),
        )
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False


def add_feature(conn, sequence_id, feature_type, start_pos, end_pos, strand):
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO feature (sequence_id, feature_type, start_pos, end_pos, strand) VALUES (?, ?, ?, ?, ?)",
            (sequence_id, feature_type, start_pos, end_pos, strand),
        )
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False


def get_organism_by_name(conn, name):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM organism WHERE name = ?", (name,))
    return cursor.fetchone()


def get_sequence_by_accession(conn, accession):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sequence WHERE accession = ?", (accession,))
    return cursor.fetchone()


def export_analysis_to_markdown(accession, counts, gc, rev_comp, rna, output_path):
    with open(output_path, "w") as f:
        f.write(f"# Sequence Analysis Report: {accession}\n\n")
        f.write(f"**GC Content:** {gc}%\n\n")
        f.write("**Nucleotide Counts:**\n")
        for nt, count in counts.items():
            f.write(f"- {nt}: {count}\n")
        f.write(f"\n**Reverse Complement:**\n```\n{rev_comp}\n```\n")
        f.write(f"\n**Transcribed RNA:**\n```\n{rna}\n```\n")
