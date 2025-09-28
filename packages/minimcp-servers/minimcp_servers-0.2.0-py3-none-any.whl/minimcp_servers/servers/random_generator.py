import anyio

import minimcp_servers.modules.random_generator as random_generator
from minimcp_servers.core.builder import mcp_from_module, stdio_server
from minimcp_servers.core.logger import configure_logging

configure_logging()


def main():
    mcp = mcp_from_module(
        "random-generator",
        "1.0.0",
        """
        Random Generator - Cryptographically secure random data generation.

        This server provides cryptographically secure random generation functions for:
        - UUID generation (generate_uuid) - Creates RFC 4122 compliant UUID4 strings
        - Secure random numbers (generate_random_number) - Generates integers within specified ranges
        - Random text strings (generate_random_text) - Creates alphanumeric strings of specified length

        Use this server for:
        - Authentication token generation
        - Session ID and API key creation
        - Password and passphrase generation
        - Unique identifier creation for database records
        - Security testing and mock data generation
        - Cryptographic nonce and salt generation
        - Random sampling for security applications

        All generated values are cryptographically secure and suitable for production
        security applications.
        """,
        [random_generator],
    )

    anyio.run(stdio_server(mcp))


if __name__ == "__main__":
    main()
