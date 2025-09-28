import anyio

from minimcp_servers.core.builder import mcp_from_module, stdio_server
from minimcp_servers.core.logger import configure_logging
from minimcp_servers.modules.math import arithmetic, continuous, discrete, stats

configure_logging()


def main():
    mcp = mcp_from_module(
        "math-utils",
        "1.0.0",
        """
        Math Utils - Offers a complete suite of mathematical tools across various mathematical domains.

        It includes:
        **Basic Arithmetic & Operations:**
        - Fundamental arithmetic (add, subtract, multiply, divide, modulo, floor_divide)
        - Power and root functions (pow, sqrt, isqrt)
        - Rounding and truncation (round, ceil, floor, trunc, absolute)
        - Array operations (minimum, maximum, sum, product)
        - Utility functions (sign, clamp, copysign, frexp, ldexp, modf)

        **Continuous Mathematics:**
        - Trigonometric functions (sin, cos, tan, asin, acos, atan, atan2)
        - Hyperbolic functions (sinh, cosh, tanh, asinh, acosh, atanh)
        - Exponential and logarithmic functions (exp, expm1, log, log10, log2, log1p)
        - Angle conversion (degrees, radians)
        - Distance and geometry (hypot, multidimensional_hypot, dist)
        - Special functions (gamma, lgamma, erf, erfc)

        **Discrete Mathematics:**
        - Number theory (factorial, gcd, lcm)
        - Combinatorics (combination, permutation)
        - Integer-specific operations (isqrt)

        **Statistical Analysis:**
        - Central tendency (mean, geometric_mean, harmonic_mean, median variants, mode, multimode)
        - Dispersion measures (variance, pvariance, stdev, pstdev)
        - Distribution analysis (quantiles, median_grouped)
        - Bivariate analysis (covariance, correlation, linear_regression)

        Use this server for comprehensive mathematical problem-solving across:
        - Scientific computing and research applications
        - Engineering calculations and simulations
        - Data analysis and statistical modeling
        - Financial modeling and risk analysis
        - Machine learning and AI applications
        - Educational and academic computations
        - Algorithm development and optimization
        """,
        [arithmetic, continuous, discrete, stats],
    )

    anyio.run(stdio_server(mcp))


if __name__ == "__main__":
    main()
