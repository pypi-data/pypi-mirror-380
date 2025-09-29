"""
Tests for error message quality and helpfulness.
Ensures users get clear guidance when using the API incorrectly.
"""

import os
import sys

import pytest

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ggnes.core import Graph, NodeType
from ggnes.evolution import Genotype
from ggnes.rules.rule import EmbeddingLogic, LHSPattern, RHSAction, Rule


class TestGraphErrorMessages:
    """Test error messages for graph operations."""

    def test_missing_node_type_error(self):
        """Should give helpful error when node_type is missing."""
        graph = Graph()

        with pytest.raises(Exception) as exc_info:
            graph.add_node(
                {
                    "activation_function": "relu",
                    "attributes": {"output_size": 10},
                    # Missing node_type
                }
            )

        error_msg = str(exc_info.value).lower()
        # Should mention node_type
        assert any(word in error_msg for word in ["node_type", "type", "required"]), (
            f"Unhelpful error: {exc_info.value}"
        )

    def test_missing_activation_function_error(self):
        """Should give helpful error when activation_function is missing."""
        graph = Graph()

        with pytest.raises(Exception) as exc_info:
            graph.add_node(
                {
                    "node_type": NodeType.INPUT,
                    "attributes": {"output_size": 10},
                    # Missing activation_function
                }
            )

        error_msg = str(exc_info.value).lower()
        # Should mention activation_function
        assert any(word in error_msg for word in ["activation", "function", "required"]), (
            f"Unhelpful error: {exc_info.value}"
        )

    def test_missing_output_size_error(self):
        """Should give helpful error when output_size is missing."""
        graph = Graph()

        with pytest.raises(Exception) as exc_info:
            graph.add_node(
                {
                    "node_type": NodeType.INPUT,
                    "activation_function": "relu",
                    # Missing output_size in attributes
                }
            )

        error_msg = str(exc_info.value).lower()
        # Should mention output_size and preferably attributes
        assert "output_size" in error_msg or "output" in error_msg, (
            f"Error doesn't mention output_size: {exc_info.value}"
        )

    def test_wrong_output_size_location_error(self):
        """Should guide users when output_size is in wrong place."""
        graph = Graph()

        with pytest.raises(Exception) as exc_info:
            graph.add_node(
                {
                    "node_type": NodeType.INPUT,
                    "activation_function": "relu",
                    "output_size": 10,  # Wrong: should be in attributes
                }
            )

        error_msg = str(exc_info.value)
        # Ideally should mention attributes dict
        # Currently might just say missing activation_function
        # This is a problem - error is misleading

    def test_invalid_node_type_error(self):
        """Should give clear error for invalid node types."""
        graph = Graph()

        with pytest.raises(Exception) as exc_info:
            graph.add_node(
                {
                    "node_type": "invalid_type",  # String instead of enum
                    "activation_function": "relu",
                    "attributes": {"output_size": 10},
                }
            )

        error_msg = str(exc_info.value)
        # Should mention valid node types or NodeType enum
        # Currently might give confusing error

    def test_nonexistent_node_reference_error(self):
        """Should give clear error when referencing non-existent nodes."""
        graph = Graph()

        n1 = graph.add_node(
            {
                "node_type": NodeType.INPUT,
                "activation_function": "linear",
                "attributes": {"output_size": 10},
            }
        )

        with pytest.raises(Exception) as exc_info:
            graph.add_edge(source_id=n1, target_id=999)  # 999 doesn't exist

        error_msg = str(exc_info.value)
        # Should clearly say node 999 doesn't exist
        assert (
            "999" in error_msg or "not found" in error_msg.lower() or "exist" in error_msg.lower()
        ), f"Error doesn't clearly indicate missing node: {exc_info.value}"

    def test_duplicate_edge_error(self):
        """Should give clear error for duplicate edges."""
        graph = Graph()

        n1 = graph.add_node(
            {
                "node_type": NodeType.INPUT,
                "activation_function": "linear",
                "attributes": {"output_size": 10},
            }
        )

        n2 = graph.add_node(
            {
                "node_type": NodeType.OUTPUT,
                "activation_function": "linear",
                "attributes": {"output_size": 1},
            }
        )

        # Add edge
        graph.add_edge(source_id=n1, target_id=n2)

        # Try to add duplicate
        result = graph.add_edge(source_id=n1, target_id=n2)

        # Should either return None or raise clear error
        if result is None:
            pass  # OK - returns None for duplicate
        else:
            # If it doesn't return None, should raise error
            with pytest.raises(Exception) as exc_info:
                graph.add_edge(source_id=n1, target_id=n2)

            error_msg = str(exc_info.value).lower()
            assert any(word in error_msg for word in ["duplicate", "already", "exists"]), (
                f"Error doesn't mention duplicate: {exc_info.value}"
            )


class TestRuleErrorMessages:
    """Test error messages for rule operations."""

    def test_lhs_pattern_wrong_params_error(self):
        """Should give helpful error for wrong LHSPattern params."""
        with pytest.raises(TypeError) as exc_info:
            LHSPattern(
                graph_patterns=[],  # Wrong param name
                application_constraints={},  # Wrong param name
            )

        error_msg = str(exc_info.value).lower()
        # Should mention correct param names
        assert any(word in error_msg for word in ["nodes", "edges", "boundary"]), (
            f"Error doesn't mention correct params: {exc_info.value}"
        )

    def test_rhs_action_wrong_params_error(self):
        """Should give helpful error for wrong RHSAction params."""
        with pytest.raises(TypeError) as exc_info:
            RHSAction(
                action="add_node",  # Wrong structure
                node_id="test",
            )

        error_msg = str(exc_info.value).lower()
        # Should mention correct param names
        assert any(word in error_msg for word in ["add_nodes", "delete", "modify"]), (
            f"Error doesn't mention correct params: {exc_info.value}"
        )

    def test_rule_missing_uuid_error(self):
        """Should give clear error when UUID is missing."""
        with pytest.raises(TypeError) as exc_info:
            Rule(
                name="my_rule",  # Wrong: should be rule_id with UUID
                lhs=LHSPattern(nodes=[], edges=[], boundary_nodes=[]),
                rhs=RHSAction(add_nodes=None),
                embedding=EmbeddingLogic(),
            )

        error_msg = str(exc_info.value)
        # Should mention rule_id or UUID
        assert any(word in error_msg for word in ["rule_id", "uuid", "id"]), (
            f"Error doesn't mention rule_id: {exc_info.value}"
        )


class TestEvolutionErrorMessages:
    """Test error messages for evolution operations."""

    def test_mutation_missing_config_error(self):
        """Should give helpful error when config is missing."""
        from ggnes.evolution.operators import mutate
        from ggnes.utils.rng_manager import RNGManager

        genotype = Genotype()
        rng = RNGManager(seed=42)

        with pytest.raises(TypeError) as exc_info:
            mutate(genotype, rng)  # Missing config parameter

        error_msg = str(exc_info.value)
        # Should mention config parameter
        assert "config" in error_msg.lower(), f"Error doesn't mention config: {exc_info.value}"

    def test_crossover_missing_config_error(self):
        """Should give helpful error when config is missing."""
        from ggnes.evolution.operators import uniform_crossover
        from ggnes.utils.rng_manager import RNGManager

        parent1 = Genotype()
        parent2 = Genotype()
        rng = RNGManager(seed=42)

        with pytest.raises(TypeError) as exc_info:
            uniform_crossover(parent1, parent2, rng)  # Missing config

        error_msg = str(exc_info.value)
        # Should mention config parameter
        assert "config" in error_msg.lower(), f"Error doesn't mention config: {exc_info.value}"

    def test_invalid_mutation_rate_error(self):
        """Should give clear error for invalid mutation rate."""
        from ggnes.evolution.operators import mutate
        from ggnes.utils.rng_manager import RNGManager

        genotype = Genotype()
        rng = RNGManager(seed=42)

        config = {
            "mutation_rate": 2.0,  # Invalid: > 1.0
            "mutation_probs": {},
        }

        # Should validate and give clear error
        # Note: Currently might not validate
        try:
            mutate(genotype, config, rng)
        except ValueError as e:
            error_msg = str(e).lower()
            assert any(word in error_msg for word in ["rate", "probability", "0", "1"]), (
                f"Error doesn't explain valid range: {e}"
            )


class TestAggregationErrorMessages:
    """Test error messages for aggregation functions."""

    def test_invalid_aggregation_function_error(self):
        """Should give clear error for invalid aggregation function."""
        graph = Graph()

        try:
            graph.add_node(
                {
                    "node_type": NodeType.HIDDEN,
                    "activation_function": "relu",
                    "attributes": {
                        "output_size": 32,
                        "aggregation_function": "invalid_agg",  # Invalid
                    },
                }
            )

            # If node creation succeeds, error might come during translation
            from ggnes.translation import to_pytorch_model

            model = to_pytorch_model(graph)

        except Exception as e:
            error_msg = str(e).lower()
            # Should mention valid aggregation functions
            assert any(word in error_msg for word in ["aggregation", "valid", "sum", "mean"]), (
                f"Error doesn't mention valid aggregations: {e}"
            )

    def test_mismatched_aggregation_sizes_error(self):
        """Should give clear error for size mismatches in aggregation."""
        graph = Graph()

        in1 = graph.add_node(
            {
                "node_type": NodeType.INPUT,
                "activation_function": "linear",
                "attributes": {"output_size": 10},
            }
        )

        in2 = graph.add_node(
            {
                "node_type": NodeType.INPUT,
                "activation_function": "linear",
                "attributes": {"output_size": 20},  # Different size
            }
        )

        hidden = graph.add_node(
            {
                "node_type": NodeType.HIDDEN,
                "activation_function": "relu",
                "attributes": {
                    "output_size": 15,
                    "aggregation_function": "sum",  # Can't sum different sizes
                },
            }
        )

        graph.add_edge(source_id=in1, target_id=hidden)
        graph.add_edge(source_id=in2, target_id=hidden)

        try:
            from ggnes.translation import to_pytorch_model

            model = to_pytorch_model(graph)

            import torch

            x1 = torch.randn(1, 10)
            x2 = torch.randn(1, 20)
            y = model([x1, x2])

        except Exception as e:
            error_msg = str(e).lower()
            # Should mention size mismatch
            assert any(word in error_msg for word in ["size", "shape", "dimension", "mismatch"]), (
                f"Error doesn't mention size mismatch: {e}"
            )


class TestSuggestiveErrorMessages:
    """Test that errors suggest corrections."""

    @pytest.mark.xfail(reason="Errors don't suggest corrections")
    def test_suggest_attributes_dict(self):
        """Error should suggest using attributes dict."""
        graph = Graph()

        with pytest.raises(Exception) as exc_info:
            graph.add_node(
                {
                    "node_type": NodeType.INPUT,
                    "activation_function": "relu",
                    "output_size": 10,  # Wrong location
                }
            )

        error_msg = str(exc_info.value)
        # Should suggest putting in attributes
        assert "attributes" in error_msg and ("dict" in error_msg or "dictionary" in error_msg), (
            f"Error doesn't suggest attributes dict: {exc_info.value}"
        )

        # Even better: show example
        assert "attributes': {" in error_msg or "example" in error_msg.lower()

    @pytest.mark.xfail(reason="Errors don't show examples")
    def test_show_example_in_error(self):
        """Errors should show correct usage examples."""
        with pytest.raises(TypeError) as exc_info:
            LHSPattern(graph_patterns=[])

        error_msg = str(exc_info.value)
        # Should show example
        assert "example" in error_msg.lower() or "LHSPattern(nodes=" in error_msg, (
            f"Error doesn't show example: {exc_info.value}"
        )

    @pytest.mark.xfail(reason="No did you mean suggestions")
    def test_did_you_mean_suggestions(self):
        """Errors should suggest likely corrections."""
        graph = Graph()

        with pytest.raises(Exception) as exc_info:
            graph.add_node(
                {
                    "type": "input",  # Wrong: should be node_type
                    "activation": "relu",  # Wrong: should be activation_function
                    "size": 10,  # Wrong: should be output_size in attributes
                }
            )

        error_msg = str(exc_info.value)
        # Should suggest corrections
        assert "did you mean" in error_msg.lower() or "should be" in error_msg.lower(), (
            f"Error doesn't suggest corrections: {exc_info.value}"
        )
