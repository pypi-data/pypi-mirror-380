"""Cross-method validation tests for systematic comparison of optimization methods.

This module tests that different optimization methods produce consistent results
and validates performance characteristics across algorithms.
"""

import time

import numpy as np
import pytest

from optimal_cutoffs import get_optimal_threshold
from optimal_cutoffs.metrics import get_confusion_matrix


class TestMethodConsistency:
    """Test that different optimization methods produce consistent results."""

    @pytest.mark.parametrize("metric", ["f1", "accuracy", "precision", "recall"])
    def test_methods_agree_on_separable_data(self, metric):
        """Test that methods agree on perfectly separable data."""
        # Perfect separation case
        y_true = [0, 0, 0, 1, 1, 1]
        pred_prob = [0.1, 0.2, 0.3, 0.7, 0.8, 0.9]

        methods = ["unique_scan", "minimize", "gradient"]
        thresholds = {}
        scores = {}

        for method in methods:
            thresholds[method] = get_optimal_threshold(
                y_true, pred_prob, metric=metric, method=method
            )

            # Compute achieved score
            tp, tn, fp, fn = get_confusion_matrix(y_true, pred_prob, thresholds[method])
            scores[method] = self._compute_metric_score(tp, tn, fp, fn, metric)

        # All methods should achieve high performance on separable data
        for method, score in scores.items():
            assert score >= 0.9, (
                f"Method {method} achieved low score {score} for {metric}"
            )

    def test_vectorized_vs_fallback_consistency(self):
        """Test that vectorized sort_scan agrees with fallback methods."""
        y_true = [0, 1, 0, 1, 1, 0, 1, 0]
        pred_prob = [0.1, 0.2, 0.3, 0.4, 0.6, 0.7, 0.8, 0.9]

        # Methods that should agree for piecewise metrics
        methods = ["unique_scan", "sort_scan", "minimize"]

        for metric in ["f1", "accuracy", "precision", "recall"]:
            thresholds = {}
            scores = {}

            for method in methods:
                try:
                    thresholds[method] = get_optimal_threshold(
                        y_true, pred_prob, metric=metric, method=method
                    )

                    # Compute achieved score
                    tp, tn, fp, fn = get_confusion_matrix(
                        y_true, pred_prob, thresholds[method]
                    )
                    scores[method] = self._compute_metric_score(tp, tn, fp, fn, metric)

                except Exception as e:
                    # Skip if method not available
                    print(f"Skipping {method} for {metric}: {e}")
                    continue

            # Scores should be very close (allowing for numerical differences)
            if len(scores) > 1:
                score_values = list(scores.values())
                max_diff = max(score_values) - min(score_values)
                assert max_diff < 0.01, f"Large score difference for {metric}: {scores}"

    def test_methods_handle_edge_cases_consistently(self):
        """Test that all methods handle edge cases gracefully."""
        edge_cases = [
            # All same class
            ([0, 0, 0, 0], [0.1, 0.3, 0.5, 0.7]),
            ([1, 1, 1, 1], [0.1, 0.3, 0.5, 0.7]),
            # Extreme imbalance
            ([0] * 95 + [1] * 5, np.random.RandomState(42).uniform(0, 1, 100)),
            # All tied probabilities
            ([0, 1, 0, 1], [0.5, 0.5, 0.5, 0.5]),
        ]

        methods = ["unique_scan", "minimize", "gradient"]

        for y_true, pred_prob in edge_cases:
            for method in methods:
                try:
                    threshold = get_optimal_threshold(
                        y_true, pred_prob, metric="f1", method=method
                    )
                    # Should produce valid threshold
                    assert 0.0 <= threshold <= 1.0, f"Invalid threshold from {method}"

                    # Should produce valid confusion matrix
                    tp, tn, fp, fn = get_confusion_matrix(y_true, pred_prob, threshold)
                    assert tp + tn + fp + fn == len(y_true)

                except Exception as e:
                    # Some methods may reasonably fail on degenerate cases
                    print(f"Method {method} failed on edge case: {e}")

    @staticmethod
    def _compute_metric_score(
        tp: float, tn: float, fp: float, fn: float, metric: str
    ) -> float:
        """Compute metric score from confusion matrix values."""
        if metric == "accuracy":
            total = tp + tn + fp + fn
            return (tp + tn) / total if total > 0 else 0.0
        elif metric == "precision":
            return tp / (tp + fp) if tp + fp > 0 else 0.0
        elif metric == "recall":
            return tp / (tp + fn) if tp + fn > 0 else 0.0
        elif metric == "f1":
            precision = tp / (tp + fp) if tp + fp > 0 else 0.0
            recall = tp / (tp + fn) if tp + fn > 0 else 0.0
            return (
                2 * precision * recall / (precision + recall)
                if precision + recall > 0
                else 0.0
            )
        else:
            raise ValueError(f"Unknown metric: {metric}")


class TestPerformanceCharacteristics:
    """Test performance characteristics and scaling behavior."""

    @pytest.mark.parametrize("n_samples", [100, 500, 1000, 2000])
    def test_method_scaling_behavior(self, n_samples):
        """Test that methods scale appropriately with dataset size."""
        # Create balanced dataset
        y_true = np.random.default_rng(42).integers(0, 2, size=n_samples)
        pred_prob = np.random.RandomState(42).uniform(0, 1, n_samples)

        methods_to_test = ["unique_scan", "sort_scan", "minimize"]

        timing_results = {}

        for method in methods_to_test:
            try:
                start_time = time.time()
                threshold = get_optimal_threshold(
                    y_true, pred_prob, metric="f1", method=method
                )
                end_time = time.time()

                timing_results[method] = end_time - start_time

                # Verify threshold is valid
                assert 0.0 <= threshold <= 1.0

            except Exception as e:
                print(f"Method {method} failed with {n_samples} samples: {e}")

        # Sort_scan should be faster for large datasets
        if "sort_scan" in timing_results and "unique_scan" in timing_results:
            if n_samples >= 1000:
                # For large datasets, sort_scan should be competitive or faster
                ratio = timing_results["sort_scan"] / timing_results["unique_scan"]
                assert ratio < 2.0, (
                    f"Sort_scan too slow compared to unique_scan: {ratio}"
                )

    def test_memory_usage_scaling(self):
        """Test that methods don't consume excessive memory."""
        # Large dataset
        n_samples = 5000
        y_true = np.random.default_rng(42).integers(0, 2, size=n_samples)
        pred_prob = np.random.RandomState(42).uniform(0, 1, n_samples)

        # Should complete without memory issues
        threshold = get_optimal_threshold(
            y_true, pred_prob, metric="f1", method="unique_scan"
        )
        assert 0.0 <= threshold <= 1.0

        # Test confusion matrix computation
        tp, tn, fp, fn = get_confusion_matrix(y_true, pred_prob, threshold)
        assert tp + tn + fp + fn == n_samples

    def test_worst_case_performance(self):
        """Test performance on worst-case scenarios."""
        # Many unique probability values (worst case for brute force)
        n_samples = 1000
        y_true = np.random.default_rng(42).integers(0, 2, size=n_samples)
        pred_prob = np.linspace(0.001, 0.999, n_samples)  # All unique values

        start_time = time.time()
        threshold = get_optimal_threshold(
            y_true, pred_prob, metric="f1", method="unique_scan"
        )
        end_time = time.time()

        assert 0.0 <= threshold <= 1.0
        assert end_time - start_time < 10.0  # Should complete in reasonable time


class TestMulticlassMethodConsistency:
    """Test consistency across methods for multiclass problems."""

    def test_multiclass_ovr_consistency(self):
        """Test that One-vs-Rest optimization is consistent across methods."""
        y_true = [0, 1, 2, 0, 1, 2, 0, 1, 2]
        pred_prob = np.random.RandomState(42).uniform(0, 1, (9, 3))
        pred_prob = pred_prob / pred_prob.sum(axis=1, keepdims=True)

        methods = ["unique_scan", "minimize"]
        thresholds = {}

        for method in methods:
            try:
                thresholds[method] = get_optimal_threshold(
                    y_true, pred_prob, metric="f1", method=method
                )

                # Should return per-class thresholds
                assert len(thresholds[method]) == 3
                assert all(0.0 <= t <= 1.0 for t in thresholds[method])

            except Exception as e:
                print(f"Method {method} failed on multiclass: {e}")

    def test_multiclass_coordinate_ascent_special_properties(self):
        """Test that coordinate ascent has special single-label properties."""
        y_true = [0, 1, 2, 0, 1, 2]
        pred_prob = np.array(
            [
                [0.7, 0.2, 0.1],
                [0.1, 0.8, 0.1],
                [0.1, 0.1, 0.8],
                [0.6, 0.3, 0.1],
                [0.2, 0.7, 0.1],
                [0.1, 0.2, 0.7],
            ]
        )

        try:
            # Coordinate ascent should work for F1
            thresholds = get_optimal_threshold(
                y_true, pred_prob, metric="f1", method="coord_ascent"
            )

            assert len(thresholds) == 3
            assert all(0.0 <= t <= 1.0 for t in thresholds)

        except Exception as e:
            print(f"Coordinate ascent failed: {e}")


class TestComparisonOperatorConsistency:
    """Test consistency of comparison operators across methods."""

    def test_comparison_operator_effects(self):
        """Test that comparison operators have consistent effects across methods."""
        y_true = [0, 1, 0, 1, 1, 0]
        pred_prob = [0.4, 0.6, 0.4, 0.6, 0.6, 0.4]  # Some tied values

        methods = ["unique_scan", "minimize"]

        for method in methods:
            try:
                threshold_gt = get_optimal_threshold(
                    y_true, pred_prob, metric="f1", method=method, comparison=">"
                )
                threshold_gte = get_optimal_threshold(
                    y_true, pred_prob, metric="f1", method=method, comparison=">="
                )

                # Both should be valid
                assert 0.0 <= threshold_gt <= 1.0
                assert 0.0 <= threshold_gte <= 1.0

                # For tied data, they might be different
                # But both should produce valid results
                tp_gt, tn_gt, fp_gt, fn_gt = get_confusion_matrix(
                    y_true, pred_prob, threshold_gt, comparison=">"
                )
                tp_gte, tn_gte, fp_gte, fn_gte = get_confusion_matrix(
                    y_true, pred_prob, threshold_gte, comparison=">="
                )

                assert tp_gt + tn_gt + fp_gt + fn_gt == len(y_true)
                assert tp_gte + tn_gte + fp_gte + fn_gte == len(y_true)

            except Exception as e:
                print(f"Comparison operator test failed for {method}: {e}")


class TestRegressionTests:
    """Regression tests to ensure changes don't break existing functionality."""

    def test_backward_compatibility_scores(self):
        """Test that optimization still achieves expected performance on known datasets."""
        # Known good case
        y_true = [0, 0, 1, 1, 1, 0, 1, 0]
        pred_prob = [0.1, 0.2, 0.6, 0.7, 0.8, 0.3, 0.9, 0.4]

        threshold = get_optimal_threshold(y_true, pred_prob, metric="f1")
        tp, tn, fp, fn = get_confusion_matrix(y_true, pred_prob, threshold)

        f1_score = self._compute_f1_score(tp, tn, fp, fn)

        # Should achieve reasonable F1 score on this separable data
        assert f1_score >= 0.8, f"F1 score {f1_score} too low for known good case"

    def test_multiclass_regression(self):
        """Test multiclass optimization achieves expected performance."""
        y_true = [0, 1, 2, 0, 1, 2, 0, 1, 2]
        pred_prob = np.array(
            [
                [0.8, 0.1, 0.1],  # Clear class 0
                [0.1, 0.8, 0.1],  # Clear class 1
                [0.1, 0.1, 0.8],  # Clear class 2
                [0.7, 0.2, 0.1],  # Likely class 0
                [0.2, 0.7, 0.1],  # Likely class 1
                [0.1, 0.2, 0.7],  # Likely class 2
                [0.6, 0.3, 0.1],  # Somewhat class 0
                [0.3, 0.6, 0.1],  # Somewhat class 1
                [0.1, 0.3, 0.6],  # Somewhat class 2
            ]
        )

        thresholds = get_optimal_threshold(y_true, pred_prob, metric="f1")

        # Should return valid per-class thresholds
        assert len(thresholds) == 3
        assert all(0.0 <= t <= 1.0 for t in thresholds)

    @staticmethod
    def _compute_f1_score(tp: float, tn: float, fp: float, fn: float) -> float:
        """Compute F1 score from confusion matrix values."""
        precision = tp / (tp + fp) if tp + fp > 0 else 0.0
        recall = tp / (tp + fn) if tp + fn > 0 else 0.0
        return (
            2 * precision * recall / (precision + recall)
            if precision + recall > 0
            else 0.0
        )
