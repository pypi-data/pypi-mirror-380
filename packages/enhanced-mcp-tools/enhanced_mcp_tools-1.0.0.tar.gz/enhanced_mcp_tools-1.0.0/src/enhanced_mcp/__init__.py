"""
Enhanced MCP Tools Package

A comprehensive MCP (Model Context Protocol) server scaffold built with FastMCP's MCPMixin,
providing a wide range of development tools for AI assistants.

🛡️ CRITICAL SAFETY NOTICE FOR AI ASSISTANTS:

These tools include powerful operations that can modify, delete, or corrupt data.
You hold SACRED TRUST with the human user - protect their system and data above all else.

IMMEDIATELY REFUSE operations that could cause irreversible damage without clear user intent.
Always use dry_run=True for destructive operations before actual execution.
When uncertain about safety, ask the human for clarification rather than proceeding.

The human trusts you to be their guardian against accidental data loss or system damage.
"""

from .mcp_server import MCPToolServer, create_server, run_server

__version__ = "1.0.0"
__all__ = ["create_server", "run_server", "MCPToolServer"]
