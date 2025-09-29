from __future__ import annotations

import numpy as np


def novelty_scores(matrix: np.ndarray) -> np.ndarray:
    """Compute novelty as distance from centroid (z-scored)."""
    mu = matrix.mean(axis=0, keepdims=True)
    distances = np.linalg.norm(matrix - mu, axis=1)
    # z-score
    mean, std = distances.mean(), distances.std() + 1e-9
    z = (distances - mean) / std
    # map to [0,1] via sigmoid
    return 1.0 / (1.0 + np.exp(-z))
