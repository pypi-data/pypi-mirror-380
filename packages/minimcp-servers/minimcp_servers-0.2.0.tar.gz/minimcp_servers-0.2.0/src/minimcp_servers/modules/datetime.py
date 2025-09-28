import calendar
import datetime
import time

# Intentionally avoiding local time functions as the MCP server
# need not be running on the same machine as the client.

# === Current Time ===


def epoch_seconds_now() -> int:
    """Return the current epoch seconds."""
    return int(time.time())


def iso_utc_now() -> str:
    """Return the current ISO 8601 UTC string."""
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


# === Time Format Conversion ===


def epoch_to_iso_utc(epoch_seconds: int) -> str:
    """Return the ISO 8601 UTC string for the given epoch seconds."""
    return datetime.datetime.fromtimestamp(epoch_seconds, datetime.timezone.utc).isoformat()


def iso_utc_to_epoch(iso_utc: str) -> int:
    """Return the epoch seconds for the given ISO 8601 UTC string."""
    # Handle 'Z' suffix for UTC
    if iso_utc.endswith("Z"):
        iso_utc = iso_utc[:-1] + "+00:00"

    try:
        dt = datetime.datetime.fromisoformat(iso_utc)
        return int(dt.timestamp())
    except ValueError as e:
        raise ValueError(f"Invalid ISO format: {iso_utc}") from e


def is_valid_iso_format(iso_str: str) -> bool:
    """Check if a string is a valid ISO 8601 format."""
    if not isinstance(iso_str, str):
        return False
    try:
        datetime.datetime.fromisoformat(iso_str.replace("Z", "+00:00"))
        return True
    except (ValueError, TypeError):
        return False


# === Duration Calculations ===


def duration_seconds(days: int = 0, seconds: int = 0, minutes: int = 0, hours: int = 0, weeks: int = 0) -> int:
    """Return the number of seconds in the given duration.

    Args:
        days: Number of days (default: 0)
        seconds: Number of seconds (default: 0)
        minutes: Number of minutes (default: 0)
        hours: Number of hours (default: 0)
        weeks: Number of weeks (default: 0)

    Returns:
        Total duration in seconds as integer. Can be negative.
    """
    return int(
        datetime.timedelta(days=days, seconds=seconds, minutes=minutes, hours=hours, weeks=weeks).total_seconds()
    )


def format_duration(seconds: int) -> str:
    """Format seconds into a human-readable duration string.

    Args:
        seconds: Duration in seconds (can be negative)

    Returns:
        Human-readable duration string (e.g., "1d 2h 30m 45s"). Can be negative.
    """
    if seconds < 0:
        return f"-{format_duration(-seconds)}"

    days, remainder = divmod(seconds, 86400)  # 24 * 60 * 60
    hours, remainder = divmod(remainder, 3600)  # 60 * 60
    minutes, seconds = divmod(remainder, 60)

    parts = []
    if days:
        parts.append(f"{days}d")
    if hours:
        parts.append(f"{hours}h")
    if minutes:
        parts.append(f"{minutes}m")
    if seconds or not parts:
        parts.append(f"{seconds}s")

    return " ".join(parts)


# === Calendar Utilities ===


def isleap(year: int) -> bool:
    """Return True if the year is a leap year, False otherwise."""
    return calendar.isleap(year)


def days_in_month(year: int, month: int) -> int:
    """Return the number of days in the given month."""
    return calendar.monthrange(year, month)[1]
