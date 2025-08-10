"""Module for insert input file and output file paths."""

from pathlib import Path

# current python file path.
CURRENT_FILE = Path(__file__).resolve()

#! this paths is in my system.
# get raw datas folder.
MAIN_RAW_DATAS_FOLDER = CURRENT_FILE.parent.parent.parent.parent.parent.parent
MAIN_RAW_FILE = MAIN_RAW_DATAS_FOLDER / "Raw_datas/Bioinformatics/FASTA/Homo_sapiens.GRCh38.dna.chromosome.1.fa"

#! this paths is you must used.
# # get root parent folder.
# parent_folder = CURRENT_FILE.parent.parent.parent  # go 2 folder back

# # get main file.
# RAW_DATA = parent_folder / "datas/fasta.fa"
