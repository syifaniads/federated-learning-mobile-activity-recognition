"""Minimal portfolio reference for weighted Federated Averaging.

This is a small explanatory implementation written for this portfolio.
The original collaborative project source remains linked in SOURCE_EVIDENCE.md.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class ClientUpdate:
    coef: np.ndarray
    intercept: np.ndarray
    n_samples: int


def fedavg(updates: list[ClientUpdate]) -> tuple[np.ndarray, np.ndarray]:
    """Aggregate compatible client parameters using sample-count weighting."""
    if not updates:
        raise ValueError("at least one client update is required")

    if any(update.n_samples <= 0 for update in updates):
        raise ValueError("n_samples must be positive")

    coef_shape = updates[0].coef.shape
    intercept_shape = updates[0].intercept.shape

    for update in updates:
        if update.coef.shape != coef_shape:
            raise ValueError("all coefficient matrices must have the same shape")
        if update.intercept.shape != intercept_shape:
            raise ValueError("all intercept vectors must have the same shape")

    total_samples = sum(update.n_samples for update in updates)
    global_coef = np.zeros(coef_shape, dtype=float)
    global_intercept = np.zeros(intercept_shape, dtype=float)

    for update in updates:
        weight = update.n_samples / total_samples
        global_coef += weight * update.coef
        global_intercept += weight * update.intercept

    return global_coef, global_intercept


if __name__ == "__main__":
    updates = [
        ClientUpdate(np.array([[1.0, 2.0]]), np.array([0.1]), 1200),
        ClientUpdate(np.array([[2.0, 4.0]]), np.array([0.2]), 1800),
        ClientUpdate(np.array([[3.0, 6.0]]), np.array([0.3]), 900),
        ClientUpdate(np.array([[4.0, 8.0]]), np.array([0.4]), 1400),
    ]

    coef, intercept = fedavg(updates)
    print("global coef:", coef)
    print("global intercept:", intercept)
