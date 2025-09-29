from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class Item:
    id: str
    text: str | None = None
    meta: dict[str, Any] | None = None
    # raw fields for future adapters (e.g., tabular rows, JSON objects)


@dataclass
class ItemScore:
    id: str
    coverage_gain: float
    novelty: float
    quality: float
    combined: float
    explain: dict[str, Any] | None = None

    @property
    def value_score(self) -> float:
        """Alias for the combined value score."""
        return self.combined
