#!/usr/bin/env python3
"""
================================================================================
GGNES Neural Architecture Search Demo (California Housing) - Professional Edition
================================================================================

Goal
- Demonstrate GGNES (Graph Grammar Neuroevolution System) end-to-end:
  1) Define a grammar-driven search space (rules) over neural architectures
  2) Evolve architectures with NSGA-II (multi-objective selection)
  3) Translate the resulting graph to a PyTorch model and train/evaluate it
  4) Persist results (history, Pareto summaries, metrics, artifacts, plots)

Audience
- Practitioners who know Python/PyTorch and want to leverage GGNES for NAS.

Key Concepts
- Search space as rules: GGNES uses graph rewriting rules (grammar) to generate
  architectures. A "genotype" is a collection of rules and metadata that drives
  a network "generation" process.
- Evolution: We use NSGA-II to balance conflicting objectives (validation loss,
  model complexity) while satisfying constraints (acyclicity, size limits).
- Translation: The final graph is converted to a torch.nn.Module; advanced
  aggregations (attention, MoE, concat, etc.) are supported.

Outputs
- All artifacts are saved under: demo/california_housing_demo_output/
  * evolution_history.json: per-generation metrics and persisted Pareto summaries
  * generation_metrics.json: timeseries metrics for plotting/analysis
  * pareto_front_summary.json: investor-friendly summary of Pareto fronts
  * config.json: effective configuration for reproducibility
  * best_{genotype,architecture,graph_edges}.json: selected final solution
  * best_metrics.json, retrain_metrics.json: performance KMIs
  * evolution_progress.png, test_predictions.png: key visuals
  * run_report.txt: concise summary report (environment, config, results)

Quickstart (no GGNES knowledge required)
1) Create a Python virtualenv:
   - python3 -m venv .venv && .venv/bin/python -m pip install --upgrade pip
   - .venv/bin/pip install -r requirements.txt
2) Run a tiny CPU sanity test:
   - CUDA_VISIBLE_DEVICES="" .venv/bin/python -u demo/california_housing_fixed.py --pop 8 --gen 2 --eval-workers 2
3) Scale up safely (still CPU):
   - CUDA_VISIBLE_DEVICES="" GGNES_DEMO_EVAL_WORKERS=4 .venv/bin/python -u demo/california_housing_fixed.py --pop 50 --gen 5

Controls you might tweak
- eval_workers (env/CLI): number of parallel evaluations (CPU threads)
- batch_size (Config): per-step batch for training; raise if CPU has headroom
- init_epochs/final_epochs: training depth during candidate eval and final fit
- max_iterations: grammar iterations budget during network generation

================================================================================
"""

import os
import logging
import sys
import warnings
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Any, Dict, List, Tuple

import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from tqdm import tqdm
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score

# Suppress non-critical warnings to keep the console investor-friendly
warnings.filterwarnings('ignore')

# Ensure local project imports are visible
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_ROOT)

# GGNES imports
from ggnes import (
    Graph, NodeType,
    Rule, LHSPattern, RHSAction, EmbeddingLogic,
    Genotype, Population,
    mutate, crossover, evolve, nsga2_evolve,
    apply_grammar,
    to_pytorch_model,
    register_aggregation
)
from ggnes.generation.network_gen import generate_network as generate_network_from_genotype
from ggnes.evolution.metrics import ConvergenceDetector, calculate_diversity
from ggnes.evolution.checkpointing import EvolutionCheckpoint
from ggnes.utils.rng_manager import RNGManager

# Device selection (CPU/GPU)
DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(f"Using device: {DEVICE}")


class Config:
    """Centralized configuration for the demo.

    You can override values via CLI or environment variables (see below).
    """

    # Data
    test_size = 0.2
    val_size = 0.2
    random_state = 42

    # Training (demo-friendly defaults; adjust for more accurate results)
    initial_epochs = 12
    final_epochs = 40
    batch_size = 64
    learning_rate = 0.001

    # Parallel evaluation workers during genotype evaluation
    # - None -> auto (1 on GPU, up to 4 on CPU)
    eval_workers = None

    # Evolution (demo-friendly; increase for stronger results)
    population_size = 80
    generations = 20
    mutation_rate = 0.3
    crossover_rate = 0.7

    # Grammar presets (example palette)
    rule_preset = 'dense_attention'
    use_all_combinations = True

    # Outputs
    results_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'california_housing_demo_output')
    use_timestamp = False

    # Retraining (longer training pass on exported architecture)
    retrain_exported = True
    retrain_epochs = 200

    # Grammar generation constraints
    initial_rules = 5
    max_rules = 200
    max_network_size = 200
    max_iterations = 30

    # Search space parameters
    min_layer_size = 16
    max_layer_size = 128
    layer_sizes = [16, 32, 64, 128, 256, 512]
    activations = ['relu', 'leaky_relu', 'elu', 'gelu', 'tanh', 'sigmoid', 'selu', 'silu', 'softplus', 'softsign']
    aggregations = [
        'sum', 'mean', 'max', 'concat',
        'attention', 'multi_head_attention', 'attn_pool',
        'moe', 'gated_sum', 'topk_weighted_sum', 'matrix_product'
    ]

    # Stagnation and diversity heuristics
    stagnation_patience = 25
    immigrants_fraction = 0.2
    # Disable early convergence stop and schedule periodic immigration (0 = off)
    disable_convergence = False
    immigrant_interval = 0

    @staticmethod
    def apply_env_overrides() -> None:
        """Apply environment variable overrides for quick experimentation.

        Supported environment variables:
        - GGNES_DEMO_POP, GGNES_DEMO_GEN
        - GGNES_DEMO_INIT_EPOCHS, GGNES_DEMO_FINAL_EPOCHS
        - GGNES_DEMO_MAX_ITERS, GGNES_DEMO_MAX_NET_SIZE
        - GGNES_DEMO_EVAL_WORKERS
        """
        def _intenv(name: str, default: Any) -> Any:
            try:
                val = os.getenv(name, None)
                return int(val) if val is not None and str(val).strip() != '' else default
            except Exception:
                return default
        def _floatenv(name: str, default: Any) -> Any:
            try:
                val = os.getenv(name, None)
                return float(val) if val is not None and str(val).strip() != '' else default
            except Exception:
                return default

        Config.population_size = _intenv("GGNES_DEMO_POP", Config.population_size)
        Config.generations = _intenv("GGNES_DEMO_GEN", Config.generations)
        Config.initial_epochs = _intenv("GGNES_DEMO_INIT_EPOCHS", Config.initial_epochs)
        Config.final_epochs = _intenv("GGNES_DEMO_FINAL_EPOCHS", Config.final_epochs)
        Config.max_iterations = _intenv("GGNES_DEMO_MAX_ITERS", Config.max_iterations)
        Config.max_network_size = _intenv("GGNES_DEMO_MAX_NET_SIZE", Config.max_network_size)
        # Treat 0 as "auto" for eval_workers
        ev_auto = _intenv("GGNES_DEMO_EVAL_WORKERS", Config.eval_workers or 0)
        Config.eval_workers = None if ev_auto == 0 else ev_auto

        # Extra exploration and stopping controls (optional)
        Config.mutation_rate        = _floatenv("GGNES_DEMO_MUTATION_RATE", Config.mutation_rate)
        Config.crossover_rate       = _floatenv("GGNES_DEMO_CROSSOVER_RATE", Config.crossover_rate)
        Config.stagnation_patience  = _intenv("GGNES_DEMO_STAGNATION", Config.stagnation_patience)
        Config.immigrants_fraction  = _floatenv("GGNES_DEMO_IMM_FRAC", Config.immigrants_fraction)
        Config.immigrant_interval   = _intenv("GGNES_DEMO_IMM_INTERVAL", getattr(Config, "immigrant_interval", 0))
        dc = _intenv("GGNES_DEMO_DISABLE_CONV", 0)
        Config.disable_convergence  = bool(dc)


def parse_args() -> argparse.Namespace:
    """Parse optional CLI arguments for convenience and reproducibility."""
    p = argparse.ArgumentParser(description="GGNES NAS Demo (California Housing)")
    p.add_argument("--pop", type=int, default=None, help="Population size")
    p.add_argument("--gen", type=int, default=None, help="Number of generations")
    p.add_argument("--init-epochs", type=int, default=None, help="Initial training epochs per candidate")
    p.add_argument("--final-epochs", type=int, default=None, help="Final training epochs")
    p.add_argument("--max-iters", type=int, default=None, help="Max grammar iterations during generation")
    p.add_argument("--eval-workers", type=int, default=None, help="Parallel workers during evaluation")
    p.add_argument("--results-dir", type=str, default=None, help="Output directory for artifacts")
    p.add_argument("--smoke", action="store_true", help="Run with tiny, fast settings for a quick end-to-end check")
    return p.parse_args()


def apply_cli_overrides(args: argparse.Namespace) -> None:
    """Apply CLI overrides to Config if provided."""
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
        # Treat 0 as "auto" (None). Negative also maps to auto.
        try:
            _w = int(args.eval_workers)
        except Exception:
            _w = None
        Config.eval_workers = None if (_w is None or _w <= 0) else _w
    if args.results_dir is not None:
        Config.results_dir = str(args.results_dir)
    # --smoke: tiny, fast settings for immediate progress
    if getattr(args, "smoke", False):
        Config.population_size = 2
        Config.generations = 1
        Config.initial_epochs = 1
        Config.final_epochs = 1
        Config.max_iterations = max(1, min(Config.max_iterations, 3))
        Config.max_network_size = min(Config.max_network_size, 50)
        # Prefer a single worker for predictable progress on CPU
        Config.eval_workers = 1 if torch.cuda.is_available() else 1


def ensure_results_dir() -> str:
    """Prepare results directory by cleaning known files from prior runs."""
    out_dir = Config.results_dir
    os.makedirs(out_dir, exist_ok=True)
    for name in [
        'evolution_history.json',
        'pareto_front_summary.json',
        'generation_metrics.json',
        'config.json',
        'best_metrics.json',
        'best_genotype.json',
        'best_graph_edges.json',
        'evolution_progress.png',
        'test_predictions.png',
        'run_report.txt',
        'evolution_checkpoint.pkl',
        'retrain_metrics.json',
    ]:
        try:
            path = os.path.join(out_dir, name)
            if os.path.exists(path):
                os.remove(path)
        except Exception:
            pass
    return out_dir


def load_data() -> Tuple[Tuple[torch.Tensor, torch.Tensor],
                         Tuple[torch.Tensor, torch.Tensor],
                         Tuple[torch.Tensor, torch.Tensor]]:
    """Load and preprocess the California Housing dataset.

    Returns
    - (X_train, y_train), (X_val, y_val), (X_test, y_test) ready for PyTorch
    """
    print("Loading California Housing dataset...")
    data = fetch_california_housing()
    X, y = data.data, data.target

    X_temp, X_test, y_temp, y_test = train_test_split(
        X, y, test_size=Config.test_size, random_state=Config.random_state
    )
    X_train, X_val, y_train, y_val = train_test_split(
        X_temp, y_temp, test_size=Config.val_size, random_state=Config.random_state
    )

    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_val = scaler.transform(X_val)
    X_test = scaler.transform(X_test)

    X_train = torch.FloatTensor(X_train).to(DEVICE)
    y_train = torch.FloatTensor(y_train).unsqueeze(1).to(DEVICE)
    X_val = torch.FloatTensor(X_val).to(DEVICE)
    y_val = torch.FloatTensor(y_val).unsqueeze(1).to(DEVICE)
    X_test = torch.FloatTensor(X_test).to(DEVICE)
    y_test = torch.FloatTensor(y_test).unsqueeze(1).to(DEVICE)

    print(f"  Training samples: {len(X_train)}")
    print(f"  Validation samples: {len(X_val)}")
    print(f"  Test samples: {len(X_test)}")
    print(f"  Features: {X_train.shape[1]}")
    return (X_train, y_train), (X_val, y_val), (X_test, y_test)


def create_axiom_graph(input_size: int = 8) -> Graph:
    """Create the initial graph (axiom) with INPUT, HIDDEN, OUTPUT nodes."""
    graph = Graph()
    graph.add_node({
        "id": "input",
        "node_type": NodeType.INPUT,
        "activation_function": "linear",
        "output_size": input_size
    })
    graph.add_node({
        "id": "hidden1",
        "node_type": NodeType.HIDDEN,
        "activation_function": "relu",
        "output_size": 32
    })
    graph.add_node({
        "id": "output",
        "node_type": NodeType.OUTPUT,
        "activation_function": "linear",
        "output_size": 1
    })
    graph.add_edge("input", "hidden1")
    graph.add_edge("hidden1", "output")
    return graph


def create_grammar_rules() -> List[Rule]:
    """Create a rule library for a dense/attention-rich search space.

    Notes
    - You can replace this with domain-specific rules (e.g., conv blocks).
    - Each Rule uses a LHSPattern and RHSAction to add/modify nodes/edges.
    """
    rules: List[Rule] = []

    # Dense layer insertion after HIDDEN node
    for size in Config.layer_sizes:
        for activation in Config.activations:
            emb = EmbeddingLogic()
            try:
                emb.boundary_handling = 'IGNORE'
            except Exception:
                pass
            rule = Rule(
                name=f"add_dense_{size}_{activation}",
                pattern=LHSPattern(
                    nodes=[{"label": "A", "match_criteria": {"node_type": NodeType.HIDDEN}}],
                    edges=[],
                    boundary_nodes=["A"]
                ),
                action=RHSAction(
                    add_nodes=[{
                        "label": "NEW",
                        "properties": {
                            "node_type": NodeType.HIDDEN,
                            "activation_function": activation,
                            "attributes": {"output_size": size}
                        }
                    }],
                    add_edges=[{"source_label": "A", "target_label": "NEW"}]
                ),
                application_probability=0.8,
                embedding=emb
            )
            rules.append(rule)

    # Skip connection rule
    emb_skip = EmbeddingLogic()
    try:
        emb_skip.boundary_handling = 'IGNORE'
    except Exception:
        pass
    skip_rule = Rule(
        name="add_skip_connection",
        pattern=LHSPattern(
            nodes=[
                {"label": "A", "match_criteria": {"node_type": NodeType.HIDDEN}},
                {"label": "B", "match_criteria": {"node_type": NodeType.HIDDEN}},
                {"label": "C", "match_criteria": {}}
            ],
            edges=[
                {"source_label": "A", "target_label": "B"},
                {"source_label": "B", "target_label": "C"}
            ],
            boundary_nodes=["A", "B", "C"]
        ),
        action=RHSAction(add_edges=[{"source_label": "A", "target_label": "C"}]),
        application_probability=0.3,
        embedding=emb_skip
    )
    rules.append(skip_rule)

    # Aggregation nodes (attention, MoE, concat, etc.)
    for aggregation in Config.aggregations:
        for activation in Config.activations:
            emb_attn = EmbeddingLogic()
            try:
                emb_attn.boundary_handling = 'IGNORE'
            except Exception:
                pass
            rule = Rule(
                name=f"add_{aggregation}_{activation}",
                pattern=LHSPattern(
                    nodes=[
                        {"label": "A", "match_criteria": {"node_type": NodeType.HIDDEN}},
                        {"label": "B", "match_criteria": {"node_type": NodeType.HIDDEN}}
                    ],
                    edges=[],
                    boundary_nodes=["A", "B"]
                ),
                action=RHSAction(
                    add_nodes=[{
                        "label": "AGG",
                        "properties": {
                            "node_type": NodeType.HIDDEN,
                            "activation_function": activation,
                            "attributes": {"output_size": 128, "aggregation_function": aggregation}
                        }
                    }],
                    add_edges=[{"source_label": "A", "target_label": "AGG"},
                               {"source_label": "B", "target_label": "AGG"}]
                ),
                application_probability=0.4,
                embedding=emb_attn
            )
            rules.append(rule)

    # Grow small hidden layers to 64
    emb_grow = EmbeddingLogic()
    try:
        emb_grow.boundary_handling = 'IGNORE'
    except Exception:
        pass
    growth_rule = Rule(
        name="grow_layer",
        pattern=LHSPattern(
            nodes=[{"label": "SMALL",
                    "match_criteria": {"node_type": NodeType.HIDDEN, "output_size": lambda s: s < 64}}],
            edges=[],
            boundary_nodes=[]
        ),
        action=RHSAction(modify_nodes=[{"label": "SMALL", "new_properties": {"attributes": {"output_size": 128}}}]),
        application_probability=0.5,
        embedding=emb_grow
    )
    rules.append(growth_rule)

    return rules


def create_genotype(num_rules: int = 5) -> Genotype:
    """Create a genotype from the rule library.

    Strategy
    - If use_all_combinations=True, do systematic coverage of rule names plus extras
      up to max_rules. Otherwise, sample a subset of rules randomly.

    Tip
    - For your use case, replace with your own curated rule selection strategy.
    """
    all_rules = create_grammar_rules()
    if getattr(Config, 'use_all_combinations', False):
        systematic: List[Rule] = []
        seen = set()
        for r in all_rules:
            key = getattr(r, 'name', None)
            if key and key not in seen:
                systematic.append(r)
                seen.add(key)
        target_size = min(len(all_rules), max(len(systematic), getattr(Config, 'max_rules', 50)))
        extras_needed = max(0, target_size - len(systematic))
        extra_idx = np.random.choice(len(all_rules), extras_needed, replace=False)
        selected_rules = systematic + [all_rules[i] for i in extra_idx if all_rules[i] not in systematic]
        selected_rules = selected_rules[:getattr(Config, 'max_rules', len(selected_rules))]
    else:
        selected_indices = np.random.choice(len(all_rules), min(num_rules, len(all_rules)), replace=False)
        selected_rules = [all_rules[i] for i in selected_indices]
    return Genotype(rules=selected_rules)


def train_model(model: nn.Module,
                train_data: Tuple[torch.Tensor, torch.Tensor],
                val_data: Tuple[torch.Tensor, torch.Tensor],
                epochs: int = 10,
                verbose: bool = False) -> Tuple[List[float], List[float]]:
    """Train provided torch.nn.Module and return loss curves."""
    X_train, y_train = train_data
    X_val, y_val = val_data

    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=Config.learning_rate)
    train_losses, val_losses = [], []

    for epoch in range(epochs):
        # Train step
        model.train()
        optimizer.zero_grad()
        outputs = model(X_train)
        loss = criterion(outputs, y_train)
        loss.backward()
        optimizer.step()
        train_losses.append(loss.item())

        # Validation step
        model.eval()
        with torch.no_grad():
            val_outputs = model(X_val)
            val_loss = criterion(val_outputs, y_val)
            val_losses.append(val_loss.item())

        if verbose and epoch % 5 == 0:
            print(f"    Epoch {epoch}: Train Loss = {loss.item():.4f}, Val Loss = {val_loss.item():.4f}")

    return train_losses, val_losses


def _seed_for(genotype: Any, base: int = 42) -> int:
    """Derive a deterministic seed for a genotype (reproducible evaluations)."""
    gid = getattr(genotype, 'genotype_id', None) or getattr(genotype, 'id', None)
    try:
        key = int(str(gid).replace('-', '')[:8], 16)
    except Exception:
        key = 0
    return base + (key % (2**31 - 1))


def evaluate_genotype(genotype: Genotype,
                      train_data: Tuple[torch.Tensor, torch.Tensor],
                      val_data: Tuple[torch.Tensor, torch.Tensor]) -> Tuple[float, int, Dict[str, Any]]:
    """Evaluate a single genotype by generating a network and brief training."""
    try:
        # Heartbeat: surface that evaluation started (minimal noise at small pop sizes)
        try:
            _gid = getattr(genotype, 'genotype_id', None) or getattr(genotype, 'id', None)
            print(f"[eval] start genotype={_gid}")
        except Exception:
            pass
        axiom = create_axiom_graph(input_size=8)
        rng = RNGManager(seed=_seed_for(genotype))
        # Configure generation (parallel rule application)
        parallel_workers = max(1, min((os.cpu_count() or 2), 8))
        config = {
            'max_iterations': Config.max_iterations,
            'parallel_execution': True,
            'max_parallel_workers': parallel_workers,
            'parallel_batch_policy': 'FIXED_SIZE',
            'parallel_fixed_size': 2,
            'parallel_conflict_strategy': 'SKIP'
        }
        network, info = generate_network_from_genotype(
            genotype=genotype,
            axiom_graph=axiom,
            config=config,
            rng_manager=rng
        )

        # Size constraint
        if len(network.nodes) > Config.max_network_size:
            return float('inf'), 0, {}

        # Prune to contributing subgraph, then translate and do quick training
        try:
            from ggnes.api.mvp import prune_graph_contributing as _prune
            network = _prune(network)
        except Exception:
            pass
        model = to_pytorch_model(network).to(DEVICE)
        num_params = sum(p.numel() for p in model.parameters())
        _, val_losses = train_model(model, train_data, val_data, epochs=Config.initial_epochs, verbose=False)
        final_val_loss = float(val_losses[-1])
        try:
            print(f"[eval] done genotype={_gid} val_loss={final_val_loss:.4f} params={num_params}")
        except Exception:
            pass
        return final_val_loss, num_params, info
    except Exception as e:
        # Robust to rule conflicts or translation hiccups in demo setting
        return float('inf'), 0, {}


def evolve_architectures(train_data, val_data) -> Tuple[Genotype, List[Dict[str, Any]]]:
    """Run NSGA-II evolution and return (best_genotype, history).

    - Objectives: minimize val_loss and parameter count (converted to maximization by negation)
    - Constraints: DAG topology, max network size
    - History: best/mean metrics, diversity, persisted Pareto summaries per generation
    """
    print("\nStarting architecture evolution (NSGA-II)...")

    # Initialize population of genotypes
    current_pop: List[Genotype] = []
    for _ in range(Config.population_size):
        num_rules = np.random.randint(3, Config.initial_rules + 1)
        current_pop.append(create_genotype(num_rules))

    def objectives(genotype: Genotype) -> Dict[str, float]:
        val_loss, params, _ = evaluate_genotype(genotype, train_data, val_data)
        return {"neg_val_loss": -val_loss, "neg_params": -float(params)}

    def constraints(genotype: Genotype) -> Dict[str, bool]:
        """Try generating a small graph to check constraints quickly."""
        try:
            axiom = create_axiom_graph(input_size=8)
            rng = RNGManager(seed=42)
            config = {'max_iterations': max(3, Config.max_iterations // 2)}
            net, _ = generate_network_from_genotype(axiom_graph=axiom, genotype=genotype, config=config, rng_manager=rng)
            # DAG and size
            is_dag = True
            try:
                net.topological_sort()
            except Exception:
                is_dag = False
            within_size = len(net.nodes) <= Config.max_network_size
            return {"is_dag": is_dag, "within_size": within_size}
        except Exception:
            return {"is_dag": False, "within_size": False}

    history: List[Dict[str, Any]] = []
    best: Genotype | None = None
    best_val = float('inf')
    stagnant_generations = 0
    prev_best = None

    # Evaluate-evolve loop
    for gen in range(Config.generations):
        print(f"\nGeneration {gen + 1}/{Config.generations}")

        # Parallel evaluation of current population
        vals, sizes, iter_counts = [], [], []
        cfg_workers = Config.eval_workers
        if cfg_workers is None:
            max_workers = 1 if torch.cuda.is_available() else max(2, min(4, Config.population_size))
        else:
            max_workers = int(cfg_workers)

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_to_idx = {executor.submit(evaluate_genotype, g, train_data, val_data): i
                             for i, g in enumerate(current_pop)}
            for fut in tqdm(as_completed(future_to_idx), total=len(future_to_idx), desc="Evaluating"):
                try:
                    v, p, info = fut.result()
                except Exception:
                    v, p, info = float('inf'), 0, {}
                i = future_to_idx.get(fut, None)
                vals.append(v)
                sizes.append(p)
                if isinstance(info, dict):
                    iter_counts.append(info.get('iterations', None))
                if v < best_val and i is not None and 0 <= i < len(current_pop):
                    best_val = v
                    best = current_pop[i]

        # Aggregate per-generation metrics for plotting/reporting
        mean_v = float(np.nanmean([x for x in vals if x != float('inf')])) if vals else float('inf')
        mean_p = float(np.nanmean([x for x in sizes if x > 0])) if sizes else 0.0
        mean_iters = float(np.nanmean([x for x in iter_counts if isinstance(x, (int, float))])) if iter_counts else 0.0
        history.append({
            "generation": gen,
            "best_fitness": best_val,
            "mean_fitness": mean_v,
            "mean_complexity": mean_p,
            "mean_rule_applications": mean_iters
        })
        print(f"  Best fitness: {best_val:.4f}")
        print(f"  Mean fitness: {mean_v:.4f}")
        print(f"  Mean complexity: {int(mean_p)} params")
        if mean_iters:
            print(f"  Mean rule applications: {int(mean_iters)}")

        # Diversity and stagnation checks
        diversity = calculate_diversity(current_pop)
        history[-1]["diversity"] = diversity

        if prev_best is None or best_val >= prev_best:
            stagnant_generations += 1
        else:
            stagnant_generations = 0
        prev_best = best_val

        if stagnant_generations >= Config.stagnation_patience:
            # Inject immigrants to escape stagnation
            num_immigrants = max(1, int(Config.immigrants_fraction * Config.population_size))
            print(f"  Injecting {num_immigrants} immigrant genotypes to escape stagnation...")
            immigrants = [create_genotype(np.random.randint(3, Config.initial_rules + 1))
                          for _ in range(num_immigrants)]
            ranks = np.argsort(vals)  # lower is better
            worst_indices = ranks[-num_immigrants:]
            for idx, immigrant in zip(worst_indices, immigrants):
                current_pop[idx] = immigrant
            stagnant_generations = 0

        # NSGA-II selection (persisted objectives)
        solutions = nsga2_evolve(
            current_pop,
            objectives=objectives,
            generations=1,
            population_size=Config.population_size,
            mutation_rate=Config.mutation_rate,
            crossover_rate=Config.crossover_rate,
            constraints=constraints,
            return_solutions=True
        )
        current_pop = [s.genotype for s in solutions]
        pareto_summary = [
            {"rank": int(getattr(s, "rank", 0)),
             "crowding": float(getattr(s, "crowding_distance", 0.0)),
             "objectives": dict(getattr(s, "objectives", {}))}
            for s in solutions
        ]
        history[-1]["pareto_summary"] = pareto_summary

        # Top up population if NSGA-II front returned fewer individuals
        while len(current_pop) < Config.population_size:
            clone = best.clone() if best else create_genotype(np.random.randint(3, Config.initial_rules + 1))
            try:
                clone = mutate(clone)
            except Exception:
                pass
            current_pop.append(clone)

        # Checkpoint (pickle-safe, lightweight population)
        try:
            pop_light = []
            for g in current_pop:
                if hasattr(g, "to_dict"):
                    pop_light.append(g.to_dict())
                else:
                    pop_light.append({"id": str(getattr(g, "id", ""))})
            EvolutionCheckpoint(checkpoint_dir=Config.results_dir).save(
                population=pop_light, generation=gen, best_fitness=best_val, metadata={"diversity": diversity}
            )
        except Exception:
            pass

        # Periodic immigration to maintain diversity (optional)
        try:
            interval = int(getattr(Config, "immigrant_interval", 0) or 0)
            if interval and (gen + 1) % interval == 0:
                num_imm = max(1, int(getattr(Config, "immigrants_fraction", 0.0) * Config.population_size))
                immigrants = [create_genotype(np.random.randint(3, Config.initial_rules + 1)) for _ in range(num_imm)]
                ranks = np.argsort(vals)  # lower is better
                worst_indices = ranks[-num_imm:]
                for idx, immigrant in zip(worst_indices, immigrants):
                    current_pop[idx] = immigrant
                print(f"  Periodic immigrants injected: {num_imm}")
        except Exception:
            pass

        # Early convergence detection (optional and can be disabled)
        if not getattr(Config, "disable_convergence", False):
            try:
                detector = globals().get("_GGNES_DETECTOR", None)
                if detector is None:
                    detector = ConvergenceDetector(window_size=10, threshold=0.01)
                    globals()["_GGNES_DETECTOR"] = detector
                if detector.check_convergence([h.get("best_fitness", float('inf')) for h in history]):
                    print("Convergence detected; stopping evolution early.")
                    break
            except Exception:
                pass

    return best, history


def evaluate_best_model(best_genotype: Genotype,
                        train_data, val_data, test_data,
                        out_dir: str | None = None) -> Tuple[nn.Module, float, float]:
    """Generate network from best genotype, train thoroughly, and test."""
    print("\nEvaluating best model...")
    axiom = create_axiom_graph(input_size=8)
    rng = RNGManager(seed=42)
    config = {'max_iterations': Config.max_iterations}

    # Generate network directly from genotype
    network, info = generate_network_from_genotype(
        genotype=best_genotype, axiom_graph=axiom, config=config, rng_manager=rng
    )

    # Alternative grammar-only path to demonstrate apply_grammar (optional)
    try:
        tiny_grammar = create_grammar_rules()[:3]
        network_grammar = apply_grammar(axiom, tiny_grammar, max_iterations=3)
        if len(getattr(network_grammar, 'nodes', {})) > len(getattr(network, 'nodes', {})):
            network = network_grammar
    except Exception:
        pass

    print(f"  Network size: {len(network.nodes)} nodes")
    # Prune before final translation/export
    try:
        from ggnes.api.mvp import prune_graph_contributing as _prune
        pruned = _prune(network)
    except Exception:
        pruned = network
    model = to_pytorch_model(pruned).to(DEVICE)
    num_params = sum(p.numel() for p in model.parameters())
    print(f"  Model parameters: {num_params}")

    print("  Training final model...")
    train_losses, val_losses = train_model(model, train_data, val_data, epochs=Config.final_epochs, verbose=True)

    # Test evaluation
    X_test, y_test = test_data
    model.eval()
    with torch.no_grad():
        predictions = model(X_test)
        test_mse = mean_squared_error(y_test.cpu(), predictions.cpu())
        test_r2 = r2_score(y_test.cpu(), predictions.cpu())

    print(f"\nFinal Test Results:\n  Test MSE: {test_mse:.4f}\n  Test R2 Score: {test_r2:.4f}")

    # Visualization removed: predictions plot omitted

    # Persist artifacts for reuse
    try:
        import json
        if out_dir:
            try:
                genod = best_genotype.to_dict() if hasattr(best_genotype, 'to_dict') else {}
            except Exception:
                genod = {}
            with open(os.path.join(out_dir, 'best_genotype.json'), 'w') as f:
                json.dump(genod, f, indent=2)

            edges = []
            try:
                for e in network.list_edges():
                    src = getattr(e, 'src_id', getattr(e, 'source_node_id', None))
                    dst = getattr(e, 'dst_id', getattr(e, 'target_node_id', None))
                    edges.append([str(src), str(dst)])
            except Exception:
                pass
            with open(os.path.join(out_dir, 'best_graph_edges.json'), 'w') as f:
                json.dump(edges, f, indent=2)

            def _arch(graph: Graph):
                nodes = []
                for nid, node in getattr(graph, 'nodes', {}).items():
                    nodes.append({
                        'id': str(nid),
                        'node_type': str(getattr(node, 'node_type', '')),
                        'activation_function': getattr(node, 'activation_function', None),
                        'output_size': (node.attributes.get('output_size')
                                        if hasattr(node, 'attributes') and isinstance(node.attributes, dict) else None)
                    })
                es = []
                try:
                    e_pairs = []
                    for e in graph.list_edges():
                        src = getattr(e, 'src_id', getattr(e, 'source_node_id', None))
                        dst = getattr(e, 'dst_id', getattr(e, 'target_node_id', None))
                        if src is None or dst is None:
                            continue
                        e_pairs.append((str(src), str(dst)))
                    es = [[s, d] for s, d in sorted(e_pairs)]
                except Exception:
                    es = edges
                return {'nodes': nodes, 'edges': es}

            raw_arch = _arch(network)
            pruned_arch = _arch(pruned)
            # Default export is pruned, keep raw for audit
            with open(os.path.join(out_dir, 'best_architecture.json'), 'w') as f:
                json.dump(pruned_arch, f, indent=2)
            with open(os.path.join(out_dir, 'best_architecture_raw.json'), 'w') as f:
                json.dump(raw_arch, f, indent=2)
    except Exception:
        pass

    return model, float(test_mse), float(test_r2)


def write_reports(history: List[Dict[str, Any]], out_dir: str) -> None:
    """Write JSON artifacts and a human-readable run report."""
    import json

    # Evolution history (per generation), Pareto summary replication for investor deck
    with open(os.path.join(out_dir, "evolution_history.json"), "w") as f:
        json.dump(history, f, indent=2)
    with open(os.path.join(out_dir, "pareto_front_summary.json"), "w") as f:
        json.dump(history, f, indent=2)

    # Config and generation metrics (timeseries)
    cfg = {
        'population_size': Config.population_size,
        'generations': Config.generations,
        'mutation_rate': Config.mutation_rate,
        'crossover_rate': Config.crossover_rate,
        'eval_workers': Config.eval_workers,
        'max_iterations': Config.max_iterations,
        'max_network_size': Config.max_network_size,
        'layer_sizes': Config.layer_sizes,
        'activations': Config.activations,
        'aggregations': Config.aggregations,
        'rule_preset': getattr(Config, 'rule_preset', 'dense_attention'),
        'random_state': Config.random_state,
        # Exploration/stop toggles
        'disable_convergence': getattr(Config, 'disable_convergence', False),
        'immigrant_interval': getattr(Config, 'immigrant_interval', 0),
        'immigrants_fraction': getattr(Config, 'immigrants_fraction', 0.0),
        # Device snapshot
        'device': str(DEVICE),
    }
    metrics = {
        'num_generations': len(history),
        'best_fitness_over_time': [h.get('best_fitness') for h in history],
        'mean_fitness_over_time': [h.get('mean_fitness') for h in history],
        'mean_complexity_over_time': [h.get('mean_complexity') for h in history]
    }
    with open(os.path.join(out_dir, "config.json"), "w") as f:
        json.dump(cfg, f, indent=2)
    with open(os.path.join(out_dir, "generation_metrics.json"), "w") as f:
        json.dump(metrics, f, indent=2)

    # Reproducibility manifest and environment snapshot
    try:
        import sys, platform, subprocess, time
        import torch as _torch
        import numpy as _np
        try:
            import sklearn as _skl
        except Exception:
            _skl = None
        try:
            import matplotlib as _mpl
        except Exception:
            _mpl = None
        try:
            import tqdm as _tqdm
        except Exception:
            _tqdm = None

        # Capture relevant env overrides
        env_overrides = {k: os.environ.get(k) for k in sorted(os.environ.keys()) if k.startswith("GGNES_DEMO_")}

        # Git commit (if repo)
        git_commit = None
        try:
            proc = subprocess.run(["git", "rev-parse", "HEAD"], cwd=PROJECT_ROOT, capture_output=True, text=True)
            if proc.returncode == 0:
                git_commit = proc.stdout.strip()
        except Exception:
            pass

        manifest = {
            'timestamp': time.time(),
            'python': sys.version,
            'platform': {
                'system': platform.system(),
                'release': platform.release(),
                'machine': platform.machine(),
                'python_implementation': platform.python_implementation(),
            },
            'package_versions': {
                'torch': getattr(_torch, "__version__", None),
                'numpy': getattr(_np, "__version__", None),
                'sklearn': getattr(_skl, "__version__", None) if _skl else None,
                'matplotlib': getattr(_mpl, "__version__", None) if _mpl else None,
                'tqdm': getattr(_tqdm, "__version__", None) if _tqdm else None,
            },
            'git_commit': git_commit,
            'cmdline': sys.argv,
            'env_overrides': env_overrides,
            'config': cfg,
        }
        with open(os.path.join(out_dir, "repro_manifest.json"), "w") as f:
            json.dump(manifest, f, indent=2)

        # Freeze exact environment for bitwise repro (optional)
        try:
            pf = subprocess.run([sys.executable, "-m", "pip", "freeze"], capture_output=True, text=True)
            if pf.returncode == 0:
                with open(os.path.join(out_dir, "pip_freeze.txt"), "w") as pfw:
                    pfw.write(pf.stdout)
        except Exception:
            pass
    except Exception:
        pass


def write_run_report(out_dir: str, model: nn.Module, test_mse: float, test_r2: float) -> None:
    """Write a concise text report of environment, config, and results."""
    report_path = os.path.join(out_dir, 'run_report.txt')
    with open(report_path, 'w') as rf:
        rf.write("GGNES California Housing Demo - Run Report\n")
        rf.write("=" * 72 + "\n\n")
        rf.write("Environment\n")
        rf.write(f"  Device: {DEVICE}\n")
        if torch.cuda.is_available():
            rf.write(f"  GPU: {torch.cuda.get_device_name(0)}\n")
        rf.write("\nConfig\n")
        rf.write(f"  population_size: {Config.population_size}\n")
        rf.write(f"  generations: {Config.generations}\n")
        rf.write(f"  mutation_rate: {Config.mutation_rate}\n")
        rf.write(f"  crossover_rate: {Config.crossover_rate}\n")
        rf.write(f"  eval_workers: {Config.eval_workers}\n")
        rf.write(f"  max_iterations: {Config.max_iterations}\n")
        rf.write(f"  max_network_size: {Config.max_network_size}\n")
        rf.write(f"  layer_sizes: {Config.layer_sizes}\n")
        rf.write(f"  activations: {Config.activations}\n")
        rf.write(f"  aggregations: {Config.aggregations}\n")
        rf.write(f"  use_all_combinations: {Config.use_all_combinations}\n")
        rf.write(f"  disable_convergence: {getattr(Config, 'disable_convergence', False)}\n")
        rf.write(f"  immigrant_interval: {getattr(Config, 'immigrant_interval', 0)}\n")
        rf.write(f"  immigrants_fraction: {getattr(Config, 'immigrants_fraction', 0.0)}\n\n")
        rf.write("Performance\n")
        rf.write(f"  Test MSE: {float(test_mse):.6f}\n")
        rf.write(f"  Test R2: {float(test_r2):.6f}\n")
        rf.write("\nThis report was auto-generated by the demo script.\n")


def main() -> None:
    """End-to-end demo execution."""
    # Configure logging: suppress engine internals; show our INFO prints only
    try:
        logging.getLogger().setLevel(logging.CRITICAL)
    except Exception:
        pass

    # Apply overrides (ENV first, then CLI for explicit precedence)
    Config.apply_env_overrides()
    args = parse_args()
    apply_cli_overrides(args)
    print(f"[Demo Controls] eval_workers={Config.eval_workers} | batch_size={Config.batch_size} | init_epochs={Config.initial_epochs} | final_epochs={Config.final_epochs}")

    print("=" * 80)
    print("GGNES Neural Architecture Search - California Housing")
    print("Using Fixed and Improved API")
    print("=" * 80)

    out_dir = ensure_results_dir()
    print(f"Artifacts will be saved under: {os.path.abspath(out_dir)}")

    # Seed and prepare data
    np.random.seed(Config.random_state)
    torch.manual_seed(Config.random_state)
    train_data, val_data, test_data = load_data()

    # Register a custom aggregation to demonstrate extensibility
    @register_aggregation("custom_topk")
    def custom_topk(inputs, **kwargs):
        from ggnes.aggregations import topk_weighted_sum_aggregation
        return topk_weighted_sum_aggregation(inputs, top_k=2, temperature=0.7)

    # Evolve architectures
    best_genotype, history = evolve_architectures(train_data, val_data)

    # Persist evolution artifacts (visualization removed)
    write_reports(history, out_dir)

    # Evaluate and persist best model artifacts
    if best_genotype:
        model, test_mse, test_r2 = evaluate_best_model(best_genotype, train_data, val_data, test_data, out_dir)
        print("\n" + "=" * 80)
        print("Evolution Complete!")
        print(f"Best Test MSE: {test_mse:.4f}")
        print(f"Best Test R2: {test_r2:.4f}")
        print("=" * 80)

        # Final metrics and report
        try:
            import json
            with open(os.path.join(out_dir, "best_metrics.json"), "w") as f:
                json.dump({"test_mse": float(test_mse), "test_r2": float(test_r2)}, f, indent=2)
        except Exception:
            pass
        write_run_report(out_dir, model, test_mse, test_r2)

        # Optional: retrain exported architecture for a longer pass (portfolio-quality curves)
        if getattr(Config, 'retrain_exported', False):
            try:
                import json
                arch_path = os.path.join(out_dir, 'best_architecture.json')
                if os.path.exists(arch_path):
                    with open(arch_path) as f:
                        arch = json.load(f)

                    # Rebuild Graph from exported spec (shows how to reuse an exported architecture)
                    rebuilt = Graph()
                    id_map: Dict[str, Any] = {}
                    for n in arch.get('nodes', []):
                        props = {
                            'id': n['id'],
                            'node_type': getattr(NodeType, str(n['node_type']).split('.')[-1], NodeType.HIDDEN),
                            'activation_function': n.get('activation_function') or 'relu'
                        }
                        if n.get('output_size') is not None:
                            props['output_size'] = n['output_size']
                        rid = rebuilt.add_node(props)
                        id_map[n['id']] = rid
                    for src, dst in arch.get('edges', []):
                        s = id_map.get(str(src), src)
                        d = id_map.get(str(dst), dst)
                        try:
                            rebuilt.add_edge(s, d)
                        except Exception:
                            pass

                    retrain_model = to_pytorch_model(rebuilt).to(DEVICE)
                    print("\nRetraining exported architecture...")
                    train_model(retrain_model, train_data, val_data, epochs=Config.retrain_epochs, verbose=True)
                    retrain_model.eval()
                    X_test, y_test = test_data
                    with torch.no_grad():
                        preds = retrain_model(X_test)
                        retrain_mse = mean_squared_error(y_test.cpu(), preds.cpu())
                        retrain_r2 = r2_score(y_test.cpu(), preds.cpu())
                    print(f"Retrained Test MSE: {retrain_mse:.4f} | R2: {retrain_r2:.4f}")
                    with open(os.path.join(out_dir, 'retrain_metrics.json'), 'w') as f:
                        json.dump({'test_mse': float(retrain_mse), 'test_r2': float(retrain_r2)}, f, indent=2)
            except Exception:
                # Demo-first: ignore retraining errors while keeping the rest intact
                pass
    else:
        print("No valid architecture found!")


if __name__ == "__main__":
    main()
