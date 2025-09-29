import json
import os

import torch


def _make_toy_data():
    X = torch.randn(32, 8)
    y = X @ torch.randn(8, 1) + 0.05 * torch.randn(32, 1)
    return X, y


def test_prune_graph_contributing_deterministic_sorted():
    from ggnes.core.graph import Graph
    from ggnes.core.node import NodeType
    from ggnes.api.mvp import prune_graph_contributing

    g = Graph()
    inp = g.add_node({"node_type": NodeType.INPUT, "activation_function": "linear", "attributes": {"output_size": 8}})
    h1 = g.add_node({"node_type": NodeType.HIDDEN, "activation_function": "relu", "attributes": {"output_size": 16}})
    out = g.add_node({"node_type": NodeType.OUTPUT, "activation_function": "linear", "attributes": {"output_size": 1}})
    g.add_edge(inp, h1)
    g.add_edge(h1, out)
    # Dead branch: hidden node with no path to output
    dead = g.add_node({"node_type": NodeType.HIDDEN, "activation_function": "relu", "attributes": {"output_size": 16}})
    # Another dead node completely isolated
    g.add_node({"node_type": NodeType.HIDDEN, "activation_function": "relu", "attributes": {"output_size": 16}})

    g2 = prune_graph_contributing(g)
    # Expect only 3 nodes in the contributing path (inp, h1, out)
    assert len(getattr(g2, "nodes", {})) == 3
    # Re-running should be stable (same sizes / IDs may differ but count is same)
    g3 = prune_graph_contributing(g)
    assert len(getattr(g3, "nodes", {})) == 3


def test_search_writes_dual_arch_exports(tmp_path):
    from ggnes.api.mvp import Search

    X, y = _make_toy_data()
    s = Search(smoke=True, seed=123)
    res = s.fit(X, y, validation_data=(X, y))

    outdir = res.artifacts
    assert os.path.isdir(outdir)

    raw_path = os.path.join(outdir, "best_architecture_raw.json")
    pruned_path = os.path.join(outdir, "best_architecture_pruned.json")
    assert os.path.exists(raw_path)
    assert os.path.exists(pruned_path)

    with open(raw_path, "r", encoding="utf-8") as f:
        raw = json.load(f)
    with open(pruned_path, "r", encoding="utf-8") as f:
        prn = json.load(f)

    assert isinstance(raw.get("nodes", []), list)
    assert isinstance(prn.get("nodes", []), list)
    assert len(raw["nodes"]) >= len(prn["nodes"]) >= 1


def test_dead_nodes_objective_presence():
    from ggnes.api.mvp import Search

    X, y = _make_toy_data()
    s = Search(smoke=True, seed=7)
    s.objectives = [("val_mse", "min"), ("params", "min"), ("dead_nodes", "min")]
    res = s.fit(X, y, validation_data=(X, y))

    assert isinstance(res.pareto, list) and len(res.pareto) >= 1
    obj = res.pareto[0]["objectives"]
    assert "dead_nodes" in obj
    assert isinstance(obj["dead_nodes"], float)


