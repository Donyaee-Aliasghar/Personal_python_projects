CREATE TABLE organism (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOY NULL,
    taxonomy TEXT NOT NULL
);
INSERT INTO organism (name, taxonomy)
VALUES 
    ('Homo sapiens','Eukaryota,Metazoa'),
    ('E.coli','Bacteria,Gammaproteo');

CREATE TABLE sequence (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    organism_id INTEGER,
    accession TEXT UNIQUE NOT NULL,
    description TEXT NOT NULL,
    seq_dna TEXT NOT NULL,
    alphabet TEXT CHECK(alphabet IN ("DNA", "RNA", "PROTEIN")) NOT NULL,
    FOREIGN KEY (organism_id) REFERENCES organism(id)
);
INSERT INTO sequence (accession, description, seq_dna, alphabet)
VALUES 
    ('NM_000518', 'Beta-globin gene', 'ATGGTGCACCTGACT', 'DNA'),
    ('EC_001', 'lacZ gene fragment', 'ATGAATATCCTCCAGTGTGGAAT', 'DNA');

CREATE TABLE feature (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sequence_id INTEGER,
    feature_type TEXT NOT NULL,
    start INTEGER NOT NULL,
    end INTEGER NOT NULL,
    strand TEXT CHECK(strand IN ("+","-")) NOT NULL,
    FOREIGN KEY (sequence_id) REFERENCES sequence(id)
);
INSERT INTO feature (feature_type, start, end, strand)
VALUES 
    ('exon', 1, 150, '+'),
    ('CDS', 30, 120, '+'),
    ('promoter', 35, 1, '-');

