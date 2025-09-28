import anyio

import minimcp_servers.modules.text as text
from minimcp_servers.core.builder import mcp_from_module, stdio_server
from minimcp_servers.core.logger import configure_logging

configure_logging()


def main():
    mcp = mcp_from_module(
        "text-utils",
        "1.0.0",
        """
        Text Utils - Comprehensive text analysis, manipulation, and encoding utilities.

        It includes:

        **Text Analysis & Search:**
        - String metrics (length, character counting)
        - Substring operations (count_substr, first_index_of_substr, last_index_of_substr)
        - Text analysis (most_common_words with frequency counts)
        - Case-sensitive and case-insensitive search options

        **Text Manipulation:**
        - Text normalization (normalize_text for consistent formatting)
        - String slicing and extraction (slice_text)
        - Find and replace operations (replace_substr)

        **Encoding & Hashing:**
        - Cryptographic hashing (md5, sha1, sha256, sha512)
        - Base64 encoding/decoding (standard and URL-safe variants)
        - Hexadecimal encoding/decoding

        Use this server for:
        - Document analysis and text mining applications
        - Content management and search functionality
        - Data validation and integrity checking
        - API token and identifier processing
        - Log file analysis and text parsing
        - Content normalization and cleanup
        - Security applications requiring text hashing
        - Data serialization and transmission encoding

        All functions handle UTF-8 encoded strings and provide text processing
        capabilities for modern applications requiring text analysis, manipulation,
        and secure data handling.
        """,
        [text],
    )

    anyio.run(stdio_server(mcp))


if __name__ == "__main__":
    main()
