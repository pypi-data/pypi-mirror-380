import logging
import json
from typing import Dict, Any, List, Optional

from mcp.server.fastmcp import FastMCP, Context
from utils.unreal_connection_utils import send_unreal_command

logger = logging.getLogger("UnrealMCP")

def register_material_tools(mcp: FastMCP):
    """Register material tools with the MCP server."""

    @mcp.tool()
    def get_material_tool(
        ctx: Context,
        material_path: str
    ) -> Dict[str, Any]:
        """
        Retrieves the entire graph structure and properties of a specified Material asset
        from Unreal Engine and returns it in a structured JSON format.

        Args:
            material_path: The full content browser path to the material asset.
                        Example: "/Game/Materials/M_Brick_Clay_New"
            
        Returns:
            A dictionary containing the detailed graph of the material, including nodes,
            properties, and connections.
        """
        logger.info(f"Getting material information for asset at path: {material_path}")
        
        params = {
            "material_path": material_path
        }
        
        result = send_unreal_command("get_material_tool", params)

        json_path = ''
        if 'status' in result and result['status'] == 'success':
            response_data = result.get('result', {})
            if response_data.get('success'):
                json_path = response_data['result']
            else:
                error_message = response_data.get('result', 'Unknown error from Unreal.')
                raise Exception(f"Failed to get Material JSON: {error_message}")
        else:
            raise Exception("Failed to fetch temporary JSON path from Unreal.")
        
        graph_json = {}
        try:
            with open(json_path, 'r') as json_file:
                graph_json = json.load(json_file)
        except IOError as e:
            raise Exception(f'Error reading temporary JSON file: {e}')
        finally:
            if os.path.exists(json_path):
                os.remove(json_path)

        return graph_json

    @mcp.tool()
    def post_material_tool(
        ctx: Context,
        material_name: str,
        material_data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Creates or overwrites a Material asset in Unreal Engine using a detailed JSON graph structure.

        Args:
            material_name: The name for the new material asset (e.g., "M_CustomBrick").
            material_data: A dictionary representing the entire material graph, including nodes,
                        properties, and connections.
            
        Returns:
            A dictionary containing the status of the operation and the content browser path
            of the saved material asset.
            
        Example:
            material_graph_data = { "MaterialGraph": { "Name": "M_CustomBrick", "Nodes": [...], "Connections": [...] } }
            post_material_tool(material_name="M_CustomBrick", material_data=material_graph_data)
        """
        logger.info(f"Sending request to create/update material: {material_name}")
        
        # Convert the entire material_data dictionary to a JSON string for transmission
        material_json_string = json.dumps(material_data)
        
        params = {
            "material_name": material_name,
            "material_data": material_json_string,
        }
        
        return send_unreal_command("post_material_tool", params)


    @mcp.tool()
    def download_textures_tool(
        ctx: Context,
        texture_urls: List[str],
        texture_names: List[str]
    ) -> Dict[str, Any]:
        """
        Downloads textures from a list of URLs and imports them directly into Unreal Engine.

        Args:
            texture_urls: A list of direct URLs to the texture files (e.g., .png, .jpg).
            texture_names: A corresponding list of asset names for the textures in Unreal
                        (e.g., "T_Brick_Diffuse"). The list must be the same size
                        as texture_urls.
            
        Returns:
            A dictionary containing the import report from Unreal Engine, including a list
            of the final saved asset paths for successful imports.
            
        Example:
            download_textures_tool(
                texture_urls=["https://example.com/brick_d.png", "https://example.com/brick_n.png"],
                texture_names=["T_Brick_Diffuse", "T_Brick_Normal"]
            )
        """
        if len(texture_urls) != len(texture_names):
            return {"status": "Failure", "message": "The number of texture URLs must match the number of texture names."}
        
        logger.info(f"Preparing {len(texture_urls)} textures for download and import into Unreal Engine...")
        
        textures_to_import = []
        for url, name in zip(texture_urls, texture_names):
            textures_to_import.append({
                "url": url,
                "name": name,
            })
        
        textures_json_string = json.dumps(textures_to_import)
        
        params = {
            "textures_json": textures_json_string
        }
        
        return send_unreal_command("download_textures_tool", params)