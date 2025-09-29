"""Read-only GraphView wrapper for condition evaluation (spec §10.3)."""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any


class ReadOnlyNode:
    """Read-only node wrapper that blocks mutating attribute access."""

    def __init__(self, node: Any):
        self._node = node

    def __getattr__(self, name: str) -> Any:
        # Disallow obvious mutators by convention
        if name.startswith("_") or name in ("set", "update", "add", "remove"):
            raise AttributeError(f"Cannot access '{name}' on read-only node")
        return getattr(self._node, name)


class ReadOnlyDict(Mapping):
    """Read-only dict-like view that returns wrapped nodes when present."""

    def __init__(self, source: dict):
        self._source = source

    def __getitem__(self, key: Any) -> Any:
        value = self._source[key]
        # Wrap Node-like objects
        if hasattr(value, "node_id") and hasattr(value, "edges_in") and hasattr(value, "edges_out"):
            return ReadOnlyNode(value)
        return value

    def __iter__(self):
        return iter(self._source)

    def __len__(self) -> int:
        return len(self._source)

    def get(self, key: Any, default: Any = None) -> Any:
        if key in self._source:
            return self[key]
        return default


class GraphView:
    """Read-only view of a graph for condition evaluation."""

    def __init__(self, graph: Any):
        self._graph = graph

    @property
    def nodes(self) -> ReadOnlyDict:
        return ReadOnlyDict(self._graph.nodes)

    def get_node(self, node_id: int) -> ReadOnlyNode | None:
        node = self._graph.nodes.get(node_id)
        return ReadOnlyNode(node) if node else None

    def count_nodes_by_type(self, node_type: Any) -> int:
        return sum(
            1 for n in self._graph.nodes.values() if getattr(n, "node_type", None) == node_type
        )
