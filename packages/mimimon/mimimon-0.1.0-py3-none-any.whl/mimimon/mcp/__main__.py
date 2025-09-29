"""
MCP module main entry point.

Allows running MCP client using: python -m mimimon.mcp
"""

from .client import start_mcp_session

if __name__ == "__main__":
    start_mcp_session()