#!/usr/bin/env python3
"""
================================================================================
GGNES Neural Architecture Search Demo (California Housing) - GPU Optimized
================================================================================

What this is
- A GPU-optimized duplicate of the Professional Edition demo focused on:
  - Automatic CUDA use when available
  - Mixed precision (AMP) training on GPU for speed
  - Mini-batch training via DataLoader for better GPU utilization
  - Safe fallbacks to CPU when CUDA is not available

Quick run (brief sanity check)
- CPU or GPU (auto-detect):
    python demo/california_housing_gpu.py --pop 8 --gen 2 --max-iters 5 --eval-workers 1
- Environment overrides (optional, same as the main demo):
    export GGNES_DEMO_POP=8 GGNES_DEMO_GEN=2 GGNES_DEMO_MAX_ITERS=5 GGNES_DEMO_EVAL_WORKERS=1
    python demo/california_housing_gpu.py

Notes
- On GPU: evaluation uses a single worker to avoid CUDA context contention (same as main demo).
- AMP is enabled by default when CUDA is available; runs in full precision on CPU.

Quickstart (no GGNES knowledge required)
1) Create a Python 3.11 virtualenv (once):
   - python3.11 -m venv .venv311gpu && .venv311gpu/bin/python -m pip install --upgrade pip
   - .venv311gpu/bin/pip install --index-url https://download.pytorch.org/whl/cu121 torch==2.5.1+cu121 torchvision==0.20.1+cu121 torchaudio==2.5.1+cu121
   - .venv311gpu/bin/pip install -r requirements.txt
2) Run a tiny GPU sanity test:
   - .venv311gpu/bin/python -u demo/california_housing_gpu.py --pop 8 --gen 2 --max-iters 5
3) Speed it up safely (optional):
   - GGNES_GPU_CONCURRENCY=2 GGNES_PREP_WORKERS=0 .venv311gpu/bin/python -u demo/california_housing_gpu.py --pop 12 --gen 2 --max-iters 5
     • gpu_concurrency=2 lets two models train in parallel (bounded to avoid OOM)
     • prep_workers=0 is safest under threaded evaluation (can set to 2 if stable)

Controls you might tweak
- gpu_concurrency (env: GGNES_GPU_CONCURRENCY, default 1)
  • How many models train on the GPU at once; increase for better utilization
  • The code gates GPU training with a semaphore to avoid VRAM over-subscription
- prep_workers (env: GGNES_PREP_WORKERS, default None→0 on CUDA)
  • DataLoader CPU workers; use 0 for maximum stability; try 2 if you need faster input staging
- batch_size (Config.batch_size, default 128)
  • Effective batch is auto-scaled by gpu_concurrency to keep memory in check
- eval_workers (CLI/ENV)
  • ThreadPool workers coordinating candidate evaluations; on GPU this ties to gpu_concurrency

Safety
- Tensors remain on CPU; batches transfer to GPU per step (non_blocking=True)
- TF32 is enabled on CUDA (if available) for faster matmul with near-FP32 quality
- Final test evaluation explicitly moves tensors to the GPU to prevent device mismatch

================================================================================
"""

import os
import sys
import time
import json
import math
import logging
import warnings
import argparse
import platform
import subprocess
from typing import Any, Dict, List, Tuple
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading

import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from torch.cuda.amp import autocast, GradScaler
from torch.utils.data import DataLoader, TensorDataset

from tqdm import tqdm
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score

# Suppress non-critical warnings
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
USE_AMP = (DEVICE.type == 'cuda')  # use AMP only on CUDA
try:
    if DEVICE.type == 'cuda':
        torch.backends.cudnn.benchmark = True  # speed up on fixed-size layers
        try:
            torch.backends.cuda.matmul.allow_tf32 = True
            torch.backends.cudnn.allow_tf32 = True
        except Exception:
            pass
except Exception:
    pass
print(f"Using device: {DEVICE} | AMP: {USE_AMP}")

# Bounded GPU concurrency (gate GPU training to avoid contention/OOM)
_GPU_SEM = None
def _get_gpu_semaphore():
    global _GPU_SEM
    if _GPU_SEM is None:
        try:
            c = int(getattr(Config, 'gpu_concurrency', 1))
        except Exception:
            c = 1
        if c < 1:
            c = 1
        _GPU_SEM = threading.BoundedSemaphore(c)
    return _GPU_SEM


class Config:
    """Centralized configuration."""

    # Data
    test_size = 0.2
    val_size = 0.2
    random_state = 42

    # Training
    initial_epochs = 8
    final_epochs = 20
    batch_size = 128
    learning_rate = 0.001
    use_amp = True  # only used if DEVICE is CUDA

    # Evaluation workers / GPU concurrency
    # eval_workers controls ThreadPoolExecutor workers evaluating genotypes.
    # On GPU, we gate training via a semaphore to allow controlled concurrency.
    eval_workers = None  # None->auto
    gpu_concurrency = 1  # number of concurrent GPU trainings (1 is safest)
    prep_workers = None  # DataLoader workers for CPU-side input pipeline (None->auto)

    # Evolution
    population_size = 80
    generations = 20
    mutation_rate = 0.3
    crossover_rate = 0.7

    # Grammar presets
    rule_preset = 'dense_attention'
    use_all_combinations = True

    # Outputs
    results_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'california_housing_demo_output_gpu')
    use_timestamp = False

    # Retraining
    retrain_exported = True
    retrain_epochs = 100

    # Grammar generation constraints
    initial_rules = 5
    max_rules = 200
    max_network_size = 200
    max_iterations = 30

    # Search space params
    min_layer_size = 16
    max_layer_size = 128
    layer_sizes = [16, 32, 64, 128, 256, 512]
    activations = ['relu', 'leaky_relu', 'elu', 'gelu', 'tanh', 'sigmoid', 'selu', 'silu', 'softplus', 'softsign']
    aggregations = [
        'sum', 'mean', 'max', 'concat',
        'attention', 'multi_head_attention', 'attn_pool',
        'moe', 'gated_sum', 'topk_weighted_sum', 'matrix_product'
    ]

    # Stagnation and diversity
    stagnation_patience = 25
    immigrants_fraction = 0.2
    disable_convergence = False
    immigrant_interval = 0

    @staticmethod
    def apply_env_overrides() -> None:
        """Apply environment variable overrides."""
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

        Config.mutation_rate        = _floatenv("GGNES_DEMO_MUTATION_RATE", Config.mutation_rate)
        Config.crossover_rate       = _floatenv("GGNES_DEMO_CROSSOVER_RATE", Config.crossover_rate)
        Config.stagnation_patience  = _intenv("GGNES_DEMO_STAGNATION", Config.stagnation_patience)
        Config.immigrants_fraction  = _floatenv("GGNES_DEMO_IMM_FRAC", Config.immigrants_fraction)
        Config.immigrant_interval   = _intenv("GGNES_DEMO_IMM_INTERVAL", getattr(Config, "immigrant_interval", 0))
        dc = _intenv("GGNES_DEMO_DISABLE_CONV", 0)
        Config.disable_convergence  = bool(dc)

        # GPU and input pipeline controls
        Config.gpu_concurrency      = _intenv("GGNES_GPU_CONCURRENCY", getattr(Config, "gpu_concurrency", 1))
        pw = _intenv("GGNES_PREP_WORKERS", 0 if Config.prep_workers is None else Config.prep_workers)
        Config.prep_workers         = None if pw == 0 else pw


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="GPU Demo for California Housing — easy mode (no prior GGNES knowledge needed). "
                    "This script evolves small neural nets and trains them on your GPU with safe defaults."
    )
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
        'evolution_progress.png',
        'test_predictions.png',
        'run_report.txt',
        'evolution_checkpoint.pkl',
        'retrain_metrics.json',
        'repro_manifest.json',
        'pip_freeze.txt',
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
    """Load and preprocess the California Housing dataset and return tensors on DEVICE."""
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

    # Keep tensors on CPU; move batches to GPU non_blocking during training
    X_train = torch.tensor(X_train, dtype=torch.float32)
    y_train = torch.tensor(y_train, dtype=torch.float32).unsqueeze(1)
    X_val = torch.tensor(X_val, dtype=torch.float32)
    y_val = torch.tensor(y_val, dtype=torch.float32).unsqueeze(1)
    X_test = torch.tensor(X_test, dtype=torch.float32)
    y_test = torch.tensor(y_test, dtype=torch.float32).unsqueeze(1)

    print(f"  Training samples: {len(X_train)}")
    print(f"  Validation samples: {len(X_val)}")
    print(f"  Test samples: {len(X_test)}")
    print(f"  Features: {X_train.shape[1]}")
    return (X_train, y_train), (X_val, y_val), (X_test, y_test)


def create_axiom_graph(input_size: int = 8) -> Graph:
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

    # Skip connection
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

    # Aggregations
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
        if extras_needed > 0:
            extra_idx = np.random.choice(len(all_rules), extras_needed, replace=False)
            selected_rules = systematic + [all_rules[i] for i in extra_idx if all_rules[i] not in systematic]
        else:
            selected_rules = systematic
        selected_rules = selected_rules[:getattr(Config, 'max_rules', len(selected_rules))]
    else:
        selected_indices = np.random.choice(len(all_rules), min(num_rules, len(all_rules)), replace=False)
        selected_rules = [all_rules[i] for i in selected_indices]
    return Genotype(rules=selected_rules)


def make_loaders(train_data, val_data, batch_size: int):
    X_train, y_train = train_data
    X_val, y_val = val_data
    train_ds = TensorDataset(X_train, y_train)
    val_ds = TensorDataset(X_val, y_val)
    # Utilize CPU workers and pinned memory to overlap host<->device transfers
    # Default to 0 workers on CUDA to avoid multiprocessing issues under threaded eval.
    workers = (int(Config.prep_workers) if Config.prep_workers is not None
               else (0 if DEVICE.type == 'cuda' else 0))
    pin = (DEVICE.type == 'cuda')
    eff_bs = int(max(16, Config.batch_size // max(1, getattr(Config, 'gpu_concurrency', 1)))) if DEVICE.type == 'cuda' else int(Config.batch_size)
    train_loader = DataLoader(train_ds, batch_size=eff_bs, shuffle=True,
                              num_workers=workers, pin_memory=pin,
                              persistent_workers=(workers > 0))
    # larger val batch to speed up
    val_bs = max(eff_bs, 1024)
    val_loader = DataLoader(val_ds, batch_size=val_bs, shuffle=False,
                            num_workers=workers, pin_memory=pin,
                            persistent_workers=(workers > 0))
    return train_loader, val_loader


def train_model(model: nn.Module,
                train_data: Tuple[torch.Tensor, torch.Tensor],
                val_data: Tuple[torch.Tensor, torch.Tensor],
                epochs: int = 10,
                verbose: bool = False) -> Tuple[List[float], List[float]]:
    """Mini-batch training with AMP on GPU, full precision on CPU."""
    scaler = GradScaler(enabled=(USE_AMP and Config.use_amp))
    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=Config.learning_rate)

    train_loader, val_loader = make_loaders(train_data, val_data, Config.batch_size)

    train_losses, val_losses = [], []
    for epoch in range(epochs):
        # Train
        model.train()
        running = 0.0
        for xb, yb in train_loader:
            if xb.device.type != DEVICE.type:
                xb = xb.to(DEVICE, non_blocking=True)
                yb = yb.to(DEVICE, non_blocking=True)
            optimizer.zero_grad(set_to_none=True)
            if USE_AMP and Config.use_amp:
                with autocast():
                    pred = model(xb)
                    loss = criterion(pred, yb)
                scaler.scale(loss).backward()
                scaler.step(optimizer)
                scaler.update()
            else:
                pred = model(xb)
                loss = criterion(pred, yb)
                loss.backward()
                optimizer.step()
            running += loss.item() * xb.shape[0]
        train_losses.append(running / len(train_loader.dataset))

        # Validate
        model.eval()
        vloss = 0.0
        with torch.no_grad():
            for xb, yb in val_loader:
                if xb.device.type != DEVICE.type:
                    xb = xb.to(DEVICE, non_blocking=True)
                    yb = yb.to(DEVICE, non_blocking=True)
                if USE_AMP and Config.use_amp:
                    with autocast():
                        pred = model(xb)
                        loss = criterion(pred, yb)
                else:
                    pred = model(xb)
                    loss = criterion(pred, yb)
                vloss += loss.item() * xb.shape[0]
        val_losses.append(vloss / len(val_loader.dataset))

        if verbose and epoch % 5 == 0:
            print(f"    Epoch {epoch}: Train Loss = {train_losses[-1]:.4f}, Val Loss = {val_losses[-1]:.4f}")

    return train_losses, val_losses


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
    """Generate a network for the genotype and do a brief mini-batch training."""
    try:
        axiom = create_axiom_graph(input_size=8)
        rng = RNGManager(seed=_seed_for(genotype))
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

        if len(network.nodes) > Config.max_network_size:
            return float('inf'), 0, {}

        if DEVICE.type == 'cuda':
            _sem = _get_gpu_semaphore()
            _sem.acquire()
        try:
            model = to_pytorch_model(network).to(DEVICE)
            num_params = sum(p.numel() for p in model.parameters())
            _, val_losses = train_model(model, train_data, val_data, epochs=Config.initial_epochs, verbose=False)
            final_val_loss = float(val_losses[-1])
        finally:
            if DEVICE.type == 'cuda':
                try:
                    _sem.release()
                except Exception:
                    pass
        return final_val_loss, num_params, info
    except Exception:
        return float('inf'), 0, {}


def evolve_architectures(train_data, val_data) -> Tuple[Genotype, List[Dict[str, Any]]]:
    print("\nStarting architecture evolution (NSGA-II)...")

    # Init population
    current_pop: List[Genotype] = []
    for _ in range(Config.population_size):
        num_rules = np.random.randint(3, Config.initial_rules + 1)
        current_pop.append(create_genotype(num_rules))

    def objectives(genotype: Genotype) -> Dict[str, float]:
        val_loss, params, _ = evaluate_genotype(genotype, train_data, val_data)
        return {"neg_val_loss": -val_loss, "neg_params": -float(params)}

    def constraints(genotype: Genotype) -> Dict[str, bool]:
        try:
            axiom = create_axiom_graph(input_size=8)
            rng = RNGManager(seed=42)
            config = {'max_iterations': max(3, Config.max_iterations // 2)}
            net, _ = generate_network_from_genotype(axiom_graph=axiom, genotype=genotype, config=config, rng_manager=rng)
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

    for gen in range(Config.generations):
        print(f"\nGeneration {gen + 1}/{Config.generations}")

        vals, sizes, iter_counts = [], [], []
        cfg_workers = Config.eval_workers
        if cfg_workers is None:
            max_workers = int(getattr(Config, 'gpu_concurrency', 1)) if DEVICE.type == 'cuda' else max(2, min(4, Config.population_size))
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

        diversity = calculate_diversity(current_pop)
        history[-1]["diversity"] = diversity

        if prev_best is None or best_val >= prev_best:
            stagnant_generations += 1
        else:
            stagnant_generations = 0
        prev_best = best_val

        if stagnant_generations >= Config.stagnation_patience:
            num_immigrants = max(1, int(Config.immigrants_fraction * Config.population_size))
            print(f"  Injecting {num_immigrants} immigrant genotypes to escape stagnation...")
            immigrants = [create_genotype(np.random.randint(3, Config.initial_rules + 1))
                          for _ in range(num_immigrants)]
            ranks = np.argsort(vals)  # lower is better
            worst_indices = ranks[-num_immigrants:]
            for idx, immigrant in zip(worst_indices, immigrants):
                current_pop[idx] = immigrant
            stagnant_generations = 0

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

        while len(current_pop) < Config.population_size:
            clone = best.clone() if best else create_genotype(np.random.randint(3, Config.initial_rules + 1))
            try:
                clone = mutate(clone)
            except Exception:
                pass
            current_pop.append(clone)

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

        # Optional periodic immigrants
        try:
            interval = int(getattr(Config, "immigrant_interval", 0) or 0)
            if interval and (gen + 1) % interval == 0:
                num_imm = max(1, int(getattr(Config, "immigrants_fraction", 0.0) * Config.population_size))
                immigrants = [create_genotype(np.random.randint(3, Config.initial_rules + 1)) for _ in range(num_imm)]
                ranks = np.argsort(vals)
                worst_indices = ranks[-num_imm:]
                for idx, immigrant in zip(worst_indices, immigrants):
                    current_pop[idx] = immigrant
                print(f"  Periodic immigrants injected: {num_imm}")
        except Exception:
            pass

        # Convergence stop (can be disabled)
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
    print("\nEvaluating best model...")
    axiom = create_axiom_graph(input_size=8)
    rng = RNGManager(seed=42)
    config = {'max_iterations': Config.max_iterations}

    network, info = generate_network_from_genotype(
        genotype=best_genotype, axiom_graph=axiom, config=config, rng_manager=rng
    )

    print(f"  Network size: {len(network.nodes)} nodes")
    model = to_pytorch_model(network).to(DEVICE)
    num_params = sum(p.numel() for p in model.parameters())
    print(f"  Model parameters: {num_params}")

    print("  Training final model...")
    train_losses, val_losses = train_model(model, train_data, val_data, epochs=Config.final_epochs, verbose=True)

    # Test evaluation
    X_test, y_test = test_data
    if X_test.device.type != DEVICE.type:
        X_test = X_test.to(DEVICE, non_blocking=True)
        y_test = y_test.to(DEVICE, non_blocking=True)
    model.eval()
    with torch.no_grad():
        if USE_AMP and Config.use_amp:
            with autocast():
                predictions = model(X_test)
        else:
            predictions = model(X_test)
        test_mse = mean_squared_error(y_test.detach().cpu().numpy(), predictions.detach().cpu().numpy())
        test_r2 = r2_score(y_test.detach().cpu().numpy(), predictions.detach().cpu().numpy())

    print(f"\nFinal Test Results:\n  Test MSE: {test_mse:.4f}\n  Test R2 Score: {test_r2:.4f}")

    # Visualization removed: predictions plot omitted

    # Persist simple artifacts
    try:
        if out_dir:
            # genotype
            try:
                genod = best_genotype.to_dict() if hasattr(best_genotype, 'to_dict') else {}
            except Exception:
                genod = {}
            with open(os.path.join(out_dir, 'best_genotype.json'), 'w') as f:
                json.dump(genod, f, indent=2)
            # edges
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
            # minimal architecture
            arch = {
                'nodes': [
                    {
                        'id': str(nid),
                        'node_type': str(getattr(node, 'node_type', '')),
                        'activation_function': getattr(node, 'activation_function', None),
                        'output_size': (node.attributes.get('output_size')
                                        if hasattr(node, 'attributes') and isinstance(node.attributes, dict) else None)
                    }
                    for nid, node in getattr(network, 'nodes', {}).items()
                ],
                'edges': edges
            }
            with open(os.path.join(out_dir, 'best_architecture.json'), 'w') as f:
                json.dump(arch, f, indent=2)
    except Exception:
        pass

    return model, float(test_mse), float(test_r2)


def write_reports(history: List[Dict[str, Any]], out_dir: str) -> None:
    metrics = {
        'num_generations': len(history),
        'best_fitness_over_time': [h.get('best_fitness') for h in history],
        'mean_fitness_over_time': [h.get('mean_fitness') for h in history],
        'mean_complexity_over_time': [h.get('mean_complexity') for h in history]
    }
    with open(os.path.join(out_dir, "generation_metrics.json"), "w") as f:
        json.dump(metrics, f, indent=2)

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
        'disable_convergence': getattr(Config, 'disable_convergence', False),
        'immigrant_interval': getattr(Config, 'immigrant_interval', 0),
        'immigrants_fraction': getattr(Config, 'immigrants_fraction', 0.0),
        'device': str(DEVICE),
        'use_amp': bool(USE_AMP and Config.use_amp),
        'batch_size': Config.batch_size,
    }
    with open(os.path.join(out_dir, "config.json"), "w") as f:
        json.dump(cfg, f, indent=2)

    # Simple history dump as pareto summary mirror
    with open(os.path.join(out_dir, "evolution_history.json"), "w") as f:
        json.dump(history, f, indent=2)
    with open(os.path.join(out_dir, "pareto_front_summary.json"), "w") as f:
        json.dump(history, f, indent=2)

    # Repro manifest
    try:
        env_overrides = {k: os.environ.get(k) for k in sorted(os.environ.keys()) if k.startswith("GGNES_DEMO_")}
        git_commit = None
        try:
            proc = subprocess.run(["git", "rev-parse", "HEAD"], cwd=PROJECT_ROOT, capture_output=True, text=True)
            if proc.returncode == 0:
                git_commit = proc.stdout.strip()
        except Exception:
            pass

        def _ver(mod):
            try:
                return getattr(mod, "__version__", None)
            except Exception:
                return None

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
                'torch': _ver(torch),
                'numpy': _ver(np),
                'matplotlib': None,
            },
            'git_commit': git_commit,
            'cmdline': sys.argv,
            'env_overrides': env_overrides,
            'config': cfg,
        }
        with open(os.path.join(out_dir, "repro_manifest.json"), "w") as f:
            json.dump(manifest, f, indent=2)

        # pip freeze
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
    report_path = os.path.join(out_dir, 'run_report.txt')
    with open(report_path, 'w') as rf:
        rf.write("GGNES California Housing Demo - Run Report (GPU Optimized)\n")
        rf.write("=" * 72 + "\n\n")
        rf.write("Environment\n")
        rf.write(f"  Device: {DEVICE}\n")
        if torch.cuda.is_available():
            rf.write(f"  GPU: {torch.cuda.get_device_name(0)}\n")
            rf.write(f"  AMP: {bool(USE_AMP and Config.use_amp)}\n")
        rf.write("\nConfig\n")
        rf.write(f"  population_size: {Config.population_size}\n")
        rf.write(f"  generations: {Config.generations}\n")
        rf.write(f"  mutation_rate: {Config.mutation_rate}\n")
        rf.write(f"  crossover_rate: {Config.crossover_rate}\n")
        rf.write(f"  eval_workers: {Config.eval_workers}\n")
        rf.write(f"  max_iterations: {Config.max_iterations}\n")
        rf.write(f"  max_network_size: {Config.max_network_size}\n")
        rf.write(f"  batch_size: {Config.batch_size}\n")
        rf.write(f"  use_amp: {bool(USE_AMP and Config.use_amp)}\n\n")
        rf.write("Performance\n")
        rf.write(f"  Test MSE: {float(test_mse):.6f}\n")
        rf.write(f"  Test R2: {float(test_r2):.6f}\n")


def main() -> None:
    try:
        logging.getLogger().setLevel(logging.CRITICAL)
    except Exception:
        pass

    Config.apply_env_overrides()
    args = parse_args()
    apply_cli_overrides(args)
    # Print effective tuning knobs for transparency (helps new users)
    print(f"[Demo Controls] gpu_concurrency={Config.gpu_concurrency} | prep_workers={Config.prep_workers} | batch_size={Config.batch_size}")

    print("=" * 80)
    print("GGNES Neural Architecture Search - California Housing (GPU Optimized)")
    print("=" * 80)

    out_dir = ensure_results_dir()
    print(f"Artifacts will be saved under: {os.path.abspath(out_dir)}")

    # Seed and data
    np.random.seed(Config.random_state)
    torch.manual_seed(Config.random_state)
    train_data, val_data, test_data = load_data()

    # Custom aggregation example
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
        model, test_mse, test_r2 = evaluate_best_model(best_genotype, train_data, val_data, test_data, out_dir)
        print("\n" + "=" * 80)
        print("Evolution Complete!")
        print(f"Best Test MSE: {test_mse:.4f}")
        print(f"Best Test R2: {test_r2:.4f}")
        print("=" * 80)

        try:
            with open(os.path.join(out_dir, "best_metrics.json"), "w") as f:
                json.dump({"test_mse": float(test_mse), "test_r2": float(test_r2)}, f, indent=2)
        except Exception:
            pass
        write_run_report(out_dir, model, test_mse, test_r2)
    else:
        print("No valid architecture found!")


if __name__ == "__main__":
    main()
