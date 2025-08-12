"""Module for insert input file and output file paths."""

from pathlib import Path

# Current python file path.
CURRENT_FILE = Path(__file__).resolve()

# =================== This part is mine. ============================
MAIN_RAW_FASTA_FILE = "/home/ubuntu/Programming/Raw_datas/Bioinformatics/FASTA/Homo_sapiens.GRCh38.dna.chromosome.1.fa"
MAIN_RAW_GTF_FILE = "/home/ubuntu/Programming/Raw_datas/Bioinformatics/GTF/Homo_sapiens.GRCh38.114.chr.gtf"
# ==================== This part is yourse. ===========================
# # Get root parent folder.
# parent_raw_data_folder = CURRENT_FILE.parent.parent.parent  # go 2 folder back

# # Get main file.
# MAIN_RAW_FILE = parent_raw_data_folder / "datas/fasta.fa"
# ===============================================

# Root project path.
ROOT_PATH = CURRENT_FILE.parent.parent.parent  # go 3 folder back.

# Pure sequence file output path.(pure file)
PS_OUTPUT_DIR = Path(f"{ROOT_PATH}/results/outputs")
PS_OUTPUT_DIR.mkdir(exist_ok=True)

# Fasta file purification details path.(log file)
FFPD_LOG_DIR = Path(f"{ROOT_PATH}/results/logs")
FFPD_LOG_DIR.mkdir(exist_ok=True)

# Get results directory files.
parent_pure_sequence_folder = CURRENT_FILE.parent.parent.parent
PS_FILE = parent_pure_sequence_folder / "results/outputs/pure_sequence.fasta"

# Repeat regions and interspersed repeats output file path.
RRAIR_OUTPUT_DIR = Path(f"{PS_OUTPUT_DIR}/repeat_regions_and_interspersed_repeats_operations")
RRAIR_OUTPUT_DIR.mkdir(exist_ok=True)

# Gene and regulatory element annotation output file path.
GAREA_OUTPUT_DIR = Path(f"{PS_OUTPUT_DIR}/gene_and_regulatory_element_annotation")
GAREA_OUTPUT_DIR.mkdir(exist_ok=True)

# Find all RNAs output file path.
FAR_OUTPUT_DIR = Path(f"{PS_OUTPUT_DIR}/finding_all_rnas")
FAR_OUTPUT_DIR.mkdir(exist_ok=True)
