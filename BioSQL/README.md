1. go directory BioSQL
2. run for create database:
    +. poetry run python3 src/cli.py initdb
3. run for add organism:
    +. poetry run python3 src/cli.py add-organism
4. run for add sequence:
    +. poetry run python3 src/cli.py add-sequence
5. run for add feature:
    +. poetry run python src/cli.py add-feature
6. run for analysis and reporting:
    +. poetry run python3 src/cli.py analyze-sequence --save --export datas/<file_name>.md
7. run test:
    +. poetry run pytest tests/test_analysis.py
8. run for find orfs sequences:
    +. poetry run python3 src/cli.py find-orfs
9. run for graph:
    +. poetry run python3 src/cli.py show-graph-info
10. run for export graph:
    +. poetry run python3 src/cli.py export-graph --outdir results/graph_exports
