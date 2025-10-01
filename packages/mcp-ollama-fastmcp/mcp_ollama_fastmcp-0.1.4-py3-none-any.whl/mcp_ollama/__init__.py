"""MCP server for Ollama integration."""

__version__ = "0.1.0"

from .server import mcp, run_server

__all__ = ["mcp", "run_server"]