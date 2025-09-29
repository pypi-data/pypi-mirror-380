#!/usr/bin/env python3
"""
================================================================================
GGNES Neural Architecture Search Demo (MNIST) - Classification
================================================================================

What this is
- A classification demo using MNIST-like data (28x28 grayscale digits, 10 classes).
- Uses the same grammar/evolution pipeline structure as the California Housing demos,
  adapted for classification (cross-entropy) and accuracy metrics.

Quickstart (no GGNES knowledge required)
1) Create a Python virtualenv:
   - python3 -m venv .venv && .venv/bin/python -m pip install --upgrade pip
   - .venv/bin/pip install -r requirements.txt
   - For GPU, follow README GPU notes to install CUDA wheels first.

2) Run a small sanity test (subsampled MNIST, quick):
   - .venv/bin/python -u demo/mnist_demo.py --pop 8 --gen 1
   - You should see per-generation progress, then final Test Accuracy.

3) Full(er) run (still bounded):
   - .venv/bin/python -u demo/mnist_demo.py --pop 100 --gen 10

Notes
- If torchvision MNIST download is unavailable (no internet), the script falls back to sklearn.digits (8x8),
  upscales to 28x28-equivalent flattened vectors (padding), and proceeds. It will print a warning.
- Classification: output layer is size=10; training uses CrossEntropyLoss; selection optimizes val_error=1-accuracy.

Controls you might tweak (ENV)
- GGNES_DEMO_POP, GGNES_DEMO_GEN: population size, generations
- GGNES_DEMO_INIT_EPOCHS, GGNES_DEMO_FINAL_EPOCHS: epochs per candidate and final model
- GGNES_DEMO_MAX_ITERS: grammar generation iterations
- GGNES_DEMO_EVAL_WORKERS: parallel evaluations on CPU
- GGNES_MNIST_TRAIN_MAX / VAL_MAX / TEST_MAX: subsample caps (default small for speed)
- GGNES_DEMO_MAX_NET_SIZE: allow larger graphs (nodes), e.g. 1000

================================================================================
"""

import os
import sys
import time
import json
import logging
import warnings
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Any, Dict, List, Tuple

import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Suppress non-critical warnings
warnings.filterwarnings('ignore')

# Ensure local project imports are visible
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_ROOT)

# GGNES imports
from ggnes import (
    Graph, NodeType,
    Rule, LHSPattern, RHSAction, EmbeddingLogic,
    Genotype,
    mutate, nsga2_evolve,
    apply_grammar,
    to_pytorch_model,
    register_aggregation
)
from ggnes.generation.network_gen import generate_network as generate_network_from_genotype
from ggnes.evolution.metrics import ConvergenceDetector, calculate_diversity
from ggnes.evolution.checkpointing import EvolutionCheckpoint
from ggnes.utils.rng_manager import RNGManager

DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(f"Using device: {DEVICE}")

class Config:
    """Central configuration for MNIST demo."""
    # Data subsampling caps (defaults chosen for quick sanity runs)
    mnist_train_max = int(os.getenv("GGNES_MNIST_TRAIN_MAX", "8000"))
    mnist_val_max   = int(os.getenv("GGNES_MNIST_VAL_MAX", "2000"))
    mnist_test_max  = int(os.getenv("GGNES_MNIST_TEST_MAX", "2000"))

    random_state = 42

    # Training
    initial_epochs = 3
    final_epochs = 10
    batch_size = 128
    learning_rate = 1e-3

    # Parallel evaluation
    eval_workers = None  # None->auto

    # Evolution
    population_size = 80
    generations = 10
    mutation_rate = 0.3
    crossover_rate = 0.7

    # Grammar presets
    rule_preset = 'dense_attention'
    use_all_combinations = True

    # Outputs
    results_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'mnist_demo_output')
    use_timestamp = False

    # Grammar generation constraints
    initial_rules = 5
    max_rules = 2000
    max_network_size = int(os.getenv("GGNES_DEMO_MAX_NET_SIZE", "200"))
    max_iterations = 30

    # Search space params (wider layers; aggregation nodes larger by default)
    layer_sizes = [32, 64, 128, 256]
    activations = ['relu', 'leaky_relu', 'elu', 'gelu', 'tanh', 'sigmoid', 'selu', 'silu', 'softplus', 'softsign']
    aggregations = [
        'sum', 'mean', 'max', 'concat',
        'attention', 'multi_head_attention', 'attn_pool',
        'moe', 'gated_sum', 'topk_weighted_sum', 'matrix_product'
    ]

    stagnation_patience = 15
    immigrants_fraction = 0.2
    disable_convergence = False
    immigrant_interval = 0

    @staticmethod
    def apply_env_overrides() -> None:
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

        ev_auto = _intenv("GGNES_DEMO_EVAL_WORKERS", Config.eval_workers or 0)
        Config.eval_workers = None if ev_auto == 0 else ev_auto


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="GGNES MNIST Classification Demo")
    p.add_argument("--pop", type=int, default=None, help="Population size")
    p.add_argument("--gen", type=int, default=None, help="Number of generations")
    p.add_argument("--init-epochs", type=int, default=None, help="Initial training epochs per candidate")
    p.add_argument("--final-epochs", type=int, default=None, help="Final training epochs")
    p.add_argument("--max-iters", type=int, default=None, help="Max grammar iterations during generation")
    p.add_argument("--eval-workers", type=int, default=None, help="Parallel workers during evaluation")
    p.add_argument("--results-dir", type=str, default=None, help="Output directory for artifacts")
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
        Config.results_dir = str(args.results_dir)


def ensure_results_dir() -> str:
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
        'best_architecture.json',
        'evolution_progress.png',
        'run_report.txt',
    ]:
        try:
            path = os.path.join(out_dir, name)
            if os.path.exists(path):
                os.remove(path)
        except Exception:
            pass
    return out_dir


def _try_load_mnist() -> Tuple[np.ndarray, np.ndarray]:
    try:
        import torchvision
        from torchvision import datasets, transforms
        transform = transforms.Compose([
            transforms.ToTensor(),  # [0,1]
            transforms.Normalize((0.1307,), (0.3081,))  # standard MNIST norm
        ])
        root = os.path.join(PROJECT_ROOT, 'data')
        train_ds = datasets.MNIST(root=root, train=True, download=True, transform=transform)
        test_ds  = datasets.MNIST(root=root, train=False, download=True, transform=transform)
        X_train = train_ds.data.numpy().astype(np.float32) / 255.0
        y_train = train_ds.targets.numpy().astype(np.int64)
        X_test = test_ds.data.numpy().astype(np.float32) / 255.0
        y_test = test_ds.targets.numpy().astype(np.int64)
        # Flatten 28x28
        X_train = X_train.reshape(-1, 28*28)
        X_test  = X_test.reshape(-1, 28*28)
        return (X_train, y_train), (X_test, y_test)
    except Exception as e:
        print(f"[WARN] torchvision MNIST unavailable ({e}); falling back to sklearn.digits.", file=sys.stderr)
        try:
            from sklearn.datasets import load_digits
            digits = load_digits()  # 1797 samples of 8x8
            X = digits.data.astype(np.float32) / 16.0  # already 0..16
            y = digits.target.astype(np.int64)
            return (X, y), (X.copy(), y.copy())
        except Exception as ee:
            print(f"[ERROR] Failed to load fallback digits dataset: {ee}", file=sys.stderr)
            raise


def load_data() -> Tuple[Tuple[torch.Tensor, torch.Tensor],
                         Tuple[torch.Tensor, torch.Tensor],
                         Tuple[torch.Tensor, torch.Tensor]]:
    """Load MNIST (or fallback) and produce tensors for train/val/test."""
    (X_all, y_all), (X_test_full, y_test_full) = _try_load_mnist()

    # Train/Val split from train portion
    X_train_full, X_val_full, y_train_full, y_val_full = train_test_split(
        X_all, y_all, test_size=0.2, random_state=Config.random_state, stratify=y_all
    )

    # Subsample for speed (if specified)
    def _cap(X, y, cap):
        if cap is None or cap <= 0 or cap >= len(X):
            return X, y
        idx = np.random.RandomState(Config.random_state).choice(len(X), size=cap, replace=False)
        return X[idx], y[idx]

    X_train, y_train = _cap(X_train_full, y_train_full, Config.mnist_train_max)
    X_val,   y_val   = _cap(X_val_full, y_val_full, Config.mnist_val_max)
    X_test,  y_test  = _cap(X_test_full, y_test_full, Config.mnist_test_max)

    # Standardization per-feature (optional); here we keep as-is to not distort image scale.
    X_train = torch.tensor(X_train, dtype=torch.float32, device=DEVICE)
    y_train = torch.tensor(y_train, dtype=torch.long, device=DEVICE)
    X_val   = torch.tensor(X_val,   dtype=torch.float32, device=DEVICE)
    y_val   = torch.tensor(y_val,   dtype=torch.long, device=DEVICE)
    X_test  = torch.tensor(X_test,  dtype=torch.float32, device=DEVICE)
    y_test  = torch.tensor(y_test,  dtype=torch.long, device=DEVICE)

    print(f"  Train: {len(X_train)} | Val: {len(X_val)} | Test: {len(X_test)} | Features: {X_train.shape[1]}")
    return (X_train, y_train), (X_val, y_val), (X_test, y_test)


def create_axiom_graph(input_size: int = 28*28, num_classes: int = 10) -> Graph:
    """Initial graph with INPUT -> HIDDEN(64,relu) -> OUTPUT(10,linear)."""
    g = Graph()
    g.add_node({
        "id": "input",
        "node_type": NodeType.INPUT,
        "activation_function": "linear",
        "output_size": input_size
    })
    g.add_node({
        "id": "hidden1",
        "node_type": NodeType.HIDDEN,
        "activation_function": "relu",
        "output_size": 64
    })
    g.add_node({
        "id": "output",
        "node_type": NodeType.OUTPUT,
        "activation_function": "linear",
        "output_size": num_classes
    })
    g.add_edge("input", "hidden1")
    g.add_edge("hidden1", "output")
    return g


def create_grammar_rules() -> List[Rule]:
    rules: List[Rule] = []

    # Dense layer insertion
    for size in Config.layer_sizes:
        for activation in Config.activations:
            emb = EmbeddingLogic()
            try:
                emb.boundary_handling = 'IGNORE'
            except Exception:
                pass
            rules.append(
                Rule(
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
            )

    # Skip connection
    emb_skip = EmbeddingLogic()
    try:
        emb_skip.boundary_handling = 'IGNORE'
    except Exception:
        pass
    rules.append(
        Rule(
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
    )

    # Aggregation nodes (try all aggregations x all activations)
    for aggregation in Config.aggregations:
        for activation in Config.activations:
            emb_attn = EmbeddingLogic()
            try:
                emb_attn.boundary_handling = 'IGNORE'
            except Exception:
                pass
            rules.append(
                Rule(
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
            )

    # Grow small hidden layers to 128
    emb_grow = EmbeddingLogic()
    try:
        emb_grow.boundary_handling = 'IGNORE'
    except Exception:
        pass
    rules.append(
        Rule(
            name="grow_layer",
            pattern=LHSPattern(
                nodes=[{"label": "SMALL",
                        "match_criteria": {"node_type": NodeType.HIDDEN, "output_size": lambda s: s < 128}}],
                edges=[],
                boundary_nodes=[]
            ),
            action=RHSAction(modify_nodes=[{"label": "SMALL", "new_properties": {"attributes": {"output_size": 128}}}]),
            application_probability=0.5,
            embedding=emb_grow
        )
    )

    return rules


def train_model(model: nn.Module,
                train_data: Tuple[torch.Tensor, torch.Tensor],
                val_data: Tuple[torch.Tensor, torch.Tensor],
                epochs: int = 5,
                verbose: bool = False) -> Tuple[List[float], List[float], List[float]]:
    """Full-batch training for simplicity (small subsamples)."""
    X_train, y_train = train_data
    X_val, y_val = val_data

    crit = nn.CrossEntropyLoss()
    opt = optim.Adam(model.parameters(), lr=Config.learning_rate)
    train_losses, val_losses, val_accs = [], [], []

    for ep in range(epochs):
        model.train()
        opt.zero_grad()
        logits = model(X_train)
        loss = crit(logits, y_train)
        loss.backward()
        opt.step()
        train_losses.append(float(loss.item()))

        model.eval()
        with torch.no_grad():
            val_logits = model(X_val)
            vloss = crit(val_logits, y_val).item()
            preds = torch.argmax(val_logits, dim=1)
            vacc = accuracy_score(y_val.detach().cpu().numpy(), preds.detach().cpu().numpy())
        val_losses.append(float(vloss))
        val_accs.append(float(vacc))

        if verbose and (ep % 2 == 0):
            print(f"    Epoch {ep}: Train CE={train_losses[-1]:.4f}, Val CE={vloss:.4f}, Val ACC={vacc:.4f}")

    return train_losses, val_losses, val_accs


def _seed_for(genotype: Any, base: int = 42) -> int:
    gid = getattr(genotype, 'genotype_id', None) or getattr(genotype, 'id', None)
    try:
        key = int(str(gid).replace('-', '')[:8], 16)
    except Exception:
        key = 0
    return base + (key % (2**31 - 1))


def evaluate_genotype(genotype: Genotype,
                      train_data: Tuple[torch.Tensor, torch.Tensor],
                      val_data: Tuple[torch.Tensor, torch.Tensor]) -> Tuple[float, int, Dict[str, Any]]:
    """Generate network and brief training; return (val_error, params, info)."""
    try:
        axiom = create_axiom_graph(input_size=train_data[0].shape[1], num_classes=10)
        rng = RNGManager(seed=_seed_for(genotype))
        config = {
            'max_iterations': Config.max_iterations,
            'parallel_execution': True,
            'max_parallel_workers': max(1, min((os.cpu_count() or 2), 8)),
            'parallel_batch_policy': 'FIXED_SIZE',
            'parallel_fixed_size': 2,
            'parallel_conflict_strategy': 'SKIP'
        }
        net, info = generate_network_from_genotype(
            genotype=genotype,
            axiom_graph=axiom,
            config=config,
            rng_manager=rng
        )

        if len(net.nodes) > Config.max_network_size:
            return float('inf'), 0, {}

        model = to_pytorch_model(net).to(DEVICE)
        num_params = sum(p.numel() for p in model.parameters())

        _, vloss, vacc = train_model(model, train_data, val_data, epochs=Config.initial_epochs, verbose=False)
        # Optimize error = 1 - accuracy
        val_error = float(1.0 - float(vacc[-1] if vacc else 0.0))
        return val_error, num_params, info
    except Exception:
        return float('inf'), 0, {}


def evolve_architectures(train_data, val_data) -> Tuple[Genotype, List[Dict[str, Any]]]:
    print("\nStarting architecture evolution (NSGA-II)...")
    # Init population
    pop: List[Genotype] = [Genotype(rules=create_grammar_rules()) for _ in range(Config.population_size)]

    # Objectives and constraints
    def objectives(genotype: Genotype) -> Dict[str, float]:
        val_error, params, _ = evaluate_genotype(genotype, train_data, val_data)
        # nsga2_evolve maximizes objective values; negate to minimize error/params
        return {"neg_val_error": -float(val_error), "neg_params": -float(params)}

    def constraints(genotype: Genotype) -> Dict[str, bool]:
        try:
            axiom = create_axiom_graph(input_size=train_data[0].shape[1], num_classes=10)
            rng = RNGManager(seed=42)
            net, _ = generate_network_from_genotype(
                axiom_graph=axiom, genotype=genotype,
                config={'max_iterations': max(3, Config.max_iterations // 2)},
                rng_manager=rng
            )
            # DAG/size checks
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
    best_err = float('inf')
    prev_best = None
    stagnant_generations = 0

    for gen in range(Config.generations):
        print(f"\nGeneration {gen + 1}/{Config.generations}")

        vals, sizes, iters = [], [], []
        if Config.eval_workers is None:
            max_workers = max(2, min(4, Config.population_size))
        else:
            max_workers = int(Config.eval_workers)

        with ThreadPoolExecutor(max_workers=max_workers) as exe:
            fut2idx = {exe.submit(evaluate_genotype, g, train_data, val_data): i for i, g in enumerate(pop)}
            for fut in as_completed(fut2idx):
                try:
                    v, p, info = fut.result()
                except Exception:
                    v, p, info = float('inf'), 0, {}
                i = fut2idx[fut]
                vals.append(v); sizes.append(p)
                if v < best_err and 0 <= i < len(pop):
                    best_err = v; best = pop[i]

        mean_err = float(np.nanmean([x for x in vals if x != float('inf')])) if vals else float('inf')
        mean_p   = float(np.nanmean([x for x in sizes if x > 0])) if sizes else 0.0

        history.append({
            "generation": gen,
            "best_val_error": best_err,
            "mean_val_error": mean_err,
            "mean_params": mean_p
        })
        print(f"  Best val error: {best_err:.4f} (ACC={1-best_err:.4f})")
        print(f"  Mean val error: {mean_err:.4f}")
        print(f"  Mean params: {int(mean_p)}")

        diversity = calculate_diversity(pop)
        history[-1]["diversity"] = diversity

        if prev_best is None or best_err >= prev_best:
            stagnant_generations += 1
        else:
            stagnant_generations = 0
        prev_best = best_err

        if stagnant_generations >= Config.stagnation_patience:
            num_immigrants = max(1, int(Config.immigrants_fraction * Config.population_size))
            print(f"  Injecting {num_immigrants} immigrants...")
            immigrants = [Genotype(rules=create_grammar_rules()) for _ in range(num_immigrants)]
            ranks = np.argsort(vals)  # lower error is better
            worst = ranks[-num_immigrants:]
            for idx, im in zip(worst, immigrants):
                pop[idx] = im
            stagnant_generations = 0

        # NSGA-II selection
        solutions = nsga2_evolve(
            pop,
            objectives=objectives,
            generations=1,
            population_size=Config.population_size,
            mutation_rate=Config.mutation_rate,
            crossover_rate=Config.crossover_rate,
            constraints=constraints,
            return_solutions=True
        )
        pop = [s.genotype for s in solutions]
        pareto_summary = [
            {"rank": int(getattr(s, "rank", 0)),
             "crowding": float(getattr(s, "crowding_distance", 0.0)),
             "objectives": dict(getattr(s, "objectives", {}))}
            for s in solutions
        ]
        history[-1]["pareto_summary"] = pareto_summary
        # Top up if needed
        while len(pop) < Config.population_size:
            pop.append(Genotype(rules=create_grammar_rules()))

        # Checkpoint
        try:
            pop_light = []
            for g in pop:
                pop_light.append(g.to_dict() if hasattr(g, "to_dict") else {"id": str(getattr(g, "id", ""))})
            EvolutionCheckpoint(checkpoint_dir=Config.results_dir).save(
                population=pop_light, generation=gen, best_fitness=1.0 - best_err, metadata={"diversity": diversity}
            )
        except Exception:
            pass

        # Early convergence (optional)
        if not getattr(Config, "disable_convergence", False):
            try:
                detector = globals().get("_GGNES_DETECTOR", None)
                if detector is None:
                    detector = ConvergenceDetector(window_size=8, threshold=0.001)
                    globals()["_GGNES_DETECTOR"] = detector
                if detector.check_convergence([h.get("best_val_error", 1.0) for h in history]):
                    print("Convergence detected; stopping early.")
                    break
            except Exception:
                pass

    return best, history


def evaluate_best_model(best_genotype: Genotype,
                        train_data, val_data, test_data,
                        out_dir: str | None = None) -> Tuple[nn.Module, float]:
    print("\nEvaluating best model...")
    axiom = create_axiom_graph(input_size=train_data[0].shape[1], num_classes=10)
    rng = RNGManager(seed=42)
    net, info = generate_network_from_genotype(
        genotype=best_genotype, axiom_graph=axiom, config={'max_iterations': Config.max_iterations}, rng_manager=rng
    )

    print(f"  Network size: {len(net.nodes)} nodes")
    model = to_pytorch_model(net).to(DEVICE)
    nparams = sum(p.numel() for p in model.parameters())
    print(f"  Model parameters: {nparams}")

    print("  Training final model...")
    _, _, _ = train_model(model, train_data, val_data, epochs=Config.final_epochs, verbose=True)

    # Test accuracy
    X_test, y_test = test_data
    model.eval()
    with torch.no_grad():
        logits = model(X_test)
        preds = torch.argmax(logits, dim=1)
        acc = accuracy_score(y_test.detach().cpu().numpy(), preds.detach().cpu().numpy())
    print(f"\nFinal Test Accuracy: {acc:.4f}")

    # Save simple artifacts
    if out_dir:
        try:
            with open(os.path.join(out_dir, "best_genotype.json"), "w") as f:
                j = best_genotype.to_dict() if hasattr(best_genotype, "to_dict") else {}
                json.dump(j, f, indent=2)
            # Save minimal architecture (nodes/edges) similar to housing demo
            edges = []
            try:
                for e in net.list_edges():
                    src = getattr(e, 'src_id', getattr(e, 'source_node_id', None))
                    dst = getattr(e, 'dst_id', getattr(e, 'target_node_id', None))
                    edges.append([str(src), str(dst)])
            except Exception:
                pass
            arch = {
                'nodes': [
                    {
                        'id': str(nid),
                        'node_type': str(getattr(node, 'node_type', '')),
                        'activation_function': getattr(node, 'activation_function', None),
                        'output_size': (node.attributes.get('output_size')
                                        if hasattr(node, 'attributes') and isinstance(node.attributes, dict) else None)
                    }
                    for nid, node in getattr(net, 'nodes', {}).items()
                ],
                'edges': edges
            }
            with open(os.path.join(out_dir, 'best_architecture.json'), 'w') as f:
                json.dump(arch, f, indent=2)
            with open(os.path.join(out_dir, 'best_graph_edges.json'), 'w') as f:
                json.dump(edges, f, indent=2)
        except Exception:
            pass
    return model, float(acc)


def write_reports(history: List[Dict[str, Any]], out_dir: str) -> None:
    try:
        with open(os.path.join(out_dir, "evolution_history.json"), "w") as f:
            json.dump(history, f, indent=2)
        with open(os.path.join(out_dir, "pareto_front_summary.json"), "w") as f:
            json.dump(history, f, indent=2)
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
            'random_state': Config.random_state,
            'device': str(DEVICE),
        }
        with open(os.path.join(out_dir, "config.json"), "w") as f:
            json.dump(cfg, f, indent=2)
    except Exception:
        pass


def write_run_report(out_dir: str, acc: float) -> None:
    path = os.path.join(out_dir, 'run_report.txt')
    with open(path, 'w') as rf:
        rf.write("GGNES MNIST Demo - Run Report\n")
        rf.write("=" * 72 + "\n\n")
        rf.write(f"Device: {DEVICE}\n")
        rf.write("\nConfig\n")
        rf.write(f"  population_size: {Config.population_size}\n")
        rf.write(f"  generations: {Config.generations}\n")
        rf.write(f"  initial_epochs: {Config.initial_epochs}\n")
        rf.write(f"  final_epochs: {Config.final_epochs}\n")
        rf.write(f"  max_iterations: {Config.max_iterations}\n")
        rf.write(f"  max_network_size: {Config.max_network_size}\n\n")
        rf.write("Performance\n")
        rf.write(f"  Test Accuracy: {float(acc):.6f}\n")


def main() -> None:
    try:
        logging.getLogger().setLevel(logging.CRITICAL)
    except Exception:
        pass

    Config.apply_env_overrides()
    args = parse_args()
    apply_cli_overrides(args)

    print("=" * 80)
    print("GGNES Neural Architecture Search - MNIST (Classification)")
    print("=" * 80)

    out_dir = ensure_results_dir()
    print(f"Artifacts will be saved under: {os.path.abspath(out_dir)}")

    # Seed and data
    np.random.seed(Config.random_state)
    torch.manual_seed(Config.random_state)
    train_data, val_data, test_data = load_data()

    # Custom aggregation example (reusable)
    @register_aggregation("custom_topk")
    def custom_topk(inputs, **kwargs):
        from ggnes.aggregations import topk_weighted_sum_aggregation
        return topk_weighted_sum_aggregation(inputs, top_k=2, temperature=0.7)

    # Evolve
    best_genotype, history = evolve_architectures(train_data, val_data)

    # Persist evolution artifacts (visualization removed)
    write_reports(history, out_dir)

    # Evaluate best
    if best_genotype:
        model, test_acc = evaluate_best_model(best_genotype, train_data, val_data, test_data, out_dir)
        print("\n" + "=" * 80)
        print("Evolution Complete!")
        print(f"Best Test ACC: {test_acc:.4f}")
        print("=" * 80)

        write_run_report(out_dir, test_acc)
        try:
            with open(os.path.join(out_dir, "best_metrics.json"), "w") as f:
                json.dump({"test_accuracy": float(test_acc)}, f, indent=2)
        except Exception:
            pass
    else:
        print("No valid architecture found!")


if __name__ == "__main__":
    main()
