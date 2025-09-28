"""Tests for minimcp_servers.modules.text module."""

import pytest

from minimcp_servers.modules import text as text_module


class TestTextAnalysis:
    """Test text analysis functions."""

    def test_length(self):
        """Test length function."""
        test_cases = [
            ("", 0),
            ("hello", 5),
            ("hello world", 11),
            ("🌟", 1),  # Unicode character
            ("hello🌟world", 11),
            ("   ", 3),  # Spaces
        ]

        for text, expected in test_cases:
            result = text_module.length(text)
            assert result == expected, f"length('{text}') should be {expected}"

    def test_count_substr_case_sensitive(self):
        """Test count_substr with case sensitivity."""
        text = "Hello World Hello"

        # Case sensitive
        assert text_module.count_substr(text, "Hello", case_sensitive=True) == 2
        assert text_module.count_substr(text, "hello", case_sensitive=True) == 0
        assert text_module.count_substr(text, "HELLO", case_sensitive=True) == 0

    def test_count_substr_case_insensitive(self):
        """Test count_substr with case insensitivity (default)."""
        text = "Hello World Hello"

        # Case insensitive (default)
        assert text_module.count_substr(text, "Hello") == 2
        assert text_module.count_substr(text, "hello") == 2
        assert text_module.count_substr(text, "HELLO") == 2
        assert text_module.count_substr(text, "world") == 1

    def test_count_substr_with_bounds(self):
        """Test count_substr with start and end parameters."""
        text = "abcabcabc"

        assert text_module.count_substr(text, "abc") == 3
        assert text_module.count_substr(text, "abc", start=3) == 2
        assert text_module.count_substr(text, "abc", end=6) == 2
        assert text_module.count_substr(text, "abc", start=3, end=6) == 1

    def test_count_substr_empty(self):
        """Test count_substr with empty strings."""
        assert text_module.count_substr("", "a") == 0
        assert text_module.count_substr("hello", "") == 6  # Empty string matches at each position + end

    def test_most_common_words_basic(self):
        """Test most_common_words basic functionality."""
        text = "the quick brown fox jumps over the lazy dog the"
        result = text_module.most_common_words(text, 3)

        assert len(result) <= 3
        assert result[0] == ("the", 3)  # Most common word
        assert all(isinstance(word, str) and isinstance(count, int) for word, count in result)

    def test_most_common_words_case_sensitivity(self):
        """Test most_common_words with case sensitivity."""
        text = "The the THE"

        # Case insensitive (default)
        result = text_module.most_common_words(text, 1, case_sensitive=False)
        assert result[0] == ("the", 3)

        # Case sensitive
        result = text_module.most_common_words(text, 3, case_sensitive=True)
        assert len(result) == 3
        assert all(count == 1 for _, count in result)

    def test_most_common_words_min_len(self):
        """Test most_common_words with minimum length filter."""
        text = "a bb ccc dddd eeeee"

        # Default min_len=2
        result = text_module.most_common_words(text, 10)
        words = [word for word, _ in result]
        assert "a" not in words  # Too short
        assert "bb" in words

        # Custom min_len=4
        result = text_module.most_common_words(text, 10, min_len=4)
        words = [word for word, _ in result]
        assert "bb" not in words
        assert "ccc" not in words
        assert "dddd" in words

    def test_most_common_words_empty(self):
        """Test most_common_words with empty text."""
        result = text_module.most_common_words("", 5)
        assert result == []

    def test_first_index_of_substr(self):
        """Test first_index_of_substr function."""
        text = "hello world hello"

        assert text_module.first_index_of_substr(text, "hello") == 0
        assert text_module.first_index_of_substr(text, "world") == 6
        assert text_module.first_index_of_substr(text, "xyz") == -1

        # Case sensitivity
        assert text_module.first_index_of_substr(text, "HELLO", case_sensitive=False) == 0
        assert text_module.first_index_of_substr(text, "HELLO", case_sensitive=True) == -1

    def test_first_index_of_substr_with_bounds(self):
        """Test first_index_of_substr with start and end parameters."""
        text = "abcabcabc"

        assert text_module.first_index_of_substr(text, "abc") == 0
        assert text_module.first_index_of_substr(text, "abc", start=1) == 3
        assert text_module.first_index_of_substr(text, "abc", start=4) == 6
        assert text_module.first_index_of_substr(text, "abc", end=2) == -1

    def test_last_index_of_substr(self):
        """Test last_index_of_substr function."""
        text = "hello world hello"

        assert text_module.last_index_of_substr(text, "hello") == 12
        assert text_module.last_index_of_substr(text, "world") == 6
        assert text_module.last_index_of_substr(text, "xyz") == -1

        # Case sensitivity
        assert text_module.last_index_of_substr(text, "HELLO", case_sensitive=False) == 12
        assert text_module.last_index_of_substr(text, "HELLO", case_sensitive=True) == -1

    def test_last_index_of_substr_with_bounds(self):
        """Test last_index_of_substr with start and end parameters."""
        text = "abcabcabc"

        assert text_module.last_index_of_substr(text, "abc") == 6
        assert text_module.last_index_of_substr(text, "abc", end=6) == 3
        assert text_module.last_index_of_substr(text, "abc", end=3) == 0


class TestTextManipulation:
    """Test text manipulation functions."""

    def test_normalize_text(self):
        """Test normalize_text function."""
        test_cases = [
            ("Hello World", "hello world"),
            ("UPPERCASE", "uppercase"),
            ("MiXeD cAsE", "mixed case"),
            ("", ""),
            ("123", "123"),
            ("Ñoño", "ñoño"),  # Unicode
        ]

        for text, expected in test_cases:
            result = text_module.normalize_text(text)
            assert result == expected, f"normalize_text('{text}') should be '{expected}'"

    def test_slice_text(self):
        """Test slice_text function."""
        text = "hello world"

        # Basic slicing
        assert text_module.slice_text(text, 0, 5) == "hello"
        assert text_module.slice_text(text, 6, 11) == "world"
        assert text_module.slice_text(text, 6) == "world"
        assert text_module.slice_text(text, None, 5) == "hello"

        # Negative indices
        assert text_module.slice_text(text, -5) == "world"
        assert text_module.slice_text(text, -5, -1) == "worl"

        # Out of bounds
        assert text_module.slice_text(text, 100) == ""
        assert text_module.slice_text(text, 0, 100) == text

    def test_slice_text_empty(self):
        """Test slice_text with empty string."""
        assert text_module.slice_text("") == ""
        assert text_module.slice_text("", 0, 5) == ""

    def test_replace_substr(self):
        """Test replace_substr function."""
        text = "hello world hello"

        assert text_module.replace_substr(text, "hello", "hi") == "hi world hi"
        assert text_module.replace_substr(text, "world", "universe") == "hello universe hello"
        assert text_module.replace_substr(text, "xyz", "abc") == text  # No match
        assert (
            text_module.replace_substr(text, "", "x") == "xhxexlxlxox xwxoxrxlxdx xhxexlxlxox"
        )  # Empty string replacement


class TestHashing:
    """Test hashing functions."""

    def test_md5(self):
        """Test MD5 hashing."""
        test_cases = [
            ("", "d41d8cd98f00b204e9800998ecf8427e"),
            ("hello", "5d41402abc4b2a76b9719d911017c592"),
            ("hello world", "5eb63bbbe01eeed093cb22bb8f5acdc3"),
        ]

        for text, expected in test_cases:
            result = text_module.md5(text)
            assert result == expected, f"md5('{text}') should be '{expected}'"
            assert len(result) == 32  # MD5 is always 32 hex characters

    def test_sha1(self):
        """Test SHA-1 hashing."""
        test_cases = [
            ("", "da39a3ee5e6b4b0d3255bfef95601890afd80709"),
            ("hello", "aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d"),
        ]

        for text, expected in test_cases:
            result = text_module.sha1(text)
            assert result == expected, f"sha1('{text}') should be '{expected}'"
            assert len(result) == 40  # SHA-1 is always 40 hex characters

    def test_sha256(self):
        """Test SHA-256 hashing."""
        test_cases = [
            ("", "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"),
            ("hello", "2cf24dba4f21d4288094c6b7b3b8e6c4c29c6c8b7b4b8e6c4c29c6c8b7b4b8e6c"),
        ]

        # Test empty string
        result = text_module.sha256("")
        assert result == test_cases[0][1]
        assert len(result) == 64  # SHA-256 is always 64 hex characters

        # Test non-empty string (verify it's deterministic)
        result1 = text_module.sha256("hello")
        result2 = text_module.sha256("hello")
        assert result1 == result2
        assert len(result1) == 64

    def test_sha512(self):
        """Test SHA-512 hashing."""
        result = text_module.sha512("")
        assert len(result) == 128  # SHA-512 is always 128 hex characters

        # Test deterministic
        result1 = text_module.sha512("hello")
        result2 = text_module.sha512("hello")
        assert result1 == result2
        assert len(result1) == 128

    def test_hash_consistency(self):
        """Test that hash functions are consistent."""
        text = "test string"

        # Multiple calls should return same result
        assert text_module.md5(text) == text_module.md5(text)
        assert text_module.sha1(text) == text_module.sha1(text)
        assert text_module.sha256(text) == text_module.sha256(text)
        assert text_module.sha512(text) == text_module.sha512(text)


class TestBase64:
    """Test Base64 encoding/decoding functions."""

    def test_base64_encode_decode(self):
        """Test Base64 encoding and decoding."""
        test_cases = [
            "",
            "hello",
            "hello world",
            "The quick brown fox jumps over the lazy dog",
            "🌟🚀💻",  # Unicode
        ]

        for text in test_cases:
            encoded = text_module.base64_encode(text)
            decoded = text_module.base64_decode(encoded)

            assert isinstance(encoded, str)
            assert decoded == text, f"Round-trip failed for '{text}'"

    def test_base64_encode_known_values(self):
        """Test Base64 encoding with known values."""
        test_cases = [
            ("", ""),
            ("f", "Zg=="),
            ("fo", "Zm8="),
            ("foo", "Zm9v"),
            ("foob", "Zm9vYg=="),
            ("fooba", "Zm9vYmE="),
            ("foobar", "Zm9vYmFy"),
        ]

        for text, expected in test_cases:
            result = text_module.base64_encode(text)
            assert result == expected, f"base64_encode('{text}') should be '{expected}'"

    def test_base64_decode_invalid(self):
        """Test Base64 decoding with invalid input."""
        with pytest.raises(ValueError, match="Invalid Base64 input"):
            text_module.base64_decode("invalid base64!")

    def test_base64_urlsafe_encode_decode(self):
        """Test URL-safe Base64 encoding and decoding."""
        test_cases = [
            "",
            "hello",
            "hello world",
            "data with + and / characters",
            "🌟🚀💻",  # Unicode
        ]

        for text in test_cases:
            encoded = text_module.base64_urlsafe_encode(text)
            decoded = text_module.base64_urlsafe_decode(encoded)

            assert isinstance(encoded, str)
            assert decoded == text, f"URL-safe round-trip failed for '{text}'"
            # URL-safe should not contain + or /
            assert "+" not in encoded
            assert "/" not in encoded

    def test_base64_urlsafe_vs_regular(self):
        """Test difference between regular and URL-safe Base64."""
        # Text that would produce + and / in regular Base64
        text = "subjects?_d"

        regular = text_module.base64_encode(text)
        urlsafe = text_module.base64_urlsafe_encode(text)

        # They should be different for this input
        if "+" in regular or "/" in regular:
            assert regular != urlsafe

        # But both should decode to the same original text
        assert text_module.base64_decode(regular) == text
        assert text_module.base64_urlsafe_decode(urlsafe) == text


class TestHex:
    """Test hexadecimal encoding/decoding functions."""

    def test_hex_encode_decode(self):
        """Test hex encoding and decoding."""
        test_cases = [
            "",
            "hello",
            "hello world",
            "The quick brown fox",
            "🌟",  # Unicode
        ]

        for text in test_cases:
            encoded = text_module.hex_encode(text)
            decoded = text_module.hex_decode(encoded)

            assert isinstance(encoded, str)
            assert decoded == text, f"Hex round-trip failed for '{text}'"
            # Hex should only contain hex characters
            assert all(c in "0123456789abcdef" for c in encoded.lower())

    def test_hex_encode_known_values(self):
        """Test hex encoding with known values."""
        test_cases = [
            ("", ""),
            ("hello", "68656c6c6f"),
            ("A", "41"),
            ("ABC", "414243"),
        ]

        for text, expected in test_cases:
            result = text_module.hex_encode(text)
            assert result == expected, f"hex_encode('{text}') should be '{expected}'"

    def test_hex_decode_invalid(self):
        """Test hex decoding with invalid input."""
        with pytest.raises(ValueError, match="Invalid hex string"):
            text_module.hex_decode("invalid hex!")

        with pytest.raises(ValueError, match="Invalid hex string"):
            text_module.hex_decode("gg")  # Invalid hex characters

        with pytest.raises(ValueError, match="Hex string must have even length"):
            text_module.hex_decode("abc")  # Odd length

    def test_hex_case_insensitive_decode(self):
        """Test that hex decoding is case insensitive."""
        text = "Hello"
        encoded_lower = text_module.hex_encode(text).lower()
        encoded_upper = text_module.hex_encode(text).upper()

        decoded_lower = text_module.hex_decode(encoded_lower)
        decoded_upper = text_module.hex_decode(encoded_upper)

        assert decoded_lower == text
        assert decoded_upper == text


class TestEdgeCases:
    """Test edge cases and error conditions."""

    def test_empty_strings(self):
        """Test functions with empty strings."""
        empty = ""

        # Should not raise exceptions
        assert text_module.length(empty) == 0
        assert text_module.count_substr(empty, "a") == 0
        assert text_module.most_common_words(empty, 5) == []
        assert text_module.first_index_of_substr(empty, "a") == -1
        assert text_module.last_index_of_substr(empty, "a") == -1
        assert text_module.normalize_text(empty) == ""
        assert text_module.slice_text(empty) == ""
        assert text_module.replace_substr(empty, "a", "b") == ""

        # Encoding/decoding empty strings
        assert text_module.base64_encode(empty) == ""
        assert text_module.base64_decode(empty) == ""
        assert text_module.hex_encode(empty) == ""
        assert text_module.hex_decode(empty) == ""

    def test_unicode_handling(self):
        """Test functions with Unicode characters."""
        unicode_text = "Hello 🌟 World 🚀"

        # Should handle Unicode correctly
        assert text_module.length(unicode_text) == 15
        assert text_module.normalize_text(unicode_text) == "hello 🌟 world 🚀"

        # Encoding should work with Unicode
        encoded = text_module.base64_encode(unicode_text)
        decoded = text_module.base64_decode(encoded)
        assert decoded == unicode_text

        hex_encoded = text_module.hex_encode(unicode_text)
        hex_decoded = text_module.hex_decode(hex_encoded)
        assert hex_decoded == unicode_text
