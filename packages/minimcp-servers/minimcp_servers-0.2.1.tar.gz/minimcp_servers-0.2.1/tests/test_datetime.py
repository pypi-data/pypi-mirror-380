"""Tests for minimcp_servers.modules.datetime module."""

import datetime
import time

import pytest

from minimcp_servers.modules import datetime as dt_module


class TestCurrentTime:
    """Test current time functions."""

    def test_epoch_seconds_now(self):
        """Test epoch_seconds_now returns current epoch time."""
        before = int(time.time())
        result = dt_module.epoch_seconds_now()
        after = int(time.time())

        assert isinstance(result, int)
        assert before <= result <= after

    def test_iso_utc_now(self):
        """Test iso_utc_now returns valid ISO format."""
        result = dt_module.iso_utc_now()

        assert isinstance(result, str)
        assert dt_module.is_valid_iso_format(result)
        # Should contain timezone info
        assert result.endswith("+00:00") or result.endswith("Z")


class TestTimeFormatConversion:
    """Test time format conversion functions."""

    def test_epoch_to_iso_utc(self):
        """Test epoch to ISO UTC conversion."""
        epoch = 1609459200  # 2021-01-01 00:00:00 UTC
        result = dt_module.epoch_to_iso_utc(epoch)

        assert isinstance(result, str)
        assert result.startswith("2021-01-01T00:00:00+00:00")

    def test_iso_utc_to_epoch(self):
        """Test ISO UTC to epoch conversion."""
        iso_str = "2021-01-01T00:00:00+00:00"
        result = dt_module.iso_utc_to_epoch(iso_str)

        assert isinstance(result, int)
        assert result == 1609459200

    def test_iso_utc_to_epoch_with_z_suffix(self):
        """Test ISO UTC to epoch conversion with Z suffix."""
        iso_str = "2021-01-01T00:00:00Z"
        result = dt_module.iso_utc_to_epoch(iso_str)

        assert isinstance(result, int)
        assert result == 1609459200

    def test_iso_utc_to_epoch_invalid_format(self):
        """Test ISO UTC to epoch with invalid format raises ValueError."""
        with pytest.raises(ValueError, match="Invalid ISO format"):
            dt_module.iso_utc_to_epoch("invalid-date")

    def test_is_valid_iso_format_valid(self):
        """Test is_valid_iso_format with valid formats."""
        valid_formats = [
            "2021-01-01T00:00:00+00:00",
            "2021-01-01T00:00:00Z",
            "2021-12-31T23:59:59.999999+00:00",
            "2021-06-15T12:30:45-05:00",
        ]

        for iso_str in valid_formats:
            assert dt_module.is_valid_iso_format(iso_str), f"Should be valid: {iso_str}"

    def test_is_valid_iso_format_invalid(self):
        """Test is_valid_iso_format with invalid formats."""
        invalid_formats = [
            "invalid-date",
            "2021-13-01T00:00:00+00:00",  # Invalid month
            "2021-01-32T00:00:00+00:00",  # Invalid day
            "2021-01-01T25:00:00+00:00",  # Invalid hour
        ]

        for iso_str in invalid_formats:
            assert not dt_module.is_valid_iso_format(iso_str), f"Should be invalid: {iso_str}"

        # Test None and non-string types - should return False now
        assert not dt_module.is_valid_iso_format(None), "None should be invalid"  # type: ignore
        assert not dt_module.is_valid_iso_format(123), "Integer should be invalid"  # type: ignore


class TestDurationCalculations:
    """Test duration calculation functions."""

    def test_duration_seconds_basic(self):
        """Test basic duration_seconds calculation."""
        result = dt_module.duration_seconds(days=1, hours=2, minutes=30, seconds=45)
        expected = 1 * 86400 + 2 * 3600 + 30 * 60 + 45  # 95445
        assert result == expected

    def test_duration_seconds_weeks(self):
        """Test duration_seconds with weeks."""
        result = dt_module.duration_seconds(weeks=2)
        expected = 2 * 7 * 86400  # 1209600
        assert result == expected

    def test_duration_seconds_negative(self):
        """Test duration_seconds with negative values."""
        result = dt_module.duration_seconds(days=-1, hours=-2)
        expected = -1 * 86400 - 2 * 3600  # -93600
        assert result == expected

    def test_duration_seconds_zero(self):
        """Test duration_seconds with no arguments."""
        result = dt_module.duration_seconds()
        assert result == 0

    def test_format_duration_positive(self):
        """Test format_duration with positive seconds."""
        test_cases = [
            (0, "0s"),
            (45, "45s"),
            (90, "1m 30s"),
            (3661, "1h 1m 1s"),
            (90061, "1d 1h 1m 1s"),
            (86400, "1d"),
            (3600, "1h"),
            (60, "1m"),
        ]

        for seconds, expected in test_cases:
            result = dt_module.format_duration(seconds)
            assert result == expected, f"format_duration({seconds}) should be '{expected}', got '{result}'"

    def test_format_duration_negative(self):
        """Test format_duration with negative seconds."""
        result = dt_module.format_duration(-3661)
        assert result == "-1h 1m 1s"

    def test_format_duration_large(self):
        """Test format_duration with large values."""
        result = dt_module.format_duration(90061)  # 1 day, 1 hour, 1 minute, 1 second
        assert result == "1d 1h 1m 1s"


class TestCalendarUtilities:
    """Test calendar utility functions."""

    def test_isleap_leap_years(self):
        """Test isleap with leap years."""
        leap_years = [2000, 2004, 2008, 2012, 2016, 2020, 2024]
        for year in leap_years:
            assert dt_module.isleap(year), f"{year} should be a leap year"

    def test_isleap_non_leap_years(self):
        """Test isleap with non-leap years."""
        non_leap_years = [1900, 2001, 2002, 2003, 2005, 2100, 2200, 2300]
        for year in non_leap_years:
            assert not dt_module.isleap(year), f"{year} should not be a leap year"

    def test_days_in_month_regular_months(self):
        """Test days_in_month for regular months."""
        test_cases = [
            (2021, 1, 31),  # January
            (2021, 3, 31),  # March
            (2021, 4, 30),  # April
            (2021, 5, 31),  # May
            (2021, 6, 30),  # June
            (2021, 7, 31),  # July
            (2021, 8, 31),  # August
            (2021, 9, 30),  # September
            (2021, 10, 31),  # October
            (2021, 11, 30),  # November
            (2021, 12, 31),  # December
        ]

        for year, month, expected in test_cases:
            result = dt_module.days_in_month(year, month)
            assert result == expected, f"days_in_month({year}, {month}) should be {expected}"

    def test_days_in_month_february(self):
        """Test days_in_month for February in leap and non-leap years."""
        # Non-leap year
        assert dt_module.days_in_month(2021, 2) == 28
        # Leap year
        assert dt_module.days_in_month(2020, 2) == 29


class TestRoundTripConversions:
    """Test round-trip conversions between formats."""

    def test_epoch_iso_round_trip(self):
        """Test epoch -> ISO -> epoch conversion."""
        original_epoch = 1609459200
        iso_str = dt_module.epoch_to_iso_utc(original_epoch)
        converted_epoch = dt_module.iso_utc_to_epoch(iso_str)

        assert converted_epoch == original_epoch

    def test_iso_epoch_round_trip(self):
        """Test ISO -> epoch -> ISO conversion."""
        original_iso = "2021-01-01T00:00:00+00:00"
        epoch = dt_module.iso_utc_to_epoch(original_iso)
        converted_iso = dt_module.epoch_to_iso_utc(epoch)

        # Convert both to datetime objects for comparison (to handle timezone format differences)
        original_dt = datetime.datetime.fromisoformat(original_iso)
        converted_dt = datetime.datetime.fromisoformat(converted_iso)

        assert original_dt == converted_dt
