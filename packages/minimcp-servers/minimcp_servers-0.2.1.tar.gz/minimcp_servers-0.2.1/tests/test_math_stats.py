"""Tests for minimcp_servers.modules.math.stats module."""

import math
import statistics

import pytest

from minimcp_servers.modules.math import stats as stats_module


class TestCalculatingAverages:
    """Test functions for calculating averages."""

    def test_mean(self):
        """Test mean function."""
        test_cases = [
            ([1.0, 2.0, 3.0, 4.0, 5.0], 3.0),
            ([0.0], 0.0),
            ([5.0], 5.0),
            ([1.0, 1.0, 1.0], 1.0),
            ([-1.0, 0.0, 1.0], 0.0),
            ([1.5, 2.5, 3.5], 2.5),
            ([10.0, 20.0, 30.0], 20.0),
        ]

        for data, expected in test_cases:
            result = stats_module.mean(data)
            assert abs(result - expected) < 1e-10, f"mean({data}) should be {expected}, got {result}"

    def test_mean_empty(self):
        """Test mean function with empty data."""
        with pytest.raises(statistics.StatisticsError):
            stats_module.mean([])

    def test_geometric_mean(self):
        """Test geometric_mean function."""
        test_cases = [
            ([1.0, 4.0], 2.0),  # sqrt(1 * 4) = 2
            ([2.0, 8.0], 4.0),  # sqrt(2 * 8) = 4
            ([1.0, 1.0, 1.0], 1.0),
            ([2.0, 2.0, 2.0], 2.0),
            ([1.0, 2.0, 4.0, 8.0], 2.828427124746190),  # 4th root of 64
        ]

        for data, expected in test_cases:
            result = stats_module.geometric_mean(data)
            assert abs(result - expected) < 1e-10, f"geometric_mean({data}) should be {expected}, got {result}"

    def test_geometric_mean_invalid(self):
        """Test geometric_mean function with invalid data."""
        # Empty data
        with pytest.raises(statistics.StatisticsError):
            stats_module.geometric_mean([])

        # Zero in data
        with pytest.raises(statistics.StatisticsError):
            stats_module.geometric_mean([1.0, 0.0, 2.0])

        # Negative value in data
        with pytest.raises(statistics.StatisticsError):
            stats_module.geometric_mean([1.0, -2.0, 3.0])

    def test_harmonic_mean(self):
        """Test harmonic_mean function."""
        test_cases = [
            ([1.0, 4.0], 1.6),  # 2 / (1/1 + 1/4) = 2 / 1.25 = 1.6
            ([2.0, 2.0, 2.0], 2.0),
            ([1.0, 2.0, 3.0], 1.636363636363636),  # 3 / (1 + 1/2 + 1/3)
            ([4.0, 12.0], 6.0),  # 2 / (1/4 + 1/12) = 2 / (1/3) = 6
        ]

        for data, expected in test_cases:
            result = stats_module.harmonic_mean(data)
            assert abs(result - expected) < 1e-10, f"harmonic_mean({data}) should be {expected}, got {result}"

    def test_harmonic_mean_with_weights(self):
        """Test harmonic_mean function with weights."""
        data = [2.0, 4.0]
        weights = [1.0, 1.0]
        result = stats_module.harmonic_mean(data, weights)

        # Should be same as unweighted for equal weights
        expected = stats_module.harmonic_mean(data)
        assert abs(result - expected) < 1e-10, "weighted harmonic_mean should match unweighted for equal weights"

    def test_harmonic_mean_invalid(self):
        """Test harmonic_mean function with invalid data."""
        # Zero in data returns 0
        result = stats_module.harmonic_mean([1.0, 0.0, 2.0])
        assert result == 0.0, "harmonic_mean with zero should return 0"

        # Negative value in data
        with pytest.raises(statistics.StatisticsError):
            stats_module.harmonic_mean([1.0, -2.0, 3.0])

    def test_median(self):
        """Test median function."""
        test_cases = [
            ([1.0], 1.0),
            ([1.0, 2.0], 1.5),  # Even number of elements
            ([1.0, 2.0, 3.0], 2.0),  # Odd number of elements
            ([3.0, 1.0, 2.0], 2.0),  # Unsorted data
            ([1.0, 1.0, 2.0, 2.0], 1.5),
            ([1.0, 2.0, 3.0, 4.0, 5.0], 3.0),
        ]

        for data, expected in test_cases:
            result = stats_module.median(data)
            assert abs(result - expected) < 1e-10, f"median({data}) should be {expected}, got {result}"

    def test_median_low(self):
        """Test median_low function."""
        test_cases = [
            ([1.0], 1.0),
            ([1.0, 2.0], 1.0),  # Even number - lower middle
            ([1.0, 2.0, 3.0], 2.0),  # Odd number - same as median
            ([1.0, 2.0, 3.0, 4.0], 2.0),  # Even number - lower middle
        ]

        for data, expected in test_cases:
            result = stats_module.median_low(data)
            assert result == expected, f"median_low({data}) should be {expected}, got {result}"

    def test_median_high(self):
        """Test median_high function."""
        test_cases = [
            ([1.0], 1.0),
            ([1.0, 2.0], 2.0),  # Even number - higher middle
            ([1.0, 2.0, 3.0], 2.0),  # Odd number - same as median
            ([1.0, 2.0, 3.0, 4.0], 3.0),  # Even number - higher middle
        ]

        for data, expected in test_cases:
            result = stats_module.median_high(data)
            assert result == expected, f"median_high({data}) should be {expected}, got {result}"

    def test_median_grouped(self):
        """Test median_grouped function."""
        # Test with default interval
        data = [1.0, 2.0, 3.0, 4.0, 5.0]
        result = stats_module.median_grouped(data)
        assert isinstance(result, float), "median_grouped should return float"

        # Test with custom interval
        result_custom = stats_module.median_grouped(data, interval=2.0)
        assert isinstance(result_custom, float), "median_grouped with custom interval should return float"

    def test_mode(self):
        """Test mode function."""
        test_cases = [
            ([1.0, 1.0, 2.0, 3.0], 1.0),
            ([1.0, 2.0, 2.0, 2.0, 3.0], 2.0),
            ([5.0], 5.0),
            ([1.0, 1.0, 1.0], 1.0),
        ]

        for data, expected in test_cases:
            result = stats_module.mode(data)
            assert result == expected, f"mode({data}) should be {expected}, got {result}"

    def test_mode_no_unique_mode(self):
        """Test mode function when there's no unique mode."""
        # When all elements appear equally, mode returns the first one
        result = stats_module.mode([1.0, 2.0, 3.0])
        assert result == 1.0, "mode should return first element when all are equally frequent"

    def test_multimode(self):
        """Test multimode function."""
        test_cases = [
            ([1.0, 1.0, 2.0, 2.0, 3.0], [1.0, 2.0]),  # Two modes
            ([1.0, 2.0, 3.0], [1.0, 2.0, 3.0]),  # All equally frequent
            ([1.0, 1.0, 1.0], [1.0]),  # Single mode
            ([5.0], [5.0]),  # Single element
        ]

        for data, expected in test_cases:
            result = stats_module.multimode(data)
            assert sorted(result) == sorted(expected), f"multimode({data}) should be {expected}, got {result}"

    def test_multimode_empty(self):
        """Test multimode function with empty data."""
        result = stats_module.multimode([])
        assert result == [], "multimode of empty list should be empty list"

    def test_quantiles(self):
        """Test quantiles function."""
        data = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
        result = stats_module.quantiles(data)

        assert isinstance(result, list), "quantiles should return a list"
        assert len(result) == 3, "quantiles should return 3 quartiles by default"

        # Quartiles should be in ascending order
        assert result[0] <= result[1] <= result[2], "quantiles should be in ascending order"


class TestCalculatingVariability:
    """Test functions for calculating variability or spread."""

    def test_pvariance(self):
        """Test pvariance function."""
        test_cases = [
            ([1.0, 2.0, 3.0, 4.0, 5.0], 2.0),  # Population variance
            ([0.0, 0.0, 0.0], 0.0),  # No variance
            ([5.0], 0.0),  # Single element
            ([1.0, 3.0], 1.0),  # Simple case
        ]

        for data, expected in test_cases:
            result = stats_module.pvariance(data)
            assert abs(result - expected) < 1e-10, f"pvariance({data}) should be {expected}, got {result}"

    def test_variance(self):
        """Test variance function."""
        test_cases = [
            ([1.0, 2.0, 3.0, 4.0, 5.0], 2.5),  # Sample variance
            ([1.0, 3.0], 2.0),  # Simple case
        ]

        for data, expected in test_cases:
            result = stats_module.variance(data)
            assert abs(result - expected) < 1e-10, f"variance({data}) should be {expected}, got {result}"

    def test_variance_with_xbar(self):
        """Test variance function with provided mean."""
        data = [1.0, 2.0, 3.0, 4.0, 5.0]
        xbar = 3.0  # Known mean

        result = stats_module.variance(data, xbar)
        expected = stats_module.variance(data)  # Should be same
        assert abs(result - expected) < 1e-10, "variance with correct xbar should match regular variance"

    def test_variance_insufficient_data(self):
        """Test variance function with insufficient data."""
        with pytest.raises(statistics.StatisticsError):
            stats_module.variance([5.0])  # Need at least 2 values for sample variance

    def test_pstdev(self):
        """Test pstdev function."""
        test_cases = [
            ([1.0, 2.0, 3.0, 4.0, 5.0], math.sqrt(2.0)),  # sqrt of population variance
            ([0.0, 0.0, 0.0], 0.0),  # No standard deviation
            ([5.0], 0.0),  # Single element
        ]

        for data, expected in test_cases:
            result = stats_module.pstdev(data)
            assert abs(result - expected) < 1e-10, f"pstdev({data}) should be {expected}, got {result}"

    def test_stdev(self):
        """Test stdev function."""
        test_cases = [
            ([1.0, 2.0, 3.0, 4.0, 5.0], math.sqrt(2.5)),  # sqrt of sample variance
            ([1.0, 3.0], math.sqrt(2.0)),  # Simple case
        ]

        for data, expected in test_cases:
            result = stats_module.stdev(data)
            assert abs(result - expected) < 1e-10, f"stdev({data}) should be {expected}, got {result}"

    def test_stdev_with_xbar(self):
        """Test stdev function with provided mean."""
        data = [1.0, 2.0, 3.0, 4.0, 5.0]
        xbar = 3.0  # Known mean

        result = stats_module.stdev(data, xbar)
        expected = stats_module.stdev(data)  # Should be same
        assert abs(result - expected) < 1e-10, "stdev with correct xbar should match regular stdev"

    def test_variance_stdev_relationship(self):
        """Test relationship between variance and standard deviation."""
        test_datasets = [
            [1.0, 2.0, 3.0, 4.0, 5.0],
            [10.0, 20.0, 30.0],
            [1.5, 2.5, 3.5, 4.5],
        ]

        for data in test_datasets:
            # Population variance and standard deviation
            pvar = stats_module.pvariance(data)
            pstd = stats_module.pstdev(data)
            assert abs(pstd**2 - pvar) < 1e-10, f"pstdev^2 should equal pvariance for {data}"

            # Sample variance and standard deviation (if enough data)
            if len(data) > 1:
                var = stats_module.variance(data)
                std = stats_module.stdev(data)
                assert abs(std**2 - var) < 1e-10, f"stdev^2 should equal variance for {data}"


class TestRelationsBetweenInputs:
    """Test functions for relations between two inputs."""

    def test_covariance(self):
        """Test covariance function."""
        test_cases = [
            ([1.0, 2.0, 3.0], [1.0, 2.0, 3.0], 1.0),  # Perfect positive correlation
            ([1.0, 2.0, 3.0], [3.0, 2.0, 1.0], -1.0),  # Perfect negative correlation
            ([1.0, 1.0, 1.0], [2.0, 2.0, 2.0], 0.0),  # No variance
        ]

        for x, y, expected in test_cases:
            result = stats_module.covariance(x, y)
            assert abs(result - expected) < 1e-10, f"covariance({x}, {y}) should be {expected}, got {result}"

    def test_covariance_insufficient_data(self):
        """Test covariance function with insufficient data."""
        with pytest.raises(statistics.StatisticsError):
            stats_module.covariance([1.0], [2.0])  # Need at least 2 pairs

    def test_correlation(self):
        """Test correlation function."""
        test_cases = [
            ([1.0, 2.0, 3.0], [1.0, 2.0, 3.0], 1.0),  # Perfect positive correlation
            ([1.0, 2.0, 3.0], [3.0, 2.0, 1.0], -1.0),  # Perfect negative correlation
            ([1.0, 2.0, 3.0], [2.0, 4.0, 6.0], 1.0),  # Perfect positive correlation (scaled)
        ]

        for x, y, expected in test_cases:
            result = stats_module.correlation(x, y)
            assert abs(result - expected) < 1e-10, f"correlation({x}, {y}) should be {expected}, got {result}"

    def test_correlation_bounds(self):
        """Test that correlation is bounded between -1 and 1."""
        test_datasets = [
            ([1.0, 2.0, 3.0, 4.0], [2.0, 4.0, 1.0, 3.0]),
            ([1.0, 5.0, 3.0, 2.0], [4.0, 1.0, 2.0, 5.0]),
            ([10.0, 20.0, 30.0], [15.0, 25.0, 35.0]),
        ]

        for x, y in test_datasets:
            result = stats_module.correlation(x, y)
            assert -1.0 <= result <= 1.0, f"correlation should be between -1 and 1, got {result}"

    def test_correlation_no_variance(self):
        """Test correlation function when one variable has no variance."""
        with pytest.raises(statistics.StatisticsError):
            stats_module.correlation([1.0, 1.0, 1.0], [1.0, 2.0, 3.0])  # x has no variance

    def test_linear_regression(self):
        """Test linear_regression function."""
        test_cases = [
            ([1.0, 2.0, 3.0], [2.0, 4.0, 6.0], (2.0, 0.0)),  # y = 2x
            ([0.0, 1.0, 2.0], [1.0, 3.0, 5.0], (2.0, 1.0)),  # y = 2x + 1
            ([1.0, 2.0, 3.0], [1.0, 1.0, 1.0], (0.0, 1.0)),  # y = 1 (horizontal line)
        ]

        for x, y, expected in test_cases:
            slope, intercept = stats_module.linear_regression(x, y)
            expected_slope, expected_intercept = expected

            assert abs(slope - expected_slope) < 1e-10, (
                f"linear_regression slope for ({x}, {y}) should be {expected_slope}, got {slope}"
            )
            assert abs(intercept - expected_intercept) < 1e-10, (
                f"linear_regression intercept for ({x}, {y}) should be {expected_intercept}, got {intercept}"
            )

    def test_linear_regression_properties(self):
        """Test mathematical properties of linear regression."""
        x = [1.0, 2.0, 3.0, 4.0, 5.0]
        y = [2.1, 3.9, 6.1, 8.0, 9.9]  # Approximately y = 2x with some noise

        slope, intercept = stats_module.linear_regression(x, y)

        # Slope should be positive for this data
        assert slope > 0, "slope should be positive for positively correlated data"

        # Check that the line passes reasonably close to the data points
        for xi, yi in zip(x, y):
            predicted = slope * xi + intercept
            # Allow some tolerance for the noisy data
            assert abs(predicted - yi) < 1.0, "regression line should be reasonably close to data points"

    def test_linear_regression_no_variance(self):
        """Test linear_regression function when x has no variance."""
        with pytest.raises(statistics.StatisticsError):
            stats_module.linear_regression([1.0, 1.0, 1.0], [1.0, 2.0, 3.0])  # x has no variance


class TestEdgeCases:
    """Test edge cases and error conditions."""

    def test_empty_data(self):
        """Test functions with empty data."""
        empty_data_functions = [
            stats_module.mean,
            stats_module.geometric_mean,
            stats_module.harmonic_mean,
            stats_module.median,
            stats_module.median_low,
            stats_module.median_high,
            stats_module.median_grouped,
            stats_module.mode,
            stats_module.pvariance,
            stats_module.pstdev,
        ]

        for func in empty_data_functions:
            with pytest.raises(statistics.StatisticsError):
                func([])

    def test_single_element_data(self):
        """Test functions with single element data."""
        single_element = [5.0]

        # These should work with single element
        assert stats_module.mean(single_element) == 5.0
        assert stats_module.geometric_mean(single_element) == 5.0  # Should be exact now with precision fix
        assert stats_module.harmonic_mean(single_element) == 5.0
        assert stats_module.median(single_element) == 5.0
        assert stats_module.median_low(single_element) == 5.0
        assert stats_module.median_high(single_element) == 5.0
        assert stats_module.mode(single_element) == 5.0
        assert stats_module.multimode(single_element) == [5.0]
        assert stats_module.pvariance(single_element) == 0.0
        assert stats_module.pstdev(single_element) == 0.0

        # These should raise error with single element
        with pytest.raises(statistics.StatisticsError):
            stats_module.variance(single_element)

        with pytest.raises(statistics.StatisticsError):
            stats_module.stdev(single_element)

    def test_identical_values(self):
        """Test functions with identical values."""
        identical = [3.0, 3.0, 3.0, 3.0]

        assert stats_module.mean(identical) == 3.0
        assert stats_module.geometric_mean(identical) == 3.0  # Should be exact now with precision fix
        assert stats_module.harmonic_mean(identical) == 3.0
        assert stats_module.median(identical) == 3.0
        assert stats_module.mode(identical) == 3.0
        assert stats_module.pvariance(identical) == 0.0
        assert stats_module.variance(identical) == 0.0
        assert stats_module.pstdev(identical) == 0.0
        assert stats_module.stdev(identical) == 0.0

    def test_large_datasets(self):
        """Test functions with large datasets."""
        # Create a large dataset
        large_data = list(range(1000))
        large_data_float = [float(x) for x in large_data]

        # These should handle large datasets without issues
        mean_result = stats_module.mean(large_data_float)
        assert isinstance(mean_result, float)

        median_result = stats_module.median(large_data_float)
        assert isinstance(median_result, float)

        pvar_result = stats_module.pvariance(large_data_float)
        assert isinstance(pvar_result, float)
        assert pvar_result > 0  # Should have variance

    def test_extreme_values(self):
        """Test functions with extreme values."""
        extreme_data = [1e-10, 1e10, -1e10]

        # Functions should handle extreme values gracefully
        mean_result = stats_module.mean(extreme_data)
        assert isinstance(mean_result, float)

        median_result = stats_module.median(extreme_data)
        assert isinstance(median_result, float)

    def test_mismatched_lengths(self):
        """Test two-input functions with mismatched lengths."""
        x = [1.0, 2.0, 3.0]
        y = [1.0, 2.0]  # Different length

        two_input_functions = [
            stats_module.covariance,
            stats_module.correlation,
            stats_module.linear_regression,
        ]

        for func in two_input_functions:
            with pytest.raises(statistics.StatisticsError):
                func(x, y)
