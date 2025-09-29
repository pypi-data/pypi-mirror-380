"""Transaction management for staged graph modifications.

Implements a simple TransactionManager with a ChangeBuffer that:
- Stages node/edge additions and node deletions
- On begin(), snapshots RNGManager state
- On commit(), validates staged operations, applies them to the Graph, and
  registers created entities with IDManager (if provided), returning a mapping
  of temp handles to final IDs
- On rollback(), clears staged operations and restores RNGManager state

Per project_guide.md M6.
"""

from __future__ import annotations

import logging
import pickle
import uuid
from dataclasses import dataclass, field
from typing import Any


class ChangeBuffer:
    """In-memory buffer for staging graph mutations prior to commit."""

    def __init__(self) -> None:
        # temp handles → node properties
        self._temp_nodes: dict[str, dict[str, Any]] = {}
        # edges: list of (edge_temp_handle, src_handle_or_id, dst_handle_or_id, properties)
        self._temp_edges: list[tuple[str, Any, Any, dict[str, Any]]] = []
        # nodes (final id or temp) staged for deletion
        self._delete_nodes: set[Any] = set()
        # edges (by id) staged for deletion
        self._delete_edges: set[Any] = set()

    def reset(self) -> None:
        self._temp_nodes.clear()
        self._temp_edges.clear()
        self._delete_nodes.clear()
        self._delete_edges.clear()

    def add_node(self, properties: dict[str, Any]) -> str:
        handle = f"tmp:{uuid.uuid4()}"
        self._temp_nodes[handle] = properties
        return handle

    def add_edge(self, source: Any, target: Any, properties: dict[str, Any]) -> str:
        handle = f"tmp_edge:{uuid.uuid4()}"
        self._temp_edges.append((handle, source, target, properties))
        return handle

    def delete_node(self, node: Any) -> None:
        self._delete_nodes.add(node)

    def delete_edge(self, edge_id: Any) -> None:
        self._delete_edges.add(edge_id)


@dataclass
class TransactionManager:
    graph: Any
    rng_manager: Any
    id_manager: Any | None = None
    context_id: str = "default"
    buffer: ChangeBuffer = field(default_factory=ChangeBuffer)

    _rng_state_snapshot: bytes | None = None
    _graph_snapshot: bytes | None = None

    def begin(self) -> None:
        """Begin a transaction by snapshotting RNG state and clearing buffer."""
        if self.rng_manager is not None:
            self._rng_state_snapshot = self.rng_manager.get_state()
        self.buffer.reset()
        # Snapshot graph state for full rollback (nodes, edges, counters, indices)
        try:
            base_g = getattr(self.graph, "get_internal_graph", None)
            base_g = base_g() if callable(base_g) else self.graph
            self._graph_snapshot = pickle.dumps(
                {
                    "nodes": base_g.nodes,
                    "input_node_ids": list(base_g.input_node_ids),
                    "output_node_ids": list(base_g.output_node_ids),
                    "node_counter": int(getattr(base_g, "_node_id_counter", 0)),
                    "edge_counter": int(getattr(base_g, "_edge_id_counter", 0)),
                    "_edges_by_id": dict(getattr(base_g, "_edges_by_id", {})),
                }
            )
        except Exception as e:
            logging.error(f"Failed to snapshot graph state: {e}")
            self._graph_snapshot = None

    # Validation helpers
    def _resolve_node_ref(self, ref: Any, temp_to_real: dict[str, int]) -> Any | None:
        """Resolve a node reference (temp handle, integer id, or external id) to a concrete node id.

        Historically the graph used integer ids, but axiom nodes and some APIs use
        string identifiers (e.g. 'stem', 'collector'). This helper accepts:
          - temp handles starting with 'tmp:' -> resolved via temp_to_real mapping
          - integer ids -> returned as-is
          - any ref that exists as a key in self.graph.nodes -> returned as-is (supports string ids)
        Falls back to None when resolution fails.
        """
        # Temp handle resolution (staged node)
        if isinstance(ref, str) and ref.startswith("tmp:"):
            return temp_to_real.get(ref)
        # Native integer id
        if isinstance(ref, int):
            return ref
        # If graph stores nodes keyed by non-int ids (e.g., string ids), accept them
        try:
            base_g = getattr(self.graph, "get_internal_graph", None)
            base_g = base_g() if callable(base_g) else self.graph
            # Direct key lookup (supports integer or string keys)
            if ref in getattr(base_g, "nodes", {}):
                return ref
            # Fallback: allow matching by node attribute 'id' or 'name' (demo compatibility)
            for nid, node in getattr(base_g, "nodes", {}).items():
                try:
                    if node.attributes.get("id") == ref or node.attributes.get("name") == ref:
                        return nid
                except Exception:
                    continue
        except Exception:
            # Fall through to None on any lookup error
            pass
        return None

    def _validate(self) -> None:
        # If any edge touches a node staged for deletion, fail
        delete_set = set(self.buffer._delete_nodes)
        for _eh, src, dst, _ in self.buffer._temp_edges:
            if src in delete_set or dst in delete_set:
                raise ValueError("Cannot add edge to node staged for deletion")

        # Detect duplicate staged edges (temp-temp)
        seen = set()
        for _eh, src, dst, _ in self.buffer._temp_edges:
            key = (src, dst)
            if key in seen:
                # Allow detection; logging happens in commit
                continue
            seen.add(key)

    def rollback(self) -> None:
        """Discard staged operations and restore RNG state."""
        self.buffer.reset()
        if self._rng_state_snapshot is not None and self.rng_manager is not None:
            self.rng_manager.set_state(self._rng_state_snapshot)
            self._rng_state_snapshot = None
        # Restore graph if snapshot is available
        if self._graph_snapshot is not None:
            try:
                snap = pickle.loads(self._graph_snapshot)
                base_g = getattr(self.graph, "get_internal_graph", None)
                base_g = base_g() if callable(base_g) else self.graph
                base_g.nodes = snap["nodes"]
                base_g.input_node_ids = snap["input_node_ids"]
                base_g.output_node_ids = snap["output_node_ids"]
                setattr(base_g, "_node_id_counter", snap["node_counter"])
                setattr(base_g, "_edge_id_counter", snap["edge_counter"])
                if hasattr(base_g, "_edges_by_id"):
                    base_g._edges_by_id = snap.get("_edges_by_id", {})
            except Exception as e:
                logging.error(f"Failed to restore graph state: {e}")
            finally:
                self._graph_snapshot = None

    def commit(self) -> dict[str, Any]:
        """Validate and apply staged operations.

        Returns mapping of temp handles → final IDs for nodes and edges:
          { 'tmp:..node..': node_id, 'tmp_edge:..': edge_id }
        """
        self._validate()

        temp_to_real: dict[str, Any] = {}

        # Apply deletions first (for existing ids only)
        for e_id in list(self.buffer._delete_edges):
            self.graph.remove_edge(e_id)
        for ref in list(self.buffer._delete_nodes):
            if isinstance(ref, int):
                # Remove node if exists
                self.graph.remove_node(ref)

        # Create nodes
        for handle, props in self.buffer._temp_nodes.items():
            node_id = self.graph.add_node(props)
            temp_to_real[handle] = node_id
            if self.id_manager is not None:
                try:
                    node_obj = self.graph.nodes[node_id]
                    self.id_manager.register_node(node_obj, self.context_id)
                except Exception:
                    pass

        # Create edges
        # Resolve source/target referencing temp handles or real ids
        for edge_handle, src_ref, dst_ref, props in self.buffer._temp_edges:
            # Duplicate edge detection against existing graph
            src_real = self._resolve_node_ref(src_ref, temp_to_real)
            dst_real = self._resolve_node_ref(dst_ref, temp_to_real)
            if src_real is None or dst_real is None:
                # Provide richer diagnostics to aid debugging (include temp mappings and refs)
                temp_keys = list(temp_to_real.keys())
                raise ValueError(
                    f"Invalid edge endpoint reference for edge_handle={edge_handle!r}: "
                    f"src_ref={src_ref!r} dst_ref={dst_ref!r} temp_keys={temp_keys!r}"
                )

            existing = self.graph.find_edge_by_endpoints(src_real, dst_real)
            if existing is not None and not self.graph.config.get("multigraph"):
                logging.warning("Duplicate edge attempt detected during commit")
                continue

            edge_id = self.graph.add_edge(src_real, dst_real, props)
            if edge_id is None:
                # Graph rejected duplicate (simple-graph constraint)
                logging.warning("Duplicate edge attempt detected during commit")
                continue
            # Record edge mapping
            temp_to_real[edge_handle] = edge_id

            if self.id_manager is not None:
                try:
                    edge_obj = self.graph.find_edge_by_endpoints(src_real, dst_real)
                    if edge_obj is not None:
                        self.id_manager.register_edge(edge_obj, self.context_id)
                except Exception:
                    pass

        # Done - clear buffer and RNG snapshot remains as current state
        self.buffer.reset()
        return temp_to_real

    def discard_snapshot(self) -> None:
        """Discard any saved snapshots after a successful, finalized transaction."""
        self._graph_snapshot = None
        self._rng_state_snapshot = None
