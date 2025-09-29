import os
import json
import torch


def _make_data(n=128, d=8):
    X = torch.randn(n, d)
    # simple linear target with noise
    w = torch.randn(d, 1)
    y = X @ w + 0.1 * torch.randn(n, 1)
    return X, y


def test_search_smoke_cpu(tmp_path):
    from ggnes.api.mvp import Search, wl_fingerprint

    X, y = _make_data(64, 8)
    X_val, y_val = _make_data(32, 8)
    X_test, y_test = _make_data(32, 8)

    s = Search(smoke=True, seed=123)
    res = s.fit(X, y, validation_data=(X_val, y_val), test_data=(X_test, y_test))

    assert res.model is not None
    assert isinstance(res.metrics.get("val_mse"), float)
    assert isinstance(res.metrics.get("test_mse"), float)

    fp = wl_fingerprint(res.best_architecture)
    assert isinstance(fp, str) and len(fp) >= 16


def test_rule_and_search_space_exist():
    from ggnes.api.mvp import rule, SearchSpace
    sp = SearchSpace()
    r = rule(
        name="add_dense_16_relu",
        lhs={"node_type": "HIDDEN"},
        add_nodes=[{"node_type": "HIDDEN", "activation": "relu", "output_size": 16}],
        add_edges=[("LHSPREV", "NEW")],
        probability=0.5,
    )
    sp.add(r)
    assert len(sp.rules) == 1


def test_starter_space_returns_space():
    from ggnes.api.mvp import starter_space
    sp = starter_space("tabular_dense")
    assert hasattr(sp, "rules") and len(sp.rules) > 0


def test_determinism_signature(tmp_path):
    from ggnes.api.mvp import Search, DeterminismSignature
    X, y = _make_data(32, 8)
    Xv, yv = _make_data(16, 8)
    s1 = Search(smoke=True, seed=7)
    s2 = Search(smoke=True, seed=7)
    r1 = s1.fit(X, y, validation_data=(Xv, yv))
    r2 = s2.fit(X, y, validation_data=(Xv, yv))
    sig1 = DeterminismSignature.compute(r1)
    sig2 = DeterminismSignature.compute(r2)
    DeterminismSignature.assert_equal(sig1, sig2)


def test_repro_bundle_export_and_verify(tmp_path):
    from ggnes.api.mvp import ReproBundle
    # Create fake artifacts directory
    artifacts_dir = tmp_path / "artifacts"
    artifacts_dir.mkdir()
    (artifacts_dir / "config.json").write_text(json.dumps({"ok": True}))
    (artifacts_dir / "evolution_history.json").write_text(json.dumps([]))
    (artifacts_dir / "repro_manifest.json").write_text(json.dumps({"sig": "x"}))

    out_zip = tmp_path / "bundle.zip"
    bundle = ReproBundle.export(str(artifacts_dir), out_path=str(out_zip))
    assert os.path.exists(str(out_zip))
    # verify should not throw
    ReproBundle.verify(str(out_zip))


def test_latency_objective_smoke():
    from ggnes.api.mvp import LatencyObjective
    lo = LatencyObjective(device="cpu", dtype="float32")
    # Minimal call: pass a tiny model and inputs
    model = torch.nn.Linear(8, 1)
    x = torch.randn(4, 8)
    ms = lo.measure(model, x)
    assert isinstance(ms, float) and ms >= 0.0


