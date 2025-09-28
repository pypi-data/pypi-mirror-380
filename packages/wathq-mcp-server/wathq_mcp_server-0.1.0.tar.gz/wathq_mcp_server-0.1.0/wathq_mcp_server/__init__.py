"""
WATHQ MCP Server

MCP server for Saudi company lookup via WATHQ API.
"""

__version__ = "0.1.0"
__author__ = "WATHQ MCP Server"
__description__ = "MCP server for Saudi company lookup via WATHQ API"

from .server import server

__all__ = ["server", "__version__", "__author__", "__description__"]
