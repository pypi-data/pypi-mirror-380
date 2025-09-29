"""
Tests for the API that users would naturally expect based on documentation.
These tests SHOULD FAIL with current implementation but show what needs fixing.
"""

import os
import sys

import pytest

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ggnes.core import Edge, Graph, Node, NodeType


class TestUserExpectedAPI:
    """Test the API as users would naturally use it."""

    @pytest.mark.xfail(reason="Graph.add_node expects output_size in attributes, not top-level")
    def test_intuitive_node_creation(self):
        """Users would naturally put output_size at top level."""
        graph = Graph()

        # This is what users would naturally try
        node_id = graph.add_node(
            {
                "id": "input",  # Want to specify custom ID
                "node_type": "input",  # Want to use string
                "output_size": 10,  # Want this at top level
                "activation_function": "relu",
            }
        )

        assert node_id == "input"  # Expect custom ID
        assert graph.nodes["input"].output_size == 10

    @pytest.mark.xfail(reason="Cannot specify custom node IDs")
    def test_custom_node_ids(self):
        """Users want meaningful node names, not integers."""
        graph = Graph()

        # Users want to create meaningful architectures
        graph.add_node({"id": "image_input", "node_type": "input", "output_size": 784})
        graph.add_node({"id": "conv1", "node_type": "hidden", "output_size": 32})
        graph.add_node({"id": "conv2", "node_type": "hidden", "output_size": 64})
        graph.add_node({"id": "fc1", "node_type": "hidden", "output_size": 128})
        graph.add_node({"id": "output", "node_type": "output", "output_size": 10})

        # Should be able to reference by name
        graph.add_edge(Edge(src_id="image_input", dst_id="conv1"))
        graph.add_edge(Edge(src_id="conv1", dst_id="conv2"))
        graph.add_edge(Edge(src_id="conv2", dst_id="fc1"))
        graph.add_edge(Edge(src_id="fc1", dst_id="output"))

        assert "image_input" in graph.nodes
        assert "conv1" in graph.nodes

    @pytest.mark.xfail(reason="Node constructor doesn't accept output_size directly")
    def test_node_object_creation(self):
        """Users expect Node constructor to accept all parameters."""
        node = Node(
            id="hidden1",
            node_type="hidden",
            output_size=32,
            activation_function="relu",
            aggregation_function="sum",
        )

        assert node.id == "hidden1"
        assert node.output_size == 32

    @pytest.mark.xfail(reason="Graph.add_edge should accept Edge objects")
    def test_add_edge_with_object(self):
        """Users expect to create Edge objects and add them."""
        graph = Graph()

        n1 = graph.add_node({"node_type": "input", "output_size": 10})
        n2 = graph.add_node({"node_type": "output", "output_size": 1})

        # Should be able to create and add Edge object
        edge = Edge(src_id=n1, dst_id=n2, weight=0.5)
        graph.add_edge(edge)

        assert len(list(graph.list_edges())) == 1

    @pytest.mark.xfail(reason="LHSPattern API completely different")
    def test_intuitive_rule_creation(self):
        """Users expect intuitive rule creation based on docs."""
        from ggnes.rules.rule import EmbeddingLogic, LHSPattern, RHSAction, Rule

        # What users would try based on typical docs
        pattern = LHSPattern(
            graph_patterns=[],  # Or patterns=[]
            application_constraints={},  # Or constraints={}
        )

        action = RHSAction(
            action="add_node",
            node_id="new_hidden",
            attributes={"node_type": "hidden", "output_size": 32, "activation_function": "relu"},
        )

        rule = Rule(
            name="add_hidden_layer",  # Want to use name, not UUID
            lhs_pattern=pattern,
            rhs_actions=[action],  # Or rhs_action=action
            embedding_logic=EmbeddingLogic(),
        )

        assert rule.name == "add_hidden_layer"

    @pytest.mark.xfail(reason="Evolution operators API different")
    def test_intuitive_evolution_operators(self):
        """Users expect simple evolution operator signatures."""
        from ggnes.evolution import Genotype
        from ggnes.evolution.operators import crossover, mutate
        from ggnes.utils.rng_manager import RNGManager

        g1 = Genotype()
        g2 = Genotype()
        rng = RNGManager(seed=42)

        # Users expect simple signatures
        mutated = mutate(g1, rng)  # No config parameter expected
        child = crossover(g1, g2, rng)  # Simple crossover

        assert mutated != g1
        assert child != g1 and child != g2


class TestAggregationFunctions:
    """Test all aggregation functions that should work."""

    aggregations = [
        "sum",
        "mean",
        "max",
        "min",
        "concat",
        "matrix_product",
        "attention",
        "multi_head_attention",
        "gated_sum",
        "topk_weighted_sum",
        "moe",
        "attn_pool",
    ]

    @pytest.mark.parametrize("aggregation", aggregations)
    @pytest.mark.xfail(reason="Aggregation functions not working due to Graph API issues")
    def test_aggregation_function(self, aggregation):
        """Each aggregation function should work."""
        import torch

        from ggnes.translation import to_pytorch_model

        graph = Graph()

        # Create multi-input architecture to test aggregation
        in1 = graph.add_node(
            {"node_type": "input", "output_size": 8, "activation_function": "linear"}
        )

        in2 = graph.add_node(
            {"node_type": "input", "output_size": 8, "activation_function": "linear"}
        )

        hidden = graph.add_node(
            {
                "node_type": "hidden",
                "output_size": 16,
                "activation_function": "relu",
                "aggregation_function": aggregation,  # Test this aggregation
            }
        )

        out = graph.add_node(
            {"node_type": "output", "output_size": 1, "activation_function": "linear"}
        )

        graph.add_edge(in1, hidden)
        graph.add_edge(in2, hidden)
        graph.add_edge(hidden, out)

        # Should be able to translate and run
        model = to_pytorch_model(graph)
        x1 = torch.randn(32, 8)
        x2 = torch.randn(32, 8)

        # Model should handle multiple inputs
        y = model([x1, x2])
        assert y.shape == (32, 1)


class TestPyTorchTranslation:
    """Test PyTorch translation issues."""

    @pytest.mark.xfail(reason="Shape mismatches in complex architectures")
    def test_complex_architecture_shapes(self):
        """Complex architectures should maintain correct shapes."""
        import torch

        from ggnes.translation import to_pytorch_model

        graph = Graph()

        # Build a complex architecture
        input_id = graph.add_node(
            {
                "node_type": NodeType.INPUT,
                "activation_function": "linear",
                "attributes": {"output_size": 8},
            }
        )

        # Multiple hidden layers with different sizes
        h1 = graph.add_node(
            {
                "node_type": NodeType.HIDDEN,
                "activation_function": "relu",
                "attributes": {"output_size": 64},
            }
        )

        h2 = graph.add_node(
            {
                "node_type": NodeType.HIDDEN,
                "activation_function": "relu",
                "attributes": {"output_size": 32},
            }
        )

        h3 = graph.add_node(
            {
                "node_type": NodeType.HIDDEN,
                "activation_function": "relu",
                "attributes": {"output_size": 16},
            }
        )

        output_id = graph.add_node(
            {
                "node_type": NodeType.OUTPUT,
                "activation_function": "linear",
                "attributes": {"output_size": 1},
            }
        )

        # Create skip connections
        graph.add_edge(source_id=input_id, target_id=h1)
        graph.add_edge(source_id=h1, target_id=h2)
        graph.add_edge(source_id=h2, target_id=h3)
        graph.add_edge(source_id=h3, target_id=output_id)

        # Skip connection
        graph.add_edge(source_id=h1, target_id=h3)

        model = to_pytorch_model(graph)

        # Should handle batches correctly
        batch_sizes = [1, 16, 32, 64, 128]
        for batch_size in batch_sizes:
            x = torch.randn(batch_size, 8)
            y = model(x)
            assert y.shape == (batch_size, 1), f"Failed for batch size {batch_size}"


class TestErrorMessages:
    """Test that error messages are helpful when using wrong API."""

    def test_helpful_error_for_wrong_node_api(self):
        """Should give helpful error when using intuitive API."""
        graph = Graph()

        with pytest.raises(Exception) as exc_info:
            graph.add_node({"id": "input", "node_type": "input", "output_size": 10})

        # Error should mention putting output_size in attributes
        error_msg = str(exc_info.value).lower()
        assert "attributes" in error_msg or "output_size" in error_msg, (
            f"Unhelpful error message: {exc_info.value}"
        )

    def test_helpful_error_for_wrong_rule_api(self):
        """Should give helpful error for wrong LHSPattern."""
        from ggnes.rules.rule import LHSPattern

        with pytest.raises(TypeError) as exc_info:
            LHSPattern(graph_patterns=[], application_constraints={})

        # Error should mention correct parameters
        error_msg = str(exc_info.value).lower()
        assert "nodes" in error_msg or "edges" in error_msg, (
            f"Unhelpful error message: {exc_info.value}"
        )


class TestEndToEndWorkflow:
    """Test complete user workflows."""

    @pytest.mark.xfail(reason="Multiple API issues prevent end-to-end workflow")
    def test_complete_nas_workflow(self):
        """A complete NAS workflow should work intuitively."""

        from ggnes import Graph
        from ggnes.evolution import evolve
        from ggnes.translation import to_pytorch_model

        # Step 1: Define search space with rules
        rules = []
        rules.append(create_add_layer_rule("add_conv", "conv", 32))
        rules.append(create_add_layer_rule("add_fc", "fc", 64))
        rules.append(create_add_connection_rule())

        # Step 2: Create initial architecture
        graph = Graph()
        graph.add_node({"id": "input", "type": "input", "size": 784})
        graph.add_node({"id": "output", "type": "output", "size": 10})
        graph.add_edge("input", "output")

        # Step 3: Evolve architectures
        population = evolve(
            initial_graph=graph,
            rules=rules,
            population_size=20,
            generations=10,
            fitness_function=lambda g: evaluate_architecture(g),
        )

        # Step 4: Get best architecture
        best_graph = population.best()

        # Step 5: Train final model
        model = to_pytorch_model(best_graph)
        train_model(model)

        # Step 6: Evaluate
        accuracy = evaluate_model(model)
        assert accuracy > 0.9  # Should achieve good performance
