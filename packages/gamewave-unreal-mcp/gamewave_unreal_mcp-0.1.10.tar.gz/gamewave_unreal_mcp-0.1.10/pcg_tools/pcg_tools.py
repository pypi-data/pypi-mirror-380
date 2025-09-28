"""
PCGt Node Tools for Unreal MCP.

This module provides tools for manipulating PCG graph nodes and connections.
"""

import logging
from typing import Dict, List, Any
from mcp.server.fastmcp import FastMCP, Context
from utils.unreal_connection_utils import send_unreal_command
import os
#from utils.file_downloader import download_file
import objaverse
import objaverse.xl as oxl
import multiprocessing
import uuid
import json


# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def register_pcg_tools(mcp: FastMCP):
    """Register pcg tools with the MCP server."""

    @mcp.tool()
    def post_pcg_tool(
        ctx: Context,
        file_name: str,
        graph: Dict[str, Any] = {}
    ) -> Dict[str, Any]:
        """
        Create a PCG graph from JSON.
        Args:
            file_name: The name of the file to be created.
            graph: The graph structure which will be created as a PCGGraph.
            
        Returns:
            The file path of the created asset. If there is an error, an exception will be raised.
        """
        output = send_unreal_command("get_friday_workspace_path", {})
        workspace_path = ''
        if 'status' in output and output['status'] == 'success':
            result = output['result']
            if 'success' in result and result['success']:
                workspace_path = result['result']
        else:
            raise Exception("Failed to fetch Workspace Path")
        
        json_path = f"{workspace_path}/pcg_json_{str(uuid.uuid4())[:8]}.json"

        try:
            with open(json_path, 'w') as json_file:
                json.dump(graph, json_file, indent=2)
        except IOError as e:
            raise Exception(f'Error writing to file: {e}')

        params = {
            "file_name": file_name,
            "abs_json_path": json_path
        }

        result = send_unreal_command("post_pcg_graph_from_json", params)

        # Delete the temp file
        os.remove(json_path)

        return result

    @mcp.tool()
    def get_pcg_tool(
        ctx: Context,
        name_path: str
    ) -> Dict[str, Any]:
        """
        Get pcg graph in json format.

        Args:
            name_path: Path to the file that needs ot be created. The path is in unreal's Content folder and must start with "/Game/"
            
        Returns:
            graph: name_path that was created. If there is an error then name_path will not be returned.
        """

        params = {
            "name_path": name_path
        }

        result = send_unreal_command("get_pcg_graph_json", params)

        json_path = ''
        if 'status' in result and result['status'] == 'success':
            result = result['result']
            if 'success' in result and result['success'] == True:
                json_path = result['result']
        else:
            raise Exception("Failed to fetch Json Path")
        
        try:
            with open(json_path, 'r') as json_file:
                graph_json = json.load(json_file)
        except IOError as e:
            raise Exception(f'Error reading json from file: {e}')

        os.remove(json_path)

        return graph_json


    