import os
import networkx as nx
import matplotlib.pyplot as plt


def build_bio_graph(conn):
    G = nx.DiGraph()

    cursor = conn.cursor()

    # add organism
    cursor.execute("SELECT id, name FROM organism")
    for org_id, name in cursor.fetchall():
        G.add_node(f"org:{org_id}", label="organism", name=name)

    # add sequence, ...
    cursor.execute("SELECT id, accession, organism_id FROM sequence")
    for seq_id, acc, org_id in cursor.fetchall():
        G.add_node(f"seq:{seq_id}", label="sequence", accession=acc)
        G.add_edge(f"org:{org_id}", f"seq:{seq_id}", relation="has_sequence")

    # add fichers,...
    cursor.execute("SELECT id, sequence_id, feature_type FROM feature")
    for feat_id, seq_id, feat_type in cursor.fetchall():
        G.add_node(f"feat:{feat_id}", label="feature", type=feat_type)
        G.add_edge(f"seq:{seq_id}", f"feat:{feat_id}", relation="has_feature")

    return G


def export_graph(G, output_dir="results"):
    os.makedirs(output_dir, exist_ok=True)

    # GraphML
    graphml_path = os.path.join(output_dir, "bio_graph.graphml")
    nx.write_graphml(G, graphml_path)

    # GML
    gml_path = os.path.join(output_dir, "bio_graph.gml")
    nx.write_gml(G, gml_path)

    # JSON
    json_path = os.path.join(output_dir, "bio_graph.json")
    data = nx.readwrite.json_graph.node_link_data(G)
    with open(json_path, "w") as f:
        import json

        json.dump(data, f, indent=2)

    return {"graphml": graphml_path, "gml": gml_path, "json": json_path}


def draw_graph(G, save_path="results/graph_plot.png"):
    pos = nx.spring_layout(G, seed=42)
    labels = nx.get_node_attributes(G, "label")

    color_map = {"organism": "skyblue", "sequence": "lightgreen", "feature": "salmon"}
    node_colors = [color_map.get(labels.get(node, "unknown"), "gray") for node in G.nodes]

    plt.figure(figsize=(12, 8))
    nx.draw_networkx(G, pos, with_labels=False, node_color=node_colors, node_size=600, edge_color="gray", alpha=0.8)

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(BASE_DIR, "results")
    nx.draw_networkx_labels(G, pos, labels={n: n for n in G.nodes}, font_size=8)
    plt.axis("off")
    plt.tight_layout()
    plt.savefig(save_path)
    # plt.savefig(path)
    plt.close()
    return save_path
