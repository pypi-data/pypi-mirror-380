import io
import os
import re
import sys

import pytest

from ggnes import Graph, NodeType


def _svg_text(svg: str | bytes) -> str:
    if isinstance(svg, bytes):
        try:
            return svg.decode("utf-8")
        except Exception:
            return svg.decode("latin-1", errors="ignore")
    return svg


def _make_simple_graph() -> Graph:
    g = Graph()
    g.add_node(
        {
            "id": "in",
            "node_type": NodeType.INPUT,
            "activation_function": "linear",
            "output_size": 4,
        }
    )
    g.add_node(
        {
            "id": "h1",
            "node_type": NodeType.HIDDEN,
            "activation_function": "relu",
            "output_size": 3,
        }
    )
    g.add_node(
        {
            "id": "out",
            "node_type": NodeType.OUTPUT,
            "activation_function": "linear",
            "output_size": 1,
        }
    )
    g.add_edge("in", "h1")
    g.add_edge("h1", "out")
    return g


def test_plot_returns_svg_string_and_is_deterministic():
    g = _make_simple_graph()
    # First render (string return)
    svg1 = g.plot()
    svg1_txt = _svg_text(svg1)
    assert isinstance(svg1, (str, bytes)), "plot() should return SVG string/bytes when no location is provided"
    assert "<svg" in svg1_txt.lower(), "Returned content must be an SVG document"

    # Should include node metadata attributes for robust downstream use
    # Minimal invariants: node blocks and edge blocks with data-* attributes
    assert 'class="node"' in svg1_txt
    assert 'data-node-id="' in svg1_txt
    assert 'data-node-type="' in svg1_txt
    assert 'data-output-size="' in svg1_txt

    assert 'class="edge"' in svg1_txt
    assert 'data-edge-id="' in svg1_txt
    assert 'data-source="' in svg1_txt and 'data-target="' in svg1_txt

    # Determinism: second render identical to first
    svg2 = g.plot()
    svg2_txt = _svg_text(svg2)
    assert svg1_txt == svg2_txt, "Visualization must be deterministic for identical inputs"


def test_plot_writes_file_when_location_provided(tmp_path):
    g = _make_simple_graph()
    out_path = tmp_path / "arch.svg"
    ret = g.plot(location=str(out_path))
    assert isinstance(ret, str) and ret.endswith(".svg")
    assert out_path.exists(), "plot(location=...) should write an SVG file"
    txt = out_path.read_text(encoding="utf-8")
    assert "<svg" in txt.lower()


def test_multigraph_emits_multiple_edges_with_ids():
    g = Graph({"multigraph": True})
    g.add_node(
        {"id": "a", "node_type": NodeType.INPUT, "activation_function": "linear", "output_size": 4}
    )
    g.add_node(
        {"id": "b", "node_type": NodeType.HIDDEN, "activation_function": "relu", "output_size": 4}
    )
    # Add parallel edges a->b
    g.add_edge("a", "b", {"weight": 0.1})
    g.add_edge("a", "b", {"weight": 0.2})
    svg = _svg_text(g.plot())
    # Expect at least two edge elements (identified via data-edge-id)
    edge_id_occurrences = svg.count('data-edge-id="')
    assert edge_id_occurrences >= 2, f"Expected >=2 edges rendered, got {edge_id_occurrences}"


def test_recurrent_edge_styled_flag():
    g = _make_simple_graph()
    # Mark the edge h1->out as recurrent
    # Fetch edges and set attribute deterministically
    edges = list(g.list_edges())
    assert edges, "Expected edges to exist"
    # Choose the edge whose target is mapped to the output node (internal id may differ)
    # We will set recurrent on all edges for robustness in test
    for e in edges:
        try:
            e.attributes["is_recurrent"] = True
        except Exception:
            pass
    svg = _svg_text(g.plot())
    # Renderer should expose a data-recurrent flag on recurrent edges
    assert 'data-recurrent="true"' in svg, "Recurrent edge styling flag missing"


def test_invalid_graph_includes_warning_banner():
    g = Graph()
    # Only an OUTPUT node with no inputs makes graph invalid (unreachable output)
    g.add_node(
        {
            "id": "out_only",
            "node_type": NodeType.OUTPUT,
            "activation_function": "linear",
            "output_size": 1,
        }
    )
    svg = _svg_text(g.plot())
    # Expect a data-warning banner so downstream can detect invalid renders
    assert 'data-warning="invalid-graph"' in svg or "Invalid graph" in svg, "Missing invalid-graph warning banner"


def test_png_format_without_graphviz_raises(tmp_path):
    g = _make_simple_graph()
    out_path = tmp_path / "arch.png"
    with pytest.raises(RuntimeError):
        g.plot(location=str(out_path), format="png")
