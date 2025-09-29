from __future__ import annotations

import hashlib

import numpy as np


def unit(vector: np.ndarray, eps: float = 1e-12) -> np.ndarray:
	norm = np.linalg.norm(vector) + eps
	return vector / norm


def batch_unit(matrix: np.ndarray, eps: float = 1e-12) -> np.ndarray:
	norms = np.linalg.norm(matrix, axis=1, keepdims=True) + eps
	return matrix / norms


def cosine_matrix(left: np.ndarray, right: np.ndarray) -> np.ndarray:
	left_unit = batch_unit(left)
	right_unit = batch_unit(right)
	return left_unit @ right_unit.T


def stable_hash_embedding(text: str, dim: int = 384) -> np.ndarray:
	"""Compute a deterministic SHA-256 based embedding."""

	values = np.empty(dim, dtype=np.float32)
	tokens = text.split() or ["<EMPTY>"]
	for idx in range(dim):
		token = tokens[idx % len(tokens)]
		digest = hashlib.sha256(f"{token}::{idx}".encode()).digest()
		encoded = int.from_bytes(digest[:8], "big", signed=False)
		values[idx] = (encoded / 2**63) - 1.0
	return unit(values)


def tfidf_matrix(corpus: list[str], max_features: int = 5000) -> tuple[np.ndarray, object]:
	"""Return a TF-IDF matrix for the given corpus.

	Raises a RuntimeError if scikit-learn is not available.
	"""

	try:
		from sklearn.feature_extraction.text import TfidfVectorizer
	except Exception as exc:  # pragma: no cover - import error path
		raise RuntimeError("Install with [text] extra to use TF-IDF") from exc

	vectorizer = TfidfVectorizer(max_features=max_features)
	matrix = vectorizer.fit_transform(corpus)
	return matrix.toarray(), vectorizer
