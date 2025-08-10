"""Module for insert input file and output file paths."""

from pathlib import Path

# Current python file path.
CURRENT_FILE = Path(__file__).resolve()

#! This paths is in my system(please comment this part and use below codes).
# Get raw datas folder.
MAIN_RAW_DATAS_FOLDER = CURRENT_FILE.parent.parent.parent.parent.parent.parent
MAIN_RAW_FILE = MAIN_RAW_DATAS_FOLDER / "Raw_datas/Bioinformatics/FASTA/Homo_sapiens.GRCh38.dna.chromosome.1.fa"

#! This paths is you must used.
# # Get root parent folder.
# parent_folder = CURRENT_FILE.parent.parent.parent  # go 2 folder back

# # Get main file.
# RAW_DATA = parent_folder / "datas/fasta.fa"
