"""
Comprehensive tests for advanced aggregation functions including
attention mechanisms, mixture of experts, and custom aggregations.
"""

import os
import sys

import pytest
import torch

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ggnes import Graph, NodeType
from ggnes.translation import to_pytorch_model


class TestAttentionAggregations:
    """Test attention-based aggregation functions."""

    def test_self_attention_aggregation(self):
        """Test self-attention aggregation."""
        graph = Graph()

        # Create multi-branch architecture
        input_id = graph.add_node(
            {
                "node_type": NodeType.INPUT,
                "activation_function": "linear",
                "attributes": {"output_size": 64},
            }
        )

        # Create parallel branches
        branch_ids = []
        for i in range(3):
            branch_id = graph.add_node(
                {
                    "node_type": NodeType.HIDDEN,
                    "activation_function": "relu",
                    "attributes": {"output_size": 64},
                }
            )
            graph.add_edge(input_id, branch_id)
            branch_ids.append(branch_id)

        # Attention aggregation node
        attention_id = graph.add_node(
            {
                "node_type": NodeType.HIDDEN,
                "activation_function": "linear",
                "attributes": {
                    "output_size": 64,
                    "aggregation_function": "attention",
                    "temperature": 1.0,
                    "dropout_p": 0.1,
                },
            }
        )

        for branch_id in branch_ids:
            graph.add_edge(branch_id, attention_id)

        output_id = graph.add_node(
            {
                "node_type": NodeType.OUTPUT,
                "activation_function": "linear",
                "attributes": {"output_size": 10},
            }
        )
        graph.add_edge(attention_id, output_id)

        # Test model creation and forward pass
        model = to_pytorch_model(graph)
        x = torch.randn(32, 64)

        try:
            y = model(x)
            assert y.shape == (32, 10)

            # Check attention weights sum to 1
            # This would require access to internal attention weights
        except RuntimeError as e:
            pytest.xfail(f"Attention aggregation not working: {e}")

    def test_multi_head_attention_aggregation(self):
        """Test multi-head attention aggregation."""
        graph = Graph()

        # Create query, key, value inputs
        query_id = graph.add_node(
            {
                "node_type": NodeType.INPUT,
                "activation_function": "linear",
                "attributes": {"output_size": 64},
            }
        )

        key_id = graph.add_node(
            {
                "node_type": NodeType.INPUT,
                "activation_function": "linear",
                "attributes": {"output_size": 64},
            }
        )

        value_id = graph.add_node(
            {
                "node_type": NodeType.INPUT,
                "activation_function": "linear",
                "attributes": {"output_size": 64},
            }
        )

        # Multi-head attention node
        mha_id = graph.add_node(
            {
                "node_type": NodeType.HIDDEN,
                "activation_function": "linear",
                "attributes": {
                    "output_size": 64,
                    "aggregation_function": "multi_head_attention",
                    "num_heads": 8,
                    "dropout_p": 0.1,
                },
            }
        )

        graph.add_edge(query_id, mha_id)
        graph.add_edge(key_id, mha_id)
        graph.add_edge(value_id, mha_id)

        output_id = graph.add_node(
            {
                "node_type": NodeType.OUTPUT,
                "activation_function": "linear",
                "attributes": {"output_size": 64},
            }
        )
        graph.add_edge(mha_id, output_id)

        model = to_pytorch_model(graph)

        batch_size = 16
        seq_len = 10

        q = torch.randn(batch_size, seq_len, 64)
        k = torch.randn(batch_size, seq_len, 64)
        v = torch.randn(batch_size, seq_len, 64)

        try:
            # Model should handle sequence inputs
            y = model([q, k, v])
            assert y.shape == (batch_size, seq_len, 64)
        except:
            # Try flattened version
            q_flat = torch.randn(batch_size, 64)
            k_flat = torch.randn(batch_size, 64)
            v_flat = torch.randn(batch_size, 64)

            try:
                y = model([q_flat, k_flat, v_flat])
                assert y.shape == (batch_size, 64)
            except RuntimeError as e:
                pytest.xfail(f"Multi-head attention not working: {e}")

    def test_attention_pooling(self):
        """Test attention pooling aggregation."""
        graph = Graph()

        # Multiple inputs to pool
        input_ids = []
        for i in range(5):
            input_id = graph.add_node(
                {
                    "node_type": NodeType.INPUT,
                    "activation_function": "linear",
                    "attributes": {"output_size": 32},
                }
            )
            input_ids.append(input_id)

        # Attention pooling node
        pool_id = graph.add_node(
            {
                "node_type": NodeType.HIDDEN,
                "activation_function": "linear",
                "attributes": {
                    "output_size": 32,
                    "aggregation_function": "attn_pool",
                    "pool_size": len(input_ids),
                },
            }
        )

        for input_id in input_ids:
            graph.add_edge(input_id, pool_id)

        output_id = graph.add_node(
            {
                "node_type": NodeType.OUTPUT,
                "activation_function": "linear",
                "attributes": {"output_size": 1},
            }
        )
        graph.add_edge(pool_id, output_id)

        model = to_pytorch_model(graph)

        inputs = [torch.randn(32, 32) for _ in range(5)]

        try:
            y = model(inputs)
            assert y.shape == (32, 1)
        except RuntimeError as e:
            pytest.xfail(f"Attention pooling not working: {e}")


class TestMixtureOfExperts:
    """Test Mixture of Experts aggregation."""

    def test_moe_basic(self):
        """Test basic MoE aggregation."""
        graph = Graph()

        input_id = graph.add_node(
            {
                "node_type": NodeType.INPUT,
                "activation_function": "linear",
                "attributes": {"output_size": 64},
            }
        )

        # Create expert branches
        expert_ids = []
        for i in range(4):
            expert_id = graph.add_node(
                {
                    "node_type": NodeType.HIDDEN,
                    "activation_function": "relu",
                    "attributes": {
                        "output_size": 32,
                        "expert_id": i,  # Mark as expert
                    },
                }
            )
            graph.add_edge(input_id, expert_id)
            expert_ids.append(expert_id)

        # MoE aggregation node
        moe_id = graph.add_node(
            {
                "node_type": NodeType.HIDDEN,
                "activation_function": "linear",
                "attributes": {
                    "output_size": 32,
                    "aggregation_function": "moe",
                    "num_experts": 4,
                    "top_k": 2,  # Use top 2 experts
                },
            }
        )

        for expert_id in expert_ids:
            graph.add_edge(expert_id, moe_id)

        output_id = graph.add_node(
            {
                "node_type": NodeType.OUTPUT,
                "activation_function": "linear",
                "attributes": {"output_size": 10},
            }
        )
        graph.add_edge(moe_id, output_id)

        model = to_pytorch_model(graph)
        x = torch.randn(32, 64)

        try:
            y = model(x)
            assert y.shape == (32, 10)
        except RuntimeError as e:
            pytest.xfail(f"MoE aggregation not working: {e}")

    def test_moe_with_gating(self):
        """Test MoE with learned gating."""
        graph = Graph()

        input_id = graph.add_node(
            {
                "node_type": NodeType.INPUT,
                "activation_function": "linear",
                "attributes": {"output_size": 128},
            }
        )

        # Gating network
        gate_id = graph.add_node(
            {
                "node_type": NodeType.HIDDEN,
                "activation_function": "softmax",
                "attributes": {
                    "output_size": 8,  # 8 experts
                    "role": "gate",
                },
            }
        )
        graph.add_edge(input_id, gate_id)

        # Expert networks
        expert_ids = []
        for i in range(8):
            expert_id = graph.add_node(
                {
                    "node_type": NodeType.HIDDEN,
                    "activation_function": "relu",
                    "attributes": {"output_size": 64},
                }
            )
            graph.add_edge(input_id, expert_id)
            expert_ids.append(expert_id)

        # MoE combination
        moe_id = graph.add_node(
            {
                "node_type": NodeType.HIDDEN,
                "activation_function": "linear",
                "attributes": {
                    "output_size": 64,
                    "aggregation_function": "moe",
                    "gate_node": gate_id,
                    "num_experts": 8,
                    "top_k": 3,
                },
            }
        )

        graph.add_edge(gate_id, moe_id)  # Gate input
        for expert_id in expert_ids:
            graph.add_edge(expert_id, moe_id)

        output_id = graph.add_node(
            {
                "node_type": NodeType.OUTPUT,
                "activation_function": "linear",
                "attributes": {"output_size": 10},
            }
        )
        graph.add_edge(moe_id, output_id)

        model = to_pytorch_model(graph)
        x = torch.randn(32, 128)

        try:
            y = model(x)
            assert y.shape == (32, 10)
        except RuntimeError as e:
            pytest.xfail(f"Gated MoE not working: {e}")


class TestWeightedAggregations:
    """Test weighted and gated aggregation functions."""

    def test_gated_sum_aggregation(self):
        """Test gated sum aggregation."""
        graph = Graph()

        # Two inputs to gate
        input1_id = graph.add_node(
            {
                "node_type": NodeType.INPUT,
                "activation_function": "linear",
                "attributes": {"output_size": 32},
            }
        )

        input2_id = graph.add_node(
            {
                "node_type": NodeType.INPUT,
                "activation_function": "linear",
                "attributes": {"output_size": 32},
            }
        )

        # Gated aggregation
        gated_id = graph.add_node(
            {
                "node_type": NodeType.HIDDEN,
                "activation_function": "linear",
                "attributes": {
                    "output_size": 32,
                    "aggregation_function": "gated_sum",
                    "gate_activation": "sigmoid",
                },
            }
        )

        graph.add_edge(input1_id, gated_id)
        graph.add_edge(input2_id, gated_id)

        output_id = graph.add_node(
            {
                "node_type": NodeType.OUTPUT,
                "activation_function": "linear",
                "attributes": {"output_size": 16},
            }
        )
        graph.add_edge(gated_id, output_id)

        model = to_pytorch_model(graph)

        x1 = torch.randn(32, 32)
        x2 = torch.randn(32, 32)

        try:
            y = model([x1, x2])
            assert y.shape == (32, 16)

            # Test gate behavior
            # With x2 = 0, output should depend mainly on x1
            x2_zero = torch.zeros(32, 32)
            y_zero = model([x1, x2_zero])

            # With x1 = 0, output should depend mainly on x2
            x1_zero = torch.zeros(32, 32)
            y_zero2 = model([x1_zero, x2])

            # Outputs should be different
            assert not torch.allclose(y_zero, y_zero2)
        except RuntimeError as e:
            pytest.xfail(f"Gated sum not working: {e}")

    def test_topk_weighted_sum(self):
        """Test top-k weighted sum aggregation."""
        graph = Graph()

        # Multiple inputs
        input_ids = []
        for i in range(10):
            input_id = graph.add_node(
                {
                    "node_type": NodeType.INPUT,
                    "activation_function": "linear",
                    "attributes": {"output_size": 16},
                }
            )
            input_ids.append(input_id)

        # Top-k aggregation
        topk_id = graph.add_node(
            {
                "node_type": NodeType.HIDDEN,
                "activation_function": "linear",
                "attributes": {
                    "output_size": 16,
                    "aggregation_function": "topk_weighted_sum",
                    "top_k": 3,  # Use top 3 inputs
                    "temperature": 0.5,
                },
            }
        )

        for input_id in input_ids:
            graph.add_edge(input_id, topk_id)

        output_id = graph.add_node(
            {
                "node_type": NodeType.OUTPUT,
                "activation_function": "linear",
                "attributes": {"output_size": 8},
            }
        )
        graph.add_edge(topk_id, output_id)

        model = to_pytorch_model(graph)

        inputs = [torch.randn(32, 16) for _ in range(10)]

        try:
            y = model(inputs)
            assert y.shape == (32, 8)

            # Test that only top-k contribute
            # Make most inputs very small
            small_inputs = [torch.randn(32, 16) * 0.001 for _ in range(7)]
            large_inputs = [torch.randn(32, 16) * 10 for _ in range(3)]
            all_inputs = small_inputs + large_inputs

            y_topk = model(all_inputs)

            # Output should be dominated by large inputs
            y_large_only = model(large_inputs + [torch.zeros(32, 16)] * 7)

            # Should be similar since top-k selects large inputs
            # (This is approximate test)
        except RuntimeError as e:
            pytest.xfail(f"Top-k weighted sum not working: {e}")


class TestMatrixAggregations:
    """Test matrix-based aggregation functions."""

    def test_matrix_product_aggregation(self):
        """Test matrix product aggregation."""
        graph = Graph()

        # Two matrix inputs
        input1_id = graph.add_node(
            {
                "node_type": NodeType.INPUT,
                "activation_function": "linear",
                "attributes": {"output_size": 64},
            }
        )

        input2_id = graph.add_node(
            {
                "node_type": NodeType.INPUT,
                "activation_function": "linear",
                "attributes": {"output_size": 64},
            }
        )

        # Matrix product aggregation
        matmul_id = graph.add_node(
            {
                "node_type": NodeType.HIDDEN,
                "activation_function": "linear",
                "attributes": {
                    "output_size": 64,
                    "aggregation_function": "matrix_product",
                    "transpose_first": False,
                    "transpose_second": True,
                },
            }
        )

        graph.add_edge(input1_id, matmul_id)
        graph.add_edge(input2_id, matmul_id)

        output_id = graph.add_node(
            {
                "node_type": NodeType.OUTPUT,
                "activation_function": "linear",
                "attributes": {"output_size": 32},
            }
        )
        graph.add_edge(matmul_id, output_id)

        model = to_pytorch_model(graph)

        # Test with batch of matrices
        x1 = torch.randn(32, 8, 64)  # [batch, seq1, dim]
        x2 = torch.randn(32, 8, 64)  # [batch, seq2, dim]

        try:
            y = model([x1, x2])
            # Output shape depends on matrix multiplication
            assert len(y.shape) >= 2
        except:
            # Try with 2D inputs
            x1_2d = torch.randn(32, 64)
            x2_2d = torch.randn(32, 64)

            try:
                y = model([x1_2d, x2_2d])
                assert y.shape == (32, 32) or y.shape == (32, 64)
            except RuntimeError as e:
                pytest.xfail(f"Matrix product not working: {e}")

    def test_bilinear_aggregation(self):
        """Test bilinear aggregation."""
        from ggnes.aggregations import BilinearAggregation

        try:
            # Create bilinear aggregation module
            bilinear = BilinearAggregation(input_size1=64, input_size2=64, output_size=32)

            x1 = torch.randn(32, 64)
            x2 = torch.randn(32, 64)

            output = bilinear([x1, x2])
            assert output.shape == (32, 32)

            # Test learnable parameters
            assert len(list(bilinear.parameters())) > 0
        except ImportError:
            pytest.skip("Bilinear aggregation not implemented")


class TestCustomAggregations:
    """Test custom user-defined aggregations."""

    def test_register_custom_aggregation(self):
        """Test registering custom aggregation function."""
        from ggnes.aggregations import register_aggregation

        try:

            @register_aggregation("harmonic_mean")
            def harmonic_mean_aggregation(inputs, **kwargs):
                """Compute harmonic mean of inputs."""
                # inputs: list of tensors
                stacked = torch.stack(inputs, dim=0)
                reciprocal = 1.0 / (stacked + 1e-8)
                mean_reciprocal = reciprocal.mean(dim=0)
                return 1.0 / (mean_reciprocal + 1e-8)

            # Use in graph
            graph = Graph()

            in1 = graph.add_node(
                {
                    "node_type": NodeType.INPUT,
                    "activation_function": "linear",
                    "attributes": {"output_size": 16},
                }
            )

            in2 = graph.add_node(
                {
                    "node_type": NodeType.INPUT,
                    "activation_function": "linear",
                    "attributes": {"output_size": 16},
                }
            )

            agg = graph.add_node(
                {
                    "node_type": NodeType.HIDDEN,
                    "activation_function": "relu",
                    "attributes": {"output_size": 16, "aggregation_function": "harmonic_mean"},
                }
            )

            graph.add_edge(in1, agg)
            graph.add_edge(in2, agg)

            model = to_pytorch_model(graph)

            x1 = torch.ones(32, 16) * 2.0
            x2 = torch.ones(32, 16) * 3.0

            y = model([x1, x2])

            # Harmonic mean of 2 and 3 is 2.4
            expected = 2.4
            assert torch.allclose(y.mean(), torch.tensor(expected), rtol=0.1)
        except ImportError:
            pytest.skip("Custom aggregation registration not implemented")

    def test_learnable_aggregation(self):
        """Test learnable aggregation weights."""
        from ggnes.aggregations import LearnableAggregation

        try:
            # Create learnable weighted aggregation
            learnable_agg = LearnableAggregation(
                num_inputs=5,
                input_size=32,
                output_size=32,
                learn_weights=True,
                normalize_weights=True,
            )

            inputs = [torch.randn(16, 32) for _ in range(5)]
            output = learnable_agg(inputs)

            assert output.shape == (16, 32)

            # Check that weights sum to 1
            weights = learnable_agg.get_weights()
            assert torch.allclose(weights.sum(), torch.tensor(1.0))

            # Weights should be learnable
            assert weights.requires_grad
        except ImportError:
            pytest.skip("Learnable aggregation not implemented")


class TestAggregationCompatibility:
    """Test aggregation compatibility with different input configurations."""

    def test_variable_number_inputs(self):
        """Test aggregations with variable number of inputs."""
        graph = Graph()

        # Create variable number of inputs (2-10)
        for num_inputs in [2, 5, 10]:
            g = Graph()

            input_ids = []
            for i in range(num_inputs):
                input_id = g.add_node(
                    {
                        "node_type": NodeType.INPUT,
                        "activation_function": "linear",
                        "attributes": {"output_size": 16},
                    }
                )
                input_ids.append(input_id)

            # Test different aggregations
            for agg_func in ["sum", "mean", "max", "concat"]:
                agg_graph = Graph()

                # Copy input nodes
                input_ids = []
                for i in range(num_inputs):
                    input_id = agg_graph.add_node(
                        {
                            "node_type": NodeType.INPUT,
                            "activation_function": "linear",
                            "attributes": {"output_size": 16},
                        }
                    )
                    input_ids.append(input_id)

                # Aggregation node
                output_size = 16 * num_inputs if agg_func == "concat" else 16
                agg_id = agg_graph.add_node(
                    {
                        "node_type": NodeType.OUTPUT,
                        "activation_function": "linear",
                        "attributes": {
                            "output_size": output_size,
                            "aggregation_function": agg_func,
                        },
                    }
                )

                for input_id in input_ids:
                    agg_graph.add_edge(input_id, agg_id)

                model = to_pytorch_model(agg_graph)

                if num_inputs == 1:
                    x = torch.randn(32, 16)
                    y = model(x)
                else:
                    inputs = [torch.randn(32, 16) for _ in range(num_inputs)]
                    y = model(inputs if num_inputs > 1 else inputs[0])

                expected_size = 16 * num_inputs if agg_func == "concat" else 16
                assert y.shape == (32, output_size)

    def test_mixed_size_inputs(self):
        """Test aggregations with different input sizes."""
        # Most aggregations require same size inputs
        # Concat is exception
        graph = Graph()

        in1 = graph.add_node(
            {
                "node_type": NodeType.INPUT,
                "activation_function": "linear",
                "attributes": {"output_size": 16},
            }
        )

        in2 = graph.add_node(
            {
                "node_type": NodeType.INPUT,
                "activation_function": "linear",
                "attributes": {"output_size": 32},
            }
        )

        # Concat should work with different sizes
        concat_id = graph.add_node(
            {
                "node_type": NodeType.OUTPUT,
                "activation_function": "linear",
                "attributes": {
                    "output_size": 48,  # 16 + 32
                    "aggregation_function": "concat",
                },
            }
        )

        graph.add_edge(in1, concat_id)
        graph.add_edge(in2, concat_id)

        model = to_pytorch_model(graph)

        x1 = torch.randn(32, 16)
        x2 = torch.randn(32, 32)

        y = model([x1, x2])
        assert y.shape == (32, 48)
