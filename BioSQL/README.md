# 🧬 BioSQL: Bioinformatics SQLite CLI Tool

BioSQL یک ابزار قدرتمند برای مدیریت، آنالیز و مشاهده داده‌های زیستی (DNA/RNA/Protein) با استفاده از SQLite و Python است.

## 📦 ویژگی‌ها

- ساخت دیتابیس برای ارگانیسم، توالی، فیچر
- وارد کردن داده‌ها از طریق CLI
- تحلیل توالی: GC content, reverse complement, RNA transcription
- ترجمه ORFها به پروتئین
- تولید گزارش Markdown
- نمایش گراف داده‌ها با NetworkX
- خروجی گراف در فرمت‌های `.gml`, `.graphml`, `.json`
- رسم گراف به صورت تصویری (`.png`)

## 🛠️ نصب

```bash
1.git clone https://github.com/yourusername/BioSQL
2.cd BioSQL
3.poetry install
4. run for create database:
    +. poetry run python3 src/cli.py initdb

+. run for add organism:
    ++. poetry run python3 src/cli.py add-organism
+. run for add sequence:
    ++. poetry run python3 src/cli.py add-sequence
+. run for add feature:
    ++. poetry run python src/cli.py add-feature
+. run for analysis and reporting:
    ++. poetry run python3 src/cli.py analyze-sequence --save --export results/<file_name>.md
+. run for get list of sequence:
    ++. poetry run python3 src/cli.py list-sequences
+. run test:
    ++. poetry run pytest tests/test_analysis.py
+. run for find orfs sequences:
    ++. poetry run python3 src/cli.py find-orfs
    or
    ++. poetry run python3 src/cli.py find-orfs --accession NM_000518 --min-length 20 --top 5
+. run for graph:
    ++. poetry run python3 src/cli.py show-graph-info
+. run for show sequence:
    ++. poetry run python3 src/cli.py view-sequence
+. run for export graph:
    ++. poetry run python3 src/cli.py export-graph --outdir ../results/graph_exports
+. run for Ritual graph:
    ++. poetry run python3 src/cli.py draw-graph