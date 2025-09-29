from __future__ import annotations

import numpy as np

from .extractors.base import TextExtractor
from .selectors.facility import greedy_facility_selection
from .selectors.novelty import novelty_scores
from .selectors.quality import quality_text
from .types import Item, ItemScore
from .utils import cosine_matrix


class WorldDataFilter:
    def __init__(self, *, text_method: str = "hash", dim: int = 384) -> None:
        self.text_extractor = TextExtractor(method=text_method, dim=dim)

    def _features(self, items: list[Item]) -> tuple[np.ndarray, list[dict[str, object]]]:
        """Extract features and auxiliary metadata for the provided items."""
        return self.text_extractor.features(items)

    def score(
        self,
        items: list[Item],
        *,
        weights: dict[str, float] | None = None,
    ) -> list[ItemScore]:
        if not items:
            return []

        features, aux = self._features(items)
        similarity = cosine_matrix(features, features)

        max_candidates = min(features.shape[0], 100, max(1, features.shape[0] // 5))
        order = greedy_facility_selection(similarity, k=max_candidates)

        gains = np.zeros(features.shape[0], dtype=float)
        cover = np.zeros(features.shape[0], dtype=float)
        for idx in order:
            gains[idx] = np.maximum(0.0, similarity[idx, :] - cover).sum()
            cover = np.maximum(cover, similarity[idx, :])

        if gains.max() > 0:
            gains = gains / gains.max()

        novelty = novelty_scores(features)
        lengths = [meta.get("length", 0) for meta in aux]
        printable_ratio = [meta.get("printable_ratio", 1.0) for meta in aux]
        quality = quality_text(lengths, printable_ratio)

        combined_weights = {"cov": 0.7, "nov": 0.2, "qual": 0.1}
        if weights:
            combined_weights.update(weights)

        combined = (
            combined_weights["cov"] * gains
            + combined_weights["nov"] * novelty
            + combined_weights["qual"] * quality
        )

        scores: list[ItemScore] = []
        for idx, item in enumerate(items):
            scores.append(
                ItemScore(
                    id=item.id,
                    coverage_gain=float(gains[idx]),
                    novelty=float(novelty[idx]),
                    quality=float(quality[idx]),
                    combined=float(combined[idx]),
                    explain={
                        "length": lengths[idx],
                        "printable_ratio": printable_ratio[idx],
                    },
                ),
            )
        return scores

    def select(
        self,
        items: list[Item],
        *,
        k: int = 50,
        criterion: str = "value_score",
        weights: dict[str, float] | None = None,
        explain: bool = False,
    ) -> list[ItemScore]:
        alias_map = {"value_score": "combined"}
        resolved_criterion = alias_map.get(criterion, criterion)
        valid = {"combined", "coverage_gain", "novelty", "quality"}
        if resolved_criterion not in valid:
            raise ValueError(
                (
                    f"Invalid criterion '{criterion}'. Choose from value_score, "
                    "coverage_gain, novelty, quality."
                ),
            )

        scores = self.score(items, weights=weights)
        sorted_scores = sorted(
            scores,
            key=lambda score: getattr(score, resolved_criterion),
            reverse=True,
        )[:k]

        if not explain:
            for score in sorted_scores:
                score.explain = None
        return sorted_scores
