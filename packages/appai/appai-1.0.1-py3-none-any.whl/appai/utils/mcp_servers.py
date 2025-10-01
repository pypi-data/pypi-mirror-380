"""
MCP Server Utilities.

Factory functions for creating Model Context Protocol servers.
Simplified and adapted from old aiapp implementation.
"""

import logging
from typing import Optional, Union
from pathlib import Path

logger = logging.getLogger(__name__)


def create_filesystem_server(
    root_path: Optional[Union[str, Path]] = None,
    name: str = "Filesystem_Server"
):
    """
    Create filesystem MCP server for file operations.

    Args:
        root_path: Root directory for file operations (defaults to current directory)
        name: Server name for agent access

    Returns:
        Configured MCPServerStdio instance

    Example:
        >>> server = create_filesystem_server(Path("./project"))
        >>> # Agent can now use filesystem operations
    """
    try:
        from agents.mcp import MCPServerStdio, MCPServerStdioParams
    except ImportError:
        logger.error("❌ Failed to import MCP dependencies")
        raise RuntimeError("MCP support missing - install agents package")

    # Convert string to Path if needed
    if root_path and isinstance(root_path, str):
        root_path = Path(root_path)

    # Ensure root path exists
    if root_path and not root_path.exists():
        logger.warning(f"Root path does not exist, creating: {root_path}")
        root_path.mkdir(parents=True, exist_ok=True)

    # Create server parameters
    root_str = str(root_path) if root_path else "."
    server_params = MCPServerStdioParams(
        command="npx",
        args=["-y", "@modelcontextprotocol/server-filesystem", root_str]
    )

    # Create server
    server = MCPServerStdio(
        server_params,
        cache_tools_list=True,
        name=name
    )

    logger.info(f"✅ Created filesystem server: {name} (root: {root_str})")
    return server


def create_readonly_filesystem_server(
    root_path: Path,
    name: str = "ReadOnly_Filesystem"
):
    """
    Create read-only filesystem server for safe file access.

    Note: MCP filesystem server doesn't have built-in read-only mode,
    so this is functionally the same as create_filesystem_server.
    The name indicates intended usage pattern.

    Args:
        root_path: Root directory for read operations
        name: Server name

    Returns:
        MCPServerStdio instance
    """
    if not root_path.exists():
        raise ValueError(f"Read-only path must exist: {root_path}")

    return create_filesystem_server(root_path=root_path, name=name)
