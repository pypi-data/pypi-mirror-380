import os
from pathlib import Path

PROJECT_PATH = Path(os.path.dirname(os.path.dirname(__file__)))

TEST_PATH = PROJECT_PATH

DATA_PATH = PROJECT_PATH / 'data'
DATA_PATH_NEW = PROJECT_PATH / 'scripts' / 'data_genertion' # TODO: fix typo

GFP1_PATH = DATA_PATH / 'gfp1_seq.txt'
GFP_FIRST_EXP_FASTA = DATA_PATH / 'GFP_first_exp.fasta'

# tmp folder - for files that are dumped to disk during calculation
TMP_PATH = PROJECT_PATH / 'tmp'

# Experiments
EXPERIMENT_RESULTS = PROJECT_PATH / 'experiment_results'
CACHE_DIR = PROJECT_PATH / 'cache'

# Yeast
YEAST_DATA = DATA_PATH / 'yeast'
YEAST_FASTA_PATH = YEAST_DATA / 'GCF_000146045.2_R64_genomic.fna'
YEAST_GFF_PATH = YEAST_DATA / 'genomic.gff'
YEAST_GFF_DB_PATH = YEAST_DATA / 'yeast_gff.db'
YEAST_FIVE_PRIME_UTR = YEAST_DATA / 'SGD_all_ORFs_5prime_UTRs.fsa'
YEAST_THREE_PRIME_UTR = YEAST_DATA / 'SGD_all_ORFs_3prime_UTRs.fsa'
YEAST_README = YEAST_DATA / 'README.md'

# Human
HUMAN_DATA = DATA_PATH / 'human'
HUMAN_V34 = HUMAN_DATA / 'human_v34'
HUMAN_GTF_BASIC_GZ = HUMAN_V34 / 'gencode.v34.basic.annotation.gtf.gz'
HUMAN_GTF_BASIC = HUMAN_V34 / 'gencode.v34.basic.annotation.gtf'
HUMAN_GFF = HUMAN_V34 / 'gencode.v34.annotation.gff3'
HUMAN_GFF_GZ = HUMAN_V34 / 'gencode.v34.annotation.gff3.gz'
HUMAN_TRANSCRIPTS_FASTA_GZ = HUMAN_V34 / 'gencode.v34.transcripts.fa.gz'
HUMAN_TRANSCRIPTS_FASTA = HUMAN_V34 / 'gencode.v34.transcripts.fa'
HG38_CACHE_DIR = CACHE_DIR / 'genomes' / 'hg38'
HUMAN_GENOME_FASTA_GZ = HG38_CACHE_DIR / 'hg38.fa.gz'
HUMAN_GENOME_FASTA = HG38_CACHE_DIR / 'hg38.fa'
HUMAN_DB_PATH = HUMAN_V34 / 'dbs'
HUMAN_DB = HUMAN_DB_PATH / 'human_gff.db'
HUMAN_DB_BASIC = HUMAN_DB_PATH / 'human_gff_basic.db'
HUMAN_DB_BASIC_INTRONS = HUMAN_DB_PATH / 'human_gff_basic_introns.db'
HUMAN_DB_BASIC_INTRONS_GZ = HUMAN_DB_PATH / 'human_gff_basic_introns.db.gz'

# External
EXTERNAL_PATH = PROJECT_PATH / 'external'
RISEARCH_PATH = EXTERNAL_PATH / 'risearch'
RISEARCH1_PATH = RISEARCH_PATH / 'RIsearch1'
RISEARCH1_BINARY_PATH = RISEARCH1_PATH  / 'RIsearch'

SEQUENCE = 'Sequence'
INHIBITION = 'Inhibition(%)'
CANONICAL_GENE = 'Canonical Gene Name'
CELL_LINE_ORGANISM = 'Cell line organism'
VOLUME = 'ASO_volume(nM)'
CHEMICAL_PATTERN = 'Chemical_Pattern'
TREATMENT_PERIOD = 'Treatment_Period(hours)'
CELL_LINE = 'Cell_line'
TRANSFECTION = 'Transfection'
DENSITY = 'Density(cells/well)'
DENSITY_UPDATED = 'Density(cells_per_well)' # Avoiding /
MODIFICATION = 'Modification'
PREMRNA_FOUND = 'pre_mrna_found'
SENSE_START = 'sense_start'
SENSE_LENGTH = 'sense_length'
SENSE_TYPE = 'sense_type'
