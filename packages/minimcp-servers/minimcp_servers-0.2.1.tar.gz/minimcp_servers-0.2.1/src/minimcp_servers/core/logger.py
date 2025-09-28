import logging
import os
import sys

# Track if logging has been configured to prevent duplicate configurations
_logging_configured = False


def configure_logging() -> None:
    """Configure logging globally for stdio MCP server."""
    global _logging_configured

    # Prevent multiple configurations
    if _logging_configured:
        return

    handlers = [
        logging.StreamHandler(stream=sys.stderr),  # Log to stderr
    ]

    # Add file handler if specified
    log_file = os.environ.get("MCP_SERVER_LOG_FILE", None)
    if log_file:
        handlers.append(logging.FileHandler(log_file))

    # Validate and set log level
    log_level = os.environ.get("MCP_SERVER_LOG_LEVEL", "WARNING").upper()
    valid_levels = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
    if log_level not in valid_levels:
        print("Warning: Invalid log level '%s'. Using 'WARNING' instead.", log_level, file=sys.stderr)
        log_level = "WARNING"

    logging.basicConfig(
        level=log_level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=handlers,
    )

    _logging_configured = True
