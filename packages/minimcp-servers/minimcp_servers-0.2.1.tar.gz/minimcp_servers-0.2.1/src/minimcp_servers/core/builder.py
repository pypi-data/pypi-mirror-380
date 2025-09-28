import inspect
import logging
from collections.abc import Awaitable, Callable
from types import ModuleType

from minimcp import MiniMCP, stdio

logger = logging.getLogger(__name__)


def mcp_from_module(name: str, version: str, instructions: str, modules: list[ModuleType]) -> MiniMCP:
    """
    Create a MiniMCP server from a Python module by automatically registering
    all public callable functions as tools.

    Args:
        name: The name of the MCP server
        version: The version of the MCP server
        instructions: The instructions for the MCP server
        module: The Python module to expose as MCP tools

    Returns:
        MiniMCP server instance with all module functions registered as tools
    """

    mcp = MiniMCP(name.strip(), version=version.strip(), instructions=instructions.strip())

    # Get all public callable functions from the module
    functions = []
    for module in modules:
        for attr_name in dir(module):
            # Skip private/dunder methods
            if attr_name.startswith("_"):
                continue

            attr = getattr(module, attr_name)

            # Check if it's a callable function (regular function or builtin function)
            if callable(attr) and (inspect.isfunction(attr) or inspect.isbuiltin(attr)):
                functions.append((attr_name, attr))

        logger.info("Registering %d functions from module '%s' as MCP tools", len(functions), module.__name__)

    # Register each function as a tool
    registered_count = 0
    for func_name, func in functions:
        try:
            mcp.tool.add(func)
            registered_count += 1
            logger.debug("Registered function '%s' as tool", func_name)
        except Exception as e:  # noqa: PERF203
            logger.warning("Failed to register function '%s': %s", func_name, str(e))

    return mcp


def stdio_server(mcp: MiniMCP) -> Callable[[], Awaitable[None]]:
    """
    Create a function that starts a MiniMCP server over stdio.

    Args:
        mcp: The MiniMCP server instance

    Returns:
        A function that starts the MiniMCP server over stdio
    """

    async def stdio_server():
        logger.info("MiniMCP: Started %s server, listening for messages...", mcp.name)
        try:
            await stdio.sequential_transport(mcp.handle)
        except KeyboardInterrupt:
            logger.info("%s server shutting down gracefully...", mcp.name)

    return stdio_server
