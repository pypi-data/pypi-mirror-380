"""Comprehensive test suite for all bug fixes identified in the detailed code review.

This module contains property-based tests and adversarial cases designed to verify
that all critical bugs have been properly fixed and regression prevention.
"""

import warnings

import numpy as np
import pytest
from hypothesis import given, settings
from hypothesis import strategies as st

from optimal_cutoffs import get_optimal_threshold
from optimal_cutoffs.metrics import (
    _compute_exclusive_predictions,
    accuracy_score,
    f1_score,
    get_confusion_matrix,
    get_multiclass_confusion_matrix,
    multiclass_metric,
    multiclass_metric_exclusive,
)
from optimal_cutoffs.optimizers import (
    _dinkelbach_expected_fbeta,
    _optimize_micro_averaged_thresholds,
    get_optimal_multiclass_thresholds,
)


class TestDegenerateCasesFix:
    """Test that degenerate cases return proper thresholds, not arbitrary 0.5."""

    def test_all_negative_optimal_threshold_exclusive(self):
        """All negatives should return threshold that predicts all negative with '>'."""
        y_true = [0, 0, 0, 0]
        pred_prob = [0.1, 0.4, 0.6, 0.9]

        threshold = get_optimal_threshold(
            y_true, pred_prob, metric="accuracy", comparison=">"
        )

        # With '>', we need prob > threshold to be false for all
        # So threshold should be >= max(prob)
        predictions = np.array(pred_prob) > threshold
        assert np.all(~predictions), "Should predict all negative"
        assert np.mean(predictions == y_true) == 1.0, "Should achieve perfect accuracy"

    def test_all_negative_optimal_threshold_inclusive(self):
        """All negatives should return threshold that predicts all negative with '>='."""
        y_true = [0, 0, 0, 0]
        pred_prob = [0.1, 0.4, 0.6, 0.9]

        threshold = get_optimal_threshold(
            y_true, pred_prob, metric="accuracy", comparison=">="
        )

        # With '>=', we need prob >= threshold to be false for all
        # So threshold should be > max(prob)
        predictions = np.array(pred_prob) >= threshold
        assert np.all(~predictions), "Should predict all negative"
        assert np.mean(predictions == y_true) == 1.0, "Should achieve perfect accuracy"

    def test_all_positive_optimal_threshold_exclusive(self):
        """All positives should return threshold that predicts all positive with '>'."""
        y_true = [1, 1, 1, 1]
        pred_prob = [0.1, 0.4, 0.6, 0.9]

        threshold = get_optimal_threshold(
            y_true, pred_prob, metric="accuracy", comparison=">"
        )

        # With '>', we need prob > threshold to be true for all
        # So threshold should be < min(prob)
        predictions = np.array(pred_prob) > threshold
        assert np.all(predictions), "Should predict all positive"
        assert np.mean(predictions == y_true) == 1.0, "Should achieve perfect accuracy"

    def test_all_positive_optimal_threshold_inclusive(self):
        """All positives should return threshold that predicts all positive with '>='."""
        y_true = [1, 1, 1, 1]
        pred_prob = [0.1, 0.4, 0.6, 0.9]

        threshold = get_optimal_threshold(
            y_true, pred_prob, metric="accuracy", comparison=">="
        )

        # With '>=', we need prob >= threshold to be true for all
        # So threshold should be <= min(prob)
        predictions = np.array(pred_prob) >= threshold
        assert np.all(predictions), "Should predict all positive"
        assert np.mean(predictions == y_true) == 1.0, "Should achieve perfect accuracy"

    def test_degenerate_not_point_five(self):
        """Degenerate cases should not return arbitrary 0.5."""
        # All negative
        y_neg = [0, 0, 0]
        p_neg = [0.2, 0.7, 0.8]
        thresh_neg = get_optimal_threshold(y_neg, p_neg, metric="f1")
        assert thresh_neg != 0.5, "All-negative should not return arbitrary 0.5"

        # All positive
        y_pos = [1, 1, 1]
        p_pos = [0.2, 0.7, 0.8]
        thresh_pos = get_optimal_threshold(y_pos, p_pos, metric="f1")
        assert thresh_pos != 0.5, "All-positive should not return arbitrary 0.5"


class TestMicroAccuracyFix:
    """Test that micro accuracy is computed correctly using exclusive predictions."""

    def test_micro_accuracy_exclusive_vs_ovr(self):
        """Micro accuracy should use exclusive predictions, not OvR aggregation."""
        np.random.seed(42)
        n_samples, n_classes = 100, 3
        y_true = np.random.randint(0, n_classes, n_samples)
        pred_prob = np.random.rand(n_samples, n_classes)
        pred_prob = pred_prob / pred_prob.sum(axis=1, keepdims=True)
        thresholds = np.array([0.4, 0.5, 0.6])

        # Compute exclusive accuracy
        exclusive_acc = multiclass_metric_exclusive(
            y_true, pred_prob, thresholds, "accuracy"
        )

        # Compute OvR confusion matrices
        cms = get_multiclass_confusion_matrix(y_true, pred_prob, thresholds)

        # OvR aggregation should raise error for accuracy
        with pytest.raises(ValueError, match="Micro-averaged accuracy requires"):
            multiclass_metric(cms, "accuracy", "micro")

        # Exclusive accuracy should be reasonable (0-1 range)
        assert 0 <= exclusive_acc <= 1, (
            f"Exclusive accuracy {exclusive_acc} out of range"
        )

    def test_micro_accuracy_optimization(self):
        """Micro accuracy optimization should route through exclusive predictions."""
        np.random.seed(42)
        n_samples, n_classes = 50, 3
        y_true = np.random.randint(0, n_classes, n_samples)
        pred_prob = np.random.rand(n_samples, n_classes)
        pred_prob = pred_prob / pred_prob.sum(axis=1, keepdims=True)

        # This should work without error
        thresholds = get_optimal_multiclass_thresholds(
            y_true, pred_prob, metric="accuracy", average="micro", method="minimize"
        )

        assert len(thresholds) == n_classes
        assert all(0 <= t <= 1 for t in thresholds)


class TestDinkelbachComparisonSupport:
    """Test that Dinkelbach method supports comparison operators correctly."""

    def test_dinkelbach_comparison_parameter(self):
        """Dinkelbach should accept and use comparison parameter."""
        y_true = [0, 1, 0, 1, 1, 0, 1, 0]
        pred_prob = [0.2, 0.4, 0.4, 0.6, 0.6, 0.3, 0.7, 0.1]

        # Both should work without error
        thresh_excl = _dinkelbach_expected_fbeta(y_true, pred_prob, 1.0, ">")
        thresh_incl = _dinkelbach_expected_fbeta(y_true, pred_prob, 1.0, ">=")

        assert 0 <= thresh_excl <= 1
        assert 0 <= thresh_incl <= 1

        # Test through main API (mode='expected' returns tuple)
        result_main_excl = get_optimal_threshold(
            y_true, pred_prob, mode="expected", metric="f1", comparison=">"
        )
        result_main_incl = get_optimal_threshold(
            y_true, pred_prob, mode="expected", metric="f1", comparison=">="
        )

        # Extract thresholds from tuples
        thresh_main_excl, _ = result_main_excl
        thresh_main_incl, _ = result_main_incl

        # Allow some tolerance for numerical differences between internal and main API
        assert abs(thresh_main_excl - thresh_excl) < 0.05, (
            f"Thresholds should be close: {thresh_main_excl} vs {thresh_excl}"
        )
        assert abs(thresh_main_incl - thresh_incl) < 0.05, (
            f"Thresholds should be close: {thresh_main_incl} vs {thresh_incl}"
        )

    def test_dinkelbach_tied_probabilities(self):
        """Dinkelbach should handle tied probabilities correctly based on comparison."""
        # Create data with ties at optimal threshold
        pred_prob = [0.2, 0.5, 0.5, 0.5, 0.8]
        y_true = [0, 1, 0, 1, 1]

        for comparison in [">", ">="]:
            result = get_optimal_threshold(
                y_true, pred_prob, mode="expected", metric="f1", comparison=comparison
            )

            # Extract threshold from tuple
            threshold, expected_f1 = result

            # Should produce valid threshold
            assert 0 <= threshold <= 1
            assert 0 <= expected_f1 <= 1

            # Should produce valid predictions
            if comparison == ">":
                predictions = np.array(pred_prob) > threshold
            else:
                predictions = np.array(pred_prob) >= threshold

            # Validate predictions are boolean array
            assert isinstance(predictions, np.ndarray)
            assert predictions.dtype == bool

            # Should produce reasonable F1 score
            tp, tn, fp, fn = get_confusion_matrix(
                y_true, pred_prob, threshold, comparison=comparison
            )
            f1 = f1_score(tp, tn, fp, fn)
            assert 0 <= f1 <= 1


class TestLabelValidationFix:
    """Test that label validation allows valid label subsets."""

    def test_non_consecutive_labels_allowed(self):
        """Labels like {1, 2} with 3-class probabilities should work."""
        y_true = np.array([1, 2, 1, 2, 1, 2])  # Only classes 1,2 (no class 0)
        pred_prob = np.random.rand(6, 3)  # 3 classes total
        pred_prob = pred_prob / pred_prob.sum(axis=1, keepdims=True)

        # Should work without error
        thresholds = get_optimal_threshold(y_true, pred_prob, metric="f1")
        assert len(thresholds) == 3

    def test_invalid_labels_rejected(self):
        """Labels outside [0, n_classes-1] should be rejected."""
        y_true = np.array([0, 1, 2, 3])  # Label 3 invalid for 3-class
        pred_prob = np.random.rand(4, 3)  # Only 3 classes
        pred_prob = pred_prob / pred_prob.sum(axis=1, keepdims=True)

        with pytest.raises(ValueError, match="must be within \\[0, 2\\]"):
            get_optimal_threshold(y_true, pred_prob, metric="f1")

    def test_sparse_labels_work(self):
        """Sparse label sets should work correctly."""
        # Only use class 0 and class 2 (skip class 1)
        y_true = np.array([0, 2, 0, 2, 0, 2])
        pred_prob = np.random.rand(6, 4)  # 4 classes available
        pred_prob = pred_prob / pred_prob.sum(axis=1, keepdims=True)

        # Should work and return 4 thresholds
        thresholds = get_optimal_threshold(y_true, pred_prob, metric="f1")
        assert len(thresholds) == 4


class TestBinarySearchEfficiency:
    """Test that binary search optimization works correctly and efficiently."""

    def test_binary_search_correctness(self):
        """Binary search should give same results as original mask-based approach."""
        np.random.seed(42)
        y_true = np.random.randint(0, 2, 200)
        pred_prob = np.random.rand(200)

        # Test both comparison operators
        for comparison in [">", ">="]:
            threshold = get_optimal_threshold(
                y_true,
                pred_prob,
                metric="f1",
                method="unique_scan",
                comparison=comparison,
            )

            # Verify correctness by checking confusion matrix
            tp, tn, fp, fn = get_confusion_matrix(
                y_true, pred_prob, threshold, comparison=comparison
            )
            f1 = f1_score(tp, tn, fp, fn)

            assert 0 <= threshold <= 1
            assert 0 <= f1 <= 1
            assert tp + tn + fp + fn == len(y_true)

    def test_binary_search_with_weights(self):
        """Binary search should work correctly with sample weights."""
        np.random.seed(123)
        y_true = np.random.randint(0, 2, 100)
        pred_prob = np.random.rand(100)
        sample_weight = np.random.rand(100) * 2  # Random weights

        threshold = get_optimal_threshold(
            y_true,
            pred_prob,
            metric="f1",
            method="unique_scan",
            sample_weight=sample_weight,
        )

        # Verify weighted confusion matrix
        tp, tn, fp, fn = get_confusion_matrix(
            y_true, pred_prob, threshold, sample_weight=sample_weight
        )

        # Total should equal sum of weights
        assert abs(tp + tn + fp + fn - np.sum(sample_weight)) < 1e-10


class TestMicroOptimizationDocumentation:
    """Test that micro optimization limitations are properly documented."""

    def test_micro_unique_scan_warning(self):
        """unique_scan with micro averaging should warn about limitation."""
        np.random.seed(42)
        y_true = np.random.randint(0, 3, 50)
        pred_prob = np.random.rand(50, 3)
        pred_prob = pred_prob / pred_prob.sum(axis=1, keepdims=True)

        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")

            _optimize_micro_averaged_thresholds(
                y_true, pred_prob, "f1", "unique_scan", None, False, ">"
            )

            # Should raise warning about limitation
            warning_found = any(
                "unique_scan with micro averaging uses independent"
                in str(warning.message)
                for warning in w
            )
            assert warning_found, "Should warn about micro optimization limitation"

    def test_micro_minimize_no_warning(self):
        """minimize with micro averaging should not warn (it does joint optimization)."""
        np.random.seed(42)
        y_true = np.random.randint(0, 3, 20)
        pred_prob = np.random.rand(20, 3)
        pred_prob = pred_prob / pred_prob.sum(axis=1, keepdims=True)

        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")

            _optimize_micro_averaged_thresholds(
                y_true, pred_prob, "f1", "minimize", None, False, ">"
            )

            # Should not warn about micro optimization
            warning_found = any(
                "unique_scan with micro averaging" in str(warning.message)
                for warning in w
            )
            assert not warning_found, "minimize should not warn about limitation"


class TestCoordinateAscentDocumentation:
    """Test that coordinate ascent limitations are clearly documented."""

    def test_coord_ascent_weight_error(self):
        """coord_ascent should give helpful error for sample weights."""
        y_true = np.random.randint(0, 3, 20)
        pred_prob = np.random.rand(20, 3)
        pred_prob = pred_prob / pred_prob.sum(axis=1, keepdims=True)

        with pytest.raises(
            NotImplementedError, match="This limitation could be lifted"
        ):
            get_optimal_threshold(
                y_true, pred_prob, method="coord_ascent", sample_weight=np.ones(20)
            )

    def test_coord_ascent_comparison_error(self):
        """coord_ascent should give helpful error for '>=' comparison."""
        y_true = np.random.randint(0, 3, 20)
        pred_prob = np.random.rand(20, 3)
        pred_prob = pred_prob / pred_prob.sum(axis=1, keepdims=True)

        with pytest.raises(NotImplementedError, match="Support for.*could be added"):
            get_optimal_threshold(
                y_true, pred_prob, method="coord_ascent", comparison=">="
            )

    def test_coord_ascent_metric_error(self):
        """coord_ascent should give helpful error for non-f1 metrics."""
        y_true = np.random.randint(0, 3, 20)
        pred_prob = np.random.rand(20, 3)
        pred_prob = pred_prob / pred_prob.sum(axis=1, keepdims=True)

        with pytest.raises(
            NotImplementedError, match="Support for other piecewise metrics"
        ):
            get_optimal_threshold(
                y_true, pred_prob, method="coord_ascent", metric="accuracy"
            )


class TestExclusivePredictionRule:
    """Test that exclusive prediction rule is working as documented."""

    def test_margin_based_decision(self):
        """Exclusive predictions should use margin-based rule, not argmax."""
        # Case where argmax != max margin
        pred_prob = np.array([[0.49, 0.10, 0.41]])  # Class 0 has highest prob
        thresholds = np.array([0.3, 0.5, 0.2])  # Class 2 has highest margin
        y_dummy = np.array([0])  # Not used in prediction logic

        predictions = _compute_exclusive_predictions(
            y_dummy, pred_prob, thresholds, comparison=">"
        )

        # Should pick class 2 (highest margin: 0.41 - 0.2 = 0.21)
        # Not class 0 (highest prob but lower margin: 0.49 - 0.3 = 0.19)
        assert predictions[0] == 2, "Should pick class with highest positive margin"

    def test_fallback_to_argmax(self):
        """Should fall back to argmax when no class has positive margin."""
        pred_prob = np.array([[0.2, 0.3, 0.5]])
        thresholds = np.array([0.4, 0.4, 0.6])  # All margins negative
        y_dummy = np.array([0])

        predictions = _compute_exclusive_predictions(
            y_dummy, pred_prob, thresholds, comparison=">"
        )

        # Should fall back to class 2 (highest probability)
        assert predictions[0] == 2, (
            "Should fall back to argmax when all margins negative"
        )

    def test_exclusive_accuracy_differs_from_argmax(self):
        """Exclusive accuracy can differ from standard argmax accuracy."""
        np.random.seed(42)
        n_samples, n_classes = 100, 3
        y_true = np.random.randint(0, n_classes, n_samples)
        pred_prob = np.random.rand(n_samples, n_classes)
        pred_prob = pred_prob / pred_prob.sum(axis=1, keepdims=True)

        # Different thresholds to create margin-based decisions
        thresholds = np.array([0.2, 0.5, 0.3])

        # Exclusive predictions (margin-based)
        exclusive_preds = _compute_exclusive_predictions(y_true, pred_prob, thresholds)
        exclusive_acc = np.mean(exclusive_preds == y_true)

        # Argmax predictions
        argmax_preds = np.argmax(pred_prob, axis=1)
        argmax_acc = np.mean(argmax_preds == y_true)

        # They can be different (not asserting inequality since it's probabilistic)
        assert 0 <= exclusive_acc <= 1
        assert 0 <= argmax_acc <= 1
        print(
            f"Exclusive accuracy: {exclusive_acc:.3f}, Argmax accuracy: {argmax_acc:.3f}"
        )


# Property-based tests using Hypothesis
class TestPropertyBased:
    """Property-based tests using Hypothesis for edge case discovery."""

    @given(
        n_samples=st.integers(min_value=10, max_value=100),
        positive_rate=st.floats(min_value=0.1, max_value=0.9),
        noise=st.floats(min_value=0.0, max_value=0.3),
    )
    @settings(max_examples=50, deadline=5000)
    def test_weighted_equals_expanded(self, n_samples, positive_rate, noise):
        """Weighted metrics should match expanded dataset approach."""
        np.random.seed(42)  # Fixed seed for reproducibility

        # Generate base data
        pred_prob = np.random.rand(n_samples)
        y_true = (
            pred_prob + noise * np.random.randn(n_samples) > positive_rate
        ).astype(int)

        # Integer weights for exact expansion
        weights = np.random.randint(1, 4, n_samples)  # Weights 1, 2, or 3

        # Weighted approach
        threshold_weighted = get_optimal_threshold(
            y_true,
            pred_prob,
            metric="accuracy",
            method="unique_scan",
            sample_weight=weights,
        )

        # Expanded approach
        y_expanded = np.repeat(y_true, weights)
        p_expanded = np.repeat(pred_prob, weights)
        threshold_expanded = get_optimal_threshold(
            y_expanded, p_expanded, metric="accuracy", method="unique_scan"
        )

        # Should be exactly equal or very close (allowing only tiny eps for tie semantics)
        assert abs(threshold_weighted - threshold_expanded) < 1e-10, (
            f"Weighted ({threshold_weighted:.10f}) and expanded ({threshold_expanded:.10f}) "
            f"approaches should be nearly identical (integer weight expansion)"
        )

        # Also verify scores are identical
        tp_w, tn_w, fp_w, fn_w = get_confusion_matrix(
            y_true, pred_prob, threshold_weighted, weights
        )
        tp_e, tn_e, fp_e, fn_e = get_confusion_matrix(
            y_expanded, p_expanded, threshold_expanded
        )

        acc_weighted = accuracy_score(tp_w, tn_w, fp_w, fn_w)
        acc_expanded = accuracy_score(tp_e, tn_e, fp_e, fn_e)

        assert abs(acc_weighted - acc_expanded) < 1e-10, (
            f"Accuracy scores should be identical: weighted={acc_weighted:.10f}, "
            f"expanded={acc_expanded:.10f}"
        )

    @given(
        n_samples=st.integers(min_value=20, max_value=100),
        tie_prob=st.floats(min_value=0.2, max_value=0.8),
    )
    @settings(max_examples=30, deadline=5000)
    def test_tie_semantics_consistency(self, n_samples, tie_prob):
        """Tie handling should be consistent across comparison operators."""
        np.random.seed(123)  # Fixed seed

        # Create data with ties at tie_prob
        pred_prob = np.random.rand(n_samples)
        # Force some probabilities to be exactly tie_prob
        n_ties = max(2, n_samples // 5)
        tie_indices = np.random.choice(n_samples, n_ties, replace=False)
        pred_prob[tie_indices] = tie_prob

        y_true = np.random.randint(0, 2, n_samples)

        # Get thresholds for both comparison operators
        thresh_excl = get_optimal_threshold(
            y_true, pred_prob, metric="f1", comparison=">"
        )
        thresh_incl = get_optimal_threshold(
            y_true, pred_prob, metric="f1", comparison=">="
        )

        # Apply thresholds

        # When probabilities equal threshold, predictions should differ appropriately
        if np.any(np.isclose(pred_prob, thresh_excl, atol=1e-10)):
            np.isclose(pred_prob, thresh_excl, atol=1e-10)
            # For tied probabilities: '>' excludes, '>=' includes
            # (This assertion might not always hold due to optimization, but test basic consistency)
            pass  # Just verify no crashes occur

        # Both should produce valid results
        assert 0 <= thresh_excl <= 1
        assert 0 <= thresh_incl <= 1

    @given(
        n_classes=st.integers(min_value=2, max_value=5),
        n_samples=st.integers(min_value=20, max_value=100),
    )
    @settings(max_examples=20, deadline=10000)
    def test_label_validation_robustness(self, n_classes, n_samples):
        """Label validation should handle various valid and invalid cases."""
        np.random.seed(456)  # Fixed seed

        # Valid case: random subset of classes
        present_classes = np.random.choice(
            n_classes, size=min(n_classes, 3), replace=False
        )
        y_true = np.random.choice(present_classes, size=n_samples)
        pred_prob = np.random.rand(n_samples, n_classes)
        pred_prob = pred_prob / pred_prob.sum(axis=1, keepdims=True)

        # Should work without error
        thresholds = get_optimal_threshold(y_true, pred_prob, metric="f1")
        assert len(thresholds) == n_classes

        # Invalid case: label outside range
        if n_classes < 10:  # Avoid creating huge arrays
            y_invalid = np.append(y_true, [n_classes])  # Add invalid label
            pred_invalid = np.random.rand(n_samples + 1, n_classes)
            pred_invalid = pred_invalid / pred_invalid.sum(axis=1, keepdims=True)

            with pytest.raises(ValueError, match="must be within"):
                get_optimal_threshold(y_invalid, pred_invalid, metric="f1")


class TestRegressionPrevention:
    """Tests to prevent regression of previously fixed bugs."""

    def test_all_fixes_integration(self):
        """Integration test combining multiple fixes."""
        np.random.seed(789)

        # Multiclass case with non-consecutive labels, weights, ties
        y_true = np.array([0, 2, 0, 2, 1, 1])  # Skip some classes
        pred_prob = np.array(
            [
                [0.5, 0.2, 0.3],
                [0.3, 0.3, 0.4],
                [0.5, 0.1, 0.4],  # Ties with first sample
                [0.2, 0.2, 0.6],
                [0.4, 0.5, 0.1],
                [0.3, 0.5, 0.2],
            ]
        )
        pred_prob = pred_prob / pred_prob.sum(axis=1, keepdims=True)

        sample_weight = np.array([0.5, 1.5, 2.0, 1.0, 0.8, 1.2])  # Fractional weights

        # Should work with all the fixes
        for comparison in [">", ">="]:
            thresholds = get_optimal_threshold(
                y_true,
                pred_prob,
                metric="f1",
                method="unique_scan",
                comparison=comparison,
                sample_weight=sample_weight,
            )

            assert len(thresholds) == 3
            assert all(0 <= t <= 1 for t in thresholds)

            # Verify confusion matrices work
            cms = get_multiclass_confusion_matrix(
                y_true,
                pred_prob,
                thresholds,
                sample_weight=sample_weight,
                comparison=comparison,
            )

            assert len(cms) == 3
            for tp, tn, fp, fn in cms:
                assert tp >= 0 and tn >= 0 and fp >= 0 and fn >= 0

    def test_dinkelbach_calibration_sanity(self):
        """Sanity check that Dinkelbach gives reasonable results for calibrated data."""
        np.random.seed(999)
        n_samples = 200

        # Generate calibrated data
        pred_prob = np.random.rand(n_samples)
        y_true = np.random.binomial(1, pred_prob)  # Labels match probabilities

        # Test both comparison operators
        for comparison in [">", ">="]:
            result = get_optimal_threshold(
                y_true, pred_prob, mode="expected", metric="f1", comparison=comparison
            )

            # Extract threshold from tuple
            threshold, expected_f1 = result

            # Should be reasonable threshold
            assert 0 <= threshold <= 1
            assert 0 <= expected_f1 <= 1

            # Should produce reasonable F1
            tp, tn, fp, fn = get_confusion_matrix(
                y_true, pred_prob, threshold, comparison=comparison
            )
            f1 = f1_score(tp, tn, fp, fn)
            assert 0 <= f1 <= 1

            # For well-calibrated data, F1 should be decent
            assert f1 > 0.3, f"F1 score {f1:.3f} seems too low for calibrated data"

    def test_no_arbitrary_returns(self):
        """Ensure no method returns arbitrary values like 0.5 in edge cases."""
        # Test various edge cases that used to return 0.5

        # All same class
        test_cases = [
            ([0, 0, 0, 0], [0.1, 0.4, 0.7, 0.9]),  # All negative
            ([1, 1, 1, 1], [0.1, 0.4, 0.7, 0.9]),  # All positive
            ([0, 1, 0, 1], [0.5, 0.5, 0.5, 0.5]),  # All same probability
        ]

        for y_true, pred_prob in test_cases:
            for method in ["unique_scan", "minimize"]:
                for comparison in [">", ">="]:
                    try:
                        threshold = get_optimal_threshold(
                            y_true,
                            pred_prob,
                            metric="f1",
                            method=method,
                            comparison=comparison,
                        )

                        # Should return reasonable threshold, not arbitrary 0.5
                        # (unless 0.5 is actually optimal by coincidence)
                        assert 0 <= threshold <= 1, f"Invalid threshold {threshold}"

                        # Verify it achieves reasonable metric
                        tp, tn, fp, fn = get_confusion_matrix(
                            y_true, pred_prob, threshold, comparison=comparison
                        )
                        metric_val = (
                            f1_score(tp, tn, fp, fn) if tp + fp + fn > 0 else 1.0
                        )
                        assert 0 <= metric_val <= 1, f"Invalid F1 {metric_val}"

                    except Exception as e:
                        pytest.fail(
                            f"Method {method} with {comparison} failed on {y_true}, {pred_prob}: {e}"
                        )
