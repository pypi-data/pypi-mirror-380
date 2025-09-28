import anyio

import minimcp_servers.modules.math.arithmetic as arithmetic
from minimcp_servers.core.builder import mcp_from_module, stdio_server
from minimcp_servers.core.logger import configure_logging

configure_logging()


def main():
    mcp = mcp_from_module(
        "arithmetic-math-utils",
        "1.0.0",
        """
        Arithmetic Math Utils - Tools for fundamental mathematical operations.

        It includes:
        - Basic arithmetic operations (add, subtract, multiply, divide, modulo)
        - Power and root functions (pow, sqrt)
        - Rounding and truncation (round, ceil, floor, trunc)
        - Array operations (minimum, maximum, sum, product)
        - Utility functions (absolute, sign, clamp)
        - Floating-point operations (copysign, frexp, ldexp, modf)

        Use this server to perform mathematical calculations and numerical operations
        in your applications. All functions handle floating-point numbers and return
        appropriate numeric types.
        """,
        [arithmetic],
    )

    anyio.run(stdio_server(mcp))


if __name__ == "__main__":
    main()
