"""Tests for minimcp_servers.modules.random_generator module."""

import re
import string
import sys
import uuid

import pytest

from minimcp_servers.modules import random_generator as rg_module


class TestGenerateUUID:
    """Test UUID generation function."""

    def test_generate_uuid_format(self):
        """Test that generate_uuid returns valid UUID format."""
        result = rg_module.generate_uuid()

        assert isinstance(result, str)
        # UUID4 format: 8-4-4-4-12 hexadecimal digits
        uuid_pattern = r"^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$"
        assert re.match(uuid_pattern, result, re.IGNORECASE), f"Invalid UUID format: {result}"

    def test_generate_uuid_uniqueness(self):
        """Test that generate_uuid generates unique values."""
        uuids = [rg_module.generate_uuid() for _ in range(100)]

        # All UUIDs should be unique
        assert len(set(uuids)) == 100, "UUIDs should be unique"

    def test_generate_uuid_parseable(self):
        """Test that generated UUID can be parsed by uuid module."""
        result = rg_module.generate_uuid()

        # Should not raise an exception
        parsed_uuid = uuid.UUID(result)
        assert str(parsed_uuid) == result
        assert parsed_uuid.version == 4  # Should be UUID4


class TestGenerateRandomNumber:
    """Test random number generation function."""

    def test_generate_random_number_default_range(self):
        """Test generate_random_number with default range."""
        result = rg_module.generate_random_number()

        assert isinstance(result, int)
        assert 0 <= result <= sys.maxsize

    def test_generate_random_number_custom_range(self):
        """Test generate_random_number with custom range."""
        min_val, max_val = 10, 20
        result = rg_module.generate_random_number(min_val, max_val)

        assert isinstance(result, int)
        assert min_val <= result <= max_val

    def test_generate_random_number_single_value(self):
        """Test generate_random_number with min_value == max_value - 1."""
        min_val, max_val = 5, 5

        with pytest.raises(ValueError, match="min_value must be < max_value"):
            rg_module.generate_random_number(min_val, max_val)

    def test_generate_random_number_invalid_range(self):
        """Test generate_random_number with invalid range."""
        test_cases = [
            (10, 5),  # min > max
            (5, 5),  # min == max
            (0, -1),  # max < min
        ]

        for min_val, max_val in test_cases:
            with pytest.raises(ValueError, match="min_value must be < max_value"):
                rg_module.generate_random_number(min_val, max_val)

    def test_generate_random_number_negative_range(self):
        """Test generate_random_number with negative values."""
        min_val, max_val = -10, -5
        result = rg_module.generate_random_number(min_val, max_val)

        assert isinstance(result, int)
        assert min_val <= result <= max_val

    def test_generate_random_number_zero_range(self):
        """Test generate_random_number with range including zero."""
        min_val, max_val = -5, 5
        result = rg_module.generate_random_number(min_val, max_val)

        assert isinstance(result, int)
        assert min_val <= result <= max_val

    def test_generate_random_number_large_range(self):
        """Test generate_random_number with large range."""
        min_val, max_val = 0, 1000000
        result = rg_module.generate_random_number(min_val, max_val)

        assert isinstance(result, int)
        assert min_val <= result <= max_val

    def test_generate_random_number_distribution(self):
        """Test that generate_random_number produces varied results."""
        min_val, max_val = 1, 10
        results = [rg_module.generate_random_number(min_val, max_val) for _ in range(100)]

        # Should have some variety (not all the same number)
        unique_results = set(results)
        assert len(unique_results) > 1, "Should generate varied numbers"

        # All should be in range
        assert all(min_val <= r <= max_val for r in results)


class TestGenerateRandomText:
    """Test random text generation function."""

    def test_generate_random_text_default_length(self):
        """Test generate_random_text with default length."""
        result = rg_module.generate_random_text()

        assert isinstance(result, str)
        assert len(result) == 10  # Default length

    def test_generate_random_text_custom_length(self):
        """Test generate_random_text with custom lengths."""
        test_lengths = [0, 1, 5, 20, 100]

        for length in test_lengths:
            result = rg_module.generate_random_text(length)

            assert isinstance(result, str)
            assert len(result) == length

    def test_generate_random_text_character_set(self):
        """Test that generate_random_text uses correct character set."""
        result = rg_module.generate_random_text(100)  # Larger sample for better testing

        expected_chars = set(string.ascii_letters + string.digits)
        result_chars = set(result)

        # All characters in result should be from expected set
        assert result_chars.issubset(expected_chars), f"Unexpected characters: {result_chars - expected_chars}"

    def test_generate_random_text_variety(self):
        """Test that generate_random_text produces varied results."""
        results = [rg_module.generate_random_text(20) for _ in range(50)]

        # Should have some variety (not all the same)
        unique_results = set(results)
        assert len(unique_results) > 1, "Should generate varied text strings"

    def test_generate_random_text_empty(self):
        """Test generate_random_text with zero length."""
        result = rg_module.generate_random_text(0)

        assert isinstance(result, str)
        assert result == ""

    def test_generate_random_text_negative_length(self):
        """Test generate_random_text with negative length."""
        with pytest.raises(ValueError, match="length must be non-negative"):
            rg_module.generate_random_text(-1)

    def test_generate_random_text_contains_letters_and_digits(self):
        """Test that generate_random_text can produce both letters and digits."""
        # Generate many samples to increase chance of getting both
        samples = [rg_module.generate_random_text(50) for _ in range(20)]
        combined = "".join(samples)

        has_letter = any(c.isalpha() for c in combined)
        has_digit = any(c.isdigit() for c in combined)

        # With enough samples, we should see both letters and digits
        assert has_letter, "Should generate letters"
        assert has_digit, "Should generate digits"

    def test_generate_random_text_case_variety(self):
        """Test that generate_random_text produces both upper and lower case."""
        # Generate many samples to increase chance of getting both cases
        samples = [rg_module.generate_random_text(50) for _ in range(20)]
        combined = "".join(samples)

        has_upper = any(c.isupper() for c in combined)
        has_lower = any(c.islower() for c in combined)

        # With enough samples, we should see both cases
        assert has_upper, "Should generate uppercase letters"
        assert has_lower, "Should generate lowercase letters"


class TestSecurityProperties:
    """Test security properties of random generation functions."""

    def test_uuid_cryptographic_randomness(self):
        """Test that UUIDs show good randomness properties."""
        uuids = [rg_module.generate_uuid() for _ in range(1000)]

        # Check that we don't have obvious patterns
        # UUIDs should be well distributed across the hex space
        first_chars = [uuid[0] for uuid in uuids]
        unique_first_chars = set(first_chars)

        # Should have good variety in first character (at least 8 different hex digits)
        assert len(unique_first_chars) >= 8, "UUIDs should have good distribution"

    def test_random_number_unpredictability(self):
        """Test that random numbers are not easily predictable."""
        # Generate sequence of numbers in small range
        numbers = [rg_module.generate_random_number(1, 10) for _ in range(100)]

        # Should not be all the same (extremely unlikely with good randomness)
        unique_numbers = set(numbers)
        assert len(unique_numbers) > 1, "Numbers should vary"

        # Should not have obvious sequential patterns
        # Check that not all consecutive pairs are sequential
        sequential_pairs = sum(1 for i in range(len(numbers) - 1) if abs(numbers[i + 1] - numbers[i]) == 1)

        # With good randomness, most pairs shouldn't be sequential
        assert sequential_pairs < len(numbers) * 0.3, "Should not have too many sequential pairs"


class TestEdgeCases:
    """Test edge cases and boundary conditions."""

    def test_random_number_boundary_values(self):
        """Test random number generation at boundary values."""
        # Test with sys.maxsize
        result = rg_module.generate_random_number(0, sys.maxsize)
        assert 0 <= result <= sys.maxsize

        # Test with negative sys.maxsize (if supported)
        result = rg_module.generate_random_number(-1000, 1000)
        assert -1000 <= result <= 1000

    def test_random_text_large_length(self):
        """Test random text generation with large length."""
        large_length = 10000
        result = rg_module.generate_random_text(large_length)

        assert isinstance(result, str)
        assert len(result) == large_length

    def test_function_independence(self):
        """Test that different function calls are independent."""
        # Generate multiple values and ensure they're different
        uuids = [rg_module.generate_uuid() for _ in range(10)]
        numbers = [rg_module.generate_random_number(1, 1000) for _ in range(10)]
        texts = [rg_module.generate_random_text(20) for _ in range(10)]

        # Should have variety in each type
        assert len(set(uuids)) == 10, "UUIDs should be unique"
        assert len(set(numbers)) > 1, "Numbers should vary"
        assert len(set(texts)) > 1, "Texts should vary"


class TestTypeConsistency:
    """Test that functions return consistent types."""

    def test_return_types(self):
        """Test that functions return expected types consistently."""
        # UUID should always return string
        for _ in range(10):
            result = rg_module.generate_uuid()
            assert isinstance(result, str)

        # Random number should always return int
        for _ in range(10):
            result = rg_module.generate_random_number(1, 100)
            assert isinstance(result, int)

        # Random text should always return string
        for _ in range(10):
            result = rg_module.generate_random_text(10)
            assert isinstance(result, str)
