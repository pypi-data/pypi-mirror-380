"""
Daemon service for command management and execution.

This module provides a background daemon service that can store, manage, and execute
commands written in various programming languages (Python, Node.js, Lua, Shell).
Commands are stored in a SQLite database with embeddings for similarity search and
hierarchical grouping.
"""

from .commands import Command, CommandDatabase, CommandExecutor, DaemonService, daemon

# Export main components
__all__ = ["Command", "CommandDatabase", "CommandExecutor", "DaemonService", "daemon"]
