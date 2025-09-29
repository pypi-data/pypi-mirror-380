"""
Advanced aggregation functions for GGNES.
"""

import math
from collections.abc import Callable

import torch
import torch.nn as nn
import torch.nn.functional as F

# Registry for custom aggregations
_AGGREGATION_REGISTRY = {}


def register_aggregation(name: str):
    """Decorator to register custom aggregation functions."""

    def decorator(func: Callable):
        _AGGREGATION_REGISTRY[name] = func
        return func

    return decorator


def get_aggregation(name: str) -> Callable:
    """Get aggregation function by name."""
    if name in _AGGREGATION_REGISTRY:
        return _AGGREGATION_REGISTRY[name]

    # Built-in aggregations
    built_ins = {
        "sum": sum_aggregation,
        "mean": mean_aggregation,
        "max": max_aggregation,
        "concat": concat_aggregation,
        "attention": attention_aggregation,
        "multi_head_attention": multi_head_attention_aggregation,
        "attn_pool": attention_pooling_aggregation,
        "moe": mixture_of_experts_aggregation,
        "gated_sum": gated_sum_aggregation,
        "topk_weighted_sum": topk_weighted_sum_aggregation,
        "matrix_product": matrix_product_aggregation,
    }

    if name in built_ins:
        return built_ins[name]

    raise ValueError(f"Unknown aggregation function: {name}")


# Basic aggregations
def sum_aggregation(inputs: list[torch.Tensor], **kwargs) -> torch.Tensor:
    """Sum aggregation."""
    if len(inputs) == 1:
        return inputs[0]
    return torch.stack(inputs, dim=0).sum(dim=0)


def mean_aggregation(inputs: list[torch.Tensor], **kwargs) -> torch.Tensor:
    """Mean aggregation."""
    if len(inputs) == 1:
        return inputs[0]
    return torch.stack(inputs, dim=0).mean(dim=0)


def max_aggregation(inputs: list[torch.Tensor], **kwargs) -> torch.Tensor:
    """Max aggregation."""
    if len(inputs) == 1:
        return inputs[0]
    return torch.stack(inputs, dim=0).max(dim=0)[0]


def concat_aggregation(inputs: list[torch.Tensor], **kwargs) -> torch.Tensor:
    """Concatenation aggregation."""
    if len(inputs) == 1:
        return inputs[0]
    return torch.cat(inputs, dim=-1)


# Attention-based aggregations
class AttentionAggregation(nn.Module):
    """Self-attention aggregation module."""

    def __init__(self, input_size: int, temperature: float = 1.0, dropout_p: float = 0.0):
        super().__init__()
        self.query = nn.Linear(input_size, input_size)
        self.key = nn.Linear(input_size, input_size)
        self.value = nn.Linear(input_size, input_size)
        self.temperature = temperature
        self.dropout = nn.Dropout(dropout_p)

    def forward(self, inputs: list[torch.Tensor]) -> torch.Tensor:
        if len(inputs) == 1:
            return inputs[0]

        # Stack inputs [num_inputs, batch, features]
        x = torch.stack(inputs, dim=0)

        # Compute Q, K, V
        Q = self.query(x)
        K = self.key(x)
        V = self.value(x)

        # Compute attention scores
        scores = torch.matmul(Q.transpose(0, 1), K) / (self.temperature * math.sqrt(Q.size(-1)))
        weights = F.softmax(scores, dim=-1)
        weights = self.dropout(weights)

        # Apply attention
        output = torch.matmul(weights, V.transpose(0, 1))

        # Average over attention heads (simplified)
        return output.mean(dim=1)


def attention_aggregation(inputs: list[torch.Tensor], **kwargs) -> torch.Tensor:
    """Functional attention aggregation (simplified)."""
    if len(inputs) == 1:
        return inputs[0]

    # Stack and compute simple attention
    x = torch.stack(inputs, dim=0)  # [num_inputs, batch, features]

    # Compute attention weights (simplified - just based on magnitude)
    scores = x.norm(dim=-1)  # [num_inputs, batch]
    weights = F.softmax(scores.transpose(0, 1), dim=-1)  # [batch, num_inputs]

    # Apply weights
    x_transposed = x.transpose(0, 1)  # [batch, num_inputs, features]
    output = torch.bmm(weights.unsqueeze(1), x_transposed).squeeze(1)

    return output


class MultiHeadAttentionAggregation(nn.Module):
    """Multi-head attention aggregation module."""

    def __init__(self, input_size: int, num_heads: int = 8, dropout_p: float = 0.0):
        super().__init__()
        self.num_heads = num_heads
        self.head_dim = input_size // num_heads

        self.query = nn.Linear(input_size, input_size)
        self.key = nn.Linear(input_size, input_size)
        self.value = nn.Linear(input_size, input_size)
        self.output = nn.Linear(input_size, input_size)

        self.dropout = nn.Dropout(dropout_p)

    def forward(self, inputs: list[torch.Tensor]) -> torch.Tensor:
        if len(inputs) == 1:
            return inputs[0]

        batch_size = inputs[0].size(0)

        # Handle Q, K, V from inputs
        if len(inputs) >= 3:
            Q = self.query(inputs[0])
            K = self.key(inputs[1])
            V = self.value(inputs[2])
        else:
            # Self-attention
            x = torch.stack(inputs, dim=1)  # [batch, num_inputs, features]
            Q = self.query(x)
            K = self.key(x)
            V = self.value(x)

        # Reshape for multi-head
        Q = Q.view(batch_size, -1, self.num_heads, self.head_dim).transpose(1, 2)
        K = K.view(batch_size, -1, self.num_heads, self.head_dim).transpose(1, 2)
        V = V.view(batch_size, -1, self.num_heads, self.head_dim).transpose(1, 2)

        # Attention
        scores = torch.matmul(Q, K.transpose(-2, -1)) / math.sqrt(self.head_dim)
        weights = F.softmax(scores, dim=-1)
        weights = self.dropout(weights)

        context = torch.matmul(weights, V)
        context = (
            context.transpose(1, 2)
            .contiguous()
            .view(batch_size, -1, self.num_heads * self.head_dim)
        )

        output = self.output(context)
        return output.mean(dim=1)  # Average over sequence dimension


def multi_head_attention_aggregation(inputs: list[torch.Tensor], **kwargs) -> torch.Tensor:
    """Functional multi-head attention (simplified)."""
    return attention_aggregation(inputs, **kwargs)  # Fallback to simple attention


def attention_pooling_aggregation(inputs: list[torch.Tensor], **kwargs) -> torch.Tensor:
    """Attention pooling aggregation."""
    if len(inputs) == 1:
        return inputs[0]

    # Stack inputs
    x = torch.stack(inputs, dim=1)  # [batch, num_inputs, features]

    # Learn a query vector (simplified - use mean as query)
    query = x.mean(dim=1, keepdim=True)  # [batch, 1, features]

    # Compute attention scores
    scores = torch.bmm(query, x.transpose(1, 2)).squeeze(1)  # [batch, num_inputs]
    weights = F.softmax(scores, dim=-1)

    # Apply weights
    output = torch.bmm(weights.unsqueeze(1), x).squeeze(1)

    return output


# Mixture of Experts
class MixtureOfExpertsAggregation(nn.Module):
    """Mixture of Experts aggregation module."""

    def __init__(self, input_size: int, num_experts: int = 4, top_k: int = 2):
        super().__init__()
        self.num_experts = num_experts
        self.top_k = top_k

        # Gating network
        self.gate = nn.Linear(input_size, num_experts)

    def forward(self, inputs: list[torch.Tensor]) -> torch.Tensor:
        if len(inputs) == 1:
            return inputs[0]

        # Assume inputs are expert outputs
        expert_outputs = torch.stack(
            inputs[: self.num_experts], dim=1
        )  # [batch, num_experts, features]

        # Get input for gating (could be separate or first input)
        if len(inputs) > self.num_experts:
            gate_input = inputs[self.num_experts]
        else:
            gate_input = inputs[0]

        # Compute gates
        gates = self.gate(gate_input)  # [batch, num_experts]

        # Top-k gating
        top_k_gates, top_k_indices = torch.topk(gates, self.top_k, dim=-1)
        top_k_gates = F.softmax(top_k_gates, dim=-1)

        # Gather top-k expert outputs
        top_k_experts = torch.gather(
            expert_outputs, 1, top_k_indices.unsqueeze(-1).expand(-1, -1, expert_outputs.size(-1))
        )

        # Weighted sum of top-k experts
        output = (top_k_experts * top_k_gates.unsqueeze(-1)).sum(dim=1)

        return output


def mixture_of_experts_aggregation(inputs: list[torch.Tensor], **kwargs) -> torch.Tensor:
    """Functional MoE aggregation (simplified)."""
    if len(inputs) == 1:
        return inputs[0]

    num_experts = kwargs.get("num_experts", len(inputs))
    top_k = kwargs.get("top_k", min(2, num_experts))

    # Stack expert outputs
    expert_outputs = torch.stack(inputs, dim=1)  # [batch, num_experts, features]

    # Simple gating based on magnitudes
    gates = expert_outputs.norm(dim=-1)  # [batch, num_experts]

    # Top-k selection
    top_k_gates, top_k_indices = torch.topk(gates, min(top_k, num_experts), dim=-1)
    top_k_gates = F.softmax(top_k_gates, dim=-1)

    # Gather and combine
    top_k_experts = torch.gather(
        expert_outputs, 1, top_k_indices.unsqueeze(-1).expand(-1, -1, expert_outputs.size(-1))
    )

    output = (top_k_experts * top_k_gates.unsqueeze(-1)).sum(dim=1)

    return output


# Weighted aggregations
def gated_sum_aggregation(inputs: list[torch.Tensor], **kwargs) -> torch.Tensor:
    """Gated sum aggregation."""
    if len(inputs) == 1:
        return inputs[0]

    if len(inputs) != 2:
        # Fallback to sum for more than 2 inputs
        return sum_aggregation(inputs, **kwargs)

    x1, x2 = inputs[0], inputs[1]

    # Learn gate from concatenated inputs (simplified)
    gate = torch.sigmoid(x1 + x2)  # Simple gate

    return gate * x1 + (1 - gate) * x2


def topk_weighted_sum_aggregation(inputs: list[torch.Tensor], **kwargs) -> torch.Tensor:
    """Top-k weighted sum aggregation."""
    if len(inputs) == 1:
        return inputs[0]

    top_k = kwargs.get("top_k", min(3, len(inputs)))
    temperature = kwargs.get("temperature", 1.0)

    # Stack inputs
    x = torch.stack(inputs, dim=1)  # [batch, num_inputs, features]

    # Compute scores (based on magnitude)
    scores = x.norm(dim=-1) / temperature  # [batch, num_inputs]

    # Get top-k
    top_k_scores, top_k_indices = torch.topk(scores, min(top_k, len(inputs)), dim=-1)
    top_k_weights = F.softmax(top_k_scores, dim=-1)

    # Gather top-k inputs
    top_k_inputs = torch.gather(x, 1, top_k_indices.unsqueeze(-1).expand(-1, -1, x.size(-1)))

    # Weighted sum
    output = (top_k_inputs * top_k_weights.unsqueeze(-1)).sum(dim=1)

    return output


# Matrix aggregations
def matrix_product_aggregation(inputs: list[torch.Tensor], **kwargs) -> torch.Tensor:
    """Matrix product aggregation."""
    if len(inputs) == 1:
        return inputs[0]

    if len(inputs) != 2:
        # Fallback to sequential products for more inputs
        result = inputs[0]
        for inp in inputs[1:]:
            # Handle dimension mismatch
            if result.dim() == 2 and inp.dim() == 2:
                if result.size(-1) == inp.size(0):
                    result = torch.matmul(result, inp)
                else:
                    # Size mismatch - use hadamard product
                    min_size = min(result.size(-1), inp.size(-1))
                    result = result[..., :min_size] * inp[..., :min_size]
        return result

    x1, x2 = inputs[0], inputs[1]

    # Handle different dimensions
    if x1.dim() == 2 and x2.dim() == 2:
        if x1.size(-1) == x2.size(-2):
            return torch.matmul(x1, x2)
        else:
            # Dimension mismatch - use element-wise product
            min_size = min(x1.size(-1), x2.size(-1))
            return x1[..., :min_size] * x2[..., :min_size]

    # Fallback to element-wise
    return x1 * x2


class BilinearAggregation(nn.Module):
    """Bilinear aggregation module."""

    def __init__(self, input_size1: int, input_size2: int, output_size: int):
        super().__init__()
        self.bilinear = nn.Bilinear(input_size1, input_size2, output_size)

    def forward(self, inputs: list[torch.Tensor]) -> torch.Tensor:
        if len(inputs) == 1:
            return inputs[0]

        if len(inputs) != 2:
            raise ValueError("Bilinear aggregation requires exactly 2 inputs")

        return self.bilinear(inputs[0], inputs[1])


class LearnableAggregation(nn.Module):
    """Learnable weighted aggregation module."""

    def __init__(
        self,
        num_inputs: int,
        input_size: int,
        output_size: int,
        learn_weights: bool = True,
        normalize_weights: bool = True,
    ):
        super().__init__()
        self.num_inputs = num_inputs
        self.normalize_weights = normalize_weights

        if learn_weights:
            self.weights = nn.Parameter(torch.ones(num_inputs) / num_inputs)
        else:
            self.register_buffer("weights", torch.ones(num_inputs) / num_inputs)

        if input_size != output_size:
            self.projection = nn.Linear(input_size, output_size)
        else:
            self.projection = None

    def forward(self, inputs: list[torch.Tensor]) -> torch.Tensor:
        if len(inputs) != self.num_inputs:
            raise ValueError(f"Expected {self.num_inputs} inputs, got {len(inputs)}")

        # Get weights
        weights = self.weights
        if self.normalize_weights:
            weights = F.softmax(weights, dim=0)

        # Stack and weight inputs
        x = torch.stack(inputs, dim=0)  # [num_inputs, batch, features]
        weighted = x * weights.view(-1, 1, 1)
        output = weighted.sum(dim=0)

        # Project if needed
        if self.projection:
            output = self.projection(output)

        return output

    def get_weights(self) -> torch.Tensor:
        """Get current aggregation weights."""
        if self.normalize_weights:
            return F.softmax(self.weights, dim=0)
        return self.weights
