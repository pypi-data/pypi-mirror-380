#!/usr/bin/env python3
"""
Render a saved architecture JSON to an SVG using the new Graph.plot() API.

Usage:
  python scripts/visualize_arch.py <arch.json> <out.svg>
"""
import json
import os
import sys

# Ensure project root is importable when running this script directly
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from ggnes import Graph, NodeType  # noqa: E402


def main() -> int:
    if len(sys.argv) < 3:
        print("Usage: visualize_arch.py <arch.json> <out.svg>", file=sys.stderr)
        return 2

    arch_path = sys.argv[1]
    out_svg = sys.argv[2]

    if not os.path.exists(arch_path):
        print(f"Architecture file not found: {arch_path}", file=sys.stderr)
        return 1

    with open(arch_path, encoding="utf-8") as f:
        arch = json.load(f)

    g = Graph()

    # Maps for id resolution:
    #  - id_map: custom id -> custom id (wrapper uses custom ids)
    #  - idx_map: node list index -> custom id, for numeric edges ("0","1","2", ...)
    id_map: dict[str, str] = {}
    idx_map: dict[str, str] = {}

    for idx, n in enumerate(arch.get("nodes", [])):
        raw = str(n.get("node_type", ""))
        typ_name = raw.split(".")[-1] if raw else "HIDDEN"
        nt = getattr(NodeType, typ_name, NodeType.HIDDEN)

        custom_id = str(n.get("id"))
        # Wrapper Graph accepts top-level output_size; it will map to attributes internally
        g.add_node(
            {
                "id": custom_id,
                "node_type": nt,
                "activation_function": n.get("activation_function") or "relu",
                "output_size": n.get("output_size") or 32,
            }
        )
        id_map[custom_id] = custom_id
        idx_map[str(idx)] = custom_id

    for src, dst in arch.get("edges", []):
        s = id_map.get(str(src), idx_map.get(str(src), str(src)))
        d = id_map.get(str(dst), idx_map.get(str(dst), str(dst)))
        try:
            g.add_edge(s, d)
        except Exception:
            # Ignore duplicates or malformed edges safely
            pass

    out_dir = os.path.dirname(out_svg)
    if out_dir and not os.path.exists(out_dir):
        os.makedirs(out_dir, exist_ok=True)

    ret = g.plot(location=out_svg)
    print(ret)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
