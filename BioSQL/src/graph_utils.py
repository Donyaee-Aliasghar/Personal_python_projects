import networkx as nx
import os

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

    return {
        "graphml": graphml_path,
        "gml": gml_path,
        "json": json_path
    }
