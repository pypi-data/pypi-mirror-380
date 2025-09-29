#!/usr/bin/env python3
"""
Discovery tests to understand GGNES's actual behavior
Based on test failures, let's discover what actually works
"""

import pytest

from ggnes import Graph, NodeType
from ggnes.translation import to_pytorch_model

torch = pytest.importorskip("torch")


class TestDiscoverActivations:
    """Discover what activation functions are supported"""

    def test_find_valid_activations(self):
        """Test different activation names to find valid ones"""
        possible_activations = [
            "identity",
            "linear",
            "none",
            None,  # Identity attempts
            "relu",
            "ReLU",
            "RELU",  # ReLU variants
            "tanh",
            "TanH",
            "TANH",  # Tanh variants
            "sigmoid",
            "Sigmoid",
            "SIGMOID",  # Sigmoid variants
            "elu",
            "ELU",
            "leaky_relu",
            "LeakyReLU",  # Other activations
            "softmax",
            "Softmax",
            "gelu",
            "GELU",
        ]

        valid_activations = []

        for activation in possible_activations:
            try:
                # Try to create a simple network with this activation
                graph = Graph()

                input_id = graph.add_node(
                    {
                        "node_type": NodeType.INPUT,
                        "activation_function": "linear",  # Use known good for input
                        "attributes": {"output_size": 1},
                    }
                )

                hidden_id = graph.add_node(
                    {
                        "node_type": NodeType.HIDDEN,
                        "activation_function": activation if activation else "linear",
                        "attributes": {"output_size": 1},
                    }
                )

                output_id = graph.add_node(
                    {
                        "node_type": NodeType.OUTPUT,
                        "activation_function": "linear",  # Use known good for output
                        "attributes": {"output_size": 1},
                    }
                )

                graph.add_edge(input_id, hidden_id)
                graph.add_edge(hidden_id, output_id)

                # Try to convert to PyTorch
                _ = to_pytorch_model(graph, {"device": "cpu"})

                # If we get here, it worked!
                valid_activations.append(activation)
                print(f"✓ Valid activation: {activation}")

            except Exception as e:
                print(f"✗ Invalid activation: {activation} - {e}")

        print(f"\nValid activations found: {valid_activations}")
        assert len(valid_activations) > 0, "No valid activations found!"


class TestDiscoverGraphAPI:
    """Discover the actual Graph API behavior"""

    def test_list_edges_behavior(self):
        """Test what list_edges actually returns"""
        graph = Graph()

        # Add two nodes and an edge
        n1 = graph.add_node(
            {
                "node_type": NodeType.INPUT,
                "activation_function": "relu",
                "attributes": {"output_size": 1},
            }
        )

        n2 = graph.add_node(
            {
                "node_type": NodeType.OUTPUT,
                "activation_function": "relu",
                "attributes": {"output_size": 1},
            }
        )

        graph.add_edge(n1, n2)

        # Test list_edges
        edges = graph.list_edges()
        print(f"list_edges type: {type(edges)}")

        # Convert to list if it's a generator
        edges_list = list(edges)
        print(f"Number of edges: {len(edges_list)}")
        print(f"Edge details: {edges_list}")

        assert len(edges_list) == 1

    def test_graph_validation_behavior(self):
        """Test what validate() actually returns"""
        graph = Graph()

        # Empty graph
        result = graph.validate()
        print(f"Empty graph validation: {result} (type: {type(result)})")

        # Graph with nodes
        graph.add_node(
            {
                "node_type": NodeType.INPUT,
                "activation_function": "relu",
                "attributes": {"output_size": 1},
            }
        )

        result = graph.validate()
        print(f"Graph with node validation: {result} (type: {type(result)})")

    def test_input_output_node_ids(self):
        """Test input_node_ids and output_node_ids methods"""
        graph = Graph()

        # Add various nodes
        _ = graph.add_node(
            {
                "node_type": NodeType.INPUT,
                "activation_function": "relu",
                "attributes": {"output_size": 1},
            }
        )

        _ = graph.add_node(
            {
                "node_type": NodeType.INPUT,
                "activation_function": "relu",
                "attributes": {"output_size": 1},
            }
        )

        _ = graph.add_node(
            {
                "node_type": NodeType.HIDDEN,
                "activation_function": "relu",
                "attributes": {"output_size": 1},
            }
        )

        _ = graph.add_node(
            {
                "node_type": NodeType.OUTPUT,
                "activation_function": "relu",
                "attributes": {"output_size": 1},
            }
        )

        input_ids = graph.input_node_ids
        output_ids = graph.output_node_ids

        print(f"Input IDs: {input_ids} (type: {type(input_ids)})")
        print(f"Output IDs: {output_ids} (type: {type(output_ids)})")

        # Convert to list if needed
        input_list = list(input_ids) if hasattr(input_ids, "__iter__") else [input_ids]
        output_list = list(output_ids) if hasattr(output_ids, "__iter__") else [output_ids]

        assert len(input_list) == 2
        assert len(output_list) == 1


class TestMinimalWorkingExample:
    """Find the absolute minimal working example"""

    def test_minimal_graph_that_converts(self):
        """Find the simplest graph that successfully converts to PyTorch"""
        graph = Graph()

        # Try simplest possible: 1 input -> 1 output
        input_id = graph.add_node(
            {
                "node_type": NodeType.INPUT,
                "activation_function": "linear",  # Try 'linear' instead of 'identity'
                "attributes": {"output_size": 1},
            }
        )

        output_id = graph.add_node(
            {
                "node_type": NodeType.OUTPUT,
                "activation_function": "linear",
                "attributes": {"output_size": 1},
            }
        )

        graph.add_edge(input_id, output_id)

        # Try conversion
        try:
            model = to_pytorch_model(graph, {"device": "cpu"})
            print("✓ Minimal graph conversion successful!")

            # Test forward pass
            x = torch.randn(5, 1)
            y = model(x)
            print(f"✓ Forward pass successful! Input shape: {x.shape}, Output shape: {y.shape}")

            # Count parameters
            n_params = sum(p.numel() for p in model.parameters())
            print(f"✓ Model has {n_params} parameters")

            assert True
        except Exception as e:
            print(f"✗ Minimal graph conversion failed: {e}")
            import pytest as _pytest

            _pytest.fail(f"Minimal graph conversion failed: {e}")


class TestWorkingPatterns:
    """Test patterns that should work based on discoveries"""

    def test_working_mlp(self):
        """Create an MLP using discovered working patterns"""
        graph = Graph()

        # Input layer (2 inputs)
        input1 = graph.add_node(
            {
                "node_type": NodeType.INPUT,
                "activation_function": "linear",
                "attributes": {"output_size": 1},
            }
        )

        input2 = graph.add_node(
            {
                "node_type": NodeType.INPUT,
                "activation_function": "linear",
                "attributes": {"output_size": 1},
            }
        )

        # Hidden layer (3 neurons with relu)
        hidden_ids = []
        for i in range(3):
            hid = graph.add_node(
                {
                    "node_type": NodeType.HIDDEN,
                    "activation_function": "relu",
                    "attributes": {"output_size": 1},
                }
            )
            hidden_ids.append(hid)

            # Connect from inputs
            graph.add_edge(input1, hid)
            graph.add_edge(input2, hid)

        # Output layer
        output = graph.add_node(
            {
                "node_type": NodeType.OUTPUT,
                "activation_function": "linear",
                "attributes": {"output_size": 1},
            }
        )

        # Connect hidden to output
        for hid in hidden_ids:
            graph.add_edge(hid, output)

        # Convert and test
        try:
            model = to_pytorch_model(graph, {"device": "cpu"})

            # Test forward pass
            x = torch.randn(10, 2)
            y = model(x)

            assert y.shape == (10, 1), f"Expected shape (10, 1), got {y.shape}"
            print(f"✓ Working MLP created successfully! Output shape: {y.shape}")

            # Count parameters
            n_params = sum(p.numel() for p in model.parameters())
            print(f"✓ MLP has {n_params} parameters")

            assert True
        except Exception as e:
            print(f"✗ MLP creation failed: {e}")
            import pytest as _pytest

            _pytest.fail(f"MLP creation failed: {e}")


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s", "--tb=short"])
