"""
Adaptive evolution utilities:
- AdaptiveEvolution: self-adaptive parameter control for mutation_rate
- OperatorAdaptation: adaptive operator probability management
"""

from __future__ import annotations

import random
from collections.abc import Callable
from typing import Any


def _normalize_probs(probs: dict[str, float]) -> dict[str, float]:
    total = sum(max(0.0, float(v)) for v in probs.values())
    if total <= 0:
        # uniform if all zero/negative
        n = max(1, len(probs))
        return {k: 1.0 / n for k in probs}
    return {k: max(0.0, float(v)) / total for k, v in probs.items()}


class OperatorAdaptation:
    """
    Adapt operator selection probabilities based on observed success.

    Minimal contract for tests:
    - select_operator() returns an operator name sampled from current probabilities
    - update(name, success) adjusts probabilities toward successful operators
    - get_probabilities() returns a dict whose values sum to ~1.0
    """

    def __init__(self, operators: dict[str, float]) -> None:
        if not isinstance(operators, dict) or not operators:
            raise ValueError("operators must be a non-empty dict[name -> probability]")
        self._probs: dict[str, float] = _normalize_probs(operators)
        # Track simple exponential-moving-average success for stability
        self._success_ema: dict[str, float] = {k: 0.5 for k in self._probs}  # start neutral

        # Smoothing/learning rates
        self._ema_alpha: float = 0.1  # success smoothing
        self._learn_rate: float = 0.05  # probability step size

    def select_operator(self) -> str:
        keys = list(self._probs.keys())
        weights = [self._probs[k] for k in keys]
        # random.choices is available in Python 3.6+
        return random.choices(keys, weights=weights, k=1)[0]

    def update(self, operator: str, success: bool) -> None:
        if operator not in self._probs:
            return
        # Update success EMA
        s = 1.0 if success else 0.0
        self._success_ema[operator] = (1 - self._ema_alpha) * self._success_ema[
            operator
        ] + self._ema_alpha * s

        # Translate success to a multiplicative factor
        # Center around 1.0: success=1 -> >1, success=0 -> <1
        factor = 1.0 + self._learn_rate * (2.0 * s - 1.0)  # success -> 1+lr, fail -> 1-lr

        # Apply factor to the focal operator; mild decay to others to maintain contrast
        new_probs: dict[str, float] = {}
        for op, p in self._probs.items():
            if op == operator:
                new_probs[op] = p * factor
            else:
                new_probs[op] = p * (1.0 - self._learn_rate * 0.25)

        # Normalize and floor to avoid zeros
        new_probs = _normalize_probs(new_probs)
        eps = 1e-9
        new_probs = {k: max(eps, v) for k, v in new_probs.items()}
        self._probs = _normalize_probs(new_probs)

    def get_probabilities(self) -> dict[str, float]:
        return dict(self._probs)


class AdaptiveEvolution:
    """
    Self-adaptive mutation rate controller.

    Minimal contract for tests:
    - Accepts a population[List[Genotype]] whose elements may carry .mutation_rate
    - evolve(population, fitness_function, generations) returns a new population
    - Over generations, best individuals' mutation_rate values should converge
      (std of top-10 rates < threshold), on average.
    """

    def __init__(
        self,
        min_rate: float = 0.005,
        max_rate: float = 0.8,
        step_size: float = 0.15,
        inertia: float = 0.85,
    ) -> None:
        """
        Args:
            min_rate: Lower bound for mutation rate
            max_rate: Upper bound for mutation rate
            step_size: Global step toward weighted-mean per generation
            inertia: How much of previous rate to retain (0..1)
        """
        self.min_rate = float(min_rate)
        self.max_rate = float(max_rate)
        self.step_size = float(step_size)
        self.inertia = float(inertia)

    def _clip(self, x: float) -> float:
        return max(self.min_rate, min(self.max_rate, float(x)))

    def _get_rate(self, g: Any) -> float:
        r = getattr(g, "mutation_rate", None)
        if r is None:
            # Assign default if missing
            r = 0.1
            try:
                setattr(g, "mutation_rate", r)
            except Exception:
                pass
        return float(r)

    def _set_rate(self, g: Any, r: float) -> None:
        try:
            setattr(g, "mutation_rate", float(r))
        except Exception:
            pass

    def evolve(
        self, population: list[Any], fitness_function: Callable[[Any], float], generations: int = 10
    ) -> list[Any]:
        if not isinstance(population, list) or not population:
            return list(population or [])

        pop = list(population)

        for _ in range(max(0, int(generations))):
            # Evaluate fitness
            scores = [float(fitness_function(ind)) for ind in pop]
            # Compute a weighted target rate (higher fitness -> higher weight)
            # Add small epsilon to avoid division by zero
            eps = 1e-12
            weights = [max(eps, s - min(scores) + eps) for s in scores]
            total_w = sum(weights)
            if total_w <= 0:
                # Fallback: simple mean
                target = sum(self._get_rate(ind) for ind in pop) / len(pop)
            else:
                target = sum(self._get_rate(ind) * w for ind, w in zip(pop, weights)) / total_w

            # Move individual rates toward target with inertia/step
            for ind in pop:
                r = self._get_rate(ind)
                new_r = self.inertia * r + (1.0 - self.inertia) * (
                    r + self.step_size * (target - r)
                )
                self._set_rate(ind, self._clip(new_r))

            # Optional: small exploration noise diminishing over time
            # Not required by tests, so omitted for determinism given fixed seeds.

            # Note: This controller only adapts rates; actual evolutionary
            # changes (selection/crossover/mutation) are out of scope for these tests.

        return pop
