import anyio

import minimcp_servers.modules.math.discrete as discrete
from minimcp_servers.core.builder import mcp_from_module, stdio_server
from minimcp_servers.core.logger import configure_logging

configure_logging()


def main():
    mcp = mcp_from_module(
        "discrete-math-utils",
        "1.0.0",
        """
        Discrete Math Utils - Mathematical tools for discrete mathematics and combinatorics.

        It includes:
        - Integer arithmetic (isqrt - integer square root)
        - Number theory functions (factorial, gcd, lcm)
        - Combinatorial functions (combination, permutation)

        Use this server for discrete mathematics applications including:
        - Combinatorial analysis and counting problems
        - Number theory computations
        - Algorithm design and analysis
        - Probability calculations involving discrete distributions
        - Cryptographic applications requiring integer operations
        - Graph theory and discrete optimization problems

        All functions operate on integers and return integer results, making them
        suitable for exact discrete mathematical computations without floating-point
        precision issues.
        """,
        [discrete],
    )

    anyio.run(stdio_server(mcp))


if __name__ == "__main__":
    main()
