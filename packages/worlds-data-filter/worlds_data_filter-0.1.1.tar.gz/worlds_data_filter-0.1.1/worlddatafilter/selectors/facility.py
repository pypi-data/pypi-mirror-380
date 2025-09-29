from __future__ import annotations

import numpy as np


def facility_location_gains(selected: list[int], similarity: np.ndarray) -> np.ndarray:
    """Compute marginal gains for adding each item given current selections."""

    if not selected:
        return similarity.max(axis=1)

    cover = np.max(similarity[selected, :], axis=0)
    gains = np.maximum(0.0, similarity - cover[None, :]).sum(axis=1)
    gains[np.asarray(selected, dtype=int)] = -np.inf
    return gains


def greedy_facility_selection(similarity: np.ndarray, k: int) -> list[int]:
    selected: list[int] = []
    for _ in range(min(k, similarity.shape[0])):
        gains = facility_location_gains(selected, similarity)
        candidate = int(np.argmax(gains))
        if not selected and not np.isfinite(gains[candidate]):
            candidate = int(np.argmax(similarity.sum(axis=1)))
        if np.isfinite(gains[candidate]) and gains[candidate] <= 1e-9 and selected:
            break
        selected.append(candidate)
    return selected
