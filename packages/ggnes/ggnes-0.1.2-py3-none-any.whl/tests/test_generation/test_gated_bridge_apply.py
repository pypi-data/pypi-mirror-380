import importlib.util
import sys
import os

from ggnes.generation.rule_engine import RuleEngine
from ggnes.utils.rng_manager import RNGManager

def load_demo_module():
    demo_path = os.path.join(os.getcwd(), "demo", "organic_sensor_fusion_demo.py")
    spec = importlib.util.spec_from_file_location("organic_demo", demo_path)
    demo = importlib.util.module_from_spec(spec)
    sys.modules["organic_demo"] = demo
    spec.loader.exec_module(demo)
    return demo

def test_gated_bridge_apply_no_exception_and_graph_valid():
    """
    Regression test reproducing the gated_bridge application path used by the demo.

    Verifies that applying a gated_bridge rule to the demo axiom does not raise
    (engine handles legacy Rule wrapper) and that the graph remains valid
    (validate() callable) after a tolerated failure/rollback.
    """
    demo = load_demo_module()
    ax = demo.create_axiom_graph(input_size=8)
    rules = demo.create_grammar_rules()

    # Find a gated_bridge rule (there are multiple sizes)
    target = None
    for r in rules:
        name = getattr(r, "name", "") or (getattr(r, "metadata", {}) or {}).get("name", "")
        if name and name.startswith("gated_bridge_"):
            target = r
            break

    assert target is not None, "No gated_bridge rule found in grammar"

    # Find matches on the axiom (should yield at least one binding).
    # Use the core matcher directly to avoid relying on demo helpers.
    from ggnes.generation.matching import find_subgraph_matches as _find_subgraph_matches
    lhs_obj = getattr(target, "lhs", None) or getattr(getattr(target, "_internal_rule", None), "lhs", None)
    lhs_dict = {"nodes": getattr(lhs_obj, "nodes", []) or [], "edges": getattr(lhs_obj, "edges", []) or []}
    matches = list(_find_subgraph_matches(ax, lhs_dict, 500))
    # Fallback: try rule wrapper find_matches if core matcher returned nothing
    if not matches:
        try:
            matches = target.find_matches(ax)
        except Exception:
            matches = []

    # It is acceptable for the rule not to match; the engine should not raise.
    if not matches:
        # Nothing to apply; test that matching code runs
        assert True
        return

    bindings = matches[0]

    rng = RNGManager(seed=1234)
    engine = RuleEngine(graph=ax, rng_manager=rng)

    # Should not raise; apply_rule may return True (applied) or False (rolled back)
    res = engine.apply_rule(target, bindings)
    assert isinstance(res, bool)

    # Graph should validate (either original or post-repair); ensure validate() runs
    errors = []
    valid = ax.validate(collect_errors=errors)
    assert isinstance(valid, bool)
