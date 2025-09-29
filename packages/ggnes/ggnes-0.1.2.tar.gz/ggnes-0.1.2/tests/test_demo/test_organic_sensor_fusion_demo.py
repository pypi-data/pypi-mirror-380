import copy

from demo import organic_sensor_fusion_demo as demo


def test_grammar_rules_provide_advanced_aggregations():
    rules = demo.create_grammar_rules()
    assert len(rules) > 0

    attn_rules = [r for r in rules if "attention" in getattr(r, "name", "")]
    assert attn_rules, "Expected at least one attention-based rule"

    for rule in attn_rules:
        rhs = getattr(rule, "action", None)
        if not rhs:
            continue
        for spec in getattr(rhs, "add_nodes", []):
            attributes = spec.get("properties", {}).get("attributes", {})
            agg_fn = attributes.get("aggregation_function") or attributes.get("aggregation")
            if agg_fn is None:
                continue
            if agg_fn == "multi_head_attention":
                assert attributes.get("num_heads", 0) > 0
                assert attributes.get("head_dim", 0) > 0
            if agg_fn == "attention":
                assert 0.0 <= attributes.get("dropout_p", 0.0) < 1.0


def test_mutation_preserves_rule_bounds():
    base = demo.create_genotype(6)
    mutated = demo._mutate_genotype(copy.deepcopy(base))
    assert 1 <= len(mutated.rules) <= demo.Config.max_rules

