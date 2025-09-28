"""Tests for minimcp_servers.modules.math.continuous module."""

import math

import pytest

from minimcp_servers.modules.math import continuous as cont_module


class TestTrigonometricFunctions:
    """Test trigonometric functions."""

    def test_sin(self):
        """Test sin function."""
        test_cases = [
            (0.0, 0.0),
            (math.pi / 6, 0.5),
            (math.pi / 4, math.sqrt(2) / 2),
            (math.pi / 3, math.sqrt(3) / 2),
            (math.pi / 2, 1.0),
            (math.pi, 0.0),
            (3 * math.pi / 2, -1.0),
            (2 * math.pi, 0.0),
            (-math.pi / 2, -1.0),
        ]

        for x, expected in test_cases:
            result = cont_module.sin(x)
            assert abs(result - expected) < 1e-10, f"sin({x}) should be {expected}, got {result}"

    def test_cos(self):
        """Test cos function."""
        test_cases = [
            (0.0, 1.0),
            (math.pi / 6, math.sqrt(3) / 2),
            (math.pi / 4, math.sqrt(2) / 2),
            (math.pi / 3, 0.5),
            (math.pi / 2, 0.0),
            (math.pi, -1.0),
            (3 * math.pi / 2, 0.0),
            (2 * math.pi, 1.0),
            (-math.pi / 2, 0.0),
        ]

        for x, expected in test_cases:
            result = cont_module.cos(x)
            assert abs(result - expected) < 1e-10, f"cos({x}) should be {expected}, got {result}"

    def test_tan(self):
        """Test tan function."""
        test_cases = [
            (0.0, 0.0),
            (math.pi / 6, 1 / math.sqrt(3)),
            (math.pi / 4, 1.0),
            (math.pi / 3, math.sqrt(3)),
            (math.pi, 0.0),
            (-math.pi / 4, -1.0),
        ]

        for x, expected in test_cases:
            result = cont_module.tan(x)
            assert abs(result - expected) < 1e-10, f"tan({x}) should be {expected}, got {result}"

    def test_asin(self):
        """Test asin function."""
        test_cases = [
            (0.0, 0.0),
            (0.5, math.pi / 6),
            (math.sqrt(2) / 2, math.pi / 4),
            (math.sqrt(3) / 2, math.pi / 3),
            (1.0, math.pi / 2),
            (-0.5, -math.pi / 6),
            (-1.0, -math.pi / 2),
        ]

        for x, expected in test_cases:
            result = cont_module.asin(x)
            assert abs(result - expected) < 1e-10, f"asin({x}) should be {expected}, got {result}"

    def test_asin_domain_error(self):
        """Test asin function with out-of-domain values."""
        with pytest.raises(ValueError):
            cont_module.asin(1.5)

        with pytest.raises(ValueError):
            cont_module.asin(-1.5)

    def test_acos(self):
        """Test acos function."""
        test_cases = [
            (1.0, 0.0),
            (math.sqrt(3) / 2, math.pi / 6),
            (math.sqrt(2) / 2, math.pi / 4),
            (0.5, math.pi / 3),
            (0.0, math.pi / 2),
            (-0.5, 2 * math.pi / 3),
            (-1.0, math.pi),
        ]

        for x, expected in test_cases:
            result = cont_module.acos(x)
            assert abs(result - expected) < 1e-10, f"acos({x}) should be {expected}, got {result}"

    def test_acos_domain_error(self):
        """Test acos function with out-of-domain values."""
        with pytest.raises(ValueError):
            cont_module.acos(1.5)

        with pytest.raises(ValueError):
            cont_module.acos(-1.5)

    def test_atan(self):
        """Test atan function."""
        test_cases = [
            (0.0, 0.0),
            (1 / math.sqrt(3), math.pi / 6),
            (1.0, math.pi / 4),
            (math.sqrt(3), math.pi / 3),
            (-1.0, -math.pi / 4),
        ]

        for x, expected in test_cases:
            result = cont_module.atan(x)
            assert abs(result - expected) < 1e-10, f"atan({x}) should be {expected}, got {result}"

    def test_atan2(self):
        """Test atan2 function."""
        test_cases = [
            (0.0, 1.0, 0.0),
            (1.0, 1.0, math.pi / 4),
            (1.0, 0.0, math.pi / 2),
            (1.0, -1.0, 3 * math.pi / 4),
            (0.0, -1.0, math.pi),
            (-1.0, -1.0, -3 * math.pi / 4),
            (-1.0, 0.0, -math.pi / 2),
            (-1.0, 1.0, -math.pi / 4),
        ]

        for y, x, expected in test_cases:
            result = cont_module.atan2(y, x)
            assert abs(result - expected) < 1e-10, f"atan2({y}, {x}) should be {expected}, got {result}"

    def test_trig_identities(self):
        """Test trigonometric identities."""
        test_angles = [0.0, math.pi / 6, math.pi / 4, math.pi / 3, math.pi / 2, math.pi]

        for angle in test_angles:
            # sin^2 + cos^2 = 1
            sin_val = cont_module.sin(angle)
            cos_val = cont_module.cos(angle)
            assert abs(sin_val**2 + cos_val**2 - 1.0) < 1e-10, f"sin^2 + cos^2 identity failed for angle {angle}"

            # tan = sin/cos (when cos != 0)
            if abs(cos_val) > 1e-10:
                tan_val = cont_module.tan(angle)
                expected_tan = sin_val / cos_val
                assert abs(tan_val - expected_tan) < 1e-10, f"tan = sin/cos identity failed for angle {angle}"


class TestHyperbolicFunctions:
    """Test hyperbolic functions."""

    def test_sinh(self):
        """Test sinh function."""
        test_cases = [
            (0.0, 0.0),
            (1.0, (math.e - 1 / math.e) / 2),
            (-1.0, -(math.e - 1 / math.e) / 2),
            (math.log(2), 0.75),  # sinh(ln(2)) = 3/4
        ]

        for x, expected in test_cases:
            result = cont_module.sinh(x)
            assert abs(result - expected) < 1e-10, f"sinh({x}) should be {expected}, got {result}"

    def test_cosh(self):
        """Test cosh function."""
        test_cases = [
            (0.0, 1.0),
            (1.0, (math.e + 1 / math.e) / 2),
            (-1.0, (math.e + 1 / math.e) / 2),  # cosh is even function
            (math.log(2), 1.25),  # cosh(ln(2)) = 5/4
        ]

        for x, expected in test_cases:
            result = cont_module.cosh(x)
            assert abs(result - expected) < 1e-10, f"cosh({x}) should be {expected}, got {result}"

    def test_tanh(self):
        """Test tanh function."""
        test_cases = [
            (0.0, 0.0),
            (float("inf"), 1.0),
            (float("-inf"), -1.0),
        ]

        for x, expected in test_cases:
            result = cont_module.tanh(x)
            assert abs(result - expected) < 1e-10, f"tanh({x}) should be {expected}, got {result}"

    def test_asinh(self):
        """Test asinh function."""
        test_cases = [
            (0.0, 0.0),
            (0.75, math.log(2)),  # asinh(3/4) = ln(2)
        ]

        for x, expected in test_cases:
            result = cont_module.asinh(x)
            assert abs(result - expected) < 1e-10, f"asinh({x}) should be {expected}, got {result}"

    def test_acosh(self):
        """Test acosh function."""
        test_cases = [
            (1.0, 0.0),
            (1.25, math.log(2)),  # acosh(5/4) = ln(2)
        ]

        for x, expected in test_cases:
            result = cont_module.acosh(x)
            assert abs(result - expected) < 1e-10, f"acosh({x}) should be {expected}, got {result}"

    def test_acosh_domain_error(self):
        """Test acosh function with out-of-domain values."""
        with pytest.raises(ValueError):
            cont_module.acosh(0.5)  # x < 1

    def test_atanh(self):
        """Test atanh function."""
        test_cases = [
            (0.0, 0.0),
            (0.5, 0.5 * math.log(3)),  # atanh(1/2) = (1/2)ln(3)
        ]

        for x, expected in test_cases:
            result = cont_module.atanh(x)
            assert abs(result - expected) < 1e-10, f"atanh({x}) should be {expected}, got {result}"

    def test_atanh_domain_error(self):
        """Test atanh function with out-of-domain values."""
        with pytest.raises(ValueError):
            cont_module.atanh(1.5)  # |x| >= 1

        with pytest.raises(ValueError):
            cont_module.atanh(-1.5)

    def test_hyperbolic_identities(self):
        """Test hyperbolic identities."""
        test_values = [0.0, 0.5, 1.0, 2.0]

        for x in test_values:
            # cosh^2 - sinh^2 = 1
            sinh_val = cont_module.sinh(x)
            cosh_val = cont_module.cosh(x)
            assert abs(cosh_val**2 - sinh_val**2 - 1.0) < 1e-10, f"cosh^2 - sinh^2 identity failed for x = {x}"

            # tanh = sinh/cosh
            tanh_val = cont_module.tanh(x)
            expected_tanh = sinh_val / cosh_val
            assert abs(tanh_val - expected_tanh) < 1e-10, f"tanh = sinh/cosh identity failed for x = {x}"


class TestExponentialFunctions:
    """Test exponential functions."""

    def test_exp(self):
        """Test exp function."""
        test_cases = [
            (0.0, 1.0),
            (1.0, math.e),
            (2.0, math.e**2),
            (-1.0, 1 / math.e),
            (math.log(2), 2.0),
        ]

        for x, expected in test_cases:
            result = cont_module.exp(x)
            assert abs(result - expected) < 1e-10, f"exp({x}) should be {expected}, got {result}"

    def test_expm1(self):
        """Test expm1 function."""
        test_cases = [
            (0.0, 0.0),
            (1.0, math.e - 1),
            (-1.0, 1 / math.e - 1),
            (1e-10, 1e-10),  # Small values where expm1 is more accurate
        ]

        for x, expected in test_cases:
            result = cont_module.expm1(x)
            assert abs(result - expected) < 1e-10, f"expm1({x}) should be {expected}, got {result}"

    def test_expm1_accuracy(self):
        """Test that expm1 is more accurate than exp(x)-1 for small x."""
        small_x = 1e-15

        # For very small x, exp(x) - 1 might lose precision
        # but expm1(x) should be accurate
        result = cont_module.expm1(small_x)

        # For small x, expm1(x) ≈ x
        assert abs(result - small_x) < 1e-16, f"expm1({small_x}) should be approximately {small_x} for small x"


class TestLogarithmicFunctions:
    """Test logarithmic functions."""

    def test_log_natural(self):
        """Test log function with natural logarithm (default)."""
        test_cases = [
            (1.0, 0.0),
            (math.e, 1.0),
            (math.e**2, 2.0),
            (2.0, math.log(2)),
            (0.5, -math.log(2)),
        ]

        for x, expected in test_cases:
            result = cont_module.log(x)
            assert abs(result - expected) < 1e-10, f"log({x}) should be {expected}, got {result}"

    def test_log_custom_base(self):
        """Test log function with custom base."""
        test_cases = [
            (8.0, 2.0, 3.0),  # log_2(8) = 3
            (100.0, 10.0, 2.0),  # log_10(100) = 2
            (27.0, 3.0, 3.0),  # log_3(27) = 3
            (1.0, 5.0, 0.0),  # log_b(1) = 0 for any base
        ]

        for x, base, expected in test_cases:
            result = cont_module.log(x, base)
            assert abs(result - expected) < 1e-10, f"log({x}, {base}) should be {expected}, got {result}"

    def test_log_domain_error(self):
        """Test log function with invalid domain."""
        with pytest.raises(ValueError):
            cont_module.log(0.0)

        with pytest.raises(ValueError):
            cont_module.log(-1.0)

    def test_log10(self):
        """Test log10 function."""
        test_cases = [
            (1.0, 0.0),
            (10.0, 1.0),
            (100.0, 2.0),
            (1000.0, 3.0),
            (0.1, -1.0),
            (0.01, -2.0),
        ]

        for x, expected in test_cases:
            result = cont_module.log10(x)
            assert abs(result - expected) < 1e-10, f"log10({x}) should be {expected}, got {result}"

    def test_log2(self):
        """Test log2 function."""
        test_cases = [
            (1.0, 0.0),
            (2.0, 1.0),
            (4.0, 2.0),
            (8.0, 3.0),
            (0.5, -1.0),
            (0.25, -2.0),
        ]

        for x, expected in test_cases:
            result = cont_module.log2(x)
            assert abs(result - expected) < 1e-10, f"log2({x}) should be {expected}, got {result}"

    def test_log1p(self):
        """Test log1p function."""
        test_cases = [
            (0.0, 0.0),
            (math.e - 1, 1.0),
            (1.0, math.log(2)),
            (-0.5, math.log(0.5)),
        ]

        for x, expected in test_cases:
            result = cont_module.log1p(x)
            assert abs(result - expected) < 1e-10, f"log1p({x}) should be {expected}, got {result}"

    def test_log1p_accuracy(self):
        """Test that log1p is more accurate than log(1+x) for small x."""
        small_x = 1e-15

        result = cont_module.log1p(small_x)

        # For small x, log1p(x) ≈ x
        assert abs(result - small_x) < 1e-16, f"log1p({small_x}) should be approximately {small_x} for small x"

    def test_log_exp_inverse(self):
        """Test that log and exp are inverse functions."""
        test_values = [0.5, 1.0, 2.0, 5.0]

        for x in test_values:
            # exp(log(x)) = x
            log_x = cont_module.log(x)
            exp_log_x = cont_module.exp(log_x)
            assert abs(exp_log_x - x) < 1e-10, f"exp(log({x})) should equal {x}"

            # log(exp(x)) = x
            exp_x = cont_module.exp(x)
            log_exp_x = cont_module.log(exp_x)
            assert abs(log_exp_x - x) < 1e-10, f"log(exp({x})) should equal {x}"


class TestAngularConversion:
    """Test angular conversion functions."""

    def test_degrees(self):
        """Test degrees function."""
        test_cases = [
            (0.0, 0.0),
            (math.pi / 6, 30.0),
            (math.pi / 4, 45.0),
            (math.pi / 3, 60.0),
            (math.pi / 2, 90.0),
            (math.pi, 180.0),
            (2 * math.pi, 360.0),
            (-math.pi / 2, -90.0),
        ]

        for radians, expected_degrees in test_cases:
            result = cont_module.degrees(radians)
            assert abs(result - expected_degrees) < 1e-10, (
                f"degrees({radians}) should be {expected_degrees}, got {result}"
            )

    def test_radians(self):
        """Test radians function."""
        test_cases = [
            (0.0, 0.0),
            (30.0, math.pi / 6),
            (45.0, math.pi / 4),
            (60.0, math.pi / 3),
            (90.0, math.pi / 2),
            (180.0, math.pi),
            (360.0, 2 * math.pi),
            (-90.0, -math.pi / 2),
        ]

        for degrees_val, expected_radians in test_cases:
            result = cont_module.radians(degrees_val)
            assert abs(result - expected_radians) < 1e-10, (
                f"radians({degrees_val}) should be {expected_radians}, got {result}"
            )

    def test_degrees_radians_inverse(self):
        """Test that degrees and radians are inverse functions."""
        test_values = [0.0, 30.0, 45.0, 90.0, 180.0, 270.0, 360.0]

        for degrees_val in test_values:
            # radians(degrees(x)) = x (for radians input)
            radians_val = cont_module.radians(degrees_val)
            back_to_degrees = cont_module.degrees(radians_val)
            assert abs(back_to_degrees - degrees_val) < 1e-10, (
                f"degrees(radians({degrees_val})) should equal {degrees_val}"
            )


class TestDistanceAndGeometric:
    """Test distance and geometric functions."""

    def test_hypot(self):
        """Test hypot function."""
        test_cases = [
            (3.0, 4.0, 5.0),  # 3-4-5 triangle
            (5.0, 12.0, 13.0),  # 5-12-13 triangle
            (0.0, 0.0, 0.0),
            (1.0, 0.0, 1.0),
            (0.0, 1.0, 1.0),
            (-3.0, 4.0, 5.0),  # Should handle negative values
        ]

        for x, y, expected in test_cases:
            result = cont_module.hypot(x, y)
            assert abs(result - expected) < 1e-10, f"hypot({x}, {y}) should be {expected}, got {result}"

    def test_multidimensional_hypot(self):
        """Test multidimensional_hypot function."""
        test_cases = [
            ([3.0, 4.0], 5.0),  # 2D case
            ([1.0, 2.0, 2.0], 3.0),  # 3D case
            ([0.0, 0.0, 0.0], 0.0),  # Zero vector
            ([1.0], 1.0),  # 1D case
            ([2.0, 2.0, 2.0, 2.0], 4.0),  # 4D case
        ]

        for coords, expected in test_cases:
            result = cont_module.multidimensional_hypot(coords)
            assert abs(result - expected) < 1e-10, (
                f"multidimensional_hypot({coords}) should be {expected}, got {result}"
            )

    def test_dist(self):
        """Test dist function."""
        test_cases = [
            ([0.0, 0.0], [3.0, 4.0], 5.0),  # 2D distance
            ([1.0, 1.0], [4.0, 5.0], 5.0),  # 2D distance
            ([0.0, 0.0, 0.0], [1.0, 2.0, 2.0], 3.0),  # 3D distance
            ([1.0, 2.0], [1.0, 2.0], 0.0),  # Same point
        ]

        for p, q, expected in test_cases:
            result = cont_module.dist(p, q)
            assert abs(result - expected) < 1e-10, f"dist({p}, {q}) should be {expected}, got {result}"

    def test_dist_dimension_mismatch(self):
        """Test dist function with mismatched dimensions."""
        with pytest.raises(ValueError):
            cont_module.dist([1.0, 2.0], [1.0, 2.0, 3.0])


class TestSpecialFunctions:
    """Test special mathematical functions."""

    def test_gamma(self):
        """Test gamma function."""
        test_cases = [
            (1.0, 1.0),  # Γ(1) = 1
            (2.0, 1.0),  # Γ(2) = 1! = 1
            (3.0, 2.0),  # Γ(3) = 2! = 2
            (4.0, 6.0),  # Γ(4) = 3! = 6
            (0.5, math.sqrt(math.pi)),  # Γ(1/2) = √π
        ]

        for x, expected in test_cases:
            result = cont_module.gamma(x)
            assert abs(result - expected) < 1e-10, f"gamma({x}) should be {expected}, got {result}"

    def test_lgamma(self):
        """Test lgamma function."""
        test_cases = [
            (1.0, 0.0),  # ln(Γ(1)) = ln(1) = 0
            (2.0, 0.0),  # ln(Γ(2)) = ln(1) = 0
            (3.0, math.log(2)),  # ln(Γ(3)) = ln(2)
            (4.0, math.log(6)),  # ln(Γ(4)) = ln(6)
        ]

        for x, expected in test_cases:
            result = cont_module.lgamma(x)
            assert abs(result - expected) < 1e-10, f"lgamma({x}) should be {expected}, got {result}"

    def test_erf(self):
        """Test erf function."""
        test_cases = [
            (0.0, 0.0),
            (float("inf"), 1.0),
            (float("-inf"), -1.0),
        ]

        for x, expected in test_cases:
            result = cont_module.erf(x)
            assert abs(result - expected) < 1e-10, f"erf({x}) should be {expected}, got {result}"

    def test_erfc(self):
        """Test erfc function."""
        test_cases = [
            (0.0, 1.0),
            (float("inf"), 0.0),
            (float("-inf"), 2.0),
        ]

        for x, expected in test_cases:
            result = cont_module.erfc(x)
            assert abs(result - expected) < 1e-10, f"erfc({x}) should be {expected}, got {result}"

    def test_erf_erfc_complement(self):
        """Test that erf + erfc = 1."""
        test_values = [0.0, 0.5, 1.0, 2.0, -1.0]

        for x in test_values:
            erf_val = cont_module.erf(x)
            erfc_val = cont_module.erfc(x)
            assert abs(erf_val + erfc_val - 1.0) < 1e-10, f"erf({x}) + erfc({x}) should equal 1.0"


class TestSpecialCases:
    """Test special cases and edge conditions."""

    def test_infinity_handling(self):
        """Test functions with infinity values."""
        inf = float("inf")
        ninf = float("-inf")

        # Exponential functions
        assert cont_module.exp(inf) == inf
        assert cont_module.exp(ninf) == 0.0

        # Trigonometric functions with infinity raise ValueError
        with pytest.raises(ValueError):
            cont_module.sin(inf)

        with pytest.raises(ValueError):
            cont_module.cos(inf)

        # Hyperbolic functions
        assert cont_module.sinh(inf) == inf
        assert cont_module.sinh(ninf) == ninf
        assert cont_module.cosh(inf) == inf
        assert cont_module.cosh(ninf) == inf
        assert cont_module.tanh(inf) == 1.0
        assert cont_module.tanh(ninf) == -1.0

    def test_nan_propagation(self):
        """Test that NaN values propagate correctly."""
        nan = float("nan")

        # Most functions should propagate NaN
        functions_to_test = [
            cont_module.sin,
            cont_module.cos,
            cont_module.tan,
            cont_module.sinh,
            cont_module.cosh,
            cont_module.tanh,
            cont_module.exp,
            cont_module.log,
        ]

        for func in functions_to_test:
            result = func(nan)
            assert math.isnan(result), f"{func.__name__}(nan) should return nan"

    def test_very_small_values(self):
        """Test functions with very small values."""
        tiny = 1e-100

        # These should handle tiny values gracefully
        assert abs(cont_module.sin(tiny) - tiny) < 1e-110  # sin(x) ≈ x for small x
        assert abs(cont_module.tan(tiny) - tiny) < 1e-110  # tan(x) ≈ x for small x
        assert abs(cont_module.sinh(tiny) - tiny) < 1e-110  # sinh(x) ≈ x for small x
