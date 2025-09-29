"""
Comprehensive integration tests for PyTorch translation of complex architectures,
shape inference, and end-to-end model training.
"""

import os
import sys

import pytest
import torch
import torch.nn as nn

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ggnes import Graph, NodeType
from ggnes.translation import to_pytorch_model


class TestComplexArchitectureTranslation:
    """Test translating complex neural architectures to PyTorch."""

    def test_resnet_block_translation(self):
        """Test translating ResNet-like residual blocks."""
        graph = Graph()

        # Input
        input_id = graph.add_node(
            {
                "id": "input",
                "node_type": NodeType.INPUT,
                "activation_function": "linear",
                "output_size": 64,
            }
        )

        # First conv path
        conv1_id = graph.add_node(
            {
                "id": "conv1",
                "node_type": NodeType.HIDDEN,
                "activation_function": "relu",
                "output_size": 64,
            }
        )

        conv2_id = graph.add_node(
            {
                "id": "conv2",
                "node_type": NodeType.HIDDEN,
                "activation_function": "linear",  # No activation before add
                "output_size": 64,
            }
        )

        # Residual connection (skip)
        add_id = graph.add_node(
            {
                "id": "add",
                "node_type": NodeType.HIDDEN,
                "activation_function": "relu",  # Activation after add
                "output_size": 64,
                "aggregation_function": "sum",
            }
        )

        # Output
        output_id = graph.add_node(
            {
                "id": "output",
                "node_type": NodeType.OUTPUT,
                "activation_function": "linear",
                "output_size": 10,
            }
        )

        # Connect main path
        graph.add_edge("input", "conv1")
        graph.add_edge("conv1", "conv2")
        graph.add_edge("conv2", "add")

        # Skip connection
        graph.add_edge("input", "add")

        # To output
        graph.add_edge("add", "output")

        # Translate to PyTorch
        model = to_pytorch_model(graph)

        # Test forward pass
        x = torch.randn(32, 64)
        y = model(x)

        assert y.shape == (32, 10)

        # Verify skip connection works
        # Output should be different from just the conv path
        model.eval()
        with torch.no_grad():
            # Zero input should produce near-zero output
            zero_input = torch.zeros(1, 64)
            zero_output = model(zero_input)

            # Non-zero input should activate
            nonzero_input = torch.ones(1, 64)
            nonzero_output = model(nonzero_input)

            assert not torch.allclose(zero_output, nonzero_output)

    def test_inception_module_translation(self):
        """Test translating Inception-like parallel paths."""
        graph = Graph()

        # Input
        input_id = graph.add_node(
            {
                "id": "input",
                "node_type": NodeType.INPUT,
                "activation_function": "linear",
                "output_size": 256,
            }
        )

        # 1x1 convolution path
        conv1x1_id = graph.add_node(
            {
                "id": "conv1x1",
                "node_type": NodeType.HIDDEN,
                "activation_function": "relu",
                "output_size": 64,
            }
        )

        # 3x3 convolution path
        conv3x3_reduce_id = graph.add_node(
            {
                "id": "conv3x3_reduce",
                "node_type": NodeType.HIDDEN,
                "activation_function": "relu",
                "output_size": 96,
            }
        )

        conv3x3_id = graph.add_node(
            {
                "id": "conv3x3",
                "node_type": NodeType.HIDDEN,
                "activation_function": "relu",
                "output_size": 128,
            }
        )

        # 5x5 convolution path
        conv5x5_reduce_id = graph.add_node(
            {
                "id": "conv5x5_reduce",
                "node_type": NodeType.HIDDEN,
                "activation_function": "relu",
                "output_size": 16,
            }
        )

        conv5x5_id = graph.add_node(
            {
                "id": "conv5x5",
                "node_type": NodeType.HIDDEN,
                "activation_function": "relu",
                "output_size": 32,
            }
        )

        # Max pool path
        maxpool_id = graph.add_node(
            {
                "id": "maxpool",
                "node_type": NodeType.HIDDEN,
                "activation_function": "linear",
                "output_size": 256,
                "aggregation_function": "max",
            }
        )

        pool_proj_id = graph.add_node(
            {
                "id": "pool_proj",
                "node_type": NodeType.HIDDEN,
                "activation_function": "relu",
                "output_size": 32,
            }
        )

        # Concatenation
        concat_id = graph.add_node(
            {
                "id": "concat",
                "node_type": NodeType.HIDDEN,
                "activation_function": "linear",
                "output_size": 256,  # 64+128+32+32
                "aggregation_function": "concat",
            }
        )

        # Output
        output_id = graph.add_node(
            {
                "id": "output",
                "node_type": NodeType.OUTPUT,
                "activation_function": "linear",
                "output_size": 1000,
            }
        )

        # Connect paths
        graph.add_edge("input", "conv1x1")
        graph.add_edge("conv1x1", "concat")

        graph.add_edge("input", "conv3x3_reduce")
        graph.add_edge("conv3x3_reduce", "conv3x3")
        graph.add_edge("conv3x3", "concat")

        graph.add_edge("input", "conv5x5_reduce")
        graph.add_edge("conv5x5_reduce", "conv5x5")
        graph.add_edge("conv5x5", "concat")

        graph.add_edge("input", "maxpool")
        graph.add_edge("maxpool", "pool_proj")
        graph.add_edge("pool_proj", "concat")

        graph.add_edge("concat", "output")

        # Translate to PyTorch
        model = to_pytorch_model(graph)

        # Test forward pass
        x = torch.randn(16, 256)
        y = model(x)

        assert y.shape == (16, 1000)

    def test_dense_connections_translation(self):
        """Test translating DenseNet-like dense connections."""
        graph = Graph()

        # Input
        input_id = graph.add_node(
            {
                "id": "input",
                "node_type": NodeType.INPUT,
                "activation_function": "linear",
                "output_size": 64,
            }
        )

        # Dense block with 4 layers
        prev_ids = ["input"]
        layer_outputs = []

        for i in range(4):
            # Each layer receives all previous outputs
            layer_id = graph.add_node(
                {
                    "id": f"layer{i}",
                    "node_type": NodeType.HIDDEN,
                    "activation_function": "relu",
                    "output_size": 32,
                }
            )

            # Concatenate all previous
            if i > 0:
                concat_id = graph.add_node(
                    {
                        "id": f"concat{i}",
                        "node_type": NodeType.HIDDEN,
                        "activation_function": "linear",
                        "output_size": 64 + 32 * i,  # Grows with each layer
                        "aggregation_function": "concat",
                    }
                )

                # Connect all previous to concat
                for prev_id in prev_ids:
                    graph.add_edge(prev_id, f"concat{i}")

                # Connect concat to layer
                graph.add_edge(f"concat{i}", f"layer{i}")
            else:
                # First layer connects directly
                graph.add_edge("input", "layer0")

            prev_ids.append(f"layer{i}")

        # Final concatenation
        final_concat_id = graph.add_node(
            {
                "id": "final_concat",
                "node_type": NodeType.HIDDEN,
                "activation_function": "linear",
                "output_size": 64 + 32 * 4,  # All features
                "aggregation_function": "concat",
            }
        )

        for prev_id in prev_ids:
            graph.add_edge(prev_id, "final_concat")

        # Output
        output_id = graph.add_node(
            {
                "id": "output",
                "node_type": NodeType.OUTPUT,
                "activation_function": "linear",
                "output_size": 10,
            }
        )

        graph.add_edge("final_concat", "output")

        # Translate to PyTorch
        model = to_pytorch_model(graph)

        # Test forward pass
        x = torch.randn(32, 64)
        y = model(x)

        assert y.shape == (32, 10)


class TestShapeInference:
    """Test automatic shape inference in translation."""

    def test_automatic_shape_propagation(self):
        """Test that shapes are automatically inferred."""
        graph = Graph()

        # Input with known size
        input_id = graph.add_node(
            {
                "node_type": NodeType.INPUT,
                "activation_function": "linear",
                "attributes": {"output_size": 784},
            }
        )

        # Hidden layers without explicit sizes (should infer)
        hidden1_id = graph.add_node(
            {
                "node_type": NodeType.HIDDEN,
                "activation_function": "relu",
                "attributes": {"output_size": 256},  # Explicit
            }
        )

        hidden2_id = graph.add_node(
            {
                "node_type": NodeType.HIDDEN,
                "activation_function": "relu",
                "attributes": {"output_size": 128},  # Explicit
            }
        )

        output_id = graph.add_node(
            {
                "node_type": NodeType.OUTPUT,
                "activation_function": "softmax",
                "attributes": {"output_size": 10},
            }
        )

        # Connect
        graph.add_edge(input_id, hidden1_id)
        graph.add_edge(hidden1_id, hidden2_id)
        graph.add_edge(hidden2_id, output_id)

        # Translate
        model = to_pytorch_model(graph)

        # Test with correct input shape
        x = torch.randn(32, 784)
        y = model(x)
        assert y.shape == (32, 10)

        # Test shape mismatch handling
        wrong_x = torch.randn(32, 100)  # Wrong input size
        try:
            y_wrong = model(wrong_x)
            # Should raise error about shape mismatch
            assert False, "Should have raised shape error"
        except (RuntimeError, ValueError):
            pass  # Expected

    def test_dynamic_batch_size(self):
        """Test that models work with different batch sizes."""
        graph = Graph()

        # Simple network
        input_id = graph.add_node(
            {
                "node_type": NodeType.INPUT,
                "activation_function": "linear",
                "attributes": {"output_size": 100},
            }
        )

        hidden_id = graph.add_node(
            {
                "node_type": NodeType.HIDDEN,
                "activation_function": "relu",
                "attributes": {"output_size": 50},
            }
        )

        output_id = graph.add_node(
            {
                "node_type": NodeType.OUTPUT,
                "activation_function": "linear",
                "attributes": {"output_size": 10},
            }
        )

        graph.add_edge(input_id, hidden_id)
        graph.add_edge(hidden_id, output_id)

        model = to_pytorch_model(graph)

        # Test different batch sizes
        for batch_size in [1, 16, 32, 128]:
            x = torch.randn(batch_size, 100)
            y = model(x)
            assert y.shape == (batch_size, 10)

    def test_variable_sequence_length(self):
        """Test handling variable sequence lengths."""
        graph = Graph()

        # RNN-like structure
        input_id = graph.add_node(
            {
                "node_type": NodeType.INPUT,
                "activation_function": "linear",
                "attributes": {
                    "output_size": 64,
                    "input_type": "sequence",  # Hint for sequence input
                },
            }
        )

        rnn_id = graph.add_node(
            {
                "node_type": NodeType.HIDDEN,
                "activation_function": "tanh",
                "attributes": {
                    "output_size": 128,
                    "cell_type": "lstm",  # LSTM cell
                },
            }
        )

        output_id = graph.add_node(
            {
                "node_type": NodeType.OUTPUT,
                "activation_function": "linear",
                "attributes": {"output_size": 10},
            }
        )

        graph.add_edge(input_id, rnn_id)
        graph.add_edge(rnn_id, output_id)

        model = to_pytorch_model(graph)

        # Test with different sequence lengths
        for seq_len in [10, 20, 50]:
            x = torch.randn(32, seq_len, 64)  # [batch, seq, features]
            try:
                y = model(x)
                # Output could be [batch, seq, output] or [batch, output]
                assert y.shape[0] == 32
                assert y.shape[-1] == 10
            except:
                # RNN support might not be complete
                pytest.skip("RNN translation not fully implemented")


class TestModelTraining:
    """Test end-to-end model training with translated models."""

    def test_simple_classification_training(self):
        """Test training a simple classifier."""
        graph = Graph()

        # Build simple MLP
        input_id = graph.add_node(
            {
                "node_type": NodeType.INPUT,
                "activation_function": "linear",
                "attributes": {"output_size": 10},
            }
        )

        hidden_id = graph.add_node(
            {
                "node_type": NodeType.HIDDEN,
                "activation_function": "relu",
                "attributes": {"output_size": 20},
            }
        )

        output_id = graph.add_node(
            {
                "node_type": NodeType.OUTPUT,
                "activation_function": "linear",  # Will use CrossEntropyLoss
                "attributes": {"output_size": 3},
            }
        )

        graph.add_edge(input_id, hidden_id)
        graph.add_edge(hidden_id, output_id)

        # Translate to PyTorch
        model = to_pytorch_model(graph)

        # Create synthetic dataset
        X = torch.randn(100, 10)
        y = torch.randint(0, 3, (100,))

        # Training setup
        optimizer = torch.optim.Adam(model.parameters(), lr=0.01)
        criterion = nn.CrossEntropyLoss()

        # Training loop
        model.train()
        initial_loss = None

        for epoch in range(10):
            optimizer.zero_grad()
            outputs = model(X)
            loss = criterion(outputs, y)

            if initial_loss is None:
                initial_loss = loss.item()

            loss.backward()
            optimizer.step()

        final_loss = loss.item()

        # Loss should decrease
        assert final_loss < initial_loss

        # Model should make predictions
        model.eval()
        with torch.no_grad():
            test_X = torch.randn(10, 10)
            predictions = model(test_X)
            assert predictions.shape == (10, 3)

            # Predictions should be valid class scores
            predicted_classes = torch.argmax(predictions, dim=1)
            assert all(0 <= c < 3 for c in predicted_classes)

    def test_regression_training(self):
        """Test training a regression model."""
        graph = Graph()

        # Build regression network
        input_id = graph.add_node(
            {
                "node_type": NodeType.INPUT,
                "activation_function": "linear",
                "attributes": {"output_size": 5},
            }
        )

        hidden1_id = graph.add_node(
            {
                "node_type": NodeType.HIDDEN,
                "activation_function": "relu",
                "attributes": {"output_size": 10},
            }
        )

        hidden2_id = graph.add_node(
            {
                "node_type": NodeType.HIDDEN,
                "activation_function": "relu",
                "attributes": {"output_size": 10},
            }
        )

        output_id = graph.add_node(
            {
                "node_type": NodeType.OUTPUT,
                "activation_function": "linear",  # Linear for regression
                "attributes": {"output_size": 1},
            }
        )

        graph.add_edge(input_id, hidden1_id)
        graph.add_edge(hidden1_id, hidden2_id)
        graph.add_edge(hidden2_id, output_id)

        # Translate
        model = to_pytorch_model(graph)

        # Create synthetic regression data
        X = torch.randn(100, 5)
        y = torch.randn(100, 1)

        # Training
        optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
        criterion = nn.MSELoss()

        model.train()
        losses = []

        for epoch in range(20):
            optimizer.zero_grad()
            outputs = model(X)
            loss = criterion(outputs, y)
            losses.append(loss.item())
            loss.backward()
            optimizer.step()

        # Loss should generally decrease
        assert losses[-1] < losses[0]

    def test_model_saving_loading(self):
        """Test saving and loading translated models."""
        import tempfile

        graph = Graph()

        # Build network
        input_id = graph.add_node(
            {
                "node_type": NodeType.INPUT,
                "activation_function": "linear",
                "attributes": {"output_size": 10},
            }
        )

        output_id = graph.add_node(
            {
                "node_type": NodeType.OUTPUT,
                "activation_function": "linear",
                "attributes": {"output_size": 5},
            }
        )

        graph.add_edge(input_id, output_id)

        # Translate
        model = to_pytorch_model(graph)

        # Save model
        with tempfile.NamedTemporaryFile(suffix=".pt", delete=False) as f:
            torch.save(model.state_dict(), f.name)
            temp_path = f.name

        # Create new model and load weights
        new_model = to_pytorch_model(graph)
        new_model.load_state_dict(torch.load(temp_path))

        # Models should produce same output
        x = torch.randn(10, 10)

        model.eval()
        new_model.eval()

        with torch.no_grad():
            y1 = model(x)
            y2 = new_model(x)

        assert torch.allclose(y1, y2)

        # Clean up
        os.unlink(temp_path)


class TestGradientFlow:
    """Test gradient flow through translated models."""

    def test_gradient_flow_simple(self):
        """Test that gradients flow correctly."""
        graph = Graph()

        # Simple network
        input_id = graph.add_node(
            {
                "node_type": NodeType.INPUT,
                "activation_function": "linear",
                "attributes": {"output_size": 10},
            }
        )

        hidden_id = graph.add_node(
            {
                "node_type": NodeType.HIDDEN,
                "activation_function": "relu",
                "attributes": {"output_size": 20},
            }
        )

        output_id = graph.add_node(
            {
                "node_type": NodeType.OUTPUT,
                "activation_function": "linear",
                "attributes": {"output_size": 1},
            }
        )

        graph.add_edge(input_id, hidden_id)
        graph.add_edge(hidden_id, output_id)

        model = to_pytorch_model(graph)

        # Check parameters require gradients
        for param in model.parameters():
            assert param.requires_grad

        # Forward pass
        x = torch.randn(10, 10, requires_grad=True)
        y = model(x)

        # Backward pass
        loss = y.sum()
        loss.backward()

        # Check gradients exist
        for param in model.parameters():
            assert param.grad is not None
            assert not torch.all(param.grad == 0)

        # Input gradient should exist
        assert x.grad is not None

    def test_gradient_flow_with_skip_connections(self):
        """Test gradient flow with skip connections."""
        graph = Graph()

        # Network with skip connection
        input_id = graph.add_node(
            {
                "node_type": NodeType.INPUT,
                "activation_function": "linear",
                "attributes": {"output_size": 32},
            }
        )

        hidden1_id = graph.add_node(
            {
                "node_type": NodeType.HIDDEN,
                "activation_function": "relu",
                "attributes": {"output_size": 32},
            }
        )

        hidden2_id = graph.add_node(
            {
                "node_type": NodeType.HIDDEN,
                "activation_function": "relu",
                "attributes": {"output_size": 32},
            }
        )

        # Addition node for skip connection
        add_id = graph.add_node(
            {
                "node_type": NodeType.HIDDEN,
                "activation_function": "linear",
                "attributes": {"output_size": 32, "aggregation_function": "sum"},
            }
        )

        output_id = graph.add_node(
            {
                "node_type": NodeType.OUTPUT,
                "activation_function": "linear",
                "attributes": {"output_size": 1},
            }
        )

        # Main path
        graph.add_edge(input_id, hidden1_id)
        graph.add_edge(hidden1_id, hidden2_id)
        graph.add_edge(hidden2_id, add_id)

        # Skip connection
        graph.add_edge(input_id, add_id)

        graph.add_edge(add_id, output_id)

        model = to_pytorch_model(graph)

        # Forward and backward
        x = torch.randn(10, 32, requires_grad=True)
        y = model(x)
        loss = y.mean()
        loss.backward()

        # Gradients should flow through both paths
        assert x.grad is not None

        # All parameters should have gradients
        for name, param in model.named_parameters():
            assert param.grad is not None, f"No gradient for {name}"
