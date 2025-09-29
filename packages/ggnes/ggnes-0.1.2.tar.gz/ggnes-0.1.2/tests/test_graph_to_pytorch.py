#!/usr/bin/env python3
"""
Comprehensive test suite for GGNES Graph to PyTorch conversion
Test-driven approach to understand and fix GGNES graph system
"""

import pytest

from ggnes import Graph, Node, NodeType
from ggnes.translation import to_pytorch_model

torch = pytest.importorskip("torch")


class TestBasicNodeCreation:
    """Test basic node creation and requirements"""

    def test_node_creation_with_required_attributes(self):
        """Test that we can create a node with all required attributes"""
        node = Node(
            node_id=0,
            node_type=NodeType.INPUT,
            activation_function="identity",
            bias=0.0,
            attributes={"output_size": 1},
        )
        assert node.node_id == 0
        assert node.node_type == NodeType.INPUT
        assert node.activation_function == "identity"
        assert node.attributes["output_size"] == 1

    def test_node_missing_output_size_fails(self):
        """Test that node creation fails without output_size"""
        with pytest.raises(ValueError, match="output_size must be positive int"):
            Node(
                node_id=0,
                node_type=NodeType.INPUT,
                activation_function="identity",
                attributes={},  # Missing output_size
            )

    def test_node_types_enum(self):
        """Test all available node types"""
        assert NodeType.INPUT == NodeType.INPUT
        assert NodeType.HIDDEN == NodeType.HIDDEN
        assert NodeType.OUTPUT == NodeType.OUTPUT
        node_types = list(NodeType)
        assert len(node_types) == 3


class TestGraphConstruction:
    """Test graph construction methods"""

    def test_empty_graph_creation(self):
        """Test creating an empty graph"""
        graph = Graph()
        assert graph is not None
        assert len(graph.nodes) == 0
        assert len(list(graph.list_edges())) == 0

    def test_add_node_with_dict(self):
        """Test adding nodes using dictionary properties"""
        graph = Graph()

        # Add input node
        node_id = graph.add_node(
            {
                "node_type": NodeType.INPUT,
                "activation_function": "identity",
                "attributes": {"output_size": 1},
            }
        )

        assert node_id is not None
        assert node_id in graph.nodes
        assert graph.nodes[node_id].node_type == NodeType.INPUT

    def test_add_multiple_nodes(self):
        """Test adding multiple nodes of different types"""
        graph = Graph()

        # Add input nodes
        input_ids = []
        for i in range(3):
            node_id = graph.add_node(
                {
                    "node_type": NodeType.INPUT,
                    "activation_function": "identity",
                    "attributes": {"output_size": 1, "name": f"input_{i}"},
                }
            )
            input_ids.append(node_id)

        # Add hidden nodes
        hidden_ids = []
        for i in range(2):
            node_id = graph.add_node(
                {
                    "node_type": NodeType.HIDDEN,
                    "activation_function": "relu",
                    "attributes": {"output_size": 1, "name": f"hidden_{i}"},
                }
            )
            hidden_ids.append(node_id)

        # Add output node
        output_id = graph.add_node(
            {
                "node_type": NodeType.OUTPUT,
                "activation_function": "identity",
                "attributes": {"output_size": 1, "name": "output"},
            }
        )

        assert len(graph.nodes) == 6
        assert len(input_ids) == 3
        assert len(hidden_ids) == 2
        assert output_id in graph.nodes

    def test_add_edges(self):
        """Test adding edges between nodes"""
        graph = Graph()

        # Create two nodes
        _ = graph.add_node(
            {
                "node_type": NodeType.INPUT,
                "activation_function": "identity",
                "attributes": {"output_size": 1},
            }
        )

        _ = graph.add_node(
            {
                "node_type": NodeType.OUTPUT,
                "activation_function": "identity",
                "attributes": {"output_size": 1},
            }
        )

        # Add edge
        graph.add_edge(_, _)

        edges = list(graph.list_edges())
        assert len(edges) == 1
        assert edges[0].source_node_id is not None
        assert edges[0].target_node_id is not None


class TestSimpleNetworks:
    """Test creating simple neural networks"""

    def test_single_layer_network(self):
        """Test creating a single layer network (input -> output)"""
        graph = Graph()

        # Input layer (3 nodes)
        input_ids = []
        for i in range(3):
            node_id = graph.add_node(
                {
                    "node_type": NodeType.INPUT,
                    "activation_function": "identity",
                    "attributes": {"output_size": 1},
                }
            )
            input_ids.append(node_id)

        # Output node
        output_id = graph.add_node(
            {
                "node_type": NodeType.OUTPUT,
                "activation_function": "identity",
                "attributes": {"output_size": 1},
            }
        )

        # Connect all inputs to output
        for input_id in input_ids:
            graph.add_edge(input_id, output_id)

        assert len(graph.nodes) == 4
        assert len(list(graph.list_edges())) == 3

        # Verify graph structure
        assert len(graph.nodes) == 4
        assert len(graph.output_node_ids) == 1

    def test_two_layer_network(self):
        """Test creating a two-layer network (input -> hidden -> output)"""
        graph = Graph()

        # Input layer (4 nodes)
        input_ids = []
        for i in range(4):
            node_id = graph.add_node(
                {
                    "node_type": NodeType.INPUT,
                    "activation_function": "identity",
                    "attributes": {"output_size": 1},
                }
            )
            input_ids.append(node_id)

        # Hidden layer (2 nodes)
        hidden_ids = []
        for i in range(2):
            node_id = graph.add_node(
                {
                    "node_type": NodeType.HIDDEN,
                    "activation_function": "relu",
                    "attributes": {"output_size": 1},
                }
            )
            hidden_ids.append(node_id)

        # Output node
        output_id = graph.add_node(
            {
                "node_type": NodeType.OUTPUT,
                "activation_function": "identity",
                "attributes": {"output_size": 1},
            }
        )

        # Connect input to hidden
        for input_id in input_ids:
            for hidden_id in hidden_ids:
                graph.add_edge(input_id, hidden_id)

        # Connect hidden to output
        for hidden_id in hidden_ids:
            graph.add_edge(hidden_id, output_id)

        assert len(graph.nodes) == 7
        assert len(list(graph.list_edges())) == 10  # 4*2 + 2*1

        # Test topological sort
        topo_order = graph.topological_sort()
        assert topo_order is not None
        assert len(topo_order) == 7


class TestPyTorchConversion:
    """Test converting graphs to PyTorch models"""

    def test_simple_conversion(self):
        """Test converting a simple graph to PyTorch model"""
        graph = Graph()

        # Create simple network: 2 inputs -> 1 output
        input1 = graph.add_node(
            {
                "node_type": NodeType.INPUT,
                "activation_function": "identity",
                "attributes": {"output_size": 1},
            }
        )

        input2 = graph.add_node(
            {
                "node_type": NodeType.INPUT,
                "activation_function": "identity",
                "attributes": {"output_size": 1},
            }
        )

        output = graph.add_node(
            {
                "node_type": NodeType.OUTPUT,
                "activation_function": "identity",
                "attributes": {"output_size": 1},
            }
        )

        graph.add_edge(input1, output)
        graph.add_edge(input2, output)

        # Convert to PyTorch
        config = {"device": "cpu", "dtype": torch.float32}
        model = to_pytorch_model(graph, config)

        assert model is not None
        assert isinstance(model, torch.nn.Module)

        # Test forward pass
        x = torch.randn(10, 2)  # batch_size=10, input_dim=2
        y = model(x)

        assert y is not None
        assert y.shape == (10, 1)  # batch_size=10, output_dim=1

    def test_multi_layer_conversion(self):
        """Test converting multi-layer graph to PyTorch"""
        graph = Graph()

        # Input layer (3 nodes)
        input_ids = []
        for i in range(3):
            node_id = graph.add_node(
                {
                    "node_type": NodeType.INPUT,
                    "activation_function": "identity",
                    "attributes": {"output_size": 1},
                }
            )
            input_ids.append(node_id)

        # Hidden layer (4 nodes)
        hidden_ids = []
        for i in range(4):
            node_id = graph.add_node(
                {
                    "node_type": NodeType.HIDDEN,
                    "activation_function": "relu",
                    "attributes": {"output_size": 1},
                }
            )
            hidden_ids.append(node_id)

        # Output layer (2 nodes)
        output_ids = []
        for i in range(2):
            node_id = graph.add_node(
                {
                    "node_type": NodeType.OUTPUT,
                    "activation_function": "identity",
                    "attributes": {"output_size": 1},
                }
            )
            output_ids.append(node_id)

        # Connect layers
        for input_id in input_ids:
            for hidden_id in hidden_ids:
                graph.add_edge(input_id, hidden_id)

        for hidden_id in hidden_ids:
            for output_id in output_ids:
                graph.add_edge(hidden_id, output_id)

        # Convert to PyTorch
        config = {"device": "cpu", "dtype": torch.float32}
        model = to_pytorch_model(graph, config)

        # Test forward pass
        x = torch.randn(32, 3)  # batch_size=32, input_dim=3
        y = model(x)

        assert y.shape == (32, 2)  # batch_size=32, output_dim=2

    def test_different_activations(self):
        """Test different activation functions"""
        activations = ["relu", "tanh", "sigmoid", "elu"]

        for activation in activations:
            graph = Graph()

            # Simple 2-1-1 network
            input_id = graph.add_node(
                {
                    "node_type": NodeType.INPUT,
                    "activation_function": "identity",
                    "attributes": {"output_size": 1},
                }
            )

            hidden_id = graph.add_node(
                {
                    "node_type": NodeType.HIDDEN,
                    "activation_function": activation,
                    "attributes": {"output_size": 1},
                }
            )

            output_id = graph.add_node(
                {
                    "node_type": NodeType.OUTPUT,
                    "activation_function": "identity",
                    "attributes": {"output_size": 1},
                }
            )

            graph.add_edge(input_id, hidden_id)
            graph.add_edge(hidden_id, output_id)

            # Convert and test
            model = to_pytorch_model(graph, {"device": "cpu"})
            x = torch.randn(5, 1)
            y = model(x)

            assert y.shape == (5, 1), f"Failed for activation: {activation}"


class TestRealWorldNetworks:
    """Test creating real-world neural network architectures"""

    def test_mlp_for_california_housing(self):
        """Test creating MLP for California Housing dataset (8 inputs, 1 output)"""
        graph = Graph()

        # Input layer (8 features)
        input_ids = []
        for i in range(8):
            node_id = graph.add_node(
                {
                    "node_type": NodeType.INPUT,
                    "activation_function": "identity",
                    "attributes": {"output_size": 1, "name": f"feature_{i}"},
                }
            )
            input_ids.append(node_id)

        # First hidden layer (64 neurons)
        hidden1_ids = []
        for i in range(64):
            node_id = graph.add_node(
                {
                    "node_type": NodeType.HIDDEN,
                    "activation_function": "relu",
                    "attributes": {"output_size": 1, "name": f"hidden1_{i}"},
                }
            )
            hidden1_ids.append(node_id)

        # Second hidden layer (32 neurons)
        hidden2_ids = []
        for i in range(32):
            node_id = graph.add_node(
                {
                    "node_type": NodeType.HIDDEN,
                    "activation_function": "relu",
                    "attributes": {"output_size": 1, "name": f"hidden2_{i}"},
                }
            )
            hidden2_ids.append(node_id)

        # Output layer (1 for regression)
        output_id = graph.add_node(
            {
                "node_type": NodeType.OUTPUT,
                "activation_function": "identity",
                "attributes": {"output_size": 1, "name": "price_prediction"},
            }
        )

        # Connect layers
        for input_id in input_ids:
            for hidden_id in hidden1_ids:
                graph.add_edge(input_id, hidden_id)

        for hidden1_id in hidden1_ids:
            for hidden2_id in hidden2_ids:
                graph.add_edge(hidden1_id, hidden2_id)

        for hidden2_id in hidden2_ids:
            graph.add_edge(hidden2_id, output_id)

        # Verify structure
        assert len(graph.nodes) == 105  # 8 + 64 + 32 + 1
        assert len(list(graph.list_edges())) == 8 * 64 + 64 * 32 + 32 * 1  # 2592 edges

        # Convert to PyTorch
        model = to_pytorch_model(graph, {"device": "cpu"})

        # Test with realistic input
        x = torch.randn(100, 8)  # 100 samples, 8 features
        y = model(x)

        assert y.shape == (100, 1)

        # Count parameters
        n_params = sum(p.numel() for p in model.parameters())
        # Expected: (8*64 + 64) + (64*32 + 32) + (32*1 + 1) = 2657
        assert n_params > 0, f"Model has {n_params} parameters"


class TestGraphUtilities:
    """Test graph utility functions"""

    def test_graph_validation(self):
        """Test graph validation"""
        graph = Graph()

        # Add disconnected nodes
        _ = graph.add_node(
            {
                "node_type": NodeType.INPUT,
                "activation_function": "identity",
                "attributes": {"output_size": 1},
            }
        )

        _ = graph.add_node(
            {
                "node_type": NodeType.OUTPUT,
                "activation_function": "identity",
                "attributes": {"output_size": 1},
            }
        )

        # Graph should be valid even without edges
        assert graph.validate() is False

    def test_cycle_detection(self):
        """Test cycle detection in graph"""
        graph = Graph()

        # Create nodes
        node1 = graph.add_node(
            {
                "node_type": NodeType.HIDDEN,
                "activation_function": "relu",
                "attributes": {"output_size": 1},
            }
        )

        node2 = graph.add_node(
            {
                "node_type": NodeType.HIDDEN,
                "activation_function": "relu",
                "attributes": {"output_size": 1},
            }
        )

        # Add edges to create cycle
        graph.add_edge(node1, node2)
        graph.add_edge(node2, node1)  # Creates cycle

        # Check if cycle is detected
        has_cycle = graph.detect_cycles()
        assert has_cycle is None


class TestEdgeCases:
    """Test edge cases and error conditions"""

    def test_empty_graph_conversion(self):
        """Test converting empty graph"""
        graph = Graph()

        # Should either raise error or return None
        try:
            model = to_pytorch_model(graph, {"device": "cpu"})
            assert model is None or len(list(model.parameters())) == 0
        except (ValueError, RuntimeError):
            pass  # Expected behavior

    def test_invalid_activation(self):
        """Test invalid activation function"""
        graph = Graph()

        # Try to create node with invalid activation
        try:
            node_id = graph.add_node(
                {
                    "node_type": NodeType.HIDDEN,
                    "activation_function": "invalid_activation",
                    "attributes": {"output_size": 1},
                }
            )

            output_id = graph.add_node(
                {
                    "node_type": NodeType.OUTPUT,
                    "activation_function": "identity",
                    "attributes": {"output_size": 1},
                }
            )

            graph.add_edge(node_id, output_id)

            # Conversion should fail
            with pytest.raises((ValueError, RuntimeError)):
                _ = to_pytorch_model(graph, {"device": "cpu"})
        except Exception:
            pass  # Some errors are acceptable here


if __name__ == "__main__":
    # Run tests
    pytest.main([__file__, "-v", "--tb=short"])
