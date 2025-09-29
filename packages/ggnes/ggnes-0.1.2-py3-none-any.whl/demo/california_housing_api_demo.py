#!/usr/bin/env python3
"""
California Housing — End-to-End Demo using the new GGNES API (MVP)

This script demonstrates how to:
  1) Load and preprocess California Housing data
  2) Run a small smoke search to validate the pipeline
  3) Optionally launch a full search (population=24, generations=100) in the background

Notes
- The new API is smoke-friendly. For full runs, we set use_real_generation_nsga=True
  to translate generated candidates and evaluate simple objectives.
- We keep per-candidate training tiny (1 epoch) to bound runtime.
"""

import argparse
import json
import os
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

import numpy as np
import torch
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from ggnes import Search, starter_space, to_pytorch_model


def load_housing_as_tensors(test_size=0.2, val_size=0.2, seed=42):
    """Load California Housing, split, scale, and convert to torch tensors."""
    data = fetch_california_housing()
    X, y = data.data.astype(np.float32), data.target.astype(np.float32)
    X_temp, X_test, y_temp, y_test = train_test_split(X, y, test_size=test_size, random_state=seed)
    X_train, X_val, y_train, y_val = train_test_split(X_temp, y_temp, test_size=val_size, random_state=seed)
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_val = scaler.transform(X_val)
    X_test = scaler.transform(X_test)
    return (
        torch.from_numpy(X_train), torch.from_numpy(y_train.reshape(-1, 1)),
        torch.from_numpy(X_val), torch.from_numpy(y_val.reshape(-1, 1)),
        torch.from_numpy(X_test), torch.from_numpy(y_test.reshape(-1, 1)),
    )


def run_smoke(outdir: Path, seed=42):
    """Run a tiny smoke search to validate the end-to-end path."""
    X, y, Xv, yv, Xt, yt = load_housing_as_tensors(seed=seed)

    # Choose a starter space. "attention_tabular" introduces attention nodes in the search space.
    space = starter_space("attention_tabular")

    # Configure a smoke-friendly search: population=4, generations=2
    search = Search(
        smoke=True,
        seed=seed,
        population=4,
        generations=2,
        search_space=space,
    )
    # Objectives: minimize validation MSE and parameter count
    search.objectives = [("val_mse", "min"), ("params", "min")]
    # Real generation + NSGA over generated candidates
    search.use_real_generation_nsga = True

    res = search.fit(X, y, validation_data=(Xv, yv), test_data=(Xt, yt))
    outdir.mkdir(parents=True, exist_ok=True)
    (outdir / "smoke_result.json").write_text(json.dumps({
        "metrics": res.metrics,
        "pareto": res.pareto,
        "constraints": res.constraints,
        "artifacts": res.artifacts,
    }, indent=2))
    print("[SMOKE] Metrics:", res.metrics)
    print("[SMOKE] Pareto (top 3):", (res.pareto or [])[:3])


def _eval_candidate(graph, X, y, Xv, yv, device="cpu") -> dict:
    """Translate a graph, train 1 epoch, return objectives (val_mse, params)."""
    import torch
    import torch.nn as nn
    m = to_pytorch_model(graph, {"device": device})
    params = float(sum(p.numel() for p in m.parameters()))
    crit = nn.MSELoss(); opt = torch.optim.SGD(m.parameters(), lr=1e-3)
    m.train(); opt.zero_grad(); yp = m(X); loss = crit(yp, y); loss.backward(); opt.step()
    m.eval();
    with torch.no_grad():
        vy = m(Xv)
    val_mse = float(crit(vy, yv).item())
    return {"val_mse": val_mse, "params": params}


def launch_full(outdir: Path, seed=42, pop=24, gens=100):
    """Run a full loop in the foreground with per-generation progress."""
    X, y, Xv, yv, Xt, yt = load_housing_as_tensors(seed=seed)

    space = starter_space("attention_tabular")
    # Manual foreground loop for visible progress (uses small per-candidate training)
    import random
    from ggnes import apply_grammar
    rng = random.Random(seed)
    best = {"val_mse": float("inf"), "params": 0.0}
    history = []
    for gen in range(1, int(gens) + 1):
        objs = []
        for i in range(int(pop)):
            # Build a simple base graph and apply a small number of grammar iterations
            from ggnes import Graph, NodeType
            g = Graph()
            iid = g.add_node({"node_type": NodeType.INPUT, "activation_function": "linear", "attributes": {"output_size": int(X.shape[1])}})
            hid = g.add_node({"node_type": NodeType.HIDDEN, "activation_function": "relu", "attributes": {"output_size": 16 + (i % 3) * 16}})
            out = g.add_node({"node_type": NodeType.OUTPUT, "activation_function": "linear", "attributes": {"output_size": 1}})
            g.add_edge(iid, hid); g.add_edge(hid, out)
            iters = 1 + (i % 3)
            try:
                g = apply_grammar(g, space.rules, max_iterations=iters)
            except Exception:
                pass
            o = _eval_candidate(g, X, y, Xv, yv)
            objs.append(o)
        # Track best and print summary
        gen_best = min(objs, key=lambda d: d["val_mse"]) if objs else best
        if gen_best["val_mse"] < best["val_mse"]:
            best = gen_best
        history.append({"gen": gen, "best_val_mse": best["val_mse"], "gen_best": gen_best["val_mse"]})
        print(f"[GEN {gen}/{gens}] gen_best={gen_best['val_mse']:.4f} best_so_far={best['val_mse']:.4f} pop={pop}")
        sys.stdout.flush()
    # Write a compact result summary
    outdir.mkdir(parents=True, exist_ok=True)
    (outdir / "full_result.json").write_text(json.dumps({"best": best, "history": history[-10:]}, indent=2))
    print("[FULL] Best:", best)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--smoke-only", action="store_true", help="Only run the small validation run")
    ap.add_argument("--full", action="store_true", help="Run the full 24x100 generations now (foreground)")
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--pop", type=int, default=24)
    ap.add_argument("--gens", type=int, default=100)
    ap.add_argument("--outdir", type=str, default="demo/outputs/california_housing/api_demo")
    args = ap.parse_args()

    outdir = Path(args.outdir) / datetime.now().strftime("%Y%m%d_%H%M%S")
    print("Output directory:", str(outdir))

    # 1) Smoke run
    run_smoke(outdir, seed=args.seed)

    # 2) Full run
    if args.full:
        launch_full(outdir, seed=args.seed, pop=args.pop, gens=args.gens)
    elif not args.smoke_only:
        # Spawn a background process (detached) for the full run using this script itself
        cmd = [
            sys.executable,
            __file__,
            "--full",
            "--seed", str(args.seed),
            "--pop", str(args.pop),
            "--gens", str(args.gens),
            "--outdir", str(outdir),
        ]
        print("Launching full run in background:", " ".join(cmd))
        # Best-effort background launch; the parent process exits immediately.
        subprocess.Popen(cmd, stdout=open(os.devnull, "wb"), stderr=subprocess.STDOUT)


if __name__ == "__main__":
    main()


