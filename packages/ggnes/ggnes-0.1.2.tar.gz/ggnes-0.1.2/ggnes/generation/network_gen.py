"""Network generation per project_guide.md §7.3.

Implements:
- RuleCooldown: temporary cooldowns to avoid immediate reselection
- GraphHistory: fingerprints, action history, and metrics tracking
- generate_network: applies rules iteratively with oscillation detection,
  selection strategy, cooldowns, and optional repair on invalid final graph.
"""

from __future__ import annotations

import hashlib
import json
import time
from dataclasses import dataclass, field
from typing import Any

from ggnes.core.graph import Graph
from ggnes.core.node import NodeType
from ggnes.evolution.selection import select_match
from ggnes.generation.matching import find_subgraph_matches
from ggnes.generation.oscillation import detect_oscillation
from ggnes.generation.read_only_view import GraphView
from ggnes.generation.rule_engine import RuleEngine
from ggnes.repair.repair import repair as repair_fn
from ggnes.utils.rng_manager import RNGManager


class RuleCooldown:
    """Manages temporary rule cooldowns to prevent oscillation."""

    def __init__(self, cooldown_iterations: int = 5) -> None:
        self.cooldown_iterations = max(0, int(cooldown_iterations))
        self._cooldowns: dict[Any, int] = {}

    def add_cooldown(self, rule_id: Any) -> None:
        if self.cooldown_iterations > 0 and rule_id is not None:
            self._cooldowns[rule_id] = self.cooldown_iterations

    def update(self) -> None:
        to_delete: list[Any] = []
        for rid, val in self._cooldowns.items():
            nv = max(0, val - 1)
            if nv == 0:
                to_delete.append(rid)
            else:
                self._cooldowns[rid] = nv
        for rid in to_delete:
            del self._cooldowns[rid]

    def is_cooled_down(self, rule_id: Any) -> bool:
        return rule_id not in self._cooldowns

    def clear_cooldown(self, rule_id: Any) -> None:
        if rule_id in self._cooldowns:
            del self._cooldowns[rule_id]


@dataclass
class GraphHistory:
    """Tracks graph evolution during generation."""

    fingerprints: list[str] = field(default_factory=list)
    action_history: list[dict[str, Any]] = field(default_factory=list)
    metrics: list[dict[str, Any]] = field(default_factory=list)

    def add_fingerprint(self, fingerprint: str) -> None:
        self.fingerprints.append(fingerprint)

    def add_action(
        self, rule_type: str, rule_id: Any, affected_nodes: set[int] | None = None
    ) -> None:
        self.action_history.append(
            {
                "rule_info": (rule_type, rule_id),
                "affected_nodes": affected_nodes or set(),
            }
        )

    def add_metrics(self, metrics: dict[str, Any]) -> None:
        self.metrics.append(dict(metrics))


def generate_network(
    genotype: Any,
    axiom_graph: Graph,
    config: dict,
    rng_manager: RNGManager,
    id_manager: Any | None = None,
) -> tuple[Graph, dict]:
    """Generate a phenotype network from a genotype.

    Args:
        genotype: Object with a `rules` list. Each rule should have attributes:
                  rule_id, lhs (dict pattern), rhs, embedding, metadata, condition (optional).
        axiom_graph: Starting graph (will be deep-copied).
        config: Configuration dict (see project_guide.md §12.1 keys for Generation/Repair/Graph).
        rng_manager: RNGManager instance for determinism.
        id_manager: Optional ID manager for global ID tracking.

    Returns:
        (graph, generation_metrics)
    """
    import copy
    import logging

    graph = copy.deepcopy(axiom_graph)
    # If the provided axiom_graph is a user-friendly wrapper (exports get_internal_graph),
    # operate on the internal core Graph to ensure matching/transaction code sees integer node ids.
    try:
        if hasattr(graph, "get_internal_graph") and callable(getattr(graph, "get_internal_graph")):
            graph = copy.deepcopy(graph.get_internal_graph())
    except Exception:
        # Fall back to the copied graph if extraction fails
        pass
    graph.reset_id_counter()

    iteration_count = 0
    graph_history = GraphHistory()
    oscillation_skips_this_iter = 0
    total_oscillation_skips = 0
    rule_cooldown = RuleCooldown(int(config.get("cooldown_iterations", 5)))

    # Graph context baseline (include node_type_counts per spec)
    def _compute_node_type_counts(g: Graph) -> dict[NodeType, int]:
        return {
            NodeType.INPUT: len(g.input_node_ids),
            NodeType.HIDDEN: sum(1 for n in g.nodes.values() if n.node_type == NodeType.HIDDEN),
            NodeType.OUTPUT: len(g.output_node_ids),
        }

    graph_context: dict[str, Any] = {
        "num_nodes": len(graph.nodes),
        "num_edges": sum(len(n.edges_out) for n in graph.nodes.values()),
        "iteration": 0,
        "node_type_counts": _compute_node_type_counts(graph),
    }
    # Add configured custom metrics initialized to 0
    for key in config.get("graph_context_keys", []) or []:
        graph_context[key] = 0

    max_iterations = int(config.get("max_iterations", 50))
    selection_strategy = str(
        config.get("selection_strategy", "PRIORITY_THEN_PROBABILITY_THEN_ORDER")
    )
    parallel_enabled = bool(config.get("parallel_execution", False))
    max_workers = int(config.get("max_parallel_workers", 4))
    batch_policy = str(config.get("parallel_batch_policy", "FIXED_SIZE"))
    fixed_size = int(config.get("parallel_fixed_size", 1))
    conflict_strategy = str(config.get("parallel_conflict_strategy", "SKIP"))
    time_budget_ms = config.get("parallel_time_budget_ms")
    memory_budget_mb = config.get("parallel_memory_budget_mb")
    max_requeues = int(config.get("parallel_max_requeues", 1))

    # Validate parallel configuration early to fail fast with context
    if max_workers < 1:
        raise ValueError("Invalid config: max_parallel_workers must be >= 1")
    _allowed_policies = {"MAX_INDEPENDENT_SET", "FIXED_SIZE", "PRIORITY_CAP"}
    if batch_policy not in _allowed_policies:
        raise ValueError(
            f"Invalid config: parallel_batch_policy='{batch_policy}' not in {sorted(_allowed_policies)}"
        )
    if batch_policy == "FIXED_SIZE" and fixed_size < 1:
        raise ValueError(
            "Invalid config: parallel_fixed_size must be >= 1 when parallel_batch_policy='FIXED_SIZE'"
        )
    if conflict_strategy not in {"SKIP", "REQUEUE"}:
        raise ValueError(
            f"Invalid config: parallel_conflict_strategy='{conflict_strategy}' not in ['SKIP','REQUEUE']"
        )

    # Placeholder to capture per-iteration parallel metrics deterministically
    _last_parallel_metrics: dict | None = None

    def _binding_signature(bindings: dict[str, Any]) -> str:
        # Canonical JSON over sorted (label, node_id) where value is int
        pairs: list[tuple[str, int]] = []
        for label, value in bindings.items():
            if isinstance(value, int):
                pairs.append((str(label), int(value)))
        pairs.sort(key=lambda p: (p[0], p[1]))
        payload = {"bindings": pairs}
        return json.dumps(payload, sort_keys=True, separators=(",", ":"))

    def _matches_overlap(m1: dict[str, Any], m2: dict[str, Any]) -> bool:
        # Node overlap
        s1_nodes = {v for v in m1.values() if isinstance(v, int)}
        s2_nodes = {v for v in m2.values() if isinstance(v, int)}
        if s1_nodes & s2_nodes:
            return True
        # Edge-instance overlap via edge_id attributes when present
        s1_edges = {getattr(v, "edge_id", None) for v in m1.values() if hasattr(v, "edge_id")}
        s2_edges = {getattr(v, "edge_id", None) for v in m2.values() if hasattr(v, "edge_id")}
        s1_edges.discard(None)
        s2_edges.discard(None)
        if s1_edges & s2_edges:
            return True
        return False

    def _build_conflict_graph(matches: list[tuple[Any, dict]]) -> list[tuple[Any, dict]]:
        # Already have list - we will sort deterministically by priority, rule_id, binding sig
        def key_fn(item: tuple[Any, dict]) -> tuple:
            rule, bindings = item
            prio = getattr(rule, "metadata", {}).get("priority", 0)
            rid = str(getattr(rule, "rule_id", ""))
            bsig = _binding_signature(bindings)
            # Higher priority first -> negative for ascending sort
            return (-int(prio), rid, bsig)

        return sorted(matches, key=key_fn)

    def _select_mis(matches_sorted: list[tuple[Any, dict]]) -> list[tuple[Any, dict]]:
        independent: list[tuple[Any, dict]] = []
        used_nodes: set[int] = set()
        for rule, bindings in matches_sorted:
            nodes = {v for v in bindings.values() if isinstance(v, int)}
            if nodes.isdisjoint(used_nodes):
                independent.append((rule, bindings))
                used_nodes.update(nodes)
        return independent

    while iteration_count < max_iterations:
        # Update cooldowns
        rule_cooldown.update()

        # Gather matches across rules
        potential_matches: list[tuple[Any, dict]] = []
        for rule in getattr(genotype, "rules", []) or []:
            if not rule_cooldown.is_cooled_down(getattr(rule, "rule_id", None)):
                continue

            lhs = getattr(rule, "lhs", None) or {"nodes": [], "edges": []}
            # Support both dict LHS and LHSPattern objects from rules.rule
            if not isinstance(lhs, dict) and hasattr(lhs, "nodes") and hasattr(lhs, "edges"):
                lhs = {
                    "nodes": list(getattr(lhs, "nodes", []) or []),
                    "edges": list(getattr(lhs, "edges", []) or []),
                }
            matches_iter = find_subgraph_matches(
                graph, lhs, int(config.get("max_match_time_ms", 1000))
            )
            # Filter by condition if present
            for bindings in matches_iter:
                cond = getattr(rule, "condition", None)
                if cond is not None and not cond(GraphView(graph), dict(bindings), graph_context):
                    continue
                potential_matches.append((rule, bindings))

        # Quiescence
        if not potential_matches:
            logging.info("Quiescence: no rules match")
            break

        if not parallel_enabled:
            # Selection (serial)
            selected = select_match(potential_matches, selection_strategy, rng_manager, config)
            if not selected:
                break
            selected_rule, selected_bindings = selected

            # Oscillation detection
            detected, reason = detect_oscillation(
                graph_history, graph, selected_rule, selected_bindings, config
            )
            if detected:
                action = str(config.get("oscillation_action", "TERMINATE"))
                if action == "TERMINATE":
                    logging.info(f"Oscillation detected: {reason}. Terminating.")
                    break
                if action == "SKIP_AND_RESELECT":
                    rule_cooldown.add_cooldown(getattr(selected_rule, "rule_id", None))
                    oscillation_skips_this_iter += 1
                    total_oscillation_skips += 1
                    if oscillation_skips_this_iter > int(
                        config.get("max_consecutive_oscillation_skips", 10)
                    ):
                        logging.info("Max consecutive oscillation skips reached. Terminating.")
                        break
                    if total_oscillation_skips > int(config.get("max_total_oscillation_skips", 50)):
                        logging.info("Max total oscillation skips reached. Terminating.")
                        break
                    continue
                if action == "IGNORE":
                    logging.warning(f"Oscillation detected but ignored: {reason}")

            # Apply selected rule
            engine = RuleEngine(graph=graph, rng_manager=rng_manager, id_manager=id_manager)
            success = engine.apply_rule(selected_rule, selected_bindings)
            if not success:
                import logging as _logging

                _logging.error(
                    f"Rule application failed for rule {getattr(selected_rule, 'rule_id', None)}"
                )
                break

            # Track history and metrics after successful application
            graph_history.add_fingerprint(graph.compute_fingerprint())
            rule_type = getattr(selected_rule, "metadata", {}).get("rule_type", "unknown")
            rule_id = getattr(selected_rule, "rule_id", None)
            graph_history.add_action(rule_type, rule_id, set())

            graph_context["num_nodes"] = len(graph.nodes)
            graph_context["num_edges"] = sum(len(n.edges_out) for n in graph.nodes.values())
            graph_context["iteration"] = iteration_count + 1
            graph_context["node_type_counts"] = _compute_node_type_counts(graph)
            graph_history.add_metrics(
                {
                    "num_nodes": graph_context["num_nodes"],
                    "num_edges": graph_context["num_edges"],
                    "iteration": graph_context["iteration"],
                    "rule_applied": 1,
                }
            )

            # Reset per-iteration skip counter on success
            oscillation_skips_this_iter = 0
            # Clear cooldown for successfully applied rule
            rule_cooldown.clear_cooldown(rule_id)

            iteration_count += 1
        else:
            # Parallel MIS batching path
            t0 = time.monotonic()
            # Anchor to serial selection for parity when batch size allows
            selected_anchor = select_match(
                potential_matches, selection_strategy, rng_manager, config
            )
            matches_sorted = _build_conflict_graph(potential_matches)
            t1 = time.monotonic()
            mis: list[tuple[Any, dict]] = []
            if selected_anchor:
                # Ensure anchor is included first
                mis.append(selected_anchor)
                # Remove overlapping matches with anchor
                anchor_nodes = {v for v in selected_anchor[1].values() if isinstance(v, int)}
                remaining = [(r, b) for (r, b) in matches_sorted if (r, b) != selected_anchor]
                filtered = []
                for r, b in remaining:
                    nodes = {v for v in b.values() if isinstance(v, int)}
                    if nodes.isdisjoint(anchor_nodes):
                        filtered.append((r, b))
                # Fill MIS greedily from filtered
                mis.extend(_select_mis(filtered))
            else:
                mis = _select_mis(matches_sorted)
            # Apply batch policy
            if batch_policy == "FIXED_SIZE":
                mis = mis[: max(0, fixed_size)]
            # PRIORITY_CAP (optional): cap by priority threshold if provided
            if batch_policy == "PRIORITY_CAP":
                cap = getattr(genotype, "priority_cap", None)
                if cap is not None:
                    mis = [
                        item
                        for item in mis
                        if getattr(item[0], "metadata", {}).get("priority", 0) >= cap
                    ]
            t2 = time.monotonic()

            # Deterministic commit order
            def commit_key(item: tuple[Any, dict]) -> tuple[str, str]:
                rule, bindings = item
                rid = str(getattr(rule, "rule_id", ""))
                bsig = _binding_signature(bindings)
                return (rid, bsig)

            mis_sorted_for_commit = sorted(mis, key=commit_key)

            wl_before = graph.compute_fingerprint()

            # Budgets
            budget_events = 0
            if isinstance(time_budget_ms, int) and time_budget_ms is not None:
                # Heuristic: if MIS is large and time budget is tiny, reduce batch
                elapsed_ms = int((time.monotonic() - t0) * 1000)
                # Always register an event when a strict non-positive budget is given
                if time_budget_ms <= 0:
                    budget_events += 1
                    if len(mis_sorted_for_commit) > 1:
                        mis_sorted_for_commit = mis_sorted_for_commit[:1]
                elif elapsed_ms > time_budget_ms and len(mis_sorted_for_commit) > 1:
                    mis_sorted_for_commit = mis_sorted_for_commit[:1]
                    budget_events += 1

            # Apply sequentially in canonical order (deterministic and safe)
            conflicts = 0
            requeues = 0
            edge_instance_conflicts = 0
            applied = 0
            matches_found = len(potential_matches)
            t_apply_start = time.monotonic()
            engine = RuleEngine(graph=graph, rng_manager=rng_manager, id_manager=id_manager)
            commit_seq: list[tuple[str, str]] = []
            for rule, bindings in mis_sorted_for_commit:
                ok = engine.apply_rule(rule, bindings)
                if ok:
                    applied += 1
                    rule_cooldown.clear_cooldown(getattr(rule, "rule_id", None))
                    commit_seq.append(commit_key((rule, bindings)))
                else:
                    # Conflict handling strategies placeholder
                    if conflict_strategy == "REQUEUE" and requeues < max_requeues:
                        requeues += 1
                    else:
                        conflicts += 1
            t_apply_end = time.monotonic()

            wl_after = graph.compute_fingerprint()
            det_payload = {
                "rule_ids": [rid for rid, _ in commit_seq],
                "binding_signatures": [bs for _, bs in commit_seq],
                "commit_order": commit_seq,
                "wl_before": wl_before,
                "wl_after": wl_after,
            }
            det_json = json.dumps(det_payload, sort_keys=True, separators=(",", ":"))
            det_checksum = hashlib.sha256(det_json.encode("utf-8")).hexdigest()

            # Metrics
            parallel_metrics = {
                "enabled": True,
                "mis_size": len(mis),
                "mis_binding_signatures": [commit_key(item)[1] for item in mis],
                "commit_order": commit_seq,
                "conflicts": conflicts,
                "requeues": requeues,
                "edge_instance_conflicts": edge_instance_conflicts,
                "budget_events": budget_events,
                "memory_budget_mb": memory_budget_mb,
                "matches_found": matches_found,
                "applied": applied,
                "phase_timings_ms": {
                    "matching": int((t1 - t0) * 1000),
                    "mis": int((t2 - t1) * 1000),
                    "apply": int((t_apply_end - t_apply_start) * 1000),
                    "commit": 0,
                    "validate": 0,
                },
                "determinism_checksum": det_checksum,
            }

            # Track history
            graph_history.add_fingerprint(wl_after)
            if mis_sorted_for_commit:
                rany = mis_sorted_for_commit[0][0]
                rule_type_any = getattr(rany, "metadata", {}).get("rule_type", "unknown")
                rule_id_any = getattr(rany, "rule_id", None)
                graph_history.add_action(rule_type_any, rule_id_any, set())

            graph_context["num_nodes"] = len(graph.nodes)
            graph_context["num_edges"] = sum(len(n.edges_out) for n in graph.nodes.values())
            graph_context["iteration"] = iteration_count + 1
            graph_context["node_type_counts"] = _compute_node_type_counts(graph)
            graph_history.add_metrics(
                {
                    "num_nodes": graph_context["num_nodes"],
                    "num_edges": graph_context["num_edges"],
                    "iteration": graph_context["iteration"],
                    "rule_applied": int(applied > 0),
                }
            )

            # Attach parallel metrics to generation_metrics later
            _last_parallel_metrics = parallel_metrics  # capture in closure

            # Reset counters and advance
            oscillation_skips_this_iter = 0
            iteration_count += 1

    # Final validation and optional repair
    errors: list[Any] = []
    t_validate_start = time.monotonic()
    is_valid = graph.validate(collect_errors=errors)
    t_validate_end = time.monotonic()
    repair_metrics: dict[str, Any] | None = None
    if not is_valid:
        # Construct repair config from main config
        repair_config = {
            "strategy": config.get("repair_strategy", "MINIMAL_CHANGE"),
            "allowed_repairs": config.get(
                "allowed_repairs", ["fix_weights", "add_missing_attributes"]
            ),
            "max_repair_iterations": config.get("max_repair_iterations", 5),
        }
        repair_successful, repair_metrics = repair_fn(graph, repair_config, rng_manager)
        if not repair_successful:
            import logging as _logging

            _logging.warning("Repair failed, assigning minimal fitness (handled by caller)")

    generation_metrics = {
        "iterations": iteration_count,
        "oscillation_skips": total_oscillation_skips,
        "final_nodes": len(graph.nodes),
        "final_edges": sum(len(n.edges_out) for n in graph.nodes.values()),
        "repair_metrics": repair_metrics,
    }

    # Attach parallel metrics if enabled
    if parallel_enabled:
        try:
            generation_metrics["parallel"] = _last_parallel_metrics
            # Fill validate timing if available
            if isinstance(generation_metrics["parallel"].get("phase_timings_ms"), dict):
                generation_metrics["parallel"]["phase_timings_ms"]["validate"] = int(
                    (t_validate_end - t_validate_start) * 1000
                )
        except Exception:
            generation_metrics["parallel"] = {
                "enabled": True,
                "mis_size": 0,
                "mis_binding_signatures": [],
                "commit_order": [],
                "conflicts": 0,
                "requeues": 0,
                "edge_instance_conflicts": 0,
                "budget_events": 0,
                "matches_found": 0,
                "applied": 0,
                "phase_timings_ms": {
                    "matching": 0,
                    "mis": 0,
                    "apply": 0,
                    "commit": 0,
                    "validate": int((t_validate_end - t_validate_start) * 1000),
                },
                "determinism_checksum": hashlib.sha256(b"").hexdigest(),
            }

    return graph, generation_metrics


__all__ = [
    "RuleCooldown",
    "GraphHistory",
    "generate_network",
]
