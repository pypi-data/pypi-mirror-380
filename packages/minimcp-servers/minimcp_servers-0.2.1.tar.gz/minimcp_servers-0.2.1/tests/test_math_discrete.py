"""Tests for minimcp_servers.modules.math.discrete module."""

import pytest

from minimcp_servers.modules.math import discrete as disc_module


class TestSquareRoot:
    """Test integer square root function."""

    def test_isqrt(self):
        """Test isqrt function."""
        test_cases = [
            (0, 0),
            (1, 1),
            (4, 2),
            (9, 3),
            (16, 4),
            (25, 5),
            (8, 2),  # Non-perfect square
            (15, 3),  # Non-perfect square
            (99, 9),  # Non-perfect square
            (100, 10),
            (10000, 100),
            (999999, 999),
        ]

        for x, expected in test_cases:
            result = disc_module.isqrt(x)
            assert result == expected, f"isqrt({x}) should be {expected}, got {result}"

    def test_isqrt_negative(self):
        """Test isqrt function with negative input."""
        with pytest.raises(ValueError):
            disc_module.isqrt(-1)

    def test_isqrt_large_numbers(self):
        """Test isqrt function with large numbers."""
        large_perfect_square = 10**20
        expected = 10**10
        result = disc_module.isqrt(large_perfect_square)
        assert result == expected, f"isqrt({large_perfect_square}) should be {expected}"

    def test_isqrt_properties(self):
        """Test mathematical properties of isqrt."""
        test_values = [0, 1, 4, 9, 16, 25, 50, 100, 1000]

        for x in test_values:
            result = disc_module.isqrt(x)

            # isqrt(x)^2 <= x < (isqrt(x) + 1)^2
            assert result * result <= x, f"isqrt({x})^2 should be <= {x}"
            assert x < (result + 1) * (result + 1), f"{x} should be < (isqrt({x}) + 1)^2"


class TestFactorial:
    """Test factorial function."""

    def test_factorial(self):
        """Test factorial function."""
        test_cases = [
            (0, 1),  # 0! = 1 by definition
            (1, 1),  # 1! = 1
            (2, 2),  # 2! = 2
            (3, 6),  # 3! = 6
            (4, 24),  # 4! = 24
            (5, 120),  # 5! = 120
            (6, 720),  # 6! = 720
            (10, 3628800),  # 10! = 3,628,800
        ]

        for x, expected in test_cases:
            result = disc_module.factorial(x)
            assert result == expected, f"factorial({x}) should be {expected}, got {result}"

    def test_factorial_negative(self):
        """Test factorial function with negative input."""
        with pytest.raises(ValueError):
            disc_module.factorial(-1)

    def test_factorial_non_integer(self):
        """Test factorial function with non-integer input."""
        with pytest.raises(TypeError):
            disc_module.factorial(3.5)  # type: ignore

    def test_factorial_large(self):
        """Test factorial function with larger values."""
        # Test that it can handle reasonably large factorials
        result = disc_module.factorial(20)
        expected = 2432902008176640000
        assert result == expected, f"factorial(20) should be {expected}"

    def test_factorial_growth(self):
        """Test that factorial grows as expected."""
        # n! = n * (n-1)!
        for n in range(1, 10):
            factorial_n = disc_module.factorial(n)
            factorial_n_minus_1 = disc_module.factorial(n - 1)
            assert factorial_n == n * factorial_n_minus_1, f"factorial({n}) should equal {n} * factorial({n - 1})"


class TestNumberTheoryFunctions:
    """Test number theory functions."""

    def test_gcd(self):
        """Test gcd function."""
        test_cases = [
            (12, 8, 4),
            (48, 18, 6),
            (7, 5, 1),  # Coprime numbers
            (0, 5, 5),  # gcd(0, n) = n
            (5, 0, 5),  # gcd(n, 0) = n
            (0, 0, 0),  # gcd(0, 0) = 0
            (17, 17, 17),  # gcd(n, n) = n
            (100, 25, 25),
            (13, 26, 13),
            (-12, 8, 4),  # Negative numbers
            (12, -8, 4),
            (-12, -8, 4),
        ]

        for a, b, expected in test_cases:
            result = disc_module.gcd(a, b)
            assert result == expected, f"gcd({a}, {b}) should be {expected}, got {result}"

    def test_gcd_properties(self):
        """Test mathematical properties of gcd."""
        test_pairs = [(12, 8), (48, 18), (7, 5), (100, 25)]

        for a, b in test_pairs:
            gcd_ab = disc_module.gcd(a, b)

            # gcd(a, b) = gcd(b, a) (commutative)
            gcd_ba = disc_module.gcd(b, a)
            assert gcd_ab == gcd_ba, f"gcd should be commutative: gcd({a}, {b}) != gcd({b}, {a})"

            # gcd(a, b) divides both a and b
            if gcd_ab != 0:
                assert a % gcd_ab == 0, f"gcd({a}, {b}) = {gcd_ab} should divide {a}"
                assert b % gcd_ab == 0, f"gcd({a}, {b}) = {gcd_ab} should divide {b}"

    def test_lcm(self):
        """Test lcm function."""
        test_cases = [
            (12, 8, 24),
            (4, 6, 12),
            (7, 5, 35),  # Coprime numbers
            (10, 15, 30),
            (12, 18, 36),
            (1, 5, 5),  # lcm(1, n) = n
            (5, 1, 5),  # lcm(n, 1) = n
            (17, 17, 17),  # lcm(n, n) = n
            (0, 5, 0),  # lcm(0, n) = 0
            (5, 0, 0),  # lcm(n, 0) = 0
        ]

        for a, b, expected in test_cases:
            result = disc_module.lcm(a, b)
            assert result == expected, f"lcm({a}, {b}) should be {expected}, got {result}"

    def test_lcm_properties(self):
        """Test mathematical properties of lcm."""
        test_pairs = [(12, 8), (4, 6), (7, 5), (10, 15)]

        for a, b in test_pairs:
            if a != 0 and b != 0:  # Skip zero cases for this test
                lcm_ab = disc_module.lcm(a, b)
                gcd_ab = disc_module.gcd(a, b)

                # lcm(a, b) = gcd(b, a) (commutative)
                lcm_ba = disc_module.lcm(b, a)
                assert lcm_ab == lcm_ba, f"lcm should be commutative: lcm({a}, {b}) != lcm({b}, {a})"

                # lcm(a, b) * gcd(a, b) = |a * b|
                assert lcm_ab * gcd_ab == abs(a * b), f"lcm({a}, {b}) * gcd({a}, {b}) should equal |{a} * {b}|"

                # Both a and b should divide lcm(a, b)
                assert lcm_ab % a == 0, f"lcm({a}, {b}) = {lcm_ab} should be divisible by {a}"
                assert lcm_ab % b == 0, f"lcm({a}, {b}) = {lcm_ab} should be divisible by {b}"

    def test_gcd_lcm_relationship(self):
        """Test the relationship between gcd and lcm."""
        test_pairs = [(12, 8), (48, 18), (7, 5), (100, 25)]

        for a, b in test_pairs:
            if a != 0 and b != 0:
                gcd_val = disc_module.gcd(a, b)
                lcm_val = disc_module.lcm(a, b)

                # gcd(a, b) * lcm(a, b) = |a * b|
                assert gcd_val * lcm_val == abs(a * b), f"gcd({a}, {b}) * lcm({a}, {b}) should equal |{a} * {b}|"


class TestCombinatorics:
    """Test combinatorial functions."""

    def test_combination(self):
        """Test combination function."""
        test_cases = [
            (5, 0, 1),  # C(n, 0) = 1
            (5, 1, 5),  # C(n, 1) = n
            (5, 2, 10),  # C(5, 2) = 10
            (5, 3, 10),  # C(5, 3) = C(5, 2) = 10
            (5, 4, 5),  # C(5, 4) = C(5, 1) = 5
            (5, 5, 1),  # C(n, n) = 1
            (10, 3, 120),  # C(10, 3) = 120
            (0, 0, 1),  # C(0, 0) = 1
            (4, 2, 6),  # C(4, 2) = 6
        ]

        for n, k, expected in test_cases:
            result = disc_module.combination(n, k)
            assert result == expected, f"combination({n}, {k}) should be {expected}, got {result}"

    def test_combination_invalid(self):
        """Test combination function with invalid inputs."""
        # k > n returns 0
        assert disc_module.combination(5, 6) == 0

        # Negative n
        with pytest.raises(ValueError):
            disc_module.combination(-1, 0)

        # Negative k
        with pytest.raises(ValueError):
            disc_module.combination(5, -1)

    def test_combination_properties(self):
        """Test mathematical properties of combinations."""
        # C(n, k) = C(n, n-k) (symmetry)
        test_cases = [(5, 2), (10, 3), (8, 5)]

        for n, k in test_cases:
            comb_nk = disc_module.combination(n, k)
            comb_n_nk = disc_module.combination(n, n - k)
            assert comb_nk == comb_n_nk, f"C({n}, {k}) should equal C({n}, {n - k})"

    def test_combination_pascal_triangle(self):
        """Test Pascal's triangle property: C(n, k) = C(n-1, k-1) + C(n-1, k)."""
        test_cases = [(5, 2), (6, 3), (7, 4)]

        for n, k in test_cases:
            if n > 0 and k > 0:
                comb_nk = disc_module.combination(n, k)
                comb_left = disc_module.combination(n - 1, k - 1)
                comb_right = disc_module.combination(n - 1, k)

                assert comb_nk == comb_left + comb_right, (
                    f"C({n}, {k}) should equal C({n - 1}, {k - 1}) + C({n - 1}, {k})"
                )

    def test_permutation(self):
        """Test permutation function."""
        test_cases = [
            (5, 0, 1),  # P(n, 0) = 1
            (5, 1, 5),  # P(n, 1) = n
            (5, 2, 20),  # P(5, 2) = 5 * 4 = 20
            (5, 3, 60),  # P(5, 3) = 5 * 4 * 3 = 60
            (5, 5, 120),  # P(n, n) = n!
            (0, 0, 1),  # P(0, 0) = 1
            (4, 2, 12),  # P(4, 2) = 4 * 3 = 12
            (10, 3, 720),  # P(10, 3) = 10 * 9 * 8 = 720
        ]

        for n, k, expected in test_cases:
            result = disc_module.permutation(n, k)
            assert result == expected, f"permutation({n}, {k}) should be {expected}, got {result}"

    def test_permutation_default_k(self):
        """Test permutation function with default k (should equal n!)."""
        test_cases = [
            (0, 1),  # 0! = 1
            (1, 1),  # 1! = 1
            (3, 6),  # 3! = 6
            (4, 24),  # 4! = 24
            (5, 120),  # 5! = 120
        ]

        for n, expected in test_cases:
            result = disc_module.permutation(n)  # k defaults to n
            assert result == expected, f"permutation({n}) should be {expected}, got {result}"

    def test_permutation_invalid(self):
        """Test permutation function with invalid inputs."""
        # k > n returns 0
        assert disc_module.permutation(5, 6) == 0

        # Negative n
        with pytest.raises(ValueError):
            disc_module.permutation(-1, 0)

        # Negative k
        with pytest.raises(ValueError):
            disc_module.permutation(5, -1)

    def test_permutation_combination_relationship(self):
        """Test relationship between permutations and combinations."""
        test_cases = [(5, 2), (6, 3), (8, 4)]

        for n, k in test_cases:
            perm_nk = disc_module.permutation(n, k)
            comb_nk = disc_module.combination(n, k)
            factorial_k = disc_module.factorial(k)

            # P(n, k) = C(n, k) * k!
            assert perm_nk == comb_nk * factorial_k, f"P({n}, {k}) should equal C({n}, {k}) * {k}!"

    def test_permutation_factorial_relationship(self):
        """Test relationship between permutations and factorials."""
        test_cases = [(5, 2), (6, 3), (8, 4)]

        for n, k in test_cases:
            perm_nk = disc_module.permutation(n, k)
            factorial_n = disc_module.factorial(n)
            factorial_n_minus_k = disc_module.factorial(n - k)

            # P(n, k) = n! / (n-k)!
            assert perm_nk == factorial_n // factorial_n_minus_k, f"P({n}, {k}) should equal {n}! / ({n}-{k})!"


class TestEdgeCases:
    """Test edge cases and boundary conditions."""

    def test_zero_inputs(self):
        """Test functions with zero inputs."""
        # isqrt(0) = 0
        assert disc_module.isqrt(0) == 0

        # factorial(0) = 1
        assert disc_module.factorial(0) == 1

        # gcd with zero
        assert disc_module.gcd(0, 5) == 5
        assert disc_module.gcd(5, 0) == 5
        assert disc_module.gcd(0, 0) == 0

        # lcm with zero
        assert disc_module.lcm(0, 5) == 0
        assert disc_module.lcm(5, 0) == 0

        # Combinations with zero
        assert disc_module.combination(5, 0) == 1
        assert disc_module.combination(0, 0) == 1

        # Permutations with zero
        assert disc_module.permutation(5, 0) == 1
        assert disc_module.permutation(0, 0) == 1

    def test_large_numbers(self):
        """Test functions with large numbers."""
        # Test that functions can handle reasonably large inputs
        large_n = 1000

        # isqrt should work with large numbers
        result = disc_module.isqrt(large_n * large_n)
        assert result == large_n

        # gcd should work with large numbers
        result = disc_module.gcd(large_n, large_n // 2)
        assert result == large_n // 2

    def test_negative_handling(self):
        """Test how functions handle negative inputs."""
        # Functions that should raise ValueError with negative inputs
        negative_input_functions = [
            (disc_module.isqrt, [-1]),
            (disc_module.factorial, [-1]),
            (disc_module.combination, [-1, 0]),
            (disc_module.combination, [5, -1]),
            (disc_module.permutation, [-1, 0]),
            (disc_module.permutation, [5, -1]),
        ]

        for func, args in negative_input_functions:
            with pytest.raises(ValueError):
                func(*args)

        # gcd and lcm should handle negative inputs gracefully
        assert disc_module.gcd(-12, 8) == 4
        assert disc_module.gcd(12, -8) == 4
        assert disc_module.gcd(-12, -8) == 4

        assert disc_module.lcm(-12, 8) == 24
        assert disc_module.lcm(12, -8) == 24
        assert disc_module.lcm(-12, -8) == 24

    def test_type_consistency(self):
        """Test that functions return consistent integer types."""
        # All these functions should return integers
        functions_and_args = [
            (disc_module.isqrt, [16]),
            (disc_module.factorial, [5]),
            (disc_module.gcd, [12, 8]),
            (disc_module.lcm, [12, 8]),
            (disc_module.combination, [5, 2]),
            (disc_module.permutation, [5, 2]),
        ]

        for func, args in functions_and_args:
            result = func(*args)
            assert isinstance(result, int), f"{func.__name__} should return an integer"
