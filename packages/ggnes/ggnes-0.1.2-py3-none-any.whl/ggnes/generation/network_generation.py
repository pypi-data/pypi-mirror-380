"""
Enhanced network generation with rule application support.
"""

from ggnes.core import Graph
from ggnes.rules.rule_application import apply_grammar as _apply_grammar


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
    return _apply_grammar(axiom, grammar, max_iterations, strategy)
