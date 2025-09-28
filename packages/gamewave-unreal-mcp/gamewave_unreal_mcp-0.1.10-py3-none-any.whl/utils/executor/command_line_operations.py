"""
Command Operations for Unreal MCP.

This module provides utility functions for executing python code in unreal engine.
"""

import logging
import json
from typing import Dict, Any, List
from mcp.server.fastmcp import Context
from utils.unreal_connection_utils import send_unreal_command

# Get logger
logger = logging.getLogger("UnrealMCP")

def execute_command_line(
    ctx: Context,
    command: str
) -> Dict[str, Any]:
    """Implementation for executing command line operations in unreal engine."""
    params = {
        "command": command
    }
    return send_unreal_command("execute_command_line", params)

def get_output_log_filepath(
    ctx: Context
) -> Dict[str, Any]:
    """Implementation for getting output log file path in unreal engine."""
    params = {}
    return send_unreal_command("get_output_log_filepath", params)
