"""Genotype class for evolutionary engine (project_guide.md §9.1)."""

from __future__ import annotations

import uuid
from copy import deepcopy
from dataclasses import dataclass, field
from typing import Any


@dataclass
class Genotype:
    """Genetic representation as ordered list of rules.

    Attributes:
        genotype_id: Unique identifier for this genotype
        rules: Ordered list of rules forming the grammar
        fitness: Optional fitness value assigned by evaluation
        repair_impact: Aggregate repair impact for this genotype
        history: Additional bookkeeping data
    """

    genotype_id: uuid.UUID = field(default_factory=uuid.uuid4)
    rules: list[Any] = field(default_factory=list)
    fitness: float | None = None
    repair_impact: float = 0.0
    history: dict = field(default_factory=dict)

    # Minimal API expected by tests/workflows
    def add_rule(self, rule: Any) -> None:
        """Append a rule to this genotype."""
        self.rules.append(rule)

    def clone(self) -> Genotype:
        """Return a deep copy with a new genotype_id."""
        g = deepcopy(self)
        g.genotype_id = uuid.uuid4()
        return g

    def to_dict(self) -> dict:
        """Serialize genotype to a simple dict."""
        return {
            "genotype_id": str(self.genotype_id),
            "rules": [getattr(r, "rule_id", None) for r in self.rules],
            "fitness": self.fitness,
            "repair_impact": self.repair_impact,
            "history": dict(self.history),
        }

    @classmethod
    def from_dict(cls, data: dict) -> Genotype:
        """Deserialize from dict (rules kept as IDs/placeholders)."""
        g = cls()
        try:
            gid = data.get("genotype_id")
            if gid:
                g.genotype_id = uuid.UUID(str(gid))
        except Exception:
            # keep auto-generated id
            pass
        # Rules list can be populated by higher-level loaders if needed
        return g

    def __lt__(self, other: Any) -> bool:
        """Provide a deterministic ordering for Genotype instances.

        Enables sorting of tuples like (fitness, genotype) without TypeError
        when fitness ties occur, by comparing stable genotype identifiers.
        """
        try:
            sid = str(getattr(self, "genotype_id", ""))
            oid = str(getattr(other, "genotype_id", ""))
            if not sid:
                sid = str(id(self))
            if not oid:
                oid = str(id(other))
            return sid < oid
        except Exception:
            return id(self) < id(other)


__all__ = ["Genotype"]
