import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# find output data directory
output_dir = os.path.join(os.path.dirname(__file__), "results")
os.makedirs(output_dir, exist_ok=True)

# load datas
csv_path = os.path.join(os.path.dirname(__file__), "datas", "CSV_files", "gene_expression_data.csv")
rpc = pd.read_csv(csv_path)

# define expression columns
ex_columns = ["Sample_1", "Sample_2", "Sample_3", "Sample_4"]

# handling error not data in csv file
if "Conditions" not in rpc.columns or "Gene" not in rpc.columns:
    raise ValueError("Missing 'Gene' or 'Conditions' column in the CSV file.")

# extract gene and condition information
genes = rpc["Gene"]
conditions = rpc["Conditions"]
ex_data = rpc[ex_columns].copy()
ex_data["Conditions"] = conditions

# grouping Gene, Conditions data and sorting csv file datas
mean_rpc = rpc.groupby(["Gene", "Conditions"])[ex_columns].mean().reset_index()
pivot = mean_rpc.pivot(index="Gene", columns="Conditions", values=ex_columns)
mean_per_condition = pivot.groupby(axis=1, level=1).mean()
mean_per_condition = mean_per_condition.dropna(subset=["Tumor", "Normal"])

# handling error not data tumor and normal in csv file
if mean_per_condition.empty:
    print("bar image not created. because gene not have (Tumor) and (Normal) data")
    exit()

# calculate expression difference
mean_per_condition["Delta"] = mean_per_condition["Tumor"] - mean_per_condition["Normal"]

# select top 3 genes with highest differential expression
pivot_mean_sorted = mean_per_condition.reindex(mean_per_condition["Delta"].abs().sort_values(ascending=False).index)
top_genes = pivot_mean_sorted.head(3)

# bar plot for top genes
plt.figure(figsize=(10, 2))
top_genes_sorted = top_genes.sort_values("Delta")
plt.barh(top_genes_sorted.index, top_genes_sorted["Delta"], color="orange")
plt.xlabel("Gene expression difference (Tumor - Normal)")
plt.title("Top genes with largest expression difference")
plt.grid(True, axis="x")
plt.tight_layout()
plt.savefig(os.path.join(output_dir, f"barplot_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.png"))

# Heatmap for selected genes
selected_genes = top_genes.index
heatmap_data = rpc[rpc["Gene"].isin(selected_genes)].set_index("Gene")
heatmap_data = heatmap_data[ex_columns]

# Ensure data is not empty
if heatmap_data.empty:
    print("bar image not created. data not found")
    exit()

plt.figure(figsize=(8, 6))
sns.heatmap(heatmap_data, cmap="viridis", annot=True, fmt=".1f")
plt.title("Heatmap of selected gene expressions")
plt.tight_layout()
plt.savefig(os.path.join(output_dir, f"heatmap_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.png"))
