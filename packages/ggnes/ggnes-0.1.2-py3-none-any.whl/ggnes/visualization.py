"""
Minimal, deterministic, dependency-free visualization for GGNES graphs.

Provides:
- render_svg(graph, path: str | None = None, options: dict | None = None) -> str
  - Produces a self-contained SVG string deterministically.
  - If path is provided, writes the SVG and returns the path; otherwise returns the SVG string.

- render_graphviz(graph, path: str | None = None, format: str = "svg", options: dict | None = None) -> str
  - Optional richer backend via graphviz if installed. If unavailable, falls back to render_svg for SVG
    or raises for non-SVG formats.
"""

from __future__ import annotations

import html
from typing import Any


def _bool(val: Any) -> bool:
    try:
        return bool(val)
    except Exception:
        return False


def _escape(s: Any) -> str:
    try:
        return html.escape(str(s))
    except Exception:
        return ""


def _get_nodes_sorted(graph) -> list[int]:
    # Deterministic ordering by node_id (stable across runs for same graph)
    return sorted(getattr(graph, "nodes", {}).keys())


def _incoming_enabled_edges(graph, node_id: int) -> list[tuple[int, Any]]:
    node = graph.nodes.get(node_id)
    if not node:
        return []
    in_map = node.edges_in
    # Handle both simple and multigraph adjacency
    if isinstance(in_map, dict) and in_map and isinstance(next(iter(in_map.values())), list):
        pairs = [(sid, e) for sid, lst in in_map.items() for e in lst]
    else:
        pairs = [(sid, e) for sid, e in in_map.items()]
    # Filter enabled edges
    return [(sid, e) for sid, e in pairs if getattr(e, "enabled", True)]


def _compute_layers(graph) -> dict[int, int]:
    """
    Compute deterministic integer layers for nodes:
    - INPUT nodes: layer 0
    - Others: 1 + max(layer of any enabled, non-recurrent predecessor)
    - Nodes not covered by topo order (due to cycles) get appended deterministically.
    """
    layers: dict[int, int] = {}
    try:
        if hasattr(graph, "detect_cycles"):
            graph.detect_cycles()
    except Exception:
        pass

    topo = []
    try:
        if hasattr(graph, "topological_sort"):
            topo = list(graph.topological_sort(ignore_recurrent=True))
    except Exception:
        topo = []

    # Start with inputs at layer 0
    inputs = set(getattr(graph, "input_node_ids", []) or [])
    for nid in _get_nodes_sorted(graph):
        if nid in inputs:
            layers[nid] = 0

    # Fill layers using topo order if available, else iterate sorted nodes
    order = list(topo) if topo else _get_nodes_sorted(graph)

    for nid in order:
        if nid in layers:
            continue
        preds = _incoming_enabled_edges(graph, nid)
        # Consider only non-recurrent predecessors
        src_layers = []
        for sid, e in preds:
            if getattr(e, "attributes", {}).get("is_recurrent", False):
                continue
            if sid in layers:
                src_layers.append(layers[sid])
        if src_layers:
            layers[nid] = max(src_layers) + 1
        else:
            # No known predecessors placed; put at layer 0 (isolated) to be deterministic
            layers[nid] = 0

    # Any nodes not assigned due to exceptional cases
    for nid in _get_nodes_sorted(graph):
        if nid not in layers:
            layers[nid] = 0

    return layers


def _layer_to_nodes(layers: dict[int, int]) -> dict[int, list[int]]:
    layer_map: dict[int, list[int]] = {}
    for nid, layer in layers.items():
        layer_map.setdefault(layer, []).append(nid)
    # Deterministic order within each layer
    for layer in layer_map:
        layer_map[layer].sort()
    return dict(sorted(layer_map.items(), key=lambda kv: kv[0]))


def _compute_coordinates(graph, options: dict[str, Any]) -> tuple[dict[int, tuple[float, float]], dict[int, list[int]], dict[int, int], dict[str, float]]:
    # Visual options
    width = float(options.get("width", 800))
    margin = float(options.get("margin", 20))
    layer_spacing = float(options.get("layer_spacing", 120))
    node_w = float(options.get("node_width", 140))
    node_h = float(options.get("node_height", 50))
    min_width = max(width, margin * 2 + node_w + 1.0)

    layers = _compute_layers(graph)
    layer_map = _layer_to_nodes(layers)
    max_layer = max(layer_map.keys()) if layer_map else 0
    height = margin * 2 + (max_layer + 1) * layer_spacing
    coords: dict[int, tuple[float, float]] = {}

    # For each layer, distribute nodes evenly horizontally
    for layer_idx, nodes_in_layer in layer_map.items():
        k = len(nodes_in_layer)
        if k <= 0:
            continue
        # horizontal step
        step = (min_width - 2 * margin) / (k + 1)
        y = margin + layer_idx * layer_spacing
        for idx, nid in enumerate(nodes_in_layer, start=1):
            x = margin + step * idx
            coords[nid] = (x, y)

    metrics = {
        "canvas_width": min_width,
        "canvas_height": height,
        "node_w": node_w,
        "node_h": node_h,
        "margin": margin,
    }
    return coords, layer_map, layers, metrics


def _svg_header(w: float, h: float) -> str:
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{int(w)}" height="{int(h)}" viewBox="0 0 {int(w)} {int(h)}">\n'


def _svg_footer() -> str:
    return "</svg>\n"


def _svg_rect(x: float, y: float, w: float, h: float, rx: float = 6.0, style: str = "") -> str:
    st = f' style="{style}"' if style else ""
    return f'<rect x="{x:.2f}" y="{y:.2f}" width="{w:.2f}" height="{h:.2f}" rx="{rx:.2f}" ry="{rx:.2f}"{st}/>\n'


def _svg_text(x: float, y: float, text: str, font_size: int = 12, anchor: str = "middle") -> str:
    return f'<text x="{x:.2f}" y="{y:.2f}" text-anchor="{anchor}" font-size="{font_size}">{_escape(text)}</text>\n'


def _edge_style(enabled: bool, recurrent: bool) -> str:
    stroke = "#444" if enabled else "#999"
    dash = "4,3" if (recurrent or not enabled) else "0"
    return f"stroke:{stroke};stroke-width:1.5;fill:none;stroke-dasharray:{dash}"


def render_svg(graph, path: str | None = None, options: dict | None = None) -> str:
    """
    Render graph to a deterministic SVG. If path is provided, writes to file and returns the path;
    otherwise returns the SVG string.
    """
    opts = dict(options or {})
    coords, layer_map, layers, metrics = _compute_coordinates(graph, opts)
    cw, ch = metrics["canvas_width"], metrics["canvas_height"]
    node_w, node_h = metrics["node_w"], metrics["node_h"]

    # Start SVG
    parts: list[str] = []
    parts.append(_svg_header(cw, ch))

    # Invalid graph banner
    invalid = False
    try:
        # Collect errors but do not fail rendering
        invalid = not bool(graph.validate())
    except Exception:
        # If validate not present/failed, do not mark invalid
        invalid = False

    if invalid:
        parts.append('<g data-warning="invalid-graph">\n')
        parts.append(_svg_rect(0, 0, cw, 20, rx=0, style="fill:#fee;border:0;"))
        parts.append(_svg_text(cw / 2.0, 14, "Invalid graph — rendering may be incomplete", font_size=12))
        parts.append("</g>\n")

    # Draw edges first (lines between node centers)
    # Use deterministic edge ordering: graph.list_edges() already sorts globally by edge_id (string) when no filters.
    try:
        edges = list(graph.list_edges())
    except Exception:
        edges = []

    for e in edges:
        sid = getattr(e, "source_node_id", None)
        tid = getattr(e, "target_node_id", None)
        if sid is None or tid is None:
            continue
        if sid not in coords or tid not in coords:
            continue
        (x1, y1) = coords[sid]
        (x2, y2) = coords[tid]
        # Offset start/end to node boundary rather than center for improved aesthetics
        # Keep deterministic math for identical SVG strings
        sx = x1 + 0.0
        sy = y1 + 0.0
        tx = x2 + 0.0
        ty = y2 + 0.0

        enabled = _bool(getattr(e, "enabled", True))
        recurrent = _bool(getattr(e, "attributes", {}).get("is_recurrent", False))
        edge_id = str(getattr(e, "edge_id", ""))

        style = _edge_style(enabled, recurrent)
        parts.append(
            f'<path class="edge" d="M {sx:.2f} {sy:.2f} L {tx:.2f} {ty:.2f}" '
            f'style="{style}" data-edge-id="{_escape(edge_id)}" '
            f'data-source="{_escape(sid)}" data-target="{_escape(tid)}" '
            f'data-recurrent="{"true" if recurrent else "false"}"/>\n'
        )

    # Draw nodes
    for nid in _get_nodes_sorted(graph):
        node = graph.nodes.get(nid)
        if node is None:
            continue
        (x, y) = coords.get(nid, (10.0, 10.0))
        # Center rectangle around (x, y)
        rx = x - node_w / 2.0
        ry = y - node_h / 2.0
        # Node attributes
        node_type = getattr(node, "node_type", None)
        node_type_name = getattr(node_type, "name", "UNKNOWN")
        activation = getattr(node, "activation_function", "")
        output_size = None
        try:
            output_size = node.attributes.get("output_size")
        except Exception:
            output_size = None
        aggregation = None
        try:
            aggregation = node.attributes.get("aggregation", node.attributes.get("aggregation_function", "sum"))
        except Exception:
            aggregation = "sum"

        label = f"[{nid}] {node_type_name.lower()} • act={activation} • out={output_size} • agg={aggregation}"
        # Node group with data-* attrs
        parts.append(
            f'<g class="node" data-node-id="{_escape(nid)}" data-node-type="{_escape(node_type_name)}" '
            f'data-output-size="{_escape(output_size)}" data-activation="{_escape(activation)}" '
            f'data-aggregation="{_escape(aggregation)}">\n'
        )
        parts.append(_svg_rect(rx, ry, node_w, node_h, rx=8.0, style="fill:#f9f9f9;stroke:#333;stroke-width:1"))
        parts.append(_svg_text(x, y, label, font_size=12, anchor="middle"))
        parts.append("</g>\n")

    parts.append(_svg_footer())
    svg = "".join(parts)

    if path:
        # Write to disk
        with open(path, "w", encoding="utf-8") as f:
            f.write(svg)
        return path
    return svg


def render_graphviz(graph, path: str | None = None, format: str = "svg", options: dict | None = None) -> str:
    """
    Optional richer backend using graphviz (if installed).
    - For format == 'svg', falls back to render_svg if graphviz is not available.
    - For format in ('png', 'pdf'), raises RuntimeError if graphviz is not available.
    """
    try:
        import graphviz  # type: ignore
    except Exception:
        # No graphviz; handle format
        if format == "svg":
            # Fallback to pure SVG
            return render_svg(graph, path, options)
        raise RuntimeError("Graphviz backend is not available for non-SVG formats")

    # Build DOT graph deterministically
    dot = graphviz.Digraph(format=format)
    dot.attr(rankdir="LR")
    dot.attr("node", shape="box", style="rounded")

    # Nodes
    for nid in _get_nodes_sorted(graph):
        node = graph.nodes.get(nid)
        if not node:
            continue
        node_type = getattr(node, "node_type", None)
        node_type_name = getattr(node_type, "name", "UNKNOWN")
        activation = getattr(node, "activation_function", "")
        output_size = None
        try:
            output_size = node.attributes.get("output_size")
        except Exception:
            output_size = None
        aggregation = None
        try:
            aggregation = node.attributes.get("aggregation", node.attributes.get("aggregation_function", "sum"))
        except Exception:
            aggregation = "sum"

        label = f"[{nid}] {node_type_name.lower()}\\nact={activation} out={output_size} agg={aggregation}"
        dot.node(str(nid), label=label)

    # Edges (deterministic ordering)
    try:
        edges = list(graph.list_edges())
    except Exception:
        edges = []

    for e in edges:
        sid = getattr(e, "source_node_id", None)
        tid = getattr(e, "target_node_id", None)
        if sid is None or tid is None:
            continue
        attrs = {}
        if not getattr(e, "enabled", True):
            attrs["style"] = "dashed"
            attrs["color"] = "gray"
        elif getattr(e, "attributes", {}).get("is_recurrent", False):
            attrs["style"] = "dashed"
            attrs["color"] = "red"
        dot.edge(str(sid), str(tid), **attrs)

    # Render
    if path:
        # graphviz will append extension automatically based on format argument
        # We ensure the directory exists and use directory + filename stem
        import os

        directory = os.path.dirname(path)
        stem = os.path.splitext(os.path.basename(path))[0]
        if directory and not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)
        out = dot.render(filename=stem, directory=directory, cleanup=True)
        return out
    data = dot.pipe(format=format)
    if format == "svg":
        try:
            return data.decode("utf-8")
        except Exception:
            return data
    return data  # bytes for png/pdf
