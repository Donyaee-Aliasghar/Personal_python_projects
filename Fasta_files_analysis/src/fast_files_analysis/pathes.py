"""Module for insert input file and output file paths."""

from pathlib import Path

# Current python file path.
CURRENT_FILE = Path(__file__).resolve()

# =================== This part mine. ============================
MAIN_RAW_DATAS_FOLDER = CURRENT_FILE.parent.parent.parent.parent.parent.parent  # Get raw datas folder.
MAIN_RAW_FILE = MAIN_RAW_DATAS_FOLDER / "Raw_datas/Bioinformatics/FASTA/Homo_sapiens.GRCh38.dna.chromosome.1.fa"
# ==================== This part yourse. ===========================
# # Get root parent folder.
# parent_folder = CURRENT_FILE.parent.parent.parent  # go 2 folder back

# # Get main file.
# RAW_DATA = parent_folder / "datas/fasta.fa"
# ===============================================

# Root project path.
ROOT_PATH = CURRENT_FILE.parent.parent.parent  # go 3 folder back.

# Pure sequence file output path.
OUTPUT_DIR = Path(f"{ROOT_PATH}/results/outputs")
OUTPUT_DIR.mkdir(exist_ok=True)

LOG_DIR = Path(f"{ROOT_PATH}/results/log")
LOG_DIR.mkdir(exist_ok=True)
