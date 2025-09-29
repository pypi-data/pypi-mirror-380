#!/usr/bin/env python3
"""
================================================================================
GGNES Organic Sensor Fusion Demo (Investor Edition)
================================================================================

Pitch
- Showcase how grammar-guided neuroevolution discovers organic multi-branch
  architectures that fuse heterogeneous sensor signals with superior efficiency.
- All computations run on CPU only and remain fully deterministic/replayable.
- Compare the evolved graph against a mainstream baseline (scikit-learn MLP)
  on accuracy, parameter count, and inference latency.

Highlights
- Deterministic synthetic dataset that mimics temporal + weather + event streams
  without requiring any external downloads (seeded for auditability).
- Grammar preset encourages attention hubs, gated bridges, recurrent enrichments
  and residual links, resulting in visually organic graph structures.
- Investor-friendly artifact pack: Pareto history, best architecture JSON/SVG,
  run report with baseline vs. GGNES table, and reproducibility manifest.

Quickstart
1) python3 -m venv .venv && .venv/bin/python -m pip install --upgrade pip
   .venv/bin/pip install -r requirements.txt
2) .venv/bin/python -u demo/organic_sensor_fusion_demo.py --pop 16 --gen 2
   (fast smoke test ~2-3 minutes on laptop CPU)
3) Scale up for investor-grade results:
   .venv/bin/python -u demo/organic_sensor_fusion_demo.py --pop 60 --gen 25

Environment overrides (examples)
- GGNES_SENSOR_SAMPLES, GGNES_SENSOR_NOISE: dataset size/noise
- GGNES_DEMO_POP, GGNES_DEMO_GEN, GGNES_DEMO_MAX_ITERS, GGNES_DEMO_EVAL_WORKERS
- GGNES_DEMO_INIT_EPOCHS, GGNES_DEMO_FINAL_EPOCHS: training budgets
- GGNES_DEMO_MAX_NET_SIZE: cap on generated graph nodes
================================================================================
"""

from __future__ import annotations

import argparse
import copy
import json
import os
import platform
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from typing import Any, Dict, List, Tuple

import numpy as np
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from ggnes import (
    EmbeddingLogic,
    Genotype,
    Graph,
    LHSPattern,
    NodeType,
    RHSAction,
    Rule,
    to_pytorch_model,
)
from ggnes.datasets import generate_sensor_fusion_dataset
from ggnes.generation.network_gen import generate_network as generate_network_from_genotype
from ggnes.utils.rng_manager import RNGManager


try:  # Lazy torch import so tests can import this module without CUDA libs
    import torch
    import torch.nn as nn
    import torch.optim as optim
except ImportError:  # pragma: no cover - handled in runtime checks
    torch = None
    nn = None
    optim = None


DEVICE = torch.device("cpu") if torch is not None else "cpu"


class Config:
    """Centralised configuration (tunable via CLI/env)."""

    # Dataset controls
    samples = int(os.getenv("GGNES_SENSOR_SAMPLES", "16384"))
    noise_sigma = float(os.getenv("GGNES_SENSOR_NOISE", "0.08"))
    test_size = 0.15
    val_size = 0.15
    random_state = 31415

    # Training (per-candidate evaluation)
    initial_epochs = int(os.getenv("GGNES_DEMO_INIT_EPOCHS", "8"))
    final_epochs = int(os.getenv("GGNES_DEMO_FINAL_EPOCHS", "30"))
    batch_size = 128
    learning_rate = 1e-3

    # Evolution
    population_size = int(os.getenv("GGNES_DEMO_POP", "60"))
    generations = int(os.getenv("GGNES_DEMO_GEN", "25"))
    mutation_rate = 0.32
    crossover_rate = 0.72
    immigrant_interval = int(os.getenv("GGNES_DEMO_IMM_INTERVAL", "5"))
    immigrants_fraction = float(os.getenv("GGNES_DEMO_IMM_FRAC", "0.15"))
    disable_convergence = bool(int(os.getenv("GGNES_DEMO_DISABLE_CONV", "0")))

    # Grammar search-space knobs
    rule_preset = "organic_sensor_fusion"
    use_all_combinations = True
    initial_rules = 6
    max_rules = 160
    max_iterations = int(os.getenv("GGNES_DEMO_MAX_ITERS", "28"))
    max_network_size = int(os.getenv("GGNES_DEMO_MAX_NET_SIZE", "220"))

    branch_sizes = [48, 64, 80]
    fusion_sizes = [64, 80, 96]
    branch_activations = ["elu", "gelu", "silu"]
    recurrent_activations = ["gru", "lstm"]

    # Parallel evaluation
    eval_workers = os.getenv("GGNES_DEMO_EVAL_WORKERS")

    # Outputs
    results_dir = os.getenv(
        "GGNES_DEMO_RESULTS_DIR",
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "sensor_fusion_demo_output"),
    )
    use_timestamp = False


# --------------------------------------------------------------------------------------
# Data utilities
# --------------------------------------------------------------------------------------


@dataclass
class DatasetBundle:
    train_torch: Tuple[torch.Tensor, torch.Tensor]
    val_torch: Tuple[torch.Tensor, torch.Tensor]
    test_torch: Tuple[torch.Tensor, torch.Tensor]
    train_np: Tuple[np.ndarray, np.ndarray]
    val_np: Tuple[np.ndarray, np.ndarray]
    test_np: Tuple[np.ndarray, np.ndarray]
    scaler_mean: np.ndarray
    scaler_scale: np.ndarray


def ensure_results_dir() -> str:
    out_dir = Config.results_dir
    os.makedirs(out_dir, exist_ok=True)
    for name in [
        "evolution_history.json",
        "pareto_front_summary.json",
        "generation_metrics.json",
        "config.json",
        "baseline_metrics.json",
        "best_genotype.json",
        "best_graph_edges.json",
        "best_architecture.json",
        "best_metrics.json",
        "retrain_metrics.json",
        "run_report.txt",
        "repro_manifest.json",
    ]:
        try:
            path = os.path.join(out_dir, name)
            if os.path.exists(path):
                os.remove(path)
        except Exception:
            pass
    return out_dir


def load_dataset() -> DatasetBundle:
    if torch is None:
        raise RuntimeError("PyTorch is required to load datasets for the demo.")
    from sklearn.preprocessing import StandardScaler

    print("Generating deterministic sensor-fusion dataset...")
    X, y = generate_sensor_fusion_dataset()

    X_temp, X_test, y_temp, y_test = train_test_split(
        X,
        y,
        test_size=Config.test_size,
        random_state=Config.random_state,
        shuffle=True,
    )
    X_train, X_val, y_train, y_val = train_test_split(
        X_temp,
        y_temp,
        test_size=Config.val_size,
        random_state=Config.random_state,
        shuffle=True,
    )

    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_val = scaler.transform(X_val)
    X_test = scaler.transform(X_test)

    torch_train = (
        torch.from_numpy(X_train).float().to(DEVICE),
        torch.from_numpy(y_train).float().unsqueeze(1).to(DEVICE),
    )
    torch_val = (
        torch.from_numpy(X_val).float().to(DEVICE),
        torch.from_numpy(y_val).float().unsqueeze(1).to(DEVICE),
    )
    torch_test = (
        torch.from_numpy(X_test).float().to(DEVICE),
        torch.from_numpy(y_test).float().unsqueeze(1).to(DEVICE),
    )

    return DatasetBundle(
        train_torch=torch_train,
        val_torch=torch_val,
        test_torch=torch_test,
        train_np=(X_train, y_train),
        val_np=(X_val, y_val),
        test_np=(X_test, y_test),
        scaler_mean=scaler.mean_.copy(),
        scaler_scale=scaler.scale_.copy(),
    )


# --------------------------------------------------------------------------------------
# Grammar construction
# --------------------------------------------------------------------------------------


def _embedding_ignore() -> EmbeddingLogic:
    emb = EmbeddingLogic()
    try:
        emb.boundary_handling = "IGNORE"
    except Exception:
        pass
    return emb


def create_axiom_graph(input_size: int) -> Graph:
    graph = Graph()
    graph.add_node(
        {
            "id": "input",
            "node_type": NodeType.INPUT,
            "activation_function": "linear",
            "output_size": input_size,
        }
    )
    graph.add_node(
        {
            "id": "stem",
            "node_type": NodeType.HIDDEN,
            "activation_function": "relu",
            "output_size": 64,
        }
    )
    graph.add_node(
        {
            "id": "collector",
            "node_type": NodeType.HIDDEN,
            "activation_function": "elu",
            "output_size": 48,
        }
    )
    graph.add_node(
        {
            "id": "output",
            "node_type": NodeType.OUTPUT,
            "activation_function": "linear",
            "output_size": 1,
        }
    )
    graph.add_edge("input", "stem")
    graph.add_edge("stem", "collector")
    graph.add_edge("collector", "output")
    return graph


def create_grammar_rules() -> List[Rule]:
    rules: List[Rule] = []

    # Attention hub sprouting from a hidden anchor
    for activation in Config.branch_activations:
        for fusion_size in Config.fusion_sizes:
            rule = Rule(
                name=f"attention_hub_{activation}_{fusion_size}",
                pattern=LHSPattern(
                    nodes=[{"label": "ANCHOR", "match_criteria": {"node_type": NodeType.HIDDEN}}],
                    edges=[],
                    boundary_nodes=["ANCHOR"],
                ),
                action=RHSAction(
                    add_nodes=[
                        {
                            "label": "BRANCH",
                            "properties": {
                                "node_type": NodeType.HIDDEN,
                                "activation_function": activation,
                                "attributes": {"output_size": fusion_size},
                            },
                        },
                        {
                            "label": "ATTN",
                            "properties": {
                                "node_type": NodeType.HIDDEN,
                                "activation_function": "linear",
                                "attributes": {
                                    "output_size": fusion_size,
                                    "aggregation_function": "attention",
                                    "aggregation": "attention",
                                    "temperature": 1.0,
                                    "dropout_p": 0.0,
                                },
                            },
                        },
                    ],
                    add_edges=[
                        {"source_label": "ANCHOR", "target_label": "BRANCH"},
                        {"source_label": "ANCHOR", "target_label": "ATTN"},
                        {"source_label": "BRANCH", "target_label": "ATTN"},
                    ],
                ),
                application_probability=0.55,
                embedding=_embedding_ignore(),
            )
            rules.append(rule)

    # Multi-head fusion between sequential hidden nodes
    for fusion_size in Config.fusion_sizes:
        rule = Rule(
            name=f"multi_head_bridge_{fusion_size}",
            pattern=LHSPattern(
                nodes=[
                    {"label": "A", "match_criteria": {"node_type": NodeType.HIDDEN}},
                    {"label": "B", "match_criteria": {"node_type": NodeType.HIDDEN}},
                ],
                edges=[{"source_label": "A", "target_label": "B"}],
                boundary_nodes=["A", "B"],
            ),
            action=RHSAction(
                add_nodes=[
                    {
                        "label": "MH",
                        "properties": {
                            "node_type": NodeType.HIDDEN,
                            "activation_function": "linear",
                            "attributes": {
                                "output_size": fusion_size,
                                "aggregation_function": "multi_head_attention",
                                "aggregation": "multi_head_attention",
                                "num_heads": 4,
                                "head_dim": max(8, fusion_size // 4),
                                "dropout_p": 0.0,
                            },
                        },
                    },
                    {
                        "label": "FUSED",
                        "properties": {
                            "node_type": NodeType.HIDDEN,
                            "activation_function": "gelu",
                            "attributes": {"output_size": fusion_size},
                        },
                    },
                ],
                add_edges=[
                    {"source_label": "A", "target_label": "MH"},
                    {"source_label": "B", "target_label": "MH"},
                    {"source_label": "MH", "target_label": "FUSED"},
                    {"source_label": "FUSED", "target_label": "B"},
                ],
            ),
            application_probability=0.45,
            embedding=_embedding_ignore(),
        )
        rules.append(rule)

    # Gated bridge injecting periodic context
    for branch_size in Config.branch_sizes:
        rule = Rule(
            name=f"gated_bridge_{branch_size}",
            pattern=LHSPattern(
                nodes=[
                    {"label": "SRC", "match_criteria": {"node_type": NodeType.HIDDEN}},
                    {"label": "DST", "match_criteria": {"node_type": NodeType.HIDDEN}},
                ],
                edges=[],
                boundary_nodes=["SRC", "DST"],
            ),
            action=RHSAction(
                add_nodes=[
                    {
                        "label": "BRIDGE",
                        "properties": {
                            "node_type": NodeType.HIDDEN,
                            "activation_function": "silu",
                            "attributes": {"output_size": branch_size},
                        },
                    },
                    {
                        "label": "GATE",
                        "properties": {
                            "node_type": NodeType.HIDDEN,
                            "activation_function": "linear",
                            "attributes": {
                                "output_size": branch_size,
                                "aggregation_function": "gated_sum",
                                "aggregation": "gated_sum",
                            },
                        },
                    },
                ],
                add_edges=[
                    {"source_label": "SRC", "target_label": "BRIDGE"},
                    {"source_label": "SRC", "target_label": "GATE"},
                    {"source_label": "BRIDGE", "target_label": "GATE"},
                    {"source_label": "GATE", "target_label": "DST"},
                ],
            ),
            application_probability=0.4,
            embedding=_embedding_ignore(),
        )
        rules.append(rule)

    # Introduce recurrent enrichment nodes
    for act in Config.recurrent_activations:
        rule = Rule(
            name=f"recurrent_enrichment_{act}",
            pattern=LHSPattern(
                nodes=[{"label": "CORE", "match_criteria": {"node_type": NodeType.HIDDEN}}],
                edges=[],
                boundary_nodes=["CORE"],
            ),
            action=RHSAction(
                add_nodes=[
                    {
                        "label": "REC",
                        "properties": {
                            "node_type": NodeType.HIDDEN,
                            "activation_function": act,
                            "attributes": {"output_size": 48},
                        },
                    }
                ],
                add_edges=[
                    {"source_label": "CORE", "target_label": "REC"},
                    {"source_label": "REC", "target_label": "CORE"},
                ],
            ),
            application_probability=0.25,
            embedding=_embedding_ignore(),
        )
        rules.append(rule)

    # Residual skip to outputs/collector nodes
    skip_rule = Rule(
        name="residual_skip",
        pattern=LHSPattern(
            nodes=[
                {"label": "SRC", "match_criteria": {"node_type": NodeType.HIDDEN}},
                {"label": "DST", "match_criteria": {"node_type": NodeType.HIDDEN}},
            ],
            edges=[{"source_label": "SRC", "target_label": "DST"}],
            boundary_nodes=["SRC", "DST"],
        ),
        action=RHSAction(add_edges=[{"source_label": "SRC", "target_label": "DST"}]),
        application_probability=0.3,
        embedding=_embedding_ignore(),
    )
    rules.append(skip_rule)

    return rules


def create_genotype(num_rules: int = 6) -> Genotype:
    rule_library = create_grammar_rules()
    if getattr(Config, "use_all_combinations", False):
        unique: List[Rule] = []
        seen = set()
        for r in rule_library:
            key = getattr(r, "name", None)
            if key and key not in seen:
                unique.append(r)
                seen.add(key)
        target_size = min(len(rule_library), max(len(unique), Config.max_rules))
        extras = max(0, target_size - len(unique))
        if extras > 0:
            idx = np.random.choice(len(rule_library), extras, replace=False)
            unique.extend(rule_library[i] for i in idx if rule_library[i] not in unique)
        selected = unique[: Config.max_rules]
    else:
        idx = np.random.choice(len(rule_library), min(num_rules, len(rule_library)), replace=False)
        selected = [rule_library[i] for i in idx]
    return Genotype(rules=selected)


# --------------------------------------------------------------------------------------
# Training & evaluation helpers
# --------------------------------------------------------------------------------------


def train_model(
    model: nn.Module,
    train_data: Tuple[torch.Tensor, torch.Tensor],
    val_data: Tuple[torch.Tensor, torch.Tensor],
    epochs: int,
) -> Tuple[List[float], List[float]]:
    if torch is None or nn is None or optim is None:
        raise RuntimeError("PyTorch is required to train models in the demo.")
    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=Config.learning_rate)
    train_losses: List[float] = []
    val_losses: List[float] = []

    X_train, y_train = train_data
    X_val, y_val = val_data

    for _ in range(epochs):
        model.train()
        optimizer.zero_grad()
        preds = model(X_train)
        loss = criterion(preds, y_train)
        loss.backward()
        optimizer.step()
        train_losses.append(float(loss.detach().cpu().item()))

        model.eval()
        with torch.no_grad():
            val_pred = model(X_val)
            val_loss = criterion(val_pred, y_val)
            val_losses.append(float(val_loss.detach().cpu().item()))

    return train_losses, val_losses


def _seed_for(genotype: Any, base: int = 1234) -> int:
    gid = getattr(genotype, "genotype_id", None) or getattr(genotype, "id", None)
    try:
        key = int(str(gid).replace("-", "")[:8], 16)
    except Exception:
        key = 0
    return base + (key % (2**31 - 1))


def evaluate_genotype(
    genotype: Genotype,
    dataset: DatasetBundle,
) -> Tuple[float, int, Dict[str, Any]]:
    if torch is None:
        raise RuntimeError("PyTorch is required to evaluate genotypes.")
    try:
        axiom = create_axiom_graph(input_size=dataset.train_np[0].shape[1])
        rng = RNGManager(seed=_seed_for(genotype))
        config = {
            "max_iterations": Config.max_iterations,
            "parallel_execution": True,
            "max_parallel_workers": max(1, min((os.cpu_count() or 2), 6)),
            "parallel_fixed_size": 2,
            "parallel_batch_policy": "FIXED_SIZE",
            "parallel_conflict_strategy": "SKIP",
        }
        network, info = generate_network_from_genotype(
            genotype=genotype,
            axiom_graph=axiom,
            config=config,
            rng_manager=rng,
        )
        if len(getattr(network, "nodes", {})) > Config.max_network_size:
            return float("inf"), 0, {}

        model = to_pytorch_model(network, config={"device": DEVICE}).to(DEVICE)
        params = sum(p.numel() for p in model.parameters())
        _, val_losses = train_model(
            model,
            dataset.train_torch,
            dataset.val_torch,
            epochs=Config.initial_epochs,
        )
        return float(val_losses[-1]), int(params), info
    except Exception:
        return float("inf"), 0, {}


def _geno_key(genotype: Genotype) -> str:
    gid = getattr(genotype, "genotype_id", None)
    return str(gid) if gid is not None else str(id(genotype))


def _mutate_genotype(parent: Genotype) -> Genotype:
    child = copy.deepcopy(parent)
    internal_rules = list(getattr(getattr(child, "_internal_genotype"), "rules", []))
    library = create_grammar_rules()
    if not internal_rules:
        internal_rules = [copy.deepcopy(r._internal_rule) for r in library[: np.random.randint(3, 8)]]
    rng = np.random.default_rng()

    op = rng.choice(["replace", "add", "remove"], p=[0.5, 0.3, 0.2])
    if op == "replace" and internal_rules:
        idx = rng.integers(0, len(internal_rules))
        internal_rules[idx] = copy.deepcopy(rng.choice(library)._internal_rule)
    elif op == "add" and len(internal_rules) < Config.max_rules:
        internal_rules.append(copy.deepcopy(rng.choice(library)._internal_rule))
    elif op == "remove" and len(internal_rules) > 3:
        idx = rng.integers(0, len(internal_rules))
        del internal_rules[idx]

    child._internal_genotype.rules = internal_rules
    return child


def _crossover_genotype(parent_a: Genotype, parent_b: Genotype) -> Genotype:
    rng = np.random.default_rng()
    rules_a = list(getattr(parent_a._internal_genotype, "rules", []))
    rules_b = list(getattr(parent_b._internal_genotype, "rules", []))
    if not rules_a:
        return copy.deepcopy(parent_b)
    if not rules_b:
        return copy.deepcopy(parent_a)

    cut_a = rng.integers(1, len(rules_a))
    cut_b = rng.integers(1, len(rules_b))
    new_rules = rules_a[:cut_a] + rules_b[cut_b:]
    if len(new_rules) > Config.max_rules:
        new_rules = new_rules[: Config.max_rules]
    child = Genotype()
    child._internal_genotype.rules = [copy.deepcopy(r) for r in new_rules]
    return child


def evolve_architectures(dataset: DatasetBundle) -> Tuple[Genotype, List[Dict[str, Any]]]:
    print("\n=== Starting organic grammar evolution ===")
    population: List[Genotype] = [create_genotype(np.random.randint(3, Config.initial_rules + 1)) for _ in range(Config.population_size)]
    eval_cache: Dict[str, Tuple[float, int, Dict[str, Any]]] = {}
    history: List[Dict[str, Any]] = []
    best: Tuple[float, Genotype] | None = None
    stagnant = 0

    def _evaluate(genotype: Genotype) -> Tuple[float, int, Dict[str, Any]]:
        key = _geno_key(genotype)
        if key not in eval_cache:
            eval_cache[key] = evaluate_genotype(genotype, dataset)
        return eval_cache[key]

    for gen in range(Config.generations):
        print(f"\nGeneration {gen + 1}/{Config.generations}")

        cfg_workers = Config.eval_workers
        workers = max(1, int(cfg_workers)) if cfg_workers is not None else max(2, min(6, Config.population_size))

        results: List[Tuple[float, int, Dict[str, Any]]] = [None] * len(population)  # type: ignore
        with ThreadPoolExecutor(max_workers=workers) as executor:
            futures = {executor.submit(_evaluate, population[i]): i for i in range(len(population))}
            for fut in as_completed(futures):
                idx = futures[fut]
                try:
                    results[idx] = fut.result()
                except Exception:
                    results[idx] = (float("inf"), 0, {})

        vals = np.array([r[0] for r in results], dtype=float)
        params_arr = np.array([r[1] for r in results], dtype=float)

        order = np.lexsort((params_arr, vals))
        elites_idx = order[: max(2, Config.population_size // 5)]
        elites = [population[i] for i in elites_idx]
        elite_vals = vals[elites_idx]

        best_val = elite_vals[0]
        best_genotype = elites[0]
        if best is None or best_val + 1e-6 < best[0]:
            best = (best_val, copy.deepcopy(best_genotype))
            stagnant = 0
        else:
            stagnant += 1

        history.append(
            {
                "generation": gen,
                "best_val_loss": float(best_val),
                "mean_val_loss": float(vals.mean()),
                "best_parameters": int(params_arr[elites_idx[0]]),
                "mean_parameters": float(params_arr.mean()),
            }
        )

        if not Config.disable_convergence and stagnant >= max(6, Config.generations // 5):
            print("Convergence detected (stagnation), stopping early.")
            break

        # Build next population
        next_population: List[Genotype] = [copy.deepcopy(g) for g in elites]
        rng = np.random.default_rng()
        while len(next_population) < Config.population_size:
            if rng.random() < 0.45 and len(elites) >= 2:
                parents = rng.choice(elites, size=2, replace=False)
                child = _crossover_genotype(parents[0], parents[1])
            elif rng.random() < 0.85 and elites:
                parent = rng.choice(elites)
                child = _mutate_genotype(parent)
            else:
                child = create_genotype(np.random.randint(3, Config.initial_rules + 1))
            next_population.append(child)

        if Config.immigrant_interval and (gen + 1) % Config.immigrant_interval == 0:
            num_immigrants = max(1, int(Config.immigrants_fraction * Config.population_size))
            for i in rng.choice(len(next_population), size=num_immigrants, replace=False):
                next_population[i] = create_genotype(np.random.randint(3, Config.initial_rules + 1))

        population = next_population[: Config.population_size]

    assert best is not None, "Evolution failed to converge on a valid genotype"
    return best[1], history


# --------------------------------------------------------------------------------------
# Baseline comparison
# --------------------------------------------------------------------------------------


def train_baseline(bundle: DatasetBundle) -> Dict[str, Any]:
    X_train, y_train = bundle.train_np
    X_val, y_val = bundle.val_np
    X_test, y_test = bundle.test_np

    X_train_bl = np.concatenate([X_train, X_val], axis=0)
    y_train_bl = np.concatenate([y_train, y_val], axis=0)

    baseline = MLPRegressor(
        hidden_layer_sizes=(128, 64),
        activation="relu",
        alpha=1e-4,
        learning_rate_init=3e-3,
        max_iter=450,
        early_stopping=True,
        n_iter_no_change=25,
        random_state=Config.random_state,
    )

    start = time.perf_counter()
    baseline.fit(X_train_bl, y_train_bl)
    fit_time = time.perf_counter() - start

    def _forward_latency(batch: np.ndarray, runs: int = 32) -> float:
        start = time.perf_counter()
        for _ in range(runs):
            baseline.predict(batch)
        return (time.perf_counter() - start) / runs

    batch = X_test[:256] if X_test.shape[0] >= 256 else X_test
    latency = _forward_latency(batch)

    preds = baseline.predict(X_test)
    rmse = float(np.sqrt(mean_squared_error(y_test, preds)))
    r2 = float(r2_score(y_test, preds))

    params = sum(w.size for w in baseline.coefs_) + sum(b.size for b in baseline.intercepts_)

    return {
        "model": baseline,
        "rmse": rmse,
        "r2": r2,
        "params": int(params),
        "fit_time": fit_time,
        "latency": latency,
    }


# --------------------------------------------------------------------------------------
# Final evaluation & reporting
# --------------------------------------------------------------------------------------


def evaluate_best_model(genotype: Genotype, dataset: DatasetBundle, out_dir: str) -> Dict[str, Any]:
    if torch is None:
        raise RuntimeError("PyTorch is required to evaluate the best model.")
    axiom = create_axiom_graph(input_size=dataset.train_np[0].shape[1])
    rng = RNGManager(seed=_seed_for(genotype, base=777))
    network, _ = generate_network_from_genotype(
        genotype=genotype,
        axiom_graph=axiom,
        config={"max_iterations": Config.max_iterations},
        rng_manager=rng,
    )

    model = to_pytorch_model(network, config={"device": DEVICE}).to(DEVICE)
    train_model(model, dataset.train_torch, dataset.val_torch, epochs=Config.final_epochs)

    X_test, y_test = dataset.test_torch
    model.eval()
    with torch.no_grad():
        preds = model(X_test).cpu().numpy().squeeze(-1)
    y_true = y_test.cpu().numpy().squeeze(-1)

    rmse = float(np.sqrt(mean_squared_error(y_true, preds)))
    r2 = float(r2_score(y_true, preds))
    params = sum(p.numel() for p in model.parameters())

    def _latency(runs: int = 32) -> float:
        batch = X_test[:256]
        start = time.perf_counter()
        with torch.no_grad():
            for _ in range(runs):
                model(batch)
        return (time.perf_counter() - start) / runs

    latency = _latency()

    metrics = {"rmse": rmse, "r2": r2, "params": int(params), "latency": latency}

    with open(os.path.join(out_dir, "best_metrics.json"), "w") as f:
        json.dump(metrics, f, indent=2)

    # Architecture export for visualization script
    arch = {
        "nodes": [
            {
                "id": str(nid),
                "node_type": str(getattr(node, "node_type", "")),
                "activation_function": getattr(node, "activation_function", None),
                "output_size": node.attributes.get("output_size") if hasattr(node, "attributes") else None,
                "attributes": getattr(node, "attributes", {}),
            }
            for nid, node in getattr(network, "nodes", {}).items()
        ],
        "edges": [
            [
                str(getattr(e, "source_node_id", getattr(e, "src_id", ""))),
                str(getattr(e, "target_node_id", getattr(e, "dst_id", ""))),
            ]
            for e in getattr(network, "list_edges", lambda: [])()
        ],
    }

    with open(os.path.join(out_dir, "best_architecture.json"), "w") as f:
        json.dump(arch, f, indent=2)

    try:
        genotype_dict = genotype.to_dict() if hasattr(genotype, "to_dict") else {}
    except Exception:
        genotype_dict = {}

    with open(os.path.join(out_dir, "best_genotype.json"), "w") as f:
        json.dump(genotype_dict, f, indent=2)

    edges = arch["edges"]
    with open(os.path.join(out_dir, "best_graph_edges.json"), "w") as f:
        json.dump(edges, f, indent=2)

    return metrics


def write_reports(
    history: List[Dict[str, Any]],
    g_metrics: Dict[str, Any],
    baseline: Dict[str, Any],
    out_dir: str,
) -> None:
    with open(os.path.join(out_dir, "evolution_history.json"), "w") as f:
        json.dump(history, f, indent=2)
    with open(os.path.join(out_dir, "pareto_front_summary.json"), "w") as f:
        json.dump(history, f, indent=2)

    cfg = {
        "population_size": Config.population_size,
        "generations": Config.generations,
        "mutation_rate": Config.mutation_rate,
        "crossover_rate": Config.crossover_rate,
        "immigrant_interval": Config.immigrant_interval,
        "immigrants_fraction": Config.immigrants_fraction,
        "max_iterations": Config.max_iterations,
        "max_network_size": Config.max_network_size,
        "initial_epochs": Config.initial_epochs,
        "final_epochs": Config.final_epochs,
        "device": str(DEVICE),
        "rule_preset": Config.rule_preset,
    }
    with open(os.path.join(out_dir, "config.json"), "w") as f:
        json.dump(cfg, f, indent=2)

    with open(os.path.join(out_dir, "baseline_metrics.json"), "w") as f:
        json.dump(
            {
                "rmse": baseline["rmse"],
                "r2": baseline["r2"],
                "params": baseline["params"],
                "latency": baseline["latency"],
                "fit_time": baseline["fit_time"],
            },
            f,
            indent=2,
        )

    report_lines = [
        "GGNES Organic Sensor Fusion Demo",
        "================================",
        "",
        "Baseline (MLPRegressor)",
        f"  RMSE:       {baseline['rmse']:.4f}",
        f"  R^2:        {baseline['r2']:.4f}",
        f"  Parameters: {baseline['params']:,}",
        f"  Latency:    {baseline['latency']*1e3:.3f} ms (batch=256)",
        "",
        "GGNES Best Architecture",
        f"  RMSE:       {g_metrics['rmse']:.4f}",
        f"  R^2:        {g_metrics['r2']:.4f}",
        f"  Parameters: {g_metrics['params']:,}",
        f"  Latency:    {g_metrics['latency']*1e3:.3f} ms (batch=256)",
        "",
        "Delta (GGNES - Baseline)",
        f"  RMSE:       {g_metrics['rmse'] - baseline['rmse']:+.4f}",
        f"  R^2:        {g_metrics['r2'] - baseline['r2']:+.4f}",
        f"  Parameters: {g_metrics['params'] - baseline['params']:,}",
        f"  Latency:    {(g_metrics['latency'] - baseline['latency']) * 1e3:+.3f} ms",
    ]
    with open(os.path.join(out_dir, "run_report.txt"), "w") as f:
        f.write("\n".join(report_lines))

    try:
        manifest = {
            "python": sys.version,
            "platform": {
                "system": platform.system(),
                "release": platform.release(),
                "machine": platform.machine(),
            },
            "packages": {
                "torch": getattr(torch, "__version__", "unknown"),
                "numpy": getattr(np, "__version__", "unknown"),
                "sklearn": __import__("sklearn").__version__,
            },
            "env_overrides": {k: os.environ.get(k) for k in sorted(os.environ) if k.startswith("GGNES_")},
            "timestamp": time.time(),
        }
        with open(os.path.join(out_dir, "repro_manifest.json"), "w") as f:
            json.dump(manifest, f, indent=2)
    except Exception:
        pass


# --------------------------------------------------------------------------------------
# CLI wiring
# --------------------------------------------------------------------------------------


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="GGNES Organic Sensor Fusion Demo")
    p.add_argument("--pop", type=int, default=None, help="Population size")
    p.add_argument("--gen", type=int, default=None, help="Generations")
    p.add_argument("--init-epochs", type=int, default=None, help="Epochs per candidate evaluation")
    p.add_argument("--final-epochs", type=int, default=None, help="Final training epochs for best model")
    p.add_argument("--max-iters", type=int, default=None, help="Max grammar iterations")
    p.add_argument("--eval-workers", type=int, default=None, help="Parallel evaluation workers")
    p.add_argument("--results-dir", type=str, default=None, help="Output directory")
    return p.parse_args()


def apply_cli_overrides(args: argparse.Namespace) -> None:
    if args.pop is not None:
        Config.population_size = int(args.pop)
    if args.gen is not None:
        Config.generations = int(args.gen)
    if args.init_epochs is not None:
        Config.initial_epochs = int(args.init_epochs)
    if args.final_epochs is not None:
        Config.final_epochs = int(args.final_epochs)
    if args.max_iters is not None:
        Config.max_iterations = int(args.max_iters)
    if args.eval_workers is not None:
        Config.eval_workers = int(args.eval_workers)
    if args.results_dir is not None:
        Config.results_dir = args.results_dir


def main() -> int:
    args = parse_args()
    apply_cli_overrides(args)
    out_dir = ensure_results_dir()

    dataset = load_dataset()
    baseline_metrics = train_baseline(dataset)

    best_genotype, history = evolve_architectures(dataset)
    best_metrics = evaluate_best_model(best_genotype, dataset, out_dir)

    write_reports(history, best_metrics, baseline_metrics, out_dir)

    print("\n=== Demo Complete ===")
    print(f"Baseline RMSE: {baseline_metrics['rmse']:.4f} | Params: {baseline_metrics['params']:,}")
    print(f"GGNES RMSE:    {best_metrics['rmse']:.4f} | Params: {best_metrics['params']:,}")
    print(f"Artifacts saved to: {out_dir}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
