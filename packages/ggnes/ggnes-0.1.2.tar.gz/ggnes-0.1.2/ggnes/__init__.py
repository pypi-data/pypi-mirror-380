"""
GGNES - Graph Grammar Neuroevolution System

A system for evolving neural network architectures by evolving the generative
graph rewriting rules (grammar) that construct them.
"""

__version__ = "0.1.0"

# First import original implementations
from .core import *  # noqa: F401,F403
from .generation import *  # noqa: F401,F403
from .repair import *  # noqa: F401,F403
from .rules import *  # noqa: F401,F403
from .translation import *  # noqa: F401,F403
from .utils import *  # noqa: F401,F403

# Import user-friendly API wrappers without overriding core Graph/Node/Edge
# Keep core Graph/Node/Edge/Rule available from earlier wildcard imports.
try:
    from .api_wrappers import (
        CompositeGenotype,
        Edge,
        Genotype,  # Wrapper evolution classes
        # Override with user-friendly APIs by default at top-level
        Graph,  # Wrapper core classes
        LHSPattern,
        Node,
        Population,  # Advanced evolution
        RHSAction,
        Rule,  # Wrapper rule classes
        crossover,
        elitism_selection,
        evolve,  # Evolution functions
        hierarchical_evolve,
        mutate,
        nsga2_evolve,
        rank_selection,
        roulette_selection,
        tournament_selection,  # Selection
    )

    # EmbeddingLogic is imported from original location since wrapper not needed
    from .rules.rule import EmbeddingLogic
except ImportError:
    # Fall back to original imports if wrappers not available
    pass

# Expose configuration presets as top-level names (used in guide examples)
try:
    from .config import PRESET_MINIMAL, PRESET_RESEARCH, PRESET_STANDARD  # noqa: F401
except Exception:
    PRESET_MINIMAL = PRESET_STANDARD = PRESET_RESEARCH = None

# Export new functionality
try:
    from .generation.network_generation import apply_grammar  # noqa: F401
    from .rules.pattern_matching import PatternEdge, PatternMatcher, PatternNode  # noqa: F401
    from .rules.rule_application import RuleApplicationEngine  # noqa: F401

    # Docs alias: expose generate_network matching README examples
    generate_network = apply_grammar  # noqa: F401
    from .aggregations import get_aggregation, register_aggregation  # noqa: F401
    from .evolution.multi_objective import (  # noqa: F401
        MultiObjectiveEvolution,
        calculate_crowding_distance,
    )
    # MVP API wrappers
    from .api.mvp import (  # noqa: F401
        Search,
        SearchResult,
        SearchSpace,
        rule,
        starter_space,
        wl_fingerprint,
        DeterminismSignature,
        ReproBundle,
        LatencyObjective,
    )
except ImportError:
    pass
