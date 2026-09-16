from __future__ import annotations

import importlib.util
from pathlib import Path
import sys
import unittest

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("fedavg_reference", ROOT / "examples" / "fedavg_reference.py")
assert SPEC and SPEC.loader
module = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = module
SPEC.loader.exec_module(module)

ClientUpdate = module.ClientUpdate
fedavg = module.fedavg


class FedAvgTests(unittest.TestCase):
    def test_equal_client_sizes_reduce_to_arithmetic_mean(self):
        updates = [
            ClientUpdate(np.array([[1.0, 3.0]]), np.array([1.0]), 10),
            ClientUpdate(np.array([[3.0, 5.0]]), np.array([3.0]), 10),
        ]
        coef, intercept = fedavg(updates)
        np.testing.assert_allclose(coef, [[2.0, 4.0]])
        np.testing.assert_allclose(intercept, [2.0])

    def test_unequal_sizes_use_sample_weighting(self):
        updates = [
            ClientUpdate(np.array([[0.0]]), np.array([0.0]), 1),
            ClientUpdate(np.array([[10.0]]), np.array([20.0]), 3),
        ]
        coef, intercept = fedavg(updates)
        np.testing.assert_allclose(coef, [[7.5]])
        np.testing.assert_allclose(intercept, [15.0])

    def test_reference_sample_counts_match_documented_weights(self):
        counts = np.array([1200, 1800, 900, 1400], dtype=float)
        weights = counts / counts.sum()
        np.testing.assert_allclose(weights, [0.22641509, 0.33962264, 0.16981132, 0.26415094])
        self.assertAlmostEqual(float(weights.sum()), 1.0)

    def test_single_client_is_identity(self):
        update = ClientUpdate(np.array([[2.0, -1.0]]), np.array([0.25]), 42)
        coef, intercept = fedavg([update])
        np.testing.assert_allclose(coef, update.coef)
        np.testing.assert_allclose(intercept, update.intercept)

    def test_rejects_empty_updates(self):
        with self.assertRaises(ValueError):
            fedavg([])

    def test_rejects_non_positive_sample_counts(self):
        update = ClientUpdate(np.array([[1.0]]), np.array([0.0]), 0)
        with self.assertRaises(ValueError):
            fedavg([update])

    def test_rejects_incompatible_parameter_shapes(self):
        updates = [
            ClientUpdate(np.array([[1.0, 2.0]]), np.array([0.0]), 1),
            ClientUpdate(np.array([[1.0, 2.0, 3.0]]), np.array([0.0]), 1),
        ]
        with self.assertRaises(ValueError):
            fedavg(updates)


if __name__ == "__main__":
    unittest.main()
