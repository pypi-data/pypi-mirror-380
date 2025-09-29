"""
Stub module for Island Model evolution.

This repository provides IslandScheduler and migration observability, but does not
include a high-level IslandModel API. This stub exists to make imports succeed in
tests and to raise ImportError upon use so tests can skip appropriately.
"""


class IslandModel:
    def __init__(self, *args, **kwargs):
        raise ImportError(
            "IslandModel is not included in this repository. "
            "Use ggnes.evolution.islands.IslandScheduler and observability reports instead."
        )

    # Define placeholders to document expected interface; never reached due to __init__.
    @property
    def num_islands(self):
        return 0

    @property
    def islands(self):
        return []

    def migrate(self, *args, **kwargs):
        raise ImportError(
            "IslandModel is not included in this repository. "
            "Use ggnes.evolution.islands.IslandScheduler and observability reports instead."
        )

    def evolve(self, *args, **kwargs):
        raise ImportError(
            "IslandModel is not included in this repository. "
            "Use ggnes.evolution.islands.IslandScheduler and observability reports instead."
        )
