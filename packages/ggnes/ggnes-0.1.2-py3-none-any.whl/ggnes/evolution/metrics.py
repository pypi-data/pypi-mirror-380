"""
Evolution metrics utilities:
- ConvergenceDetector: detect convergence based on fitness history window
- calculate_diversity: estimate diversity of a population
"""

from __future__ import annotations

import hashlib
from typing import Any


class ConvergenceDetector:
    """
    Detect convergence when variation within a sliding window drops below a threshold.

    Minimal contract for tests:
    - __init__(window_size, threshold)
    - check_convergence(fitness_history) -> bool
      Returns True when the standard deviation (or range proxy) within the last 'window_size'
      items is below 'threshold'.
    """

    def __init__(self, window_size: int = 10, threshold: float = 0.01) -> None:
        self.window_size = max(2, int(window_size))
        self.threshold = float(threshold)

    def check_convergence(self, fitness_history: list[float]) -> bool:
        if not fitness_history:
            return False
        if len(fitness_history) < self.window_size:
            # Not enough samples to decide
            return False
        window = fitness_history[-self.window_size :]
        # Use range proxy (max-min) as robust variation estimator; relate to threshold
        rng = max(window) - min(window)
        return rng <= self.threshold


def _genotype_signature(g: Any) -> str:
    """
    Produce a simple hashable signature for a genotype based on its rules.

    Semantics:
    - If a wrapper clone carries _clone_signature, use it (treat clones as identical).
    - Else if rules exist, hash the sequence of rule_ids.
    - Else, fall back to a stable repr that differentiates distinct instances.
    """
    # Wrapper clone path
    sig = getattr(g, "_clone_signature", None)
    if sig is not None:
        return str(sig)

    try:
        rules = getattr(g, "rules", [])
        if rules:
            ids = []
            for r in rules:
                rid = getattr(r, "rule_id", None)
                ids.append(str(rid))
            raw = "|".join(ids)
            return hashlib.sha256(raw.encode()).hexdigest()[:16]
        else:
            # No rules: use object id to differentiate distinct new genotypes
            raw = f"empty::{id(g)}"
            return hashlib.sha256(raw.encode()).hexdigest()[:16]
    except Exception:
        raw = repr(g)
        return hashlib.sha256(raw.encode()).hexdigest()[:16]


def calculate_diversity(population: list[Any]) -> float:
    """
    Calculate a diversity score in [0,1]:
    - Count unique signatures of genotypes (based on rule_id sequences).
    - Diversity = unique_count / population_size

    Minimal contract for tests:
    - Higher diversity score for populations with more differences
    - Works even if some genotypes share identical rule sets
    """
    if not population:
        return 0.0
    sigs = {_genotype_signature(g) for g in population}
    return len(sigs) / float(len(population))
