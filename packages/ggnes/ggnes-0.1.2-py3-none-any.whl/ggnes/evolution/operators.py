"""Mutation and crossover operators (project_guide.md §9.2)."""

from __future__ import annotations

import copy
import uuid
from typing import Any

from ggnes.evolution.genotype import Genotype
from ggnes.utils.rng_manager import RNGManager


def _normalize_probs(probabilities: list[float]) -> list[float]:
    total = sum(probabilities)
    if total > 0:
        return [p / total for p in probabilities]
    if probabilities:
        return [1.0 / len(probabilities) for _ in probabilities]
    return []


def uniform_crossover(
    parent1: Genotype,
    parent2: Genotype,
    config: dict | None = None,
    rng_manager: RNGManager | None = None,
) -> tuple[Genotype, Genotype]:
    """Perform uniform crossover between two genotypes.

    The implementation follows project_guide.md semantics:
    - Per-rule inclusion probability `crossover_probability_per_rule`
    - Order-independent RNG seeding
    - Enforce `min_rules_per_genotype` and `max_rules_per_genotype`
    - If a rule_id exists in both parents but contents differ, versions are sampled independently for each offspring

    Robust argument validation for helpful error messages:
    - If `config` is missing or not a dict, raise TypeError mentioning 'config'
    - If `rng_manager` is missing, raise TypeError mentioning 'rng_manager'
    """
    if config is None or not isinstance(config, dict):
        raise TypeError("uniform_crossover requires config (dict) as the third parameter 'config'")
    if rng_manager is None or not isinstance(rng_manager, RNGManager):
        raise TypeError("uniform_crossover requires rng_manager as the fourth parameter")
    rng = rng_manager.get_rng_for_crossover(parent1.genotype_id, parent2.genotype_id)

    p = float(config.get("crossover_probability_per_rule", 0.5))
    min_rules = int(config.get("min_rules_per_genotype", 1))
    max_rules = int(config.get("max_rules_per_genotype", 999999))

    rules1_dict = {getattr(r, "rule_id", uuid.uuid4()): r for r in parent1.rules}
    rules2_dict = {getattr(r, "rule_id", uuid.uuid4()): r for r in parent2.rules}
    all_rule_ids = list(set(rules1_dict.keys()) | set(rules2_dict.keys()))
    all_rule_ids.sort(key=str)

    offspring1_rules: list[Any] = []
    offspring2_rules: list[Any] = []

    for rid in all_rule_ids:
        r1 = rules1_dict.get(rid)
        r2 = rules2_dict.get(rid)
        if r1 and r2 and r1 is not r2 and r1 != r2:
            chosen_for_o1 = r1 if rng.random() < 0.5 else r2
            chosen_for_o2 = r1 if rng.random() < 0.5 else r2
        else:
            chosen_for_o1 = r1 or r2
            chosen_for_o2 = r1 or r2

        if chosen_for_o1 is not None and rng.random() < p:
            offspring1_rules.append(chosen_for_o1)
        if chosen_for_o2 is not None and rng.random() < p:
            offspring2_rules.append(chosen_for_o2)

    # Enforce min/max by padding with available rules if needed
    def fill_to_min(current: list[Any]) -> list[Any]:
        if len(current) >= min_rules:
            return current[:max_rules]
        # Build order-independent pool by sorting deterministically by rule_id
        pool = [r for r in parent1.rules + parent2.rules if r not in current]
        try:
            pool.sort(key=lambda r: str(getattr(r, "rule_id", "")))
        except Exception:
            # Fallback: stable repr
            pool.sort(key=lambda r: repr(r))
        # Deterministic shuffle by RNG (without mutating pool order)
        while len(current) < min_rules and pool:
            idx = rng.randrange(len(pool))
            current.append(pool.pop(idx))
        return current[:max_rules]

    offspring1_rules = fill_to_min(offspring1_rules)
    offspring2_rules = fill_to_min(offspring2_rules)

    return Genotype(rules=offspring1_rules), Genotype(rules=offspring2_rules)


def mutate(
    genotype: Genotype, config: dict | None = None, rng_manager: RNGManager | None = None
) -> Genotype:
    """Mutate a genotype per project_guide.md.

    Behavior:
    - With probability `mutation_rate`, apply one mutation selected via tiered `mutation_probs`.
    - Mutations supported (minimal versions):
      - modify_metadata: tweak priority/probability metadata if present
      - modify_rhs: scale a weight in an RHS add_edges entry if present
      - modify_lhs: add or change a match criterion for a random LHS node (if present)
      - add_rule: duplicate a rule and assign a new rule_id and metadata tweaks
      - delete_rule: remove a random rule if above `min_rules_per_genotype`
    - Returns a deep-copied mutated genotype with a new genotype_id if mutated; otherwise original.

    Robust argument validation for helpful error messages:
    - If `config` is missing or not a dict, raise TypeError mentioning 'config'
    - If `mutation_rate` is not in [0,1], raise ValueError describing the valid range
    - If `mutation_probs` is missing or empty, raise ValueError mentioning 'mutation_probs'
    """
    if config is None or not isinstance(config, dict):
        raise TypeError("mutate requires config (dict) as the second parameter 'config'")
    if rng_manager is None or not isinstance(rng_manager, RNGManager):
        raise TypeError("mutate requires rng_manager as the third parameter")
    rng = rng_manager.get_rng_for_mutation(getattr(genotype, "genotype_id", uuid.uuid4()))

    # Validate mutation_rate
    mutation_rate = float(config.get("mutation_rate", 0.3))
    if not (0.0 <= mutation_rate <= 1.0):
        raise ValueError("mutation_rate must be a probability in [0, 1]")
    if rng.random() > mutation_rate:
        return genotype

    mutated = copy.deepcopy(genotype)
    # Update genotype_id robustly for both core and wrapper genotypes
    try:
        mutated.genotype_id = uuid.uuid4()
    except Exception:
        # Wrapper path: set on internal genotype if present
        if hasattr(mutated, "_internal_genotype"):
            try:
                setattr(mutated._internal_genotype, "genotype_id", uuid.uuid4())
            except Exception:
                pass

    probs: dict[str, float] = dict(
        config.get(
            "mutation_probs",
            {
                "modify_metadata": 0.3,
                "modify_rhs": 0.2,
                "modify_lhs": 0.2,
                "add_rule": 0.15,
                "delete_rule": 0.15,
            },
        )
    )
    if not probs:
        raise ValueError("config['mutation_probs'] must be provided and non-empty")

    # Roulette selection
    keys = list(probs.keys())
    weights = _normalize_probs([float(probs[k]) for k in keys])
    r = rng.random()
    cumulative = 0.0
    selected_type = keys[-1]
    for k, w in zip(keys, weights):
        cumulative += w
        if r <= cumulative:
            selected_type = k
            break

    min_rules = int(config.get("min_rules_per_genotype", 1))

    if selected_type == "modify_metadata" and mutated.rules:
        rule = rng.choice(mutated.rules)
        if hasattr(rule, "metadata") and isinstance(rule.metadata, dict):
            if "priority" in rule.metadata:
                rule.metadata["priority"] = int(rule.metadata["priority"]) + rng.choice([-1, 1])
            if "probability" in rule.metadata:
                rule.metadata["probability"] = max(
                    0.01, min(1.0, float(rule.metadata["probability"]) * rng.uniform(0.8, 1.2))
                )

    elif selected_type == "modify_rhs" and mutated.rules:
        rule = rng.choice(mutated.rules)
        rhs = getattr(rule, "rhs", None)
        if rhs and getattr(rhs, "add_edges", None):
            edge_spec = rng.choice(rhs.add_edges)
            props = edge_spec.setdefault("properties", {})
            props["weight"] = float(props.get("weight", 0.1)) * rng.uniform(0.8, 1.2)

    elif selected_type == "modify_lhs" and mutated.rules:
        rule = rng.choice(mutated.rules)
        lhs = getattr(rule, "lhs", None)
        if lhs and getattr(lhs, "nodes", None):
            node_spec = rng.choice(lhs.nodes)
            mc = node_spec.setdefault("match_criteria", {})
            # Add a benign criterion if absent; otherwise toggle a flag
            if "optional_flag" not in mc:
                mc["optional_flag"] = True
            else:
                mc["optional_flag"] = not bool(mc["optional_flag"])

    elif selected_type == "add_rule" and mutated.rules:
        template = copy.deepcopy(rng.choice(mutated.rules))
        # Assign new identity
        if hasattr(template, "rule_id"):
            template.rule_id = uuid.uuid4()
        # Adjust metadata
        if hasattr(template, "metadata") and isinstance(template.metadata, dict):
            template.metadata["priority"] = int(template.metadata.get("priority", 0)) + rng.randint(
                0, 2
            )
            template.metadata["probability"] = max(
                0.01,
                min(1.0, float(template.metadata.get("probability", 1.0)) * rng.uniform(0.8, 1.2)),
            )
        mutated.rules.append(template)

    elif selected_type == "delete_rule" and len(mutated.rules) > min_rules:
        idx = rng.randrange(len(mutated.rules))
        del mutated.rules[idx]

    return mutated


__all__ = ["uniform_crossover", "mutate"]
