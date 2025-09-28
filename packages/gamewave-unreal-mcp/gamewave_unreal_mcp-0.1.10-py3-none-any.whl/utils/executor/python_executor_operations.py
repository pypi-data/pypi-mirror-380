"""
Python Executor Operations for Unreal MCP.

This module provides utility functions for executing python code in unreal engine.
"""

import logging
import json
from typing import Dict, Any, List
from mcp.server.fastmcp import Context
from utils.unreal_connection_utils import send_unreal_command

# Get logger
logger = logging.getLogger("UnrealMCP")

def execute_python_code(
    ctx: Context,
    code: str
) -> Dict[str, Any]:
    """Implementation for executing python code in unreal engine."""
    params = {
        "code": code
    }
    return send_unreal_command("execute_python_code", params)
