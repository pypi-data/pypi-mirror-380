import torch


def _toy():
    X = torch.randn(64, 8)
    y = X @ torch.randn(8, 1) + 0.1 * torch.randn(64, 1)
    Xv = torch.randn(32, 8)
    yv = Xv @ torch.randn(8, 1) + 0.1 * torch.randn(32, 1)
    return (X, y), (Xv, yv)


def test_search_multiobjective_interface():
    from ggnes.api.mvp import Search, LatencyObjective

    (X, y), (Xv, yv) = _toy()
    search = Search(
        smoke=True,
        seed=11,
        objective=None,
    )
    # Provide multiple objectives via list (including latency)
    search.objectives = [("val_mse", "min"), ("params", "min"), LatencyObjective(device="cpu")]
    res = search.fit(X, y, validation_data=(Xv, yv))
    assert hasattr(res, "pareto")
    assert isinstance(res.pareto, list) and len(res.pareto) >= 1
    top = res.pareto[0]
    assert isinstance(top, dict) and "objectives" in top
    objs = top["objectives"]
    assert "val_mse" in objs and isinstance(objs["val_mse"], float)
    assert "params" in objs and isinstance(objs["params"], float)
    assert "latency_ms" in objs and isinstance(objs["latency_ms"], float)


def test_repro_bundle_contains_minimal_expected_files(tmp_path):
    from ggnes.api.mvp import Search, ReproBundle

    (X, y), (Xv, yv) = _toy()
    s = Search(smoke=True, seed=22)
    res = s.fit(X, y, validation_data=(Xv, yv))
    out_zip = tmp_path / "bundle.zip"
    rb = ReproBundle.export(res.artifacts, out_path=str(out_zip))
    names = set(rb.contents())
    assert "config.json" in names and "evolution_history.json" in names and "repro_manifest.json" in names
    ReproBundle.verify(str(out_zip))


def test_pareto_multiple_candidates_when_population_gt1():
    from ggnes.api.mvp import Search, LatencyObjective

    (X, y), (Xv, yv) = _toy()
    s = Search(smoke=True, seed=33, objective=None, generations=1, population=2)
    s.objectives = [("val_mse", "min"), ("params", "min"), LatencyObjective(device="cpu")]
    res = s.fit(X, y, validation_data=(Xv, yv))
    assert isinstance(res.pareto, list) and len(res.pareto) >= 2
    # Entries should be dicts with 'objectives'
    for entry in res.pareto[:2]:
        assert isinstance(entry, dict) and "objectives" in entry


def test_starter_space_attention_contains_attention_rule():
    from ggnes.api.mvp import starter_space
    sp = starter_space("attention_tabular")
    names = [getattr(getattr(r, "metadata", {}), "get", lambda *_: None)("name") for r in sp.rules]
    # Either metadata carries name or rules include attention via any attribute
    has_attention = any("attention" in str(n) for n in names)
    assert has_attention or any("attention" in str(getattr(r, "metadata", {})) for r in sp.rules)


def test_constraints_evaluated_smoke():
    from ggnes.api.mvp import Search
    (X, y), (Xv, yv) = _toy()
    s = Search(smoke=True, seed=44)
    s.constraints = [("is_dag", True), ("max_nodes", 10)]
    res = s.fit(X, y, validation_data=(Xv, yv))
    assert hasattr(res, "constraints") and isinstance(res.constraints, dict)
    assert res.constraints.get("is_dag") is True
    assert res.constraints.get("within_size") is True


def test_pareto_has_ranks():
    from ggnes.api.mvp import Search, LatencyObjective
    (X, y), (Xv, yv) = _toy()
    s = Search(smoke=True, seed=55, objective=None, generations=1, population=2)
    s.objectives = [("val_mse", "min"), LatencyObjective(device="cpu")]
    res = s.fit(X, y, validation_data=(Xv, yv))
    assert isinstance(res.pareto, list) and len(res.pareto) >= 2
    for entry in res.pareto:
        assert isinstance(entry.get("rank"), int)


def test_constraints_penalty_when_violated():
    from ggnes.api.mvp import Search
    (X, y), (Xv, yv) = _toy()
    s = Search(smoke=True, seed=66)
    # Force a too-small max_nodes to trigger violation (baseline graph has 3 nodes)
    s.constraints = [("max_nodes", 2)]
    res = s.fit(X, y, validation_data=(Xv, yv))
    assert isinstance(res.pareto, list) and len(res.pareto) >= 1
    objs = res.pareto[0]["objectives"]
    assert "constraint_penalty" in objs and objs["constraint_penalty"] > 0.0


def test_search_space_influences_fingerprint():
    from ggnes.api.mvp import Search, starter_space, wl_fingerprint
    (X, y), (Xv, yv) = _toy()
    # Baseline (dense)
    s1 = Search(smoke=True, seed=77, search_space=starter_space("tabular_dense"))
    r1 = s1.fit(X, y, validation_data=(Xv, yv))
    fp1 = wl_fingerprint(r1)
    # Attention preset should alter resulting architecture (different WL)
    s2 = Search(smoke=True, seed=77, search_space=starter_space("attention_tabular"))
    r2 = s2.fit(X, y, validation_data=(Xv, yv))
    fp2 = wl_fingerprint(r2)
    assert fp1 != fp2


def test_generation_smoke_produces_distinct_params():
    from ggnes.api.mvp import Search, LatencyObjective, starter_space
    (X, y), (Xv, yv) = _toy()
    s = Search(smoke=True, seed=88, objective=None, generations=1, population=2, search_space=starter_space("attention_tabular"))
    s.objectives = [("params", "min"), LatencyObjective(device="cpu")]
    s.use_generation_smoke = True
    res = s.fit(X, y, validation_data=(Xv, yv))
    assert isinstance(res.pareto, list) and len(res.pareto) == 2
    p0 = res.pareto[0]["objectives"]["params"]
    p1 = res.pareto[1]["objectives"]["params"]
    assert p0 != p1


def test_nsga_penalizes_violators_when_constraint_set():
    from ggnes.api.mvp import Search, LatencyObjective
    (X, y), (Xv, yv) = _toy()
    s = Search(smoke=True, seed=99, objective=None, generations=1, population=2)
    s.objectives = [("params", "min"), LatencyObjective(device="cpu")]
    s.constraints = [("max_nodes", 2)]  # baseline graph violates (3 nodes)
    res = s.fit(X, y, validation_data=(Xv, yv))
    assert isinstance(res.pareto, list) and len(res.pareto) >= 1
    for entry in res.pareto:
        objs = entry["objectives"]
        assert "constraint_penalty" in objs and objs["constraint_penalty"] > 0


def test_real_generation_smoke_produces_distinct_params():
    from ggnes.api.mvp import Search, starter_space
    (X, y), (Xv, yv) = _toy()
    s = Search(smoke=True, seed=101, objective=None, generations=1, population=2, search_space=starter_space("attention_tabular"))
    s.objectives = [("params", "min")]
    s.use_real_generation_smoke = True
    res = s.fit(X, y, validation_data=(Xv, yv))
    assert isinstance(res.pareto, list) and len(res.pareto) == 2
    params = [e["objectives"]["params"] for e in res.pareto]
    assert len(set(params)) >= 2


def test_real_nsga_over_generated_candidates():
    from ggnes.api.mvp import Search, starter_space, LatencyObjective
    (X, y), (Xv, yv) = _toy()
    s = Search(
        smoke=True,
        seed=202,
        objective=None,
        generations=1,
        population=3,
        search_space=starter_space("attention_tabular"),
    )
    s.objectives = [("params", "min"), LatencyObjective(device="cpu")]
    s.use_real_generation_nsga = True
    res = s.fit(X, y, validation_data=(Xv, yv))
    assert isinstance(res.pareto, list) and len(res.pareto) <= 3 and len(res.pareto) >= 1
    for entry in res.pareto:
        assert isinstance(entry.get("rank"), int)


def test_real_nsga_includes_val_mse():
    from ggnes.api.mvp import Search, starter_space
    (X, y), (Xv, yv) = _toy()
    s = Search(smoke=True, seed=303, objective=None, generations=1, population=2, search_space=starter_space("tabular_dense"))
    s.objectives = [("val_mse", "min")]
    s.use_real_generation_nsga = True
    res = s.fit(X, y, validation_data=(Xv, yv))
    assert isinstance(res.pareto, list) and len(res.pareto) >= 1
    assert "val_mse" in res.pareto[0]["objectives"]


def test_real_nsga_constraint_penalty_per_candidate():
    from ggnes.api.mvp import Search, starter_space
    (X, y), (Xv, yv) = _toy()
    s = Search(smoke=True, seed=404, objective=None, generations=1, population=2, search_space=starter_space("tabular_dense"))
    s.objectives = [("params", "min"), ("val_mse", "min")]
    s.constraints = [("max_nodes", 2)]
    s.use_real_generation_nsga = True
    res = s.fit(X, y, validation_data=(Xv, yv))
    assert isinstance(res.pareto, list) and len(res.pareto) >= 1
    assert "constraint_penalty" in res.pareto[0]["objectives"]


