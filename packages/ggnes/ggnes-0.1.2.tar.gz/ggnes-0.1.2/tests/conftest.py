import pytest

try:
    import torch  # type: ignore  # noqa: F401

    HAS_TORCH = True
except Exception:
    HAS_TORCH = False


def pytest_collection_modifyitems(items):  # noqa: D401
    """Dynamically skip translation-dependent tests when PyTorch is unavailable."""
    if HAS_TORCH:
        return

    skip_reason = pytest.mark.skip(
        reason="PyTorch not installed: skipping translation-dependent tests"
    )

    for item in items:
        nodeid = item.nodeid
        path = str(item.fspath)
        # Skip all tests under translation suite
        if "/tests/test_translation/" in path or "tests/test_translation/" in nodeid:
            item.add_marker(skip_reason)
            continue
        # Skip specific hierarchical test that imports torch
        if (
            "test_hierarchical/test_parallel_hierarchical.py::test_hg_translation_parity_serial_vs_parallel"
            in nodeid
        ):
            item.add_marker(skip_reason)
            continue
        # Defensive: skip any test names that clearly involve pytorch translation
        if "pytorch" in nodeid or "backend_parity" in nodeid:
            item.add_marker(skip_reason)
