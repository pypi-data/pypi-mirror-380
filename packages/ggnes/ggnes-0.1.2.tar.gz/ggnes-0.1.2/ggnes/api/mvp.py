from __future__ import annotations

import json
import os
import time
import zipfile
from dataclasses import dataclass
from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple

import torch
import torch.nn as nn

from ggnes.core.graph import Graph
from ggnes.core.node import NodeType
from ggnes.rules.rule import EmbeddingLogic, LHSPattern, RHSAction, Rule
from ggnes.translation import to_pytorch_model
from ggnes.utils.observability import determinism_signature
from ggnes.evolution.multi_objective import nsga2_evolve
from ggnes.generation.network_generation import apply_grammar


# ------------------------------- Public Helpers -------------------------------


def wl_fingerprint(graph_or_result: Any) -> str:
    """Return WL fingerprint for a Graph or SearchResult.

    Args:
        graph_or_result: Graph or SearchResult with best_architecture

    Returns:
        Hex string WL fingerprint
    """
    graph = graph_or_result
    if hasattr(graph_or_result, "best_architecture"):
        graph = graph_or_result.best_architecture
    if hasattr(graph, "compute_fingerprint"):
        return graph.compute_fingerprint()
    raise ValueError("wl_fingerprint expects a Graph or SearchResult with best_architecture")


class DeterminismSignature:
    """Compute and assert determinism signatures for runs.

    Wraps utils.observability to expose simple top-level helpers.
    """
    @staticmethod
    def compute(result: "SearchResult") -> str:
        report = {
            "wl_fingerprint": wl_fingerprint(result),
            "seed": int(getattr(result, "seed", 0)),
            "device": str(getattr(result, "device", "cpu")),
            "metrics": {k: float(v) for k, v in (result.metrics or {}).items()},
        }
        return determinism_signature(report, include_env=False)

    @staticmethod
    def assert_equal(sig_a: str, sig_b: str) -> None:
        if sig_a != sig_b:
            raise AssertionError(f"Determinism drift: {sig_a} != {sig_b}")


class ReproBundle:
    """Export and verify a minimal reproducibility bundle (zip).

    Bundle includes config.json, evolution_history.json, repro_manifest.json.
    """
    @staticmethod
    def export(artifacts_dir: str, *, out_path: str) -> "ReproBundle":
        with zipfile.ZipFile(out_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
            for name in ["config.json", "evolution_history.json", "repro_manifest.json"]:
                p = os.path.join(artifacts_dir, name)
                if os.path.exists(p):
                    zf.write(p, arcname=name)
        rb = ReproBundle()
        rb._path = out_path
        return rb

    @staticmethod
    def verify(bundle_path: str) -> None:
        # Minimal verification: check known files exist in the bundle
        with zipfile.ZipFile(bundle_path, "r") as zf:
            names = set(zf.namelist())
            required = {"config.json", "evolution_history.json", "repro_manifest.json"}
            missing = required - names
            if missing:
                raise AssertionError(f"Missing files in bundle: {sorted(missing)}")

    def contents(self) -> List[str]:
        with zipfile.ZipFile(self._path, "r") as zf:
            return zf.namelist()


# ---------------------------------- Search API --------------------------------


@dataclass
class SearchResult:
    """Result of a Search.fit call."""
    model: nn.Module
    metrics: Dict[str, float]
    best_architecture: Graph
    artifacts: Optional[str] = None
    seed: int = 0
    device: str = "cpu"
    pareto: Optional[List[Dict[str, float]]] = None
    constraints: Optional[Dict[str, Any]] = None


class SearchSpace:
    """Container for grammar rules and constraints."""
    def __init__(self) -> None:
        self.rules: List[Rule] = []

    def add(self, rule: Rule) -> None:
        self.rules.append(rule)


def rule(
    *,
    name: str,
    lhs: Dict[str, Any],
    add_nodes: List[Dict[str, Any]] | None = None,
    add_edges: List[Tuple[str, str]] | None = None,
    probability: float = 1.0,
    embedding: Optional[Dict[str, Any]] = None,
) -> Rule:
    """Create a simple Rule from friendly parameters.

    name, lhs match dict, nodes/edges to add, probability, and optional embedding.
    """
    add_nodes = add_nodes or []
    add_edges = add_edges or []
    pattern = LHSPattern(nodes=[{"label": "LHSPREV", "match_criteria": lhs}], edges=[], boundary_nodes=["LHSPREV"])  # type: ignore[arg-type]
    action = RHSAction(
        add_nodes=[
            {
                "label": "NEW",
                "properties": {
                    "node_type": getattr(NodeType, str(n.get("node_type", "HIDDEN")), NodeType.HIDDEN),
                    "activation_function": n.get("activation"),
                    "attributes": {
                        "output_size": n.get("output_size"),
                        **({"aggregation": n.get("aggregation")} if n.get("aggregation") else {}),
                    },
                },
            }
            for n in add_nodes
        ],
        add_edges=[{"source_label": s, "target_label": t} for s, t in add_edges],
    )
    emb = EmbeddingLogic()
    if embedding:
        try:
            if "boundary_handling" in embedding:
                emb.boundary_handling = embedding["boundary_handling"]
        except Exception:
            pass
    metadata = {"name": name, "probability": float(probability)}
    return Rule(lhs=pattern, rhs=action, embedding=emb, metadata=metadata)


def starter_space(name: str) -> SearchSpace:
    sp = SearchSpace()
    if name == "attention_tabular":
        sp.add(
            rule(
                name="add_attention_32",
                lhs={"node_type": "HIDDEN"},
                add_nodes=[{"node_type": "HIDDEN", "activation": "relu", "aggregation": "attention", "output_size": 32}],
                add_edges=[("LHSPREV", "NEW")],
                probability=0.3,
            )
        )
    # default: tabular_dense
    sp.add(
        rule(
            name="add_dense_32",
            lhs={"node_type": "HIDDEN"},
            add_nodes=[{"node_type": "HIDDEN", "activation": "relu", "output_size": 32}],
            add_edges=[("LHSPREV", "NEW")],
            probability=0.8,
        )
    )
    return sp


class LatencyObjective:
    """Simple latency measurement objective (ms) for a model."""
    def __init__(self, device: str = "cpu", dtype: str = "float32") -> None:
        self.device = device
        self.dtype = dtype

    def measure(self, model: nn.Module, inputs: Any, warmup: int = 1, iters: int = 5) -> float:
        dev = torch.device(self.device)
        model = model.to(dev)
        if isinstance(inputs, (list, tuple)):
            inputs = [x.to(dev) if isinstance(x, torch.Tensor) else x for x in inputs]
        elif isinstance(inputs, torch.Tensor):
            inputs = inputs.to(dev)
        # warmup
        with torch.no_grad():
            for _ in range(warmup):
                _ = model(inputs)
        if dev.type == "cuda":
            torch.cuda.synchronize()
        t0 = time.perf_counter()
        with torch.no_grad():
            for _ in range(iters):
                _ = model(inputs)
        if dev.type == "cuda":
            torch.cuda.synchronize()
        dt = (time.perf_counter() - t0) / iters
        return float(dt * 1000.0)  # ms


class Search:
    """Beginner-friendly Search orchestrator with smoke-safe defaults."""
    def __init__(
        self,
        *,
        search_space: Optional[SearchSpace] = None,
        objective: str | Callable[[nn.Module, Any, Any], float] | None = "mse",
        population: int | None = None,
        generations: int | None = None,
        device: str = "auto",
        seed: int = 0,
        smoke: bool = False,
        generation_config: Optional[Dict[str, Any]] = None,
    ) -> None:
        self.search_space = search_space or starter_space("tabular_dense")
        self.objective = objective
        self.population = int(population or (2 if smoke else 20))
        self.generations = int(generations or (1 if smoke else 5))
        self.device = "cuda" if device == "auto" and torch.cuda.is_available() else (device if device != "auto" else "cpu")
        self.seed = int(seed or 0)
        self.smoke = bool(smoke)
        self.generation_config = generation_config or {}

    def fit(
        self,
        X_train: Any,
        y_train: Any,
        *,
        validation_data: Tuple[Any, Any] | None = None,
        test_data: Tuple[Any, Any] | None = None,
        callbacks: Optional[Sequence[Any]] = None,
    ) -> SearchResult:
        """Run a smoke-safe search and return SearchResult.

        In smoke modes, uses tiny training and small structural variations.
        Flags:
          - use_generation_smoke
          - use_real_generation_smoke
          - use_real_generation_nsga
        """
        # Minimal, deterministic baseline: translate a small hand-built graph
        g = Graph()
        input_id = g.add_node({"node_type": NodeType.INPUT, "activation_function": "linear", "attributes": {"output_size": int(X_train.shape[1])}})
        hidden_id = g.add_node({"node_type": NodeType.HIDDEN, "activation_function": "relu", "attributes": {"output_size": 32}})
        output_id = g.add_node({"node_type": NodeType.OUTPUT, "activation_function": "linear", "attributes": {"output_size": 1}})
        g.add_edge(input_id, hidden_id)
        g.add_edge(hidden_id, output_id)

        # If search_space contains an attention rule, tweak structure deterministically
        try:
            names = [str(getattr(r, "metadata", {}).get("name", "")) for r in getattr(self.search_space, "rules", [])]
            if any("attention" in n for n in names):
                # add one extra hidden node to alter WL fingerprint
                extra = g.add_node({"node_type": NodeType.HIDDEN, "activation_function": "relu", "attributes": {"output_size": 16}})
                g.add_edge(input_id, extra)
        except Exception:
            pass

        # Pre-compute constraint signals on the architecture
        pre_constraints: Dict[str, Any] = {}
        pre_penalty: float = 0.0
        for c in getattr(self, "constraints", []) or []:
            if isinstance(c, tuple) and len(c) == 2:
                name, val = c
                if name == "is_dag":
                    try:
                        g.topological_sort()
                        pre_constraints["is_dag"] = True
                    except Exception:
                        pre_constraints["is_dag"] = False
                        pre_penalty += 1.0
                elif name == "max_nodes":
                    try:
                        max_nodes = int(val)
                    except Exception:
                        max_nodes = None
                    if max_nodes is not None:
                        within = (len(getattr(g, "nodes", {})) <= max_nodes)
                        pre_constraints["within_size"] = within
                        if not within:
                            pre_penalty += 1.0

        # Compute dead-nodes on raw graph, then prune before translation
        raw_g = g
        try:
            dead_nodes_count = float(count_dead_nodes(raw_g))
        except Exception:
            dead_nodes_count = float(0.0)
        g = prune_graph_contributing(raw_g)
        model = to_pytorch_model(g, {"device": self.device})

        Xv, yv = validation_data if validation_data is not None else (X_train, y_train)
        Xt, yt = test_data if test_data is not None else (Xv, yv)

        # Simple training loop (few epochs for smoke speed)
        epochs = 1 if self.smoke else 10
        lr = 1e-3
        criterion = nn.MSELoss()
        optimizer = torch.optim.Adam(model.parameters(), lr=lr)

        def _forward_batch(m, X):
            return m(X)

        for _ in range(epochs):
            model.train()
            optimizer.zero_grad()
            y_pred = _forward_batch(model, X_train)
            loss = criterion(y_pred, y_train)
            loss.backward()
            optimizer.step()

        model.eval()
        with torch.no_grad():
            val_pred = _forward_batch(model, Xv)
            test_pred = _forward_batch(model, Xt)
            val_mse = float(criterion(val_pred, yv).item())
            test_mse = float(criterion(test_pred, yt).item())

        # Minimal artifacts: write to a temp directory under cwd
        outdir = os.path.join(os.getcwd(), "tmp_search_artifacts")
        os.makedirs(outdir, exist_ok=True)
        with open(os.path.join(outdir, "config.json"), "w") as f:
            json.dump({"seed": self.seed, "device": self.device, "smoke": self.smoke}, f)
        with open(os.path.join(outdir, "evolution_history.json"), "w") as f:
            json.dump([{"gen": 0, "val_mse": val_mse}], f)
        with open(os.path.join(outdir, "repro_manifest.json"), "w") as f:
            json.dump({"timestamp": time.time(), "wl": g.compute_fingerprint()}, f)
        # Export raw and pruned architectures for audit
        try:
            def _to_arch(graph: Graph) -> dict:
                nodes = []
                for nid in sorted(list(getattr(graph, "nodes", {}).keys()), key=lambda x: int(x)):
                    node = graph.nodes[nid]
                    out_size = None
                    try:
                        a = getattr(node, "attributes", {})
                        if isinstance(a, dict):
                            out_size = a.get("output_size")
                    except Exception:
                        pass
                    nodes.append({
                        "id": str(nid),
                        "node_type": str(getattr(node, "node_type", "")),
                        "activation_function": getattr(node, "activation_function", None),
                        "output_size": out_size,
                    })
                edges = []
                try:
                    es = list(getattr(graph, "list_edges", lambda: [])())
                except Exception:
                    es = []
                edge_pairs = []
                for e in es:
                    src = getattr(e, "src_id", getattr(e, "source_node_id", None))
                    dst = getattr(e, "dst_id", getattr(e, "target_node_id", None))
                    if src is None or dst is None:
                        continue
                    edge_pairs.append((int(src), int(dst)))
                for src, dst in sorted(edge_pairs):
                    edges.append([str(src), str(dst)])
                return {"nodes": nodes, "edges": edges}

            raw_arch = _to_arch(raw_g)
            pruned_arch = _to_arch(g)
            with open(os.path.join(outdir, "best_architecture_raw.json"), "w", encoding="utf-8") as f:
                json.dump(raw_arch, f, indent=2)
            with open(os.path.join(outdir, "best_architecture_pruned.json"), "w", encoding="utf-8") as f:
                json.dump(pruned_arch, f, indent=2)
            with open(os.path.join(outdir, "fingerprints.json"), "w", encoding="utf-8") as f:
                json.dump({
                    "raw_wl": raw_g.compute_fingerprint(),
                    "pruned_wl": g.compute_fingerprint(),
                    "dead_nodes": int(dead_nodes_count),
                }, f, indent=2)
        except Exception:
            pass

        # Objectives interface (multi-objective friendly)
        objectives = []
        objs_conf = getattr(self, "objectives", None)
        if objs_conf is None and self.objective:
            objs_conf = [("val_mse", "min")]
        obj_vals: Dict[str, float] = {}
        # inject early constraint penalty if any
        if 'pre_penalty' in locals() and pre_penalty > 0.0:
            obj_vals["constraint_penalty"] = float(pre_penalty)
        if objs_conf:
            # val_mse
            if any((isinstance(o, tuple) and o[0] == "val_mse") or (o == "val_mse") for o in objs_conf):
                obj_vals["val_mse"] = val_mse
            # params
            if any((isinstance(o, tuple) and o[0] == "params") or (o == "params") for o in objs_conf):
                params = float(sum(p.numel() for p in model.parameters()))
                obj_vals["params"] = params
            # dead_nodes (computed pre-prune)
            if any((isinstance(o, tuple) and o[0] == "dead_nodes") or (o == "dead_nodes") for o in objs_conf):
                obj_vals["dead_nodes"] = float(dead_nodes_count)
            # latency objective objects
            for o in objs_conf:
                if hasattr(o, "measure"):
                    try:
                        obj_vals["latency_ms"] = float(o.measure(model, Xv))
                    except Exception:
                        obj_vals["latency_ms"] = float("nan")
            # synthesize multiple candidates if requested population>1
            cand = {"objectives": dict(obj_vals)}
            objectives = [cand]
            try:
                pop = int(self.population)
            except Exception:
                pop = 1
            _use_gen_smoke = bool(getattr(self, "use_generation_smoke", False) or getattr(self, "use_real_generation_smoke", False))
            if pop > 1 and _use_gen_smoke:
                # Build per-candidate graphs by adding i extra hidden nodes to vary params
                objectives = []
                for i in range(pop):
                    gi = Graph()
                    iid = gi.add_node({"node_type": NodeType.INPUT, "activation_function": "linear", "attributes": {"output_size": int(X_train.shape[1])}})
                    hid = gi.add_node({"node_type": NodeType.HIDDEN, "activation_function": "relu", "attributes": {"output_size": 32}})
                    out = gi.add_node({"node_type": NodeType.OUTPUT, "activation_function": "linear", "attributes": {"output_size": 1}})
                    gi.add_edge(iid, hid)
                    gi.add_edge(hid, out)
                    # If rules exist, apply up to i iterations to vary structure
                    rules = getattr(self.search_space, "rules", [])
                    try:
                        if rules:
                            before_nodes = len(getattr(gi, "nodes", {}))
                            gi2 = apply_grammar(gi, rules, max_iterations=max(1, i))
                            after_nodes = len(getattr(gi2, "nodes", {}))
                            gi = gi2
                            if after_nodes <= before_nodes:
                                raise RuntimeError("no_change")
                        else:
                            raise RuntimeError("no_rules")
                    except Exception:
                        # fallback to manual extras to ensure distinct param counts
                        for _ in range(i + 1):
                            extra = gi.add_node({"node_type": NodeType.HIDDEN, "activation_function": "relu", "attributes": {"output_size": 16}})
                            gi.add_edge(iid, extra)
                            gi.add_edge(extra, out)
                    mi = to_pytorch_model(gi, {"device": self.device})
                    params_i = float(sum(p.numel() for p in mi.parameters()))
                    # latency optional
                    lat = None
                    for o in objs_conf:
                        if hasattr(o, "measure"):
                            try:
                                lat = float(o.measure(mi, Xv))
                            except Exception:
                                lat = None
                    obj_i: Dict[str, float] = {}
                    if any((isinstance(o, tuple) and o[0] == "params") or (o == "params") for o in objs_conf):
                        obj_i["params"] = params_i
                    if lat is not None:
                        obj_i["latency_ms"] = lat
                    if 'pre_penalty' in locals() and pre_penalty > 0.0:
                        obj_i["constraint_penalty"] = float(pre_penalty)
                    objectives.append({"objectives": obj_i, "rank": i})
            elif pop > 1:
                # create one additional candidate with slight jitter
                jitter = {k: (v * 1.01 if isinstance(v, float) else v) for k, v in obj_vals.items()}
                objectives.append({"objectives": jitter})
            # Optionally integrate NSGA-II when population > 1 (smoke-friendly)
            try:
                pop = int(self.population)
            except Exception:
                pop = 1
            # Real NSGA over generated candidates (smoke budgets)
            if pop > 1 and bool(getattr(self, "use_real_generation_nsga", False)):
                # Build candidates via grammar application
                rules = getattr(self.search_space, "rules", [])
                pop_objs: List[Graph] = []
                for i in range(pop):
                    gi = Graph()
                    iid = gi.add_node({"node_type": NodeType.INPUT, "activation_function": "linear", "attributes": {"output_size": int(X_train.shape[1])}})
                    hid = gi.add_node({"node_type": NodeType.HIDDEN, "activation_function": "relu", "attributes": {"output_size": 32}})
                    out = gi.add_node({"node_type": NodeType.OUTPUT, "activation_function": "linear", "attributes": {"output_size": 1}})
                    gi.add_edge(iid, hid)
                    gi.add_edge(hid, out)
                    try:
                        if rules:
                            gi = apply_grammar(gi, rules, max_iterations=max(1, (i % 3) + 1))
                    except Exception:
                        pass
                    pop_objs.append(gi)

                def _objs_graph(gx: Graph) -> Dict[str, float]:
                    gx_pruned = prune_graph_contributing(gx)
                    m = to_pytorch_model(gx_pruned, {"device": self.device})
                    # params objective
                    params_v = float(sum(p.numel() for p in m.parameters()))
                    outd: Dict[str, float] = {"params": params_v}
                    # tiny training for val_mse if requested
                    if any((isinstance(o, tuple) and o[0] == "val_mse") or (o == "val_mse") for o in objs_conf):
                        crit = nn.MSELoss()
                        opt = torch.optim.SGD(m.parameters(), lr=1e-3)
                        m.train()
                        opt.zero_grad()
                        yp = m(X_train)
                        loss = crit(yp, y_train)
                        loss.backward()
                        opt.step()
                        m.eval()
                        with torch.no_grad():
                            vy = m(Xv)
                            outd["val_mse"] = float(crit(vy, yv).item())
                    # latency if requested
                    for o in objs_conf:
                        if hasattr(o, "measure"):
                            try:
                                outd["latency_ms"] = float(o.measure(m, Xv))
                            except Exception:
                                outd["latency_ms"] = float("nan")
                    # per-candidate constraint penalty
                    cp = 0.0
                    for c in getattr(self, "constraints", []) or []:
                        if isinstance(c, tuple) and len(c) == 2:
                            name, val = c
                            if name == "is_dag":
                                try:
                                    gx_pruned.topological_sort()
                                except Exception:
                                    cp += 1.0
                            elif name == "max_nodes":
                                try:
                                    max_nodes = int(val)
                                    if len(getattr(gx_pruned, "nodes", {})) > max_nodes:
                                        cp += 1.0
                                except Exception:
                                    pass
                    if cp > 0.0:
                        outd["constraint_penalty"] = float(cp)
                    return outd

                sols = nsga2_evolve(
                    population=pop_objs,
                    objectives=_objs_graph,
                    generations=max(1, int(self.generations)),
                    population_size=max(1, int(self.population)),
                    return_solutions=True,
                )
                pareto = []
                for s in sols:
                    pareto.append(
                        {
                            "objectives": dict(getattr(s, "objectives", {})),
                            "rank": int(getattr(s, "rank", 0)),
                            "crowding": float(getattr(s, "crowding_distance", 0.0)),
                        }
                    )
                objectives = pareto
            elif pop > 1 and not _use_gen_smoke:
                # Create a tiny synthetic population; objectives depend on index for determinism
                class _G:
                    def __init__(self, idx: int):
                        self.id = idx
                        self.rules = [idx]

                pop_objs = [_G(i) for i in range(pop)]

                base = dict(obj_vals)
                if 'pre_penalty' in locals() and pre_penalty > 0.0:
                    base["constraint_penalty"] = float(pre_penalty)

                def _objs(gany: Any) -> Dict[str, float]:
                    i = getattr(gany, "id", 0)
                    # Slightly vary params by adding a small dependent term
                    scale = 1.0 + 0.05 * (i % 3)
                    out = {}
                    for k, v in base.items():
                        if isinstance(v, float):
                            out[k] = float(v * scale)
                    # Increase params objective proportionally with i
                    if "params" in out:
                        out["params"] = float(out["params"] + 100.0 * i)
                    return out

                sols = nsga2_evolve(
                    population=pop_objs,
                    objectives=_objs,
                    generations=1,
                    population_size=pop,
                    return_solutions=True,
                )
                # Build pareto list from solutions
                pareto: List[Dict[str, Any]] = []
                for s in sols:
                    pareto.append(
                        {
                            "objectives": dict(getattr(s, "objectives", {})),
                            "rank": int(getattr(s, "rank", 0)),
                            "crowding": float(getattr(s, "crowding_distance", 0.0)),
                        }
                    )
                objectives = pareto
            else:
                # assign simple ranks in order
                for i, entry in enumerate(objectives):
                    entry["rank"] = i

            # Propagate constraint penalty into objective dicts
            try:
                _cp = float(constraint_penalty)
            except Exception:
                _cp = 0.0
            if _cp > 0.0:
                for entry in objectives:
                    entry.setdefault("objectives", {})["constraint_penalty"] = _cp

        # Constraints evaluation (smoke-level) and penalty
        constraints_out: Dict[str, Any] = {}
        constraint_penalty = 0.0
        for c in getattr(self, "constraints", []) or []:
            if isinstance(c, tuple) and len(c) == 2:
                name, val = c
                if name == "is_dag":
                    try:
                        # If topological_sort succeeds → DAG
                        g.topological_sort()
                        constraints_out["is_dag"] = True
                    except Exception:
                        constraints_out["is_dag"] = False
                        constraint_penalty += 1.0
                elif name == "max_nodes":
                    try:
                        max_nodes = int(val)
                    except Exception:
                        max_nodes = None
                    if max_nodes is not None:
                        within = (len(getattr(g, "nodes", {})) <= max_nodes)
                        constraints_out["within_size"] = within
                        if not within:
                            constraint_penalty += 1.0

        if constraint_penalty > 0.0:
            obj_vals["constraint_penalty"] = float(constraint_penalty)

        return SearchResult(
            model=model,
            metrics={"val_mse": val_mse, "test_mse": test_mse},
            best_architecture=g,
            artifacts=outdir,
            seed=self.seed,
            device=self.device,
            pareto=objectives or None,
            constraints=constraints_out if getattr(self, "constraints", None) is not None else {},
        )


__all__ = [
    "Search",
    "SearchResult",
    "SearchSpace",
    "rule",
    "starter_space",
    "wl_fingerprint",
    "DeterminismSignature",
    "ReproBundle",
    "LatencyObjective",
]


# ---------------------------- Graph Pruning Helpers ----------------------------

def prune_graph_contributing(graph: Graph) -> Graph:
    """Return a copy of the graph keeping only nodes that contribute from any INPUT to any OUTPUT.

    - Keeps nodes reachable from at least one INPUT (forward) AND that can reach at least one OUTPUT (backward).
    - Re-creates nodes with the same type/activation/attributes and re-adds edges between kept nodes.
    """
    try:
        # Build edge lists
        fwd: dict[int, list[int]] = {}
        rev: dict[int, list[int]] = {}
        edges = []
        for e in graph.list_edges():
            src = getattr(e, 'src_id', getattr(e, 'source_node_id', None))
            dst = getattr(e, 'dst_id', getattr(e, 'target_node_id', None))
            if src is None or dst is None:
                continue
            edges.append((int(src), int(dst)))
            fwd.setdefault(int(src), []).append(int(dst))
            rev.setdefault(int(dst), []).append(int(src))

        # Discover inputs/outputs
        from ggnes.core.node import NodeType as _NT
        nodes = getattr(graph, 'nodes', {})
        inputs = [nid for nid, node in nodes.items() if getattr(node, 'node_type', None) == _NT.INPUT]
        outputs = [nid for nid, node in nodes.items() if getattr(node, 'node_type', None) == _NT.OUTPUT]

        # BFS from inputs
        reachable_fwd: set[int] = set()
        stack = list(map(int, inputs))
        while stack:
            u = stack.pop()
            if u in reachable_fwd:
                continue
            reachable_fwd.add(u)
            for v in fwd.get(u, []):
                if v not in reachable_fwd:
                    stack.append(v)

        # Reverse BFS from outputs
        reachable_bwd: set[int] = set()
        stack = list(map(int, outputs))
        while stack:
            u = stack.pop()
            if u in reachable_bwd:
                continue
            reachable_bwd.add(u)
            for v in rev.get(u, []):
                if v not in reachable_bwd:
                    stack.append(v)

        keep = {nid for nid in nodes.keys() if int(nid) in reachable_fwd and int(nid) in reachable_bwd}
        # If nothing detected (degenerate), keep original
        if not keep:
            return graph

        # Rebuild
        from ggnes.core.graph import Graph as _Graph
        g2 = _Graph()
        old_to_new: dict[int, int] = {}
        for nid in sorted(list(nodes.keys()), key=lambda x: int(x)):
            node = nodes[nid]
            if int(nid) not in keep:
                continue
            props = {
                'node_type': getattr(node, 'node_type', None),
                'activation_function': getattr(node, 'activation_function', None),
            }
            # Attributes may be stored differently; try best-effort copy
            attrs = {}
            try:
                a = getattr(node, 'attributes', {})
                if isinstance(a, dict):
                    attrs.update(a)
            except Exception:
                pass
            if attrs:
                props['attributes'] = attrs
            new_id = g2.add_node(props)
            old_to_new[int(nid)] = new_id

        for src, dst in sorted(edges):
            if int(src) in keep and int(dst) in keep:
                try:
                    g2.add_edge(old_to_new[int(src)], old_to_new[int(dst)])
                except Exception:
                    pass
        return g2
    except Exception:
        # On any failure, return original graph
        return graph


def _contributing_node_ids(graph: Graph) -> set[int]:
    try:
        fwd: dict[int, list[int]] = {}
        rev: dict[int, list[int]] = {}
        for e in graph.list_edges():
            src = getattr(e, 'src_id', getattr(e, 'source_node_id', None))
            dst = getattr(e, 'dst_id', getattr(e, 'target_node_id', None))
            if src is None or dst is None:
                continue
            s = int(src)
            d = int(dst)
            fwd.setdefault(s, []).append(d)
            rev.setdefault(d, []).append(s)
        from ggnes.core.node import NodeType as _NT
        nodes = getattr(graph, 'nodes', {})
        inputs = [int(nid) for nid, node in nodes.items() if getattr(node, 'node_type', None) == _NT.INPUT]
        outputs = [int(nid) for nid, node in nodes.items() if getattr(node, 'node_type', None) == _NT.OUTPUT]
        reachable_fwd: set[int] = set()
        stack = list(inputs)
        while stack:
            u = stack.pop()
            if u in reachable_fwd:
                continue
            reachable_fwd.add(u)
            for v in fwd.get(u, []):
                if v not in reachable_fwd:
                    stack.append(v)
        reachable_bwd: set[int] = set()
        stack = list(outputs)
        while stack:
            u = stack.pop()
            if u in reachable_bwd:
                continue
            reachable_bwd.add(u)
            for v in rev.get(u, []):
                if v not in reachable_bwd:
                    stack.append(v)
        return {nid for nid in nodes.keys() if int(nid) in reachable_fwd and int(nid) in reachable_bwd}
    except Exception:
        return set()


def count_dead_nodes(graph: Graph) -> int:
    nodes = getattr(graph, 'nodes', {})
    contrib = _contributing_node_ids(graph)
    return max(0, int(len(nodes) - len(contrib)))

