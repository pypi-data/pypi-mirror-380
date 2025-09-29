from __future__ import annotations

import json
import os
from typing import Any


def ensure_dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def write_json(path: str, obj: Any) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, sort_keys=True, separators=(",", ":"))


def write_repro_bundle(
    out_dir: str, manifest: dict, plan: dict, topk: list[dict], logs: list[dict]
) -> str:
    ensure_dir(out_dir)
    write_json(os.path.join(out_dir, "manifest.json"), manifest)
    write_json(os.path.join(out_dir, "plan.json"), plan)
    write_json(os.path.join(out_dir, "topk.json"), topk)
    write_json(os.path.join(out_dir, "logs.jsonl"), logs)
    return out_dir
