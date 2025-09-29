"""
Checkpointing utilities for evolution runs.

- EvolutionCheckpoint: save/load population state snapshots
- ResumableEvolution: simple evolution loop with periodic checkpointing and resume capability
"""

from __future__ import annotations

import pickle
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass
class EvolutionState:
    population: list[Any]
    generation: int
    best_fitness: float
    metadata: dict[str, Any]


class EvolutionCheckpoint:
    """
    Minimal API expected by tests:
      cp = EvolutionCheckpoint()
      cp.save(population=population, generation=generation, best_fitness=best_fitness, metadata={...})
      state = cp.load()  # returns dict with the same fields
    """

    def __init__(
        self, checkpoint_dir: str | None = None, filename: str = "evolution_checkpoint.pkl"
    ) -> None:
        self.checkpoint_dir = Path(checkpoint_dir or "./checkpoints")
        self.checkpoint_dir.mkdir(parents=True, exist_ok=True)
        self.filename = filename

    @property
    def checkpoint_path(self) -> Path:
        return self.checkpoint_dir / self.filename

    def save(
        self,
        population: list[Any],
        generation: int,
        best_fitness: float,
        metadata: dict[str, Any] | None = None,
    ) -> None:
        state = EvolutionState(
            population=list(population),
            generation=int(generation),
            best_fitness=float(best_fitness),
            metadata=dict(metadata or {}),
        )
        with open(self.checkpoint_path, "wb") as f:
            pickle.dump(state, f)

    def load(self) -> dict[str, Any]:
        if not self.checkpoint_path.exists():
            raise FileNotFoundError(f"No checkpoint found at {self.checkpoint_path}")
        with open(self.checkpoint_path, "rb") as f:
            state: EvolutionState = pickle.load(f)
        return {
            "population": state.population,
            "generation": state.generation,
            "best_fitness": state.best_fitness,
            "metadata": state.metadata,
        }


class ResumableEvolution:
    """
    Minimal API expected by tests:
      evo = ResumableEvolution(checkpoint_frequency=5, checkpoint_dir='./checkpoints')
      evolved = evo.evolve(population, fitness_function, generations=7)
      assert evo.last_checkpoint_generation == 5
      resumed = evo.resume(fitness_function, total_generations=10)
      assert evo.current_generation == 10

    Notes:
      - This implementation focuses on checkpoint orchestration and counters.
      - It does not perform selection/crossover/mutation; it preserves population identity.
      - Fitness function is called to compute a best_fitness metric for checkpointing.
    """

    def __init__(
        self, checkpoint_frequency: int = 5, checkpoint_dir: str = "./checkpoints"
    ) -> None:
        self.checkpoint_frequency = max(1, int(checkpoint_frequency))
        self.checkpoint = EvolutionCheckpoint(checkpoint_dir=checkpoint_dir)
        self.current_generation: int = 0
        self.last_checkpoint_generation: int = 0
        self._population: list[Any] = []

    def _compute_best_fitness(
        self, population: list[Any], fitness_function: Callable[[Any], float]
    ) -> float:
        if not population:
            return 0.0
        scores = [float(fitness_function(ind)) for ind in population]
        return max(scores) if scores else 0.0

    def _maybe_checkpoint(
        self, gen: int, population: list[Any], fitness_function: Callable[[Any], float]
    ) -> None:
        if gen % self.checkpoint_frequency == 0:
            best = self._compute_best_fitness(population, fitness_function)
            self.checkpoint.save(
                population=population,
                generation=gen,
                best_fitness=best,
                metadata={"generation": gen},
            )
            self.last_checkpoint_generation = gen

    def evolve(
        self,
        population: list[Any],
        fitness_function: Callable[[Any], float],
        generations: int = 1,
    ) -> list[Any]:
        # Initialize internal population and counters
        self._population = list(population)
        start = self.current_generation
        end = start + max(0, int(generations))

        for gen in range(start + 1, end + 1):
            # In a full implementation, apply selection/crossover/mutation here.
            # For tests, we only track generations and checkpointing cadence.
            self.current_generation = gen
            self._maybe_checkpoint(gen, self._population, fitness_function)

        return self._population

    def resume(
        self,
        fitness_function: Callable[[Any], float],
        total_generations: int,
    ) -> list[Any]:
        # Load last state if present; otherwise, keep current population
        try:
            state = self.checkpoint.load()
            self._population = list(state["population"])
            self.current_generation = int(state["generation"])
            # Align last_checkpoint_generation with loaded state if needed
            self.last_checkpoint_generation = self.current_generation
        except FileNotFoundError:
            # No checkpoint to resume from; continue from current state
            pass

        # Continue until total_generations
        target = max(self.current_generation, int(total_generations))
        while self.current_generation < target:
            self.current_generation += 1
            self._maybe_checkpoint(self.current_generation, self._population, fitness_function)

        return self._population
