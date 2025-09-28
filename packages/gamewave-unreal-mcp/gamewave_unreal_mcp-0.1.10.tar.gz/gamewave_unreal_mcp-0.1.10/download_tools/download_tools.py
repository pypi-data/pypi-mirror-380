import logging
import json
import os
from typing import Dict, Any, List

from mcp.server.fastmcp import FastMCP, Context
from utils.unreal_connection_utils import send_unreal_command

import objaverse

logger = logging.getLogger("UnrealMCP")

def register_download_tools(mcp: FastMCP):
    """Register download tools with the MCP server."""

    @mcp.tool()
    def download_meshes_tool(
        ctx: Context,
        file_ids: List[str],
        filenames: List[str]
    ) -> Dict[str, Any]:
        """
        Downloads 3D models from Objaverse 1.0, then sends them to Unreal Engine
        for a direct, thread-safe import. This version uses the asset's UID for the
        folder name and expects the full asset name in the input.

        Args:
            file_ids: A list of Objaverse 1.0 unique identifiers (UIDs).
            filenames: A list of desired full asset names (e.g., "SM_Vase").

        Returns:
            The response from the Unreal Engine command execution.
        """
        if len(file_ids) != len(filenames):
            return {"status": "Failure", "message": "The number of file IDs must match the number of filenames."}

        logger.info(f"Downloading {len(file_ids)} assets from Objaverse 1.0 to the local cache...")
        try:
            downloaded_paths = objaverse.load_objects(uids=file_ids, download_processes=8)
        except Exception as e:
            error_msg = f"A critical error occurred while calling objaverse.load_objects. Error: {e}"
            logger.error(error_msg, exc_info=True)
            return {"status": "Failure", "message": error_msg}

        if not downloaded_paths:
            return {"status": "Failure", "message": f"Could not find any objects for the given UIDs: {file_ids}"}

        assets_to_import = []
        for file_id, file_path in downloaded_paths.items():
            try:
                asset_name = filenames[file_ids.index(file_id)]
                clean_path = file_path.replace('\\', '/')
                assets_to_import.append({
                    "asset_name": asset_name,
                    "file_path": clean_path,
                })
                logger.info(f"Located asset '{asset_name}' at: {clean_path}")
            except (ValueError, FileNotFoundError) as e:
                logger.warning(f"Could not process path for downloaded file ID '{file_id}'. Error: {e}. Skipping.")

        if not assets_to_import:
            return {"status": "Failure", "message": "Assets were downloaded but could not be processed."}

        # Prepare the asset data as a JSON string to be sent to Unreal.
        # Note: Escaping backslashes for the JSON string itself is handled by the json.dumps function.
        # The C++ FString will handle its own internal escaping.
        assets_json_string = json.dumps(assets_to_import)

        logger.info("Sending command to Unreal Engine to import and combine assets.")
        
        params = {
            "assets_json": assets_json_string
        }

        # The command now calls the specific C++ handler.
        return send_unreal_command("download_meshes_tool", params)