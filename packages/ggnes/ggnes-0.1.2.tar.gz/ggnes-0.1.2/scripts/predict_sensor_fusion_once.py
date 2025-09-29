#!/usr/bin/env python3
import argparse
import json
import os
import sys

# Reduce startup/thread overhead for quick preview runs
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("NUMEXPR_NUM_THREADS", "1")
os.environ.setdefault("PYTORCH_JIT", "0")

def rebuild_graph_from_best_arch(best_arch_path: str):
    from ggnes import Graph, NodeType  # wrapper Graph preferred from ggnes.__init__
    with open(best_arch_path, "r", encoding="utf-8") as f:
        arch = json.load(f)

    g = Graph()
    idx_to_rid = []

    # Build nodes in order; edges refer to indices
    for n in arch.get("nodes", []):
        node_type_str = str(n.get("node_type", "NodeType.HIDDEN"))
        node_type_name = node_type_str.split(".")[-1]
        nt = getattr(NodeType, node_type_name, NodeType.HIDDEN)
        act = n.get("activation_function") or "relu"
        out_size = n.get("output_size")
        # Prefer wrapper-Graph top-level API; fallback to core-Graph attributes on error
        props_top = {"id": n.get("id"), "node_type": nt, "activation_function": act}
        if isinstance(out_size, int):
            props_top["output_size"] = int(out_size)

        try:
            rid = g.add_node(props_top)
        except Exception:
            attrs = {}
            if isinstance(out_size, int):
                attrs["output_size"] = int(out_size)
            props_attr = {"node_type": nt, "activation_function": act, "attributes": attrs}
            rid = g.add_node(props_attr)

        idx_to_rid.append(rid)

    # Add edges using index mapping
    for e in arch.get("edges", []):
        if not (isinstance(e, (list, tuple)) and len(e) == 2):
            continue
        try:
            s = idx_to_rid[int(e[0])]
            d = idx_to_rid[int(e[1])]
            g.add_edge(s, d)
        except Exception:
            # Ignore malformed edges gracefully for preview
            pass

    return g


def main():
    ap = argparse.ArgumentParser(description="Single prediction preview from best_architecture.json")
    ap.add_argument("--arch", default="demo/sensor_fusion_demo_output/best_architecture.json", help="Path to best_architecture.json")
    ap.add_argument("--seed", type=int, default=123, help="Torch seed for deterministic input")
    ap.add_argument("--json", action="store_true", help="Emit JSON only")
    args = ap.parse_args()

    try:
        import torch
        from ggnes.translation import to_pytorch_model
    except Exception as e:
        print(json.dumps({"error": f"Runtime import failure: {e}"}, indent=2))
        sys.exit(2)

    if not os.path.exists(args.arch):
        print(json.dumps({"error": f"Architecture file not found: {args.arch}"}, indent=2))
        sys.exit(3)

    # Rebuild graph from artifact
    try:
        g = rebuild_graph_from_best_arch(args.arch)
    except Exception as e:
        print(json.dumps({"error": f"Failed to rebuild graph: {e}"}, indent=2))
        sys.exit(4)

    # Build model and run a single forward
    try:
        torch.set_num_threads(1)
        torch.set_num_interop_threads(1)
    except Exception:
        pass

    try:
        torch.manual_seed(args.seed)
        model = to_pytorch_model(g, {"device": "cpu"})
        input_dim = sum(g.nodes[i].attributes.get("output_size", 0) for i in g.input_node_ids)
        if input_dim <= 0:
            raise RuntimeError(f"Computed input_dim={input_dim} from INPUT nodes {g.input_node_ids}")
        x = torch.randn(1, input_dim, dtype=torch.float32)
        with torch.no_grad():
            y = model(x)

        def fmt(t):
            return [round(float(v), 6) for v in t.reshape(-1).tolist()]

        result = {
            "arch_path": os.path.abspath(args.arch),
            "graph": {
                "num_nodes": len(g.nodes),
                "num_edges": sum(len(n.edges_out) for n in g.nodes.values()),
                "input_nodes": list(g.input_node_ids),
                "output_nodes": list(g.output_node_ids),
            },
            "input_dim": int(input_dim),
            "input": fmt(x),
            "output_dim": int(y.shape[1]) if y.ndim == 2 else int(y.numel()),
            "output": fmt(y if y.ndim == 2 else y.reshape(1, -1)),
        }

        if args.json:
            print(json.dumps(result, indent=2))
        else:
            print("\nSample prediction (sensor-fusion):")
            print(f"  arch:   {result['arch_path']}")
            print(f"  graph:  nodes={result['graph']['num_nodes']} edges={result['graph']['num_edges']}")
            print(f"  input:  dim={result['input_dim']}  x[0,:3]={result['input'][:3]}")
            print(f"  output: dim={result['output_dim']}  y={result['output']}")
            print("\nJSON:")
            print(json.dumps(result, indent=2))

    except Exception as e:
        print(json.dumps({"error": f"Failed to build model or run prediction: {e}"}, indent=2))
        sys.exit(5)


if __name__ == "__main__":
    main()
