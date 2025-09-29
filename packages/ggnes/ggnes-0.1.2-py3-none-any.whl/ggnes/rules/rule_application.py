"""
Rule application engine for GGNES.
This module handles applying graph grammar rules to transform graphs.
"""

import copy
import random
import uuid
from typing import Any

from ggnes.core import Graph, NodeType
from ggnes.rules.pattern_matching import PatternEdge, PatternMatcher, PatternNode


class RuleApplicationEngine:
    """Handles applying rules to graphs."""

    def __init__(self, graph: Graph):
        self.graph = graph
        self.matcher = PatternMatcher(graph)

    def apply_rule(self, rule, max_applications: int = 1) -> Graph:
        """
        Apply a rule to the graph.

        Args:
            rule: The rule to apply
            max_applications: Maximum number of times to apply the rule

        Returns:
            A new graph with the rule applied
        """
        # Create a copy of the graph
        new_graph = copy.deepcopy(self.graph)
        engine = RuleApplicationEngine(new_graph)

        # Find matches
        pattern_nodes = []
        pattern_edges = []
        boundary_nodes = []

        # Extract pattern from rule
        if hasattr(rule, "pattern"):
            pattern = rule.pattern
            if hasattr(pattern, "nodes"):
                for node_spec in pattern.nodes:
                    pattern_nodes.append(
                        PatternNode(
                            label=node_spec.get("label"),
                            match_criteria=node_spec.get("match_criteria", {}),
                        )
                    )

            if hasattr(pattern, "edges"):
                for edge_spec in pattern.edges:
                    pattern_edges.append(
                        PatternEdge(
                            source_label=edge_spec.get("source_label"),
                            target_label=edge_spec.get("target_label"),
                            match_criteria=edge_spec.get("match_criteria", {}),
                        )
                    )

            if hasattr(pattern, "boundary_nodes"):
                boundary_nodes = pattern.boundary_nodes or []

        # Find all matches
        matches = engine.matcher.find_matches(pattern_nodes, pattern_edges, boundary_nodes)

        if not matches:
            return new_graph

        # Check probability once for the entire rule application
        if hasattr(rule, "application_probability"):
            if random.random() > rule.application_probability:
                return new_graph  # Don't apply rule at all

        # Apply rule to matches
        applications = 0
        for match in matches:
            if max_applications > 0 and applications >= max_applications:
                break

            # Check condition if exists
            if hasattr(rule, "condition") and callable(rule.condition):
                if not rule.condition(new_graph, match, {}):
                    continue

            # Apply the action
            if hasattr(rule, "action"):
                engine._apply_action(match, rule.action, boundary_nodes)
                applications += 1

        return new_graph

    def _apply_action(self, match: dict[str, Any], action, boundary_nodes: list[str]):
        """Apply the RHS action to transform the graph."""
        # Delete nodes (except boundary nodes)
        if hasattr(action, "delete_nodes") and action.delete_nodes:
            for label in action.delete_nodes:
                if label not in boundary_nodes and label in match:
                    node_id = match[label]
                    # Use remove_node method if available (for Graph wrapper)
                    if hasattr(self.graph, "remove_node"):
                        try:
                            self.graph.remove_node(node_id)
                        except Exception:
                            pass
                    elif node_id in self.graph.nodes:
                        # Fallback: Remove node and its edges manually
                        edges_to_remove = []
                        for edge in self.graph.list_edges():
                            if hasattr(edge, "source_node_id") and hasattr(edge, "target_node_id"):
                                if edge.source_node_id == node_id or edge.target_node_id == node_id:
                                    edges_to_remove.append(
                                        (edge.source_node_id, edge.target_node_id)
                                    )

                        for src, tgt in edges_to_remove:
                            try:
                                self.graph.remove_edge(src, tgt)
                            except Exception:
                                pass

                        # Try to delete from nodes dict
                        try:
                            del self.graph.nodes[node_id]
                        except Exception:
                            pass

        # Delete edges
        if hasattr(action, "delete_edges") and action.delete_edges:
            for edge_spec in action.delete_edges:
                src_label = edge_spec.get("source_label")
                tgt_label = edge_spec.get("target_label")
                if src_label in match and tgt_label in match:
                    try:
                        self.graph.remove_edge(match[src_label], match[tgt_label])
                    except Exception:
                        pass

        # Add new nodes
        new_node_ids = {}
        if hasattr(action, "add_nodes") and action.add_nodes:
            for node_spec in action.add_nodes:
                label = node_spec.get("label")
                props = node_spec.get("properties", {})

                # Create new node
                node_id = f"generated_{uuid.uuid4().hex[:8]}"
                node_props = {
                    "id": node_id,
                    "node_type": props.get("node_type", NodeType.HIDDEN),
                    "activation_function": props.get("activation_function", "relu"),
                }

                # Add attributes
                if "attributes" in props:
                    node_props.update(props["attributes"])
                    if "output_size" in props["attributes"]:
                        node_props["output_size"] = props["attributes"]["output_size"]

                node_id = self.graph.add_node(node_props)
                new_node_ids[label] = node_id

        # Add new edges
        if hasattr(action, "add_edges") and action.add_edges:
            for edge_spec in action.add_edges:
                src_label = edge_spec.get("source_label")
                tgt_label = edge_spec.get("target_label")

                # Get node IDs (could be existing or new)
                src_id = new_node_ids.get(src_label, match.get(src_label))
                tgt_id = new_node_ids.get(tgt_label, match.get(tgt_label))

                if src_id and tgt_id:
                    self.graph.add_edge(src_id, tgt_id)

        # Modify existing nodes
        if hasattr(action, "modify_nodes") and action.modify_nodes:
            for mod_spec in action.modify_nodes:
                label = mod_spec.get("label")
                new_props = mod_spec.get("new_properties", {})

                if label in match:
                    node_id = match[label]

                    # Use modify_node_attributes if available (for Graph wrapper)
                    if hasattr(self.graph, "modify_node_attributes"):
                        # Flatten the properties for the wrapper
                        flat_props = {}
                        for key, value in new_props.items():
                            if key == "attributes" and isinstance(value, dict):
                                flat_props.update(value)
                            else:
                                flat_props[key] = value

                        try:
                            self.graph.modify_node_attributes(node_id, flat_props)
                        except Exception:
                            pass
                    elif node_id in self.graph.nodes:
                        node = self.graph.nodes[node_id]

                        # Update properties directly
                        for key, value in new_props.items():
                            if key == "attributes" and hasattr(node, "attributes"):
                                if isinstance(node.attributes, dict):
                                    node.attributes.update(value)
                                else:
                                    for attr_key, attr_val in value.items():
                                        setattr(node.attributes, attr_key, attr_val)
                            else:
                                setattr(node, key, value)


def apply_grammar(
    axiom: Graph, grammar: list, max_iterations: int = 10, strategy: str = "random"
) -> Graph:
    """
    Apply a grammar (list of rules) to transform a graph.

    Args:
        axiom: The initial graph
        grammar: List of rules to apply
        max_iterations: Maximum number of rule applications
        strategy: How to select rules ("random", "sequential", "prioritized")

    Returns:
        The transformed graph
    """
    graph = copy.deepcopy(axiom)

    for iteration in range(max_iterations):
        # Select rule based on strategy
        if strategy == "random":
            rule = random.choice(grammar)
        elif strategy == "sequential":
            rule = grammar[iteration % len(grammar)]
        elif strategy == "prioritized":
            # Would need priority values on rules
            rule = grammar[0]  # Simplified
        else:
            rule = random.choice(grammar)

        # Apply the rule
        engine = RuleApplicationEngine(graph)
        new_graph = engine.apply_rule(rule, max_applications=1)

        # Check if graph changed
        if len(new_graph.nodes) == len(graph.nodes):
            # No change, try another rule or stop
            continue

        graph = new_graph

    return graph
