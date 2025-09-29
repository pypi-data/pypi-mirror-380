import argparse
import json
from pathlib import Path

import torch

from ggnes.api.mvp import Search, starter_space


def main() -> None:
    p = argparse.ArgumentParser(description="GGNES Search (smoke-friendly)")
    p.add_argument("--smoke", action="store_true", help="Run tiny smoke search")
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--population", type=int, default=None)
    p.add_argument("--generations", type=int, default=None)
    p.add_argument("--starter-space", type=str, default="tabular_dense", help="tabular_dense|attention_tabular")
    p.add_argument("--out", type=str, default="ggnes_results.json")
    args = p.parse_args()

    # Toy synthetic data for quick validation
    X = torch.randn(64, 8)
    y = X @ torch.randn(8, 1) + 0.1 * torch.randn(64, 1)
    Xv = torch.randn(32, 8)
    yv = Xv @ torch.randn(8, 1) + 0.1 * torch.randn(32, 1)

    s = Search(
        smoke=bool(args.smoke),
        seed=int(args.seed),
        population=args.population,
        generations=args.generations,
        search_space=starter_space(args.starter_space),
    )
    s.objectives = [("val_mse", "min"), ("params", "min")]
    s.use_real_generation_nsga = True
    res = s.fit(X, y, validation_data=(Xv, yv))

    out = {
        "metrics": res.metrics,
        "pareto": res.pareto,
        "constraints": res.constraints,
        "artifacts": res.artifacts,
    }
    Path(args.out).write_text(json.dumps(out, indent=2))
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()



