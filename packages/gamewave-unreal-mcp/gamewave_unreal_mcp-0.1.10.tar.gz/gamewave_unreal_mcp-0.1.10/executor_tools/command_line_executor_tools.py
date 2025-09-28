"""
Command line Executor Tools - Run commands in unreal engine.
"""

import os
import re
import logging
from typing import Dict, Any, List
from mcp.server.fastmcp import FastMCP, Context
from utils.executor.command_line_operations import (
    execute_command_line as execute_command_line_impl,
    get_output_log_filepath as get_output_log_filepath_impl
)
from utils.executor.python_executor_operations import (
    execute_python_code as execute_python_code_impl
)

# Get logger
logger = logging.getLogger("UnrealMCP")

def register_command_line_executor_tools(mcp: FastMCP):
    """Register command line executor tools with the MCP server."""

    @mcp.tool()
    def execute_command_line(
        ctx: Context,
        command: str
    ) -> Dict[str, Any]:
        """
        Execute command line operation in unreal engine.
        
        This tool uses Unreal's console to execute command line operations.

        Args:
            command: command to be executed in unreale engine console.
        
        Returns:
            Dict containing:
                - success: Boolean indicating if the command was executed. The executed code may have run succesfully or unsuccesfully.
                - result: Result of the command execution.
        
        Examples:
            # Command to take a high resolution screenshot of the current viewport with multiplier 1 in Unreal Engine.
            execute_command_line(command="HighResShot 1")
        """
        return execute_command_line_impl(ctx, command)

    @mcp.tool()
    def get_output_logs(
        ctx: Context,
        last_n: int = 50
    ) -> List[str]:
        """
        Get output logs unreal engine. 

        Args:
            last_n: Number of lines from the bottom of the log file to read. Value greater than max and less than 100. Default is 50.

        Returns:
            Dict containing:
                - success: Boolean if the log file path exists.
                - result: Result is the last n logs.
        
        Examples:
            # Get Output last 50 output logs in unreal engine.
            get_output_logs()

            # Get Output last 10 output logs in unreal engine.
            get_output_logs(last_n=10)
        """

        if last_n > 100:
            raise ValueError('Last N must be less than 100')
        elif last_n < 1:
            raise ValueError('Last N must be greater than zero')
    
        output = get_output_log_filepath_impl(ctx)
        output_log_filepath = ''
        if 'status' in output and output['status'] == 'success':
            result = output['result']
            if 'success' in result and result['success'] == True:
                output_log_filepath = result['result']

        if output_log_filepath == '':
            raise Exception(f'Output log filepath not found, got response: {output}')

        if (not os.path.exists(output_log_filepath)):
            raise Exception("No log file path found, output: ", output)
        
        
        try:
            with open(output_log_filepath, 'r') as file:
                lines = file.readlines()
                return lines[-last_n:]  # Return the last n elements of the list
        except FileNotFoundError:
            raise Exception("No log file path found, output: ", output)
        except Exception as e:
            raise Exception("An error occurred: ", output)
