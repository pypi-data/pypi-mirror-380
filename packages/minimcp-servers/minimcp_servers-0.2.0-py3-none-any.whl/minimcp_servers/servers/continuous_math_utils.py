import anyio

import minimcp_servers.modules.math.continuous as continuous
from minimcp_servers.core.builder import mcp_from_module, stdio_server
from minimcp_servers.core.logger import configure_logging

configure_logging()


def main():
    mcp = mcp_from_module(
        "continuous-math-utils",
        "1.0.0",
        """
        Continuous Math Utils - Tools for continuous mathematics calculations.

        It includes:
        - Trigonometric functions (sin, cos, tan, asin, acos, atan, atan2)
        - Hyperbolic functions (sinh, cosh, tanh, asinh, acosh, atanh)
        - Exponential and logarithmic functions (exp, expm1, log, log10, log2, log1p)
        - Angle conversion utilities (degrees, radians)
        - Distance and geometric functions (hypot, multidimensional_hypot, dist)
        - Special mathematical functions (gamma, lgamma, erf, erfc)

        Use this server for advanced mathematical computations involving calculus,
        trigonometry, statistics, physics simulations, signal processing, and other
        scientific applications requiring continuous mathematical functions.

        All functions operate on floating-point numbers and handle standard mathematical
        domains and ranges.
        """,
        [continuous],
    )

    anyio.run(stdio_server(mcp))


if __name__ == "__main__":
    main()
