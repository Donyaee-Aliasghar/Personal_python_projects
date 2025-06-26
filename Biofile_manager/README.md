how to run project?
    1. cd the Biofile_manager folder
    ?. poetry run python3 -m src.biofile_manager.cli [-h] -i INPUT -f {fasta,fastq} [-o OUTPUT] [--minlen <number>] [--maxlen <number>] [--minqual <number>] [--maxqual <number>]
    2. example ==> poetry run python3 -m src.biofile_manager.cli -i datas/example.fasta -f fasta -o 1.png --minlen 20 