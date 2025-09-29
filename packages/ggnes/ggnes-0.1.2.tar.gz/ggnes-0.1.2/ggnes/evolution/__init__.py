"""Evolutionary engine for GGNES.

This package exposes core genotype types and convenient evolution helpers.
Some higher-level modules (island models, adaptive strategies, metrics,
checkpointing) are provided as light-weight implementations suitable for tests
and examples.
"""

from .composite_genotype import (
    CompositeGenotype,
    G1Grammar,
    G2Policy,
    G3Hierarchy,
)
from .genotype import Genotype

# Export NSGA-II evolve helper if available
try:
    from .multi_objective import nsga2_evolve  # type: ignore[attr-defined]
except Exception:  # pragma: no cover
    nsga2_evolve = None  # type: ignore[assignment]

# Re-export convenience wrappers for simple evolve/population/hierarchical evolve
try:
    # Import from top-level wrappers to avoid circular core deps
    from ..api_wrappers import (
        Population as _WrapperPopulation,
    )
    from ..api_wrappers import (
        evolve as _wrapper_evolve,
    )
    from ..api_wrappers import (
        hierarchical_evolve as _wrapper_hierarchical_evolve,
    )

    def evolve(*args, **kwargs):
        """Simple evolution convenience (wrapper-backed)."""
        return _wrapper_evolve(*args, **kwargs)

    Population = _WrapperPopulation  # type: ignore[assignment]
    hierarchical_evolve = _wrapper_hierarchical_evolve  # type: ignore[assignment]
except Exception:  # pragma: no cover
    # Provide graceful fallbacks if wrappers are unavailable
    def evolve(*args, **kwargs):  # type: ignore[override]
        raise ImportError("evolve convenience is unavailable; wrappers not found")

    class Population:  # type: ignore[override]
        def __init__(self, *_, **__):
            raise ImportError("Population convenience is unavailable; wrappers not found")

    def hierarchical_evolve(*args, **kwargs):  # type: ignore[override]
        raise ImportError("hierarchical_evolve convenience is unavailable; wrappers not found")


__all__ = [
    "Genotype",
    "G1Grammar",
    "G2Policy",
    "G3Hierarchy",
    "CompositeGenotype",
    "evolve",
    "Population",
    "hierarchical_evolve",
    "nsga2_evolve",
]
