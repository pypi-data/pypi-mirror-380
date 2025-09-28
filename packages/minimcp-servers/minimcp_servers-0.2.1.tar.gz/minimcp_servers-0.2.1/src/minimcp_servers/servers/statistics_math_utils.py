import anyio

import minimcp_servers.modules.math.stats as statistics
from minimcp_servers.core.builder import mcp_from_module, stdio_server
from minimcp_servers.core.logger import configure_logging

configure_logging()


def main():
    mcp = mcp_from_module(
        "statistics-math-utils",
        "1.0.0",
        """
        Statistics Math Utils - Essential statistical functions for data analysis.

        It includes:
        - Measures of central tendency (mean, geometric_mean, harmonic_mean, median variants, mode, multimode)
        - Measures of dispersion (variance, pvariance, stdev, pstdev)
        - Distribution analysis (quantiles, median_grouped for grouped data)
        - Bivariate analysis (covariance, correlation, linear_regression)

        Use this server for statistical analysis applications including:
        - Exploratory data analysis and descriptive statistics
        - Quality control and process monitoring
        - Research and scientific data analysis
        - Financial and business analytics
        - Machine learning preprocessing and feature analysis
        - A/B testing and experimental design analysis

        Key features:
        - Support for both population and sample statistics (pvariance vs variance, pstdev vs stdev)
        - Robust median calculations with multiple variants
        - Weighted harmonic mean calculations
        - Complete bivariate analysis including linear regression slope and intercept
        - Handles multimodal distributions with multimode function

        All functions operate on lists of floating-point numbers and provide
        accurate statistical computations for data-driven decision making.
        """,
        [statistics],
    )

    anyio.run(stdio_server(mcp))


if __name__ == "__main__":
    main()
