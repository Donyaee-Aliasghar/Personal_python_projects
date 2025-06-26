how to run project?
    1. cd the Biofile_manager folder
    ?. python3 -m src.cli [-h] -i INPUT -f {fasta,fastq} [-o OUTPUT] [--minlen MINLEN] [--maxlen MAXLEN] [--minqual MINQUAL] [--maxqual MAXQUAL]
    2. example ==> python3 -m src.cli -i datas/example.fasta -f fasta -o 1.txt --maxlen 20