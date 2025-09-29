from __future__ import annotations

from abc import ABC, abstractmethod

import numpy as np

from ..types import Item
from ..utils import batch_unit, stable_hash_embedding, tfidf_matrix


class BaseExtractor(ABC):
    @abstractmethod
    def features(self, items: list[Item]) -> tuple[np.ndarray, list[dict[str, object]]]:
        """Return (X, aux) where X is (N,d) feature matrix and aux per-item metadata dicts."""


class TextExtractor(BaseExtractor):
    def __init__(self, method: str = "hash", dim: int = 384) -> None:
        self.method = method
        self.dim = dim

    def features(self, items: list[Item]) -> tuple[np.ndarray, list[dict[str, object]]]:
        texts = [item.text or "" for item in items]
        aux: list[dict[str, object]] = []

        if self.method == "tfidf":
            matrix, _ = tfidf_matrix(texts)
        else:
            matrix = np.vstack(
                [stable_hash_embedding(text, dim=self.dim) for text in texts],
            )

        for text in texts:
            printable = sum(char.isprintable() for char in text)
            aux.append(
                {
                    "length": len(text),
                    "printable_ratio": printable / max(1, len(text)),
                },
            )

        return batch_unit(matrix), aux
