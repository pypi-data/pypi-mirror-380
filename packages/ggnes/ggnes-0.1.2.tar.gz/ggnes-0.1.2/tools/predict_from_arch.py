#!/usr/bin/env python3
import argparse
import json
import os
import sys

import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from ggnes import Graph, NodeType, to_pytorch_model  # type: ignore


def load_data():
    data = fetch_california_housing()
    x, y = data.data, data.target

    x_temp, x_test, y_temp, y_test = train_test_split(
        x, y, test_size=0.2, random_state=42
    )
    x_train, x_val, y_train, y_val = train_test_split(
        x_temp, y_temp, test_size=0.2, random_state=42
    )

    scaler = StandardScaler()
    x_train = scaler.fit_transform(x_train)
    x_val = scaler.transform(x_val)
    x_test = scaler.transform(x_test)

    x_train = torch.FloatTensor(x_train)
    y_train = torch.FloatTensor(y_train).unsqueeze(1)
    x_val = torch.FloatTensor(x_val)
    y_val = torch.FloatTensor(y_val).unsqueeze(1)
    x_test = torch.FloatTensor(x_test)
    y_test = torch.FloatTensor(y_test).unsqueeze(1)
    return (x_train, y_train), (x_val, y_val), (x_test, y_test)


def rebuild_graph_from_best_arch(best_arch_path: str) -> Graph:
    with open(best_arch_path) as f:
        arch = json.load(f)
    g = Graph()
    # Edges in best_architecture.json are indices referring to the nodes array order.
    nodes = arch.get("nodes", [])
    idx_to_rid = []
    # Add nodes in order and remember their internal ids
    for _, n in enumerate(nodes):
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
    # Add edges using index mapping
    for src, dst in arch.get("edges", []):
        try:
            s = idx_to_rid[int(src)]
            d = idx_to_rid[int(dst)]
            g.add_edge(s, d)
        except Exception:
            # Ignore malformed edges gracefully for preview
            pass
    return g


def train_model(model: nn.Module, train_data, val_data, epochs: int = 20, lr: float = 1e-3):
    x_train, y_train = train_data
    x_val, y_val = val_data
    crit = nn.MSELoss()
    opt = optim.Adam(model.parameters(), lr=lr)
    for ep in range(epochs):
        model.train()
        opt.zero_grad()
        pred = model(x_train)
        loss = crit(pred, y_train)
        loss.backward()
        opt.step()
        if (ep % 5) == 0:
            model.eval()
            with torch.no_grad():
                v = crit(model(x_val), y_val).item()
            print(f"Epoch {ep:3d} | Train MSE={loss.item():.4f} | Val MSE={v:.4f}")
    return model


def main():
    ap = argparse.ArgumentParser(description="Preview predictions from best_architecture.json")
    ap.add_argument(
        "outdir",
        nargs="?",
        default="demo/california_housing_demo_output",
        help="Output dir containing best_architecture.json",
    )
    ap.add_argument("--epochs", type=int, default=20, help="Fine-tuning epochs for preview")
    ap.add_argument("--k", type=int, default=10, help="Number of samples to print")
    args = ap.parse_args()

    outdir = os.path.abspath(args.outdir)
    candidates = [
        os.path.join(outdir, "best_architecture.json"),
        os.path.join(outdir, "best_architecture_pruned.json"),
        os.path.join(outdir, "best_architecture_raw.json"),
    ]
    arch_path = next((p for p in candidates if os.path.exists(p)), candidates[0])
    if not os.path.exists(arch_path):
        print(f"Architecture file not found. Tried: {candidates}", file=sys.stderr)
        sys.exit(1)

    np.random.seed(42)
    torch.manual_seed(42)

    print("Loading data...")
    train_data, val_data, test_data = load_data()
    print(f"Rebuilding graph from: {arch_path}")
    g = rebuild_graph_from_best_arch(arch_path)
    print("Translating to PyTorch model...")
    model = to_pytorch_model(g)

    print(f"Training for {args.epochs} epochs (preview)...")
    train_model(model, train_data, val_data, epochs=args.epochs)

    model.eval()
    x_test, y_test = test_data
    with torch.no_grad():
        preds = model(x_test).squeeze(1).cpu().numpy()
    y_true = y_test.squeeze(1).cpu().numpy()

    k = min(args.k, len(y_true))
    rows = []
    print(f"\nSample predictions (first {k} rows):")
    header = f"{'idx':>4s} | {'y_true':>10s} | {'y_pred':>10s} | {'abs_err':>10s}"
    print(header)
    print("-" * len(header))
    for i in range(k):
        yt = float(y_true[i])
        yp = float(preds[i])
        ae = abs(yp - yt)
        rows.append((i, yt, yp, ae))
        print(f"{i:4d} | {yt:10.6f} | {yp:10.6f} | {ae:10.6f}")

    # Save to CSV for convenience
    csv_path = os.path.join(outdir, "sample_predictions.csv")
    try:
        with open(csv_path, "w", encoding="utf-8") as f:
            f.write("index,y_true,y_pred,abs_err\n")
            for i, yt, yp, ae in rows:
                f.write(f"{i},{yt:.6f},{yp:.6f},{ae:.6f}\n")
        print(f"\nSaved {k} rows to: {csv_path}")
    except Exception as e:
        print(f"Could not write CSV: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
