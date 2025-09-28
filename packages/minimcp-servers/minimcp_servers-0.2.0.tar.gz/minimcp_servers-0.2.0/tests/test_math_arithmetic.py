"""Tests for minimcp_servers.modules.math.arithmetic module."""

import math

import pytest

from minimcp_servers.modules.math import arithmetic as arith_module


class TestElementaryFunctions:
    """Test elementary arithmetic functions."""

    def test_add(self):
        """Test add function."""
        test_cases = [
            ([], 0.0),  # Empty array
            ([1.0], 1.0),
            ([1.0, 2.0, 3.0], 6.0),
            ([1.5, 2.5, 3.0], 7.0),
            ([-1.0, 1.0], 0.0),
            ([0.1, 0.2, 0.3], 0.6),  # Floating point precision test
            ([1e10, 1e-10], 1e10 + 1e-10),  # Large and small numbers
        ]

        for array, expected in test_cases:
            result = arith_module.add(array)
            assert abs(result - expected) < 1e-10, f"add({array}) should be {expected}, got {result}"

    def test_subtract(self):
        """Test subtract function."""
        test_cases = [
            (5.0, 3.0, 2.0),
            (10.0, 4.0, 6.0),
            (0.0, 0.0, 0.0),
            (-5.0, -3.0, -2.0),
            (3.0, 5.0, -2.0),
            (1.5, 0.5, 1.0),
        ]

        for a, b, expected in test_cases:
            result = arith_module.subtract(a, b)
            assert abs(result - expected) < 1e-10, f"subtract({a}, {b}) should be {expected}"

    def test_multiply(self):
        """Test multiply function."""
        test_cases = [
            ([], 1.0),  # Empty array
            ([2.0], 2.0),
            ([2.0, 3.0, 4.0], 24.0),
            ([1.5, 2.0], 3.0),
            ([-2.0, 3.0], -6.0),
            ([0.0, 5.0], 0.0),
            ([1.0, 1.0, 1.0], 1.0),
        ]

        for array, expected in test_cases:
            result = arith_module.multiply(array)
            assert abs(result - expected) < 1e-10, f"multiply({array}) should be {expected}"

    def test_divide(self):
        """Test divide function."""
        test_cases = [
            (10.0, 2.0, 5.0),
            (15.0, 3.0, 5.0),
            (1.0, 2.0, 0.5),
            (-10.0, 2.0, -5.0),
            (10.0, -2.0, -5.0),
            (0.0, 5.0, 0.0),
        ]

        for a, b, expected in test_cases:
            result = arith_module.divide(a, b)
            assert abs(result - expected) < 1e-10, f"divide({a}, {b}) should be {expected}"

    def test_divide_by_zero(self):
        """Test divide function with zero divisor."""
        with pytest.raises(ZeroDivisionError):
            arith_module.divide(5.0, 0.0)

    def test_modulo(self):
        """Test modulo function."""
        test_cases = [
            (10.0, 3.0, 1.0),
            (15.0, 4.0, 3.0),
            (10.5, 3.0, 1.5),
            (-10.0, 3.0, 2.0),  # Python's modulo behavior
            (10.0, -3.0, -2.0),
        ]

        for a, b, expected in test_cases:
            result = arith_module.modulo(a, b)
            assert abs(result - expected) < 1e-10, f"modulo({a}, {b}) should be {expected}"

    def test_floor_divide(self):
        """Test floor_divide function."""
        test_cases = [
            (10.0, 3.0, 3.0),
            (15.0, 4.0, 3.0),
            (10.5, 3.0, 3.0),
            (-10.0, 3.0, -4.0),  # Floor division rounds down
            (10.0, -3.0, -4.0),
        ]

        for a, b, expected in test_cases:
            result = arith_module.floor_divide(a, b)
            assert abs(result - expected) < 1e-10, f"floor_divide({a}, {b}) should be {expected}"

    def test_pow(self):
        """Test pow function."""
        test_cases = [
            (2.0, 3.0, 8.0),
            (5.0, 2.0, 25.0),
            (2.0, 0.0, 1.0),
            (0.0, 5.0, 0.0),
            (4.0, 0.5, 2.0),  # Square root
            (8.0, 1 / 3, 2.0),  # Cube root
            (-2.0, 3.0, -8.0),
        ]

        for a, b, expected in test_cases:
            result = arith_module.pow(a, b)
            assert abs(result - expected) < 1e-10, f"pow({a}, {b}) should be {expected}"

    def test_minimum(self):
        """Test minimum function."""
        test_cases = [
            ([1.0], 1.0),
            ([1.0, 2.0, 3.0], 1.0),
            ([3.0, 1.0, 2.0], 1.0),
            ([-1.0, -2.0, -3.0], -3.0),
            ([0.0, -1.0, 1.0], -1.0),
            ([1.5, 1.2, 1.8], 1.2),
        ]

        for array, expected in test_cases:
            result = arith_module.minimum(array)
            assert result == expected, f"minimum({array}) should be {expected}"

    def test_minimum_empty(self):
        """Test minimum function with empty array."""
        with pytest.raises(ValueError):
            arith_module.minimum([])

    def test_maximum(self):
        """Test maximum function."""
        test_cases = [
            ([1.0], 1.0),
            ([1.0, 2.0, 3.0], 3.0),
            ([3.0, 1.0, 2.0], 3.0),
            ([-1.0, -2.0, -3.0], -1.0),
            ([0.0, -1.0, 1.0], 1.0),
            ([1.5, 1.2, 1.8], 1.8),
        ]

        for array, expected in test_cases:
            result = arith_module.maximum(array)
            assert result == expected, f"maximum({array}) should be {expected}"

    def test_maximum_empty(self):
        """Test maximum function with empty array."""
        with pytest.raises(ValueError):
            arith_module.maximum([])

    def test_sign(self):
        """Test sign function."""
        test_cases = [
            (5.0, 1),
            (-5.0, -1),
            (0.0, 0),
            (0.1, 1),
            (-0.1, -1),
            (1000.0, 1),
            (-1000.0, -1),
        ]

        for x, expected in test_cases:
            result = arith_module.sign(x)
            assert result == expected, f"sign({x}) should be {expected}"

    def test_clamp(self):
        """Test clamp function."""
        test_cases = [
            (5.0, 0.0, 10.0, 5.0),  # Within range
            (-5.0, 0.0, 10.0, 0.0),  # Below minimum
            (15.0, 0.0, 10.0, 10.0),  # Above maximum
            (5.0, 5.0, 10.0, 5.0),  # At minimum
            (10.0, 0.0, 10.0, 10.0),  # At maximum
            # Removed invalid case - now raises ValueError
        ]

        for x, min_val, max_val, expected in test_cases:
            result = arith_module.clamp(x, min_val, max_val)
            assert result == expected, f"clamp({x}, {min_val}, {max_val}) should be {expected}"

    def test_clamp_invalid_range(self):
        """Test clamp function with invalid range."""
        with pytest.raises(ValueError, match="min_val must be <= max_val"):
            arith_module.clamp(5.0, 10.0, 0.0)

    def test_round_to(self):
        """Test round_to function."""
        test_cases = [
            (3.14159, 0, 3.0),
            (3.14159, 2, 3.14),
            (3.14159, 4, 3.1416),
            (123.456, -1, 120.0),  # Negative precision
            (123.456, -2, 100.0),
            (2.5, 0, 2.0),  # Banker's rounding in Python
            (3.5, 0, 4.0),
        ]

        for x, n, expected in test_cases:
            result = arith_module.round_to(x, n)
            assert result == expected, f"round_to({x}, {n}) should be {expected}"

    def test_absolute(self):
        """Test absolute function."""
        test_cases = [
            (5.0, 5.0),
            (-5.0, 5.0),
            (0.0, 0.0),
            (-0.0, 0.0),
            (3.14, 3.14),
            (-3.14, 3.14),
        ]

        for x, expected in test_cases:
            result = arith_module.absolute(x)
            assert result == expected, f"absolute({x}) should be {expected}"

    def test_sqrt(self):
        """Test sqrt function."""
        test_cases = [
            (0.0, 0.0),
            (1.0, 1.0),
            (4.0, 2.0),
            (9.0, 3.0),
            (2.0, math.sqrt(2)),
            (0.25, 0.5),
        ]

        for x, expected in test_cases:
            result = arith_module.sqrt(x)
            assert abs(result - expected) < 1e-10, f"sqrt({x}) should be {expected}"

    def test_sqrt_negative(self):
        """Test sqrt function with negative input."""
        with pytest.raises(ValueError):
            arith_module.sqrt(-1.0)


class TestRoundingFunctions:
    """Test rounding functions."""

    def test_ceil(self):
        """Test ceil function."""
        test_cases = [
            (3.1, 4),
            (3.0, 3),
            (-3.1, -3),
            (-3.0, -3),
            (0.0, 0),
            (0.1, 1),
            (-0.1, 0),
        ]

        for x, expected in test_cases:
            result = arith_module.ceil(x)
            assert result == expected, f"ceil({x}) should be {expected}"

    def test_floor(self):
        """Test floor function."""
        test_cases = [
            (3.9, 3),
            (3.0, 3),
            (-3.1, -4),
            (-3.0, -3),
            (0.0, 0),
            (0.9, 0),
            (-0.1, -1),
        ]

        for x, expected in test_cases:
            result = arith_module.floor(x)
            assert result == expected, f"floor({x}) should be {expected}"

    def test_trunc(self):
        """Test trunc function."""
        test_cases = [
            (3.9, 3),
            (3.0, 3),
            (-3.9, -3),
            (-3.0, -3),
            (0.0, 0),
            (0.9, 0),
            (-0.9, 0),
        ]

        for x, expected in test_cases:
            result = arith_module.trunc(x)
            assert result == expected, f"trunc({x}) should be {expected}"


class TestFloatingPointFunctions:
    """Test floating point manipulation functions."""

    def test_copysign(self):
        """Test copysign function."""
        test_cases = [
            (5.0, 3.0, 5.0),
            (5.0, -3.0, -5.0),
            (-5.0, 3.0, 5.0),
            (-5.0, -3.0, -5.0),
            (0.0, -1.0, -0.0),
            (0.0, 1.0, 0.0),
        ]

        for x, y, expected in test_cases:
            result = arith_module.copysign(x, y)
            assert result == expected, f"copysign({x}, {y}) should be {expected}"

    def test_frexp(self):
        """Test frexp function."""
        test_cases = [
            (0.0, (0.0, 0)),
            (1.0, (0.5, 1)),
            (2.0, (0.5, 2)),
            (4.0, (0.5, 3)),
            (8.0, (0.5, 4)),
            (-4.0, (-0.5, 3)),
        ]

        for x, expected in test_cases:
            result = arith_module.frexp(x)
            assert abs(result[0] - expected[0]) < 1e-10 and result[1] == expected[1], (
                f"frexp({x}) should be {expected}, got {result}"
            )

    def test_ldexp(self):
        """Test ldexp function."""
        test_cases = [
            (0.5, 1, 1.0),
            (0.5, 2, 2.0),
            (0.5, 3, 4.0),
            (1.0, 0, 1.0),
            (2.0, -1, 1.0),
            (-0.5, 3, -4.0),
        ]

        for x, i, expected in test_cases:
            result = arith_module.ldexp(x, i)
            assert abs(result - expected) < 1e-10, f"ldexp({x}, {i}) should be {expected}"

    def test_frexp_ldexp_inverse(self):
        """Test that frexp and ldexp are inverse operations."""
        test_values = [1.0, 2.0, 3.14, 100.0, 0.5, -5.0]

        for x in test_values:
            if x != 0.0:  # frexp(0) is special case
                mantissa, exponent = arith_module.frexp(x)
                reconstructed = arith_module.ldexp(mantissa, exponent)
                assert abs(reconstructed - x) < 1e-10, f"frexp/ldexp round-trip failed for {x}"

    def test_modf(self):
        """Test modf function."""
        test_cases = [
            (3.14, (0.14, 3.0)),
            (-3.14, (-0.14, -3.0)),
            (5.0, (0.0, 5.0)),
            (-5.0, (-0.0, -5.0)),
            (0.0, (0.0, 0.0)),
            (0.75, (0.75, 0.0)),
        ]

        for x, expected in test_cases:
            result = arith_module.modf(x)
            assert abs(result[0] - expected[0]) < 1e-10 and abs(result[1] - expected[1]) < 1e-10, (
                f"modf({x}) should be {expected}, got {result}"
            )


class TestSpecialCases:
    """Test special cases and edge conditions."""

    def test_infinity_handling(self):
        """Test functions with infinity values."""
        inf = float("inf")
        ninf = float("-inf")

        # Functions that should handle infinity
        assert arith_module.absolute(inf) == inf
        assert arith_module.absolute(ninf) == inf
        assert arith_module.sign(inf) == 1
        assert arith_module.sign(ninf) == -1

        # Clamp with infinity
        assert arith_module.clamp(5.0, ninf, inf) == 5.0
        assert arith_module.clamp(inf, 0.0, 10.0) == 10.0
        assert arith_module.clamp(ninf, 0.0, 10.0) == 0.0

    def test_nan_handling(self):
        """Test functions with NaN values."""
        nan = float("nan")

        # NaN should propagate through most operations
        assert math.isnan(arith_module.absolute(nan))
        assert arith_module.sign(nan) == 0  # Special case for sign function

    def test_very_large_numbers(self):
        """Test functions with very large numbers."""
        large = 1e100

        assert arith_module.absolute(large) == large
        assert arith_module.absolute(-large) == large
        assert arith_module.sign(large) == 1
        assert arith_module.sign(-large) == -1

    def test_very_small_numbers(self):
        """Test functions with very small numbers."""
        small = 1e-100

        assert arith_module.absolute(small) == small
        assert arith_module.absolute(-small) == small
        assert arith_module.sign(small) == 1
        assert arith_module.sign(-small) == -1
