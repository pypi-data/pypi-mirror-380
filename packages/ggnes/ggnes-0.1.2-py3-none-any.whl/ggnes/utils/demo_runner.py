from __future__ import annotations

import json
import os
import time
from collections.abc import Callable


def deterministic_now_ms() -> int:
    return int(time.time() * 1000)


def run_demo_loop(
    duration_hours: int,
    step_fn: Callable[[int], dict],
    snapshot_dir: str,
    now_fn: Callable[[], int] = deterministic_now_ms,
) -> list[dict]:
    """Run a deterministic demo loop capturing hourly snapshots.

    Args:
        duration_hours: total hours to run (wall-clock budget)
        step_fn: returns a log record for the current step (dict)
        snapshot_dir: directory to write hourly snapshots
        now_fn: injectable clock for tests
    Returns:
        list of log records (in memory)
    """
    os.makedirs(snapshot_dir, exist_ok=True)
    logs: list[dict] = []
    start_ms = now_fn()
    next_snapshot_h = 1
    # Simulate steps; in real run, this would be while work remains
    while True:
        rec = step_fn(len(logs))
        logs.append(rec)
        elapsed_h = (now_fn() - start_ms) / (1000.0 * 60.0 * 60.0)
        if elapsed_h >= next_snapshot_h and next_snapshot_h <= duration_hours:
            # Write snapshot
            path = os.path.join(snapshot_dir, f"snapshot_{next_snapshot_h:02d}.json")
            with open(path, "w", encoding="utf-8") as f:
                json.dump({"logs": logs[-100:]}, f, sort_keys=True, separators=(",", ":"))
            next_snapshot_h += 1
        if elapsed_h >= duration_hours:
            break
        # Sleep lightly (no-op in tests if now_fn is mocked)
        time.sleep(0.001)
    return logs
