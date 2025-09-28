import anyio

from minimcp_servers.core.builder import mcp_from_module, stdio_server
from minimcp_servers.core.logger import configure_logging
from minimcp_servers.modules import datetime

configure_logging()


def main():
    mcp = mcp_from_module(
        "datetime-utils",
        "1.0.0",
        """
        DateTime Utils - Comprehensive date, time, and duration utilities for temporal data processing.

        It includes:

        **Current Time Functions:**
        - epoch_seconds_now() - Get current Unix timestamp in seconds
        - iso_utc_now() - Get current UTC time in ISO 8601 format

        **Time Format Conversion:**
        - epoch_to_iso_utc(epoch_seconds) - Convert Unix timestamp to ISO 8601 UTC string
        - iso_utc_to_epoch(iso_utc) - Convert ISO 8601 UTC string to Unix timestamp
        - is_valid_iso_format(iso_string) - Validate ISO 8601 datetime format

        **Duration Calculations:**
        - duration_seconds(days, seconds, minutes, hours, weeks) - Calculate total seconds from time components
        - format_duration(seconds) - Convert seconds to human-readable duration format

        **Calendar Utilities:**
        - isleap(year) - Check if a year is a leap year
        - days_in_month(year, month) - Get number of days in a specific month/year

        Use this server for:
        - Timestamp generation and time tracking applications
        - API integration requiring time format conversions
        - Duration calculations for scheduling and timing systems
        - Data processing with temporal components
        - Log analysis and time-based filtering
        - Calendar applications and date validation
        - Time zone handling and UTC standardization
        - Performance monitoring and elapsed time calculations

        All datetime operations use UTC for consistency and avoid timezone-related
        issues in distributed applications.
        """,
        [datetime],
    )

    anyio.run(stdio_server(mcp))


if __name__ == "__main__":
    main()
