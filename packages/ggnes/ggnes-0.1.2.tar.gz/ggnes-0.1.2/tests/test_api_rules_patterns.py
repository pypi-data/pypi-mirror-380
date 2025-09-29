"""
Comprehensive tests for Rule, LHSPattern, RHSAction, and EmbeddingLogic APIs.
Tests both intuitive usage and actual implementation.
"""

import os
import sys
import uuid

import pytest

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ggnes import LHSPattern, NodeType, RHSAction, Rule
from ggnes.rules.rule import EmbeddingLogic


class TestLHSPatternAPI:
    """Test LHSPattern creation variations."""

    def test_lhs_pattern_intuitive_empty(self):
        """Users expect simple empty pattern creation."""
        pattern = LHSPattern()  # Should work with no args
        assert pattern is not None

    def test_lhs_pattern_intuitive_params(self):
        """Users expect intuitive parameter names."""
        pattern = LHSPattern(
            graph_patterns=[],  # Or patterns=[]
            application_constraints={},  # Or constraints={}
            match_condition=lambda g: True,
        )
        assert pattern is not None

    def test_lhs_pattern_actual_api(self):
        """Document actual LHSPattern API."""
        pattern = LHSPattern(
            nodes=[],  # Required
            edges=[],  # Required
            boundary_nodes=[],  # Required
        )
        assert pattern is not None

    def test_lhs_pattern_with_node_patterns(self):
        """Users expect intuitive node pattern specification."""
        pattern = LHSPattern(
            nodes=[{"id": "A", "type": "hidden", "min_size": 32}, {"id": "B", "type": "hidden"}],
            edges=[{"from": "A", "to": "B"}],
        )
        assert len(pattern.nodes) == 2

    def test_lhs_pattern_actual_node_spec(self):
        """Document actual node specification format."""
        pattern = LHSPattern(
            nodes=[
                {"label": "A", "match_criteria": {"node_type": NodeType.HIDDEN}},
                {"label": "B", "match_criteria": {"node_type": NodeType.HIDDEN}},
            ],
            edges=[{"source_label": "A", "target_label": "B", "match_criteria": {}}],
            boundary_nodes=["A"],
        )
        assert len(pattern.nodes) == 2

    def test_pattern_matching_methods(self):
        """Users expect pattern matching methods."""
        pattern = LHSPattern(patterns=[{"type": "hidden"}])

        from ggnes.core import Graph

        graph = Graph()

        # Should have matching methods
        assert pattern.matches(graph)
        assert pattern.find_matches(graph) == [...]
        assert pattern.count_matches(graph) == 0


class TestRHSActionAPI:
    """Test RHSAction creation variations."""

    def test_rhs_action_intuitive_add_node(self):
        """Users expect simple action specification."""
        action = RHSAction(
            action="add_node",
            node_id="new_hidden",
            attributes={"type": "hidden", "size": 32, "activation": "relu"},
        )
        assert action.action == "add_node"

    def test_rhs_action_intuitive_multiple(self):
        """Users expect to specify multiple actions easily."""
        action = RHSAction(
            actions=[
                {"type": "add_node", "id": "h1", "size": 32},
                {"type": "add_node", "id": "h2", "size": 64},
                {"type": "add_edge", "from": "h1", "to": "h2"},
            ]
        )
        assert len(action.actions) == 3

    def test_rhs_action_actual_api(self):
        """Document actual RHSAction API."""
        action = RHSAction(
            add_nodes=[
                {
                    "label": "new_hidden",
                    "properties": {
                        "node_type": NodeType.HIDDEN,
                        "activation_function": "relu",
                        "attributes": {"output_size": 32},
                    },
                }
            ],
            add_edges=None,
            delete_nodes=None,
            delete_edges=None,
            modify_nodes=None,
            modify_edges=None,
        )
        assert action.add_nodes is not None

    def test_rhs_action_all_operations(self):
        """Test all RHSAction operation types."""
        action = RHSAction(
            add_nodes=[
                {
                    "label": "N1",
                    "properties": {
                        "node_type": NodeType.HIDDEN,
                        "activation_function": "relu",
                        "attributes": {"output_size": 32},
                    },
                }
            ],
            add_edges=[{"source_label": "N1", "target_label": "existing_node"}],
            delete_nodes=["old_node"],
            delete_edges=[{"source_label": "A", "target_label": "B"}],
            modify_nodes=[
                {"label": "existing_node", "new_properties": {"activation_function": "tanh"}}
            ],
            modify_edges=None,
        )

        assert action.add_nodes is not None
        assert action.delete_nodes is not None

    @pytest.mark.xfail(reason="No action validation")
    def test_rhs_action_validation(self):
        """Actions should be validated."""
        with pytest.raises(ValueError) as exc_info:
            RHSAction(
                action="invalid_action",  # Invalid
                node_id="test",
            )

        assert "invalid" in str(exc_info.value).lower()


class TestEmbeddingLogicAPI:
    """Test EmbeddingLogic creation."""

    def test_embedding_logic_default(self):
        """Default EmbeddingLogic should work."""
        embedding = EmbeddingLogic()
        assert embedding is not None

    @pytest.mark.xfail(reason="EmbeddingLogic parameters unclear")
    def test_embedding_logic_with_params(self):
        """Users expect to configure embedding logic."""
        embedding = EmbeddingLogic(
            strategy="preserve_connections",
            mapping={"A": "new_A", "B": "new_B"},
            preserve_attributes=True,
        )
        assert embedding.strategy == "preserve_connections"

    def test_embedding_logic_actual_params(self):
        """Document actual EmbeddingLogic parameters."""
        from ggnes.rules.rule import EmbeddingStrategy

        embedding = EmbeddingLogic(
            strategy=EmbeddingStrategy.MAP_BOUNDARY_CONNECTIONS,
            connection_map=None,
            excess_connection_handling="WARNING",
            unknown_direction_handling="WARNING",
            boundary_handling="PROCESS_LAST",
        )
        assert embedding is not None


class TestRuleCreationAPI:
    """Test Rule creation variations."""

    def test_rule_intuitive_with_name(self):
        """Users expect to create rules with names."""
        rule = Rule(
            name="add_hidden_layer",
            pattern=LHSPattern(),
            action=RHSAction(action="add_node"),
            priority=1.0,
        )
        assert rule.name == "add_hidden_layer"

    def test_rule_intuitive_params(self):
        """Users expect intuitive parameter names."""
        rule = Rule(
            name="my_rule",
            lhs_pattern=LHSPattern(),
            rhs_actions=[RHSAction(action="add_node")],
            embedding_logic=EmbeddingLogic(),
            application_probability=0.8,
            max_applications=3,
        )
        assert rule.name == "my_rule"

    def test_rule_actual_api(self):
        """Document actual Rule API."""
        rule = Rule(
            rule_id=uuid.uuid4(),  # Required UUID
            lhs=LHSPattern(nodes=[], edges=[], boundary_nodes=[]),
            rhs=RHSAction(add_nodes=None),
            embedding=EmbeddingLogic(),
            metadata={"name": "my_rule"},  # Name goes in metadata
            condition=None,
        )
        assert rule.rule_id is not None

    @pytest.mark.xfail(reason="No rule builder pattern")
    def test_rule_builder_pattern(self):
        """Users might expect builder pattern."""
        rule = (
            Rule()
            .with_name("add_layer")
            .match_nodes(type="hidden")
            .add_node(type="hidden", size=32)
            .add_edge(from_matched=0, to_new=0)
            .with_probability(0.8)
            .build()
        )

        assert rule.name == "add_layer"

    def test_rule_with_condition(self):
        """Test rule with application condition."""

        def condition(graph, match):
            return len(graph.nodes) < 10

        rule = Rule(
            rule_id=uuid.uuid4(),
            lhs=LHSPattern(nodes=[], edges=[], boundary_nodes=[]),
            rhs=RHSAction(add_nodes=None),
            embedding=EmbeddingLogic(),
            metadata={"name": "conditional_rule"},
            condition=condition,  # Application condition
        )
        assert rule.condition is not None


class TestRuleLibrary:
    """Test creating common rule patterns."""

    def test_simple_add_layer_rule(self):
        """Creating a simple 'add layer' rule should be easy."""
        rule = Rule.create_add_layer(layer_type="dense", units=128, activation="relu")
        assert rule is not None

    def test_skip_connection_rule(self):
        """Creating skip connection rule should be simple."""
        rule = Rule.create_skip_connection(min_distance=2, max_distance=4)
        assert rule is not None

    def test_regularization_rule(self):
        """Creating regularization rule should be simple."""
        rule = Rule.create_add_dropout(dropout_rate=0.5, after_activation="relu")
        assert rule is not None

    def test_actual_complex_rule(self):
        """Document how to actually create complex rules."""
        # Add convolution block rule
        rule = Rule(
            rule_id=uuid.uuid4(),
            lhs=LHSPattern(
                nodes=[{"label": "input", "match_criteria": {"node_type": NodeType.INPUT}}],
                edges=[],
                boundary_nodes=["input"],
            ),
            rhs=RHSAction(
                add_nodes=[
                    {
                        "label": "conv1",
                        "properties": {
                            "node_type": NodeType.HIDDEN,
                            "activation_function": "relu",
                            "attributes": {
                                "output_size": 32,
                                "aggregation_function": "matrix_product",
                            },
                        },
                    },
                    {
                        "label": "pool1",
                        "properties": {
                            "node_type": NodeType.HIDDEN,
                            "activation_function": "linear",
                            "attributes": {"output_size": 32, "aggregation_function": "max"},
                        },
                    },
                ],
                add_edges=[
                    {"source_label": "input", "target_label": "conv1"},
                    {"source_label": "conv1", "target_label": "pool1"},
                ],
            ),
            embedding=EmbeddingLogic(),
            metadata={
                "name": "add_conv_block",
                "description": "Adds convolution and pooling layers",
            },
        )

        assert rule.metadata["name"] == "add_conv_block"


class TestRuleApplication:
    """Test rule application to graphs."""

    def test_simple_rule_application(self):
        """Applying rules should be simple."""
        from ggnes.core import Graph

        graph = Graph()
        # ... add some nodes ...

        rule = Rule(name="add_layer")

        # Should be simple to apply
        new_graph = rule.apply(graph)
        assert len(new_graph.nodes) > len(graph.nodes)

    def test_find_rule_matches(self):
        """Should be able to find where rules can apply."""
        from ggnes.core import Graph

        graph = Graph()
        rule = Rule(name="test_rule")

        # Should find matches
        matches = rule.find_matches(graph)
        assert isinstance(matches, list)

        # Should be able to apply to specific match
        if matches:
            new_graph = rule.apply_to_match(graph, matches[0])
            assert new_graph is not None
