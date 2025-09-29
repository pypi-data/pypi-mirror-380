"""
Pattern matching implementation for GGNES rule application.
This module provides the core pattern matching functionality for finding
subgraph matches in the main graph.
"""

import itertools
from dataclasses import dataclass
from typing import Any

from ggnes.core import Graph, Node


@dataclass
class PatternNode:
    """Represents a node in a pattern to match."""

    label: str
    match_criteria: dict[str, Any]

    def matches(self, node: Node) -> bool:
        """Check if a node matches this pattern node."""
        for key, value in self.match_criteria.items():
            if hasattr(node, key):
                node_value = getattr(node, key)
                if callable(value):
                    # Allow lambda functions for complex matching
                    if not value(node_value):
                        return False
                elif node_value != value:
                    return False
            elif key == "node_type":
                # Special handling for node_type
                if hasattr(node, "node_type"):
                    if node.node_type != value:
                        return False
            elif key == "output_size":
                # Check in attributes
                if hasattr(node, "attributes") and isinstance(node.attributes, dict):
                    node_output_size = node.attributes.get("output_size")
                    if callable(value):
                        # Apply callable to output_size value
                        if not value(node_output_size):
                            return False
                    elif node_output_size != value:
                        return False
        return True


@dataclass
class PatternEdge:
    """Represents an edge in a pattern to match."""

    source_label: str
    target_label: str
    match_criteria: dict[str, Any] = None

    def __post_init__(self):
        if self.match_criteria is None:
            self.match_criteria = {}


class PatternMatcher:
    """Handles pattern matching in graphs."""

    def __init__(self, graph: Graph):
        self.graph = graph

    def find_matches(
        self,
        pattern_nodes: list[PatternNode],
        pattern_edges: list[PatternEdge],
        boundary_nodes: list[str] = None,
    ) -> list[dict[str, Any]]:
        """
        Find all matches of the pattern in the graph.

        Returns a list of dictionaries mapping pattern labels to node IDs.
        """
        if boundary_nodes is None:
            boundary_nodes = []

        matches = []

        # Get all possible node assignments
        node_assignments = self._get_node_assignments(pattern_nodes)

        # Check each assignment
        for assignment in node_assignments:
            if self._check_edges(assignment, pattern_edges):
                matches.append(assignment)

        return matches

    def _get_node_assignments(self, pattern_nodes: list[PatternNode]) -> list[dict[str, Any]]:
        """Get all possible assignments of graph nodes to pattern nodes."""
        assignments = []

        # Get candidate nodes for each pattern node
        candidates = {}
        for pnode in pattern_nodes:
            candidates[pnode.label] = []
            for node_id, node in self.graph.nodes.items():
                if pnode.matches(node):
                    candidates[pnode.label].append(node_id)

        # Generate all combinations
        if all(candidates.values()):
            keys = list(candidates.keys())
            for combo in itertools.product(*[candidates[k] for k in keys]):
                # Check that all nodes are unique (no node maps to multiple pattern nodes)
                if len(set(combo)) == len(combo):
                    assignment = dict(zip(keys, combo))
                    assignments.append(assignment)

        return assignments

    def _check_edges(self, assignment: dict[str, Any], pattern_edges: list[PatternEdge]) -> bool:
        """Check if the edge patterns match for a given node assignment."""
        for pedge in pattern_edges:
            source_id = assignment.get(pedge.source_label)
            target_id = assignment.get(pedge.target_label)

            if source_id is None or target_id is None:
                return False

            # Check if edge exists - use the Graph's has_edge method which handles custom IDs
            if hasattr(self.graph, "has_edge"):
                if not self.graph.has_edge(source_id, target_id):
                    return False
            else:
                # Fallback for older graph implementations
                if not self._has_edge_fallback(source_id, target_id):
                    return False

            # Check edge criteria if any
            if pedge.match_criteria:
                # Get edge and check criteria
                edge = self._get_edge(source_id, target_id)
                if edge:
                    for key, value in pedge.match_criteria.items():
                        if hasattr(edge, key):
                            if getattr(edge, key) != value:
                                return False

        return True

    def _has_edge_fallback(self, source_id: Any, target_id: Any) -> bool:
        """Fallback method to check if edge exists."""
        for edge in self.graph.list_edges():
            if hasattr(edge, "source_node_id") and hasattr(edge, "target_node_id"):
                if edge.source_node_id == source_id and edge.target_node_id == target_id:
                    return True
        return False

    def _get_edge(self, source_id: Any, target_id: Any):
        """Get edge between two nodes."""
        # This is a simplified version - actual implementation would need to
        # properly retrieve edge objects from the graph
        for edge in self.graph.list_edges():
            if hasattr(edge, "source_node_id") and hasattr(edge, "target_node_id"):
                if edge.source_node_id == source_id and edge.target_node_id == target_id:
                    return edge
        return None


class NegativePattern:
    """Pattern with negative conditions (must NOT match)."""

    def __init__(
        self,
        positive_nodes: list[dict],
        negative_nodes: list[dict] = None,
        negative_edges: list[dict] = None,
    ):
        self.positive_nodes = [
            PatternNode(n["label"], n.get("match_criteria", {})) for n in positive_nodes
        ]
        self.negative_nodes = [
            PatternNode(n["label"], n.get("match_criteria", {})) for n in (negative_nodes or [])
        ]
        self.negative_edges = [PatternEdge(**e) for e in (negative_edges or [])]

    def find_matches(self, graph: Graph) -> list[dict[str, Any]]:
        """Find matches where positive conditions are met but negative are not."""
        matcher = PatternMatcher(graph)

        # Find positive matches
        positive_matches = matcher.find_matches(self.positive_nodes, [], [])

        # Filter out matches that also match negative conditions
        filtered_matches = []
        for match in positive_matches:
            # Check if any negative pattern would match
            has_negative = False

            # Check negative nodes
            for neg_node in self.negative_nodes:
                for node_id, node in graph.nodes.items():
                    if neg_node.matches(node):
                        # Check if this negative match connects to positive match
                        for pos_label, pos_id in match.items():
                            if graph.has_edge(pos_id, node_id):
                                has_negative = True
                                break

            if not has_negative:
                filtered_matches.append(match)

        return filtered_matches
