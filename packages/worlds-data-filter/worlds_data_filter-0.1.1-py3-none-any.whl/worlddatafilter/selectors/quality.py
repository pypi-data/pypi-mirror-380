from __future__ import annotations

import numpy as np


def quality_text(
    lengths: list[float] | np.ndarray,
    printable_ratios: list[float] | np.ndarray,
) -> np.ndarray:
    lengths_array = np.asarray(lengths, dtype=float)
    printable_array = np.asarray(printable_ratios, dtype=float)

    length_window = np.clip(lengths_array, 0, 2000)
    length_center = np.exp(-((length_window - 600.0) ** 2) / (2 * (400.0**2)))
    printable_score = np.clip(printable_array, 0.0, 1.0)
    return 0.5 * length_center + 0.5 * printable_score
