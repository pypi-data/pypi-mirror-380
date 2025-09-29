#!/usr/bin/env python3
"""
GGNES API Demo — M5-style Forecasting (Smoke + Full)

This demo uses the beginner-friendly API (Search/starter_space) to search
architectures for a simple forecasting formulation inspired by M5. It generates
an M5-like time-series dataset (if real CSVs are not configured), builds a
sliding-window supervised dataset, and runs a search with pruning and
multi-objective optimization.

Usage examples:
  Smoke (fast):
    PYTHONPATH=$(pwd) CUDA_VISIBLE_DEVICES="" \
    python3 -u demo/m5_forecasting_api_demo.py --smoke --seed 42

  Foreground full (example budgets):
    PYTHONPATH=$(pwd) CUDA_VISIBLE_DEVICES="" \
    python3 -u demo/m5_forecasting_api_demo.py --full --seed 42 --pop 100 --gens 100
"""
import argparse
import json
import os
from typing import Tuple

import numpy as np
import torch


def _set_determinism(seed: int) -> None:
    try:
        np.random.seed(seed)
        torch.manual_seed(seed)
    except Exception:
        pass


def generate_m5_like_series(
    num_series: int = 50,
    num_days: int = 400,
    season_days: int = 7,
    noise_scale: float = 0.3,
    seed: int = 42,
) -> Tuple[torch.Tensor, torch.Tensor]:
    """Generate synthetic M5-like daily sales for multiple series.

    Returns
    - X_all: [num_series, num_days, feature_dim]
    - y_all: [num_series, num_days, 1]
    """
    _set_determinism(seed)

    days = np.arange(num_days)
    weekday = days % 7  # 0..6
    month = (days // 30) % 12  # pseudo-month

    X_list = []
    y_list = []
    for s in range(num_series):
        base = 2.0 + 0.01 * days  # slow trend
        weekly = 0.5 * np.sin(2 * np.pi * days / season_days + 0.2 * s)
        promo = (np.random.rand(num_days) < 0.05).astype(float)  # sparse promos
        noise = noise_scale * np.random.randn(num_days)
        sales = np.maximum(0.0, base + weekly + 1.5 * promo + noise)

        # Features: [sales_lag7, sales_lag14, weekday_onehot(7), month_onehot(12), promo]
        sales_lag7 = np.concatenate([np.zeros(7), sales[:-7]])
        sales_lag14 = np.concatenate([np.zeros(14), sales[:-14]])
        wd_oh = np.eye(7)[weekday]
        mo_oh = np.eye(12)[month]
        feat = np.column_stack([sales_lag7, sales_lag14, wd_oh, mo_oh, promo])

        X_list.append(feat.astype(np.float32))
        y_list.append(sales.astype(np.float32)[:, None])

    X_all = np.stack(X_list, axis=0)  # [S, T, D]
    y_all = np.stack(y_list, axis=0)  # [S, T, 1]
    return torch.from_numpy(X_all), torch.from_numpy(y_all)


def make_supervised_from_series(
    X_all: torch.Tensor,
    y_all: torch.Tensor,
    window: int = 28,
    horizon: int = 1,
) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor]:
    """Create supervised windows across series.

    Returns train/val/test tuples of tensors (X, y) with shapes [N, D], [N, 1].
    """
    S, T, D = X_all.shape
    Xs = []
    ys = []
    s_ids = []
    for s in range(S):
        for t in range(window, T - horizon + 1):
            x_now = X_all[s, t, :]  # current-day features
            y_target = y_all[s, t + horizon - 1, 0]
            Xs.append(x_now)
            ys.append(y_target)
            s_ids.append(int(s))
    X = torch.stack(Xs, dim=0)
    y = torch.stack(ys, dim=0).unsqueeze(1)
    sid = torch.tensor(s_ids, dtype=torch.long)

    # Split
    N = X.size(0)
    n_train = int(0.7 * N)
    n_val = int(0.15 * N)
    idx = torch.arange(N)
    # deterministic shuffle by seed applied earlier if desired
    X_train, y_train, s_train = X[idx[:n_train]], y[idx[:n_train]], sid[idx[:n_train]]
    X_val, y_val, s_val = X[idx[n_train:n_train + n_val]], y[idx[n_train:n_train + n_val]], sid[idx[n_train:n_train + n_val]]
    X_test, y_test, s_test = X[idx[n_train + n_val:]], y[idx[n_train + n_val:]], sid[idx[n_train + n_val:]]
    return X_train, y_train, s_train, X_val, y_val, s_val, X_test, y_test, s_test


def compute_wrmsse_approx(
    s_ids: torch.Tensor,
    y_pred: np.ndarray,
    y_true: np.ndarray,
    y_all: torch.Tensor,
    train_ratio: float = 0.7,
) -> float:
    """Approximate WRMSSE:
    - For each series s, compute scale as mean((y_t - y_{t-1})^2) over first train_ratio of its timeline.
    - RMSSE_s = sqrt(mean((y_pred - y_true)^2) / (scale + 1e-8)) over that series' test samples.
    - Weight for series s = sum(y_all[s]) / sum over all series (proxy for importance).
    """
    S, T, _ = y_all.shape
    y_all_np = y_all.squeeze(-1).numpy()
    cutoff = max(2, int(train_ratio * T))
    scales = []
    weights = []
    for s in range(S):
        diffs = np.diff(y_all_np[s, :cutoff])
        scale = float(np.mean(diffs * diffs)) if diffs.size else 1.0
        scales.append(scale if scale > 1e-8 else 1.0)
        weights.append(float(np.sum(y_all_np[s])))
    weights = np.array(weights)
    weights = weights / max(1e-12, weights.sum())

    # Group test errors by series
    s_ids_np = s_ids.cpu().numpy()
    err2 = (y_pred - y_true) ** 2
    wrmsse = 0.0
    for s in range(S):
        mask = (s_ids_np == s)
        if not mask.any():
            continue
        mse_s = float(np.mean(err2[mask]))
        rmsse_s = np.sqrt(mse_s / scales[s])
        wrmsse += weights[s] * rmsse_s
    return float(wrmsse)


def run_search(X_train, y_train, X_val, y_val, *, seed: int, smoke: bool,
               population: int | None, generations: int | None, outdir: str) -> dict:
    from ggnes.api.mvp import Search, starter_space

    s = Search(
        smoke=bool(smoke),
        seed=int(seed),
        population=population,
        generations=generations,
        search_space=starter_space("attention_tabular"),
        generation_config={"use_real_generation_nsga": bool(not smoke)},
    )
    # Encourage compact, effective nets
    s.objectives = [("val_mse", "min"), ("params", "min"), ("dead_nodes", "min")]

    res = s.fit(X_train, y_train, validation_data=(X_val, y_val))

    # Persist a Mermaid diagram for convenience
    try:
        arch_path = os.path.join(res.artifacts, "best_architecture_pruned.json")
        mm_path = os.path.join(outdir, "M5_ARCH.mmd")
        with open(arch_path, "r", encoding="utf-8") as f:
            arch = json.load(f)
        with open(mm_path, "w", encoding="utf-8") as f:
            f.write("flowchart LR\n")
            for n in arch.get("nodes", []):
                nid = str(n.get("id"))
                t = str(n.get("node_type", "")).split(".")[-1]
                sz = n.get("output_size")
                act = n.get("activation_function") or "relu"
                f.write(f'  n{nid}["{nid} {t} ({sz}) {act}"]\n')
            for s_id, t_id in arch.get("edges", []):
                f.write(f"  n{s_id} --> n{t_id}\n")
        print(f"[demo] Mermaid written: {mm_path}")
    except Exception:
        pass

    return {
        "metrics": res.metrics,
        "artifacts": res.artifacts,
        "pareto": res.pareto,
        "best_arch_path": os.path.join(res.artifacts, "best_architecture_pruned.json"),
    }


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="GGNES M5-style forecasting demo")
    p.add_argument("--smoke", action="store_true", help="Run tiny smoke search")
    p.add_argument("--full", action="store_true", help="Run a larger foreground search")
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--pop", type=int, default=None)
    p.add_argument("--gens", type=int, default=None)
    p.add_argument("--outdir", type=str, default="demo/outputs/m5_api_demo")
    p.add_argument("--final-epochs", type=int, default=60, help="Final retrain epochs for selected arch")
    return p.parse_args()


def main() -> None:
    args = parse_args()
    os.makedirs(args.outdir, exist_ok=True)
    _set_determinism(args.seed)

    # Data (synthetic M5-like). Replace with real CSV loader if available.
    X_all, y_all = generate_m5_like_series(
        num_series=60 if args.full else 20,
        num_days=600 if args.full else 120,
        seed=args.seed,
    )
    X_train, y_train, s_train, X_val, y_val, s_val, X_test, y_test, s_test = make_supervised_from_series(
        X_all, y_all, window=28, horizon=1
    )

    # Budgets
    if args.smoke and not args.full:
        pop = 8 if args.pop is None else int(args.pop)
        gens = 2 if args.gens is None else int(args.gens)
    else:
        pop = 100 if args.pop is None else int(args.pop)
        gens = 100 if args.gens is None else int(args.gens)

    res = run_search(
        X_train, y_train, X_val, y_val,
        seed=args.seed,
        smoke=bool(args.smoke and not args.full),
        population=pop,
        generations=gens,
        outdir=args.outdir,
    )

    # --- Retrain selected pruned architecture on train+val and plot forecast ---
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        from ggnes import Graph, NodeType, to_pytorch_model
        import torch.nn as nn
        import torch.optim as optim

        arch_path = res.get("best_arch_path")
        with open(arch_path, "r", encoding="utf-8") as f:
            arch = json.load(f)

        # Rebuild graph from JSON
        g = Graph()
        idx_to_rid = []
        for i, n in enumerate(arch.get("nodes", [])):
            node_type_str = str(n.get("node_type", "NodeType.HIDDEN"))
            node_type_name = node_type_str.split(".")[-1]
            node_type = getattr(NodeType, node_type_name, NodeType.HIDDEN)
            props = {
                "id": n.get("id"),
                "node_type": node_type,
                "activation_function": n.get("activation_function") or "relu",
            }
            if n.get("output_size") is not None:
                props["attributes"] = {"output_size": int(n["output_size"]) }
            rid = g.add_node(props)
            idx_to_rid.append(rid)
        for src, dst in arch.get("edges", []):
            try:
                s = idx_to_rid[int(src)]
                d = idx_to_rid[int(dst)]
                g.add_edge(s, d)
            except Exception:
                pass

        model = to_pytorch_model(g)
        # Initialize scalar edge weights away from zero to avoid flat outputs at start
        try:
            for name, p in model.named_parameters():
                if name.startswith("weight_") and p.numel() == 1:
                    with torch.no_grad():
                        p.fill_(1.0)
        except Exception:
            pass
        params = sum(p.numel() for p in model.parameters())

        # Retrain on train+val
        X_tr = torch.cat([X_train, X_val], dim=0)
        y_tr = torch.cat([y_train, y_val], dim=0)
        crit = nn.MSELoss()
        opt = optim.Adam(model.parameters(), lr=1e-3)
        model.train()
        for ep in range(int(args.final_epochs)):
            opt.zero_grad()
            pred = model(X_tr)
            loss = crit(pred, y_tr)
            loss.backward()
            opt.step()
        # Evaluate on test and plot
        model.eval()
        with torch.no_grad():
            preds = model(X_test).squeeze(1).cpu().numpy()
            ytrue = y_test.squeeze(1).cpu().numpy()
            test_mse = float(((preds - ytrue) ** 2).mean())
            wrmsse = compute_wrmsse_approx(s_test, preds, ytrue, y_all)

        # Plot first 300 points
        k = min(300, len(ytrue))
        plt.figure(figsize=(10, 4))
        plt.plot(ytrue[:k], label="y_true", lw=1.5)
        plt.plot(preds[:k], label="y_pred", lw=1.5)
        plt.title("M5-style Forecast — Selected Architecture")
        plt.xlabel("Window index")
        plt.ylabel("Unit sales (normalized)")
        plt.legend()
        png_path = os.path.join(args.outdir, "M5_FORECAST.png")
        plt.tight_layout()
        plt.savefig(png_path)
        print(json.dumps({
            "final_retrain": {
                "params": int(params),
                "test_mse": test_mse,
                "wrmsse_approx": wrmsse,
                "forecast_plot": png_path
            }
        }, indent=2))
    except Exception as e:
        print(json.dumps({"final_retrain_error": str(e)}, indent=2))

    # --- LightGBM baseline comparison (approximate) ---
    try:
        import lightgbm as lgb
        lgb_train = lgb.Dataset(X_train.numpy(), label=y_train.squeeze(1).numpy())
        lgb_valid = lgb.Dataset(X_val.numpy(), label=y_val.squeeze(1).numpy(), reference=lgb_train)
        params_lgb = {
            "objective": "regression",
            "metric": "l2",
            "learning_rate": 0.05,
            "num_leaves": 64,
            "min_data_in_leaf": 50,
            "verbose": -1,
        }
        booster = lgb.train(params_lgb, lgb_train, num_boost_round=300, valid_sets=[lgb_valid], verbose_eval=False)
        y_pred_lgb = booster.predict(X_test.numpy())
        y_true_np = y_test.squeeze(1).numpy()
        mse_lgb = float(np.mean((y_pred_lgb - y_true_np) ** 2))
        wrmsse_lgb = compute_wrmsse_approx(s_test, y_pred_lgb, y_true_np, y_all)
        print(json.dumps({
            "baseline_lgb": {
                "mse": mse_lgb,
                "wrmsse_approx": wrmsse_lgb,
                "rounds": 300
            }
        }, indent=2))
    except Exception as e:
        print(json.dumps({"baseline_lgb_error": str(e)}, indent=2))

    print(json.dumps({
        "metrics": res["metrics"],
        "artifacts": res["artifacts"],
        "pareto_top1": (res["pareto"][0] if res.get("pareto") else None)
    }, indent=2))


if __name__ == "__main__":
    main()


