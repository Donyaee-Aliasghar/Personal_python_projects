CREATE TABLE organism (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    taxonomy TEXT NOT NULL,
    metadata JSON -- or TEXT
);
CREATE TABLE sequence (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    organism_id INTEGER NOT NULL,
    accession TEXT UNIQUE NOT NULL,
    description TEXT NOT NULL,
    seq TEXT NOT NULL,
    alphabet TEXT CHECK(alphabet IN ("DNA", "RNA", "PROTEIN")) NOT NULL,
    FOREIGN KEY (organism_id) REFERENCES organism(id)
);
CREATE TABLE feature (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sequence_id INTEGER NOT NULL,
    feature_type TEXT NOT NULL,
    start_pos INTEGER NOT NULL,
    end_pos INTEGER NOT NULL,
    strand TEXT CHECK(strand IN ("+","-")) NOT NULL,
    FOREIGN KEY (sequence_id) REFERENCES sequence(id)
);
CREATE TABLE analysis (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sequence_id INTEGER,
    feature_id INTEGER,
    analysis_type TEXT NOT NULL,
    result TEXT NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (sequence_id) REFERENCES sequence(id),
    FOREIGN KEY (feature_id) REFERENCES feature(id)
);
CREATE TABLE metadata(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    organism_id INTEGER,
    sequence_id INTEGER,
    key TEXT NOT NULL,
    value TEXT NOT NULL,
    FOREIGN KEY (organism_id) REFERENCES organism(id),
    FOREIGN KEY (sequence_id) REFERENCES sequence(id)
);
