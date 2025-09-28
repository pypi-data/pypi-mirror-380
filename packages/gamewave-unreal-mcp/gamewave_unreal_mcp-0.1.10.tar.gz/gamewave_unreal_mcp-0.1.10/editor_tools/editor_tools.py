"""
Editor Tools for Unreal MCP.

This module provides tools for controlling the Unreal Editor viewport and other editor functionality.
"""
import os
import time
import re
import logging
from typing import Dict, List, Any, Optional
from mcp.server.fastmcp import FastMCP, Context, Image
from utils.editor.editor_operations import (
    get_actors_in_level as get_actors_in_level_impl,
    find_actors_by_name as find_actors_by_name_impl,
    spawn_actor as spawn_actor_impl,
    spawn_actor_v2 as spawn_actor_v2_impl,
    delete_actor as delete_actor_impl,
    set_actor_transform as set_actor_transform_impl,
    get_actor_properties as get_actor_properties_impl,
    set_actor_property as set_actor_property_impl,
    set_light_property as set_light_property_impl,
    focus_viewport as focus_viewport_impl,
    spawn_blueprint_actor as spawn_blueprint_actor_impl,
    spline_tool as spline_tool_impl
    

)
from utils.executor.python_executor_operations import (
    execute_python_code as execute_python_code_impl
)

# Get logger
logger = logging.getLogger("UnrealMCP")

def register_editor_tools(mcp: FastMCP):
    """Register editor tools with the MCP server."""
    
    @mcp.tool()
    def spline_tool(
        ctx: Context,
        strokes: List[Dict[str, Any]],
        scale_factor: float = 20.0
    ) -> Dict[str, Any]:
        """
        Creates multiple spline actors in the level based on a list of stroke data.
        This tool is designed to take structured 2D point data and render it as 3D splines in the editor.

        Args:
            strokes: A list of stroke dictionaries. Each dictionary must contain:
                     - "id" (str): A unique identifier for the spline (e.g., "head", "left_eye").
                     - "points" (List[str]): A list of point strings in "x{int}y{int}" format (e.g., "x10y20").
            scale_factor: A multiplier to increase the size of the final drawing in the world. Defaults to 20.0.

        Returns:
            A dictionary containing a list of the created spline actor details and success status.

        Examples:
            # Define a simple square sketch
            square_sketch = [
                {
                    "id": "square_outline",
                    "points": ["x10y10", "x40y10", "x40y40", "x10y40", "x10y10"]
                }
            ]
            # Create the spline in the editor
            spline_tool(strokes=square_sketch, scale_factor=50.0)
        """
        # This now correctly calls the implementation from your utils file
        return spline_tool_impl(ctx, strokes, scale_factor)


    @mcp.tool()
    def get_actors_in_level(ctx: Context) -> Dict[str, Any]:
        """
        Get a list of all actors in the current level.
        
        Returns:
            List of actors in the current level with their properties
            
        Examples:
            actors = get_actors_in_level()
            # Print names of all actors in level
            for actor in actors:
                print(actor["name"])
        """
        return get_actors_in_level_impl(ctx)

    @mcp.tool()
    def find_actors_by_name(ctx: Context, pattern: str) -> List[str]:
        """
        Find actors by name pattern.
        
        Args:
            pattern: Name pattern to search for (supports wildcards using *)
            
        Returns:
            List of actor names matching the pattern
            
        Examples:
            # Find all Point Light actors
            lights = find_actors_by_name("*PointLight*")
            
            # Find a specific actor
            player = find_actors_by_name("Player*")
        """
        return find_actors_by_name_impl(ctx, pattern)
    
    @mcp.tool()
    def spawn_actor(
        ctx: Context,
        name: str,
        type: str,
        location: List[float] = None,
        rotation: List[float] = None
    ) -> Dict[str, Any]:
        """
        Create a new basic Unreal Engine actor in the current level.
        This function is used for spawning built-in Unreal Engine actor types only.
        
        Args:
            name: The name to give the new actor (must be unique)
            type: The type of built-in actor to create. Supported types:
                  - StaticMeshActor: Basic static mesh actor
                  - PointLight: Point light source
                  - SpotLight: Spot light source
                  - DirectionalLight: Directional light source
                  - CameraActor: Camera actor
            location: The [x, y, z] world location to spawn at
            rotation: The [pitch, yaw, roll] rotation in degrees
            
        Returns:
            Dict containing the created actor's properties
            
        Examples:
            # Spawn a point light at origin
            spawn_actor(name="MyLight", type="PointLight")
            
            # Spawn a static mesh at a specific location
            spawn_actor(name="MyCube", type="StaticMeshActor", 
                       location=[100, 200, 50], 
                       rotation=[0, 45, 0])
                       
        Note:
            This function is for basic actor types only. For spawning custom Blueprint 
            actors with custom logic and components, use spawn_blueprint_actor() instead.
        """
        return spawn_actor_impl(ctx, name, type, location, rotation)
    
    @mcp.tool()
    def spawn_actor_v2(
        ctx: Context,
        name: str,
        type: str,
        additional_params: Dict[str, Any] = {}
    ) -> Dict[str, Any]:
        """
        Create a new basic Unreal Engine actor in the current level.
        This function is used for spawning built-in Unreal Engine actor types only.
        
        Args:
            name: The name to give the new actor (must be unique)
            type: The type of built-in actor to create. Supported types:
                  - StaticMeshActor: Basic static mesh actor
                  - PointLight: Point light source
                  - SpotLight: Spot light source
                  - DirectionalLight: Directional light source
                  - CameraActor: Camera actor
            additional_params:
                location: The [x, y, z] world location to spawn at
                rotation: The [pitch, yaw, roll] rotation in degrees
            
        Returns:
            Dict containing the created actor's properties
            
        Examples:
            # Spawn a point light at origin
            spawn_actor_v2(name="MyLight", type="PointLight")
            
            # Spawn a static mesh at a specific location
            spawn_actor_v2(name="MyCube", type="StaticMeshActor", 
                       additional_params={
                            "location":[100, 200, 50], 
                            "rotation":[0, 45, 0]
                        })
                       
        Note:
            This function is for basic actor types only. For spawning custom Blueprint 
            actors with custom logic and components, use spawn_blueprint_actor() instead.
        """
        return spawn_actor_v2_impl(ctx, name, type, additional_params)
    

    @mcp.tool()
    def delete_actor(ctx: Context, name: str) -> Dict[str, Any]:
        """
        Delete an actor by name.
        
        Args:
            name: Name of the actor to delete
            
        Returns:
            Dict containing response information
            
        Examples:
            # Delete an actor named "MyCube"
            delete_actor(name="MyCube")
        """
        return delete_actor_impl(ctx, name)
    
    @mcp.tool()
    def set_actor_transform(
        ctx: Context,
        name: str,
        location: List[float] = None,
        rotation: List[float] = None,
        scale: List[float] = None
    ) -> Dict[str, Any]:
        """
        Set the transform of an actor.
        
        Args:
            name: Name of the actor
            location: Optional [X, Y, Z] position
            rotation: Optional [Pitch, Yaw, Roll] rotation in degrees
            scale: Optional [X, Y, Z] scale
            
        Returns:
            Dict containing response information
            
        Examples:
            # Move an actor named "MyCube" to a new position
            set_actor_transform(name="MyCube", location=[100, 200, 50])
            
            # Rotate an actor named "MyCube" 45 degrees around Z axis
            set_actor_transform(name="MyCube", rotation=[0, 0, 45])
            
            # Scale an actor named "MyCube" to be twice as big
            set_actor_transform(name="MyCube", scale=[2.0, 2.0, 2.0])
            
            # Move, rotate, and scale an actor all at once
            set_actor_transform(
                name="MyCube", 
                location=[100, 200, 50],
                rotation=[0, 0, 45],
                scale=[2.0, 2.0, 2.0]
            )
        """
        return set_actor_transform_impl(ctx, name, location, rotation, scale)
    
    @mcp.tool()
    def get_actor_properties(ctx: Context, name: str) -> Dict[str, Any]:
        """
        Get all properties of an actor.
        
        Args:
            name: Name of the actor
            
        Returns:
            Dict containing actor properties
            
        Examples:
            # Get properties of an actor named "MyCube"
            props = get_actor_properties(name="MyCube")
            
            # Print location
            print(props["transform"]["location"])
        """
        return get_actor_properties_impl(ctx, name)

    @mcp.tool()
    def set_actor_property(
        ctx: Context,
        name: str,
        property_name: str,
        property_value
    ) -> Dict[str, Any]:
        """
        Set a property on an actor.
        
        Note: Currently there's a limitation with the property_value parameter type.
        Please contact the MCP system administrator for proper usage.
        
        Args:
            name: Name of the actor
            property_name: Name of the property to set
            property_value: Value to set the property to. Different property types accept different value formats:
                - For boolean properties: True/False
                - For numeric properties: int or float values
                - For string properties: string values
                - For color properties: [R, G, B, A] list (0-255 values)
                - For vector properties: [X, Y, Z] list
                - For enum properties: String name of the enum value or integer index
            
        Returns:
            Dict containing response information
            
        Examples:
            # Change the color of a light
            set_actor_property(
                name="MyPointLight",
                property_name="LightColor",
                property_value=[255, 0, 0, 255]  # RGBA
            )
            
            # Change the mobility of an actor
            set_actor_property(
                name="MyCube",
                property_name="Mobility",
                property_value="Movable"  # "Static", "Stationary", or "Movable"
            )
            
            # Set a boolean property
            set_actor_property(
                name="MyCube",
                property_name="bHidden",
                property_value=True
            )
            
            # Set a numeric property
            set_actor_property(
                name="PointLightTest",
                property_name="Intensity",
                property_value=5000.0
            )
        """
        return set_actor_property_impl(ctx, name, property_name, property_value)

    @mcp.tool()
    def set_light_property(
        ctx: Context,
        name: str,
        property_name: str,
        property_value
    ) -> Dict[str, Any]:
        """
        Set a property on a light component.
        
        This function accesses the LightComponent of a light actor and sets properties on it.
        
        Args:
            name: Name of the light actor
            property_name: Property to set, one of:
                - "Intensity": Brightness of the light (float)
                - "LightColor": Color of the light (array [R, G, B] with values 0-1)
                - "AttenuationRadius": How far the light reaches (float)
                - "SourceRadius": Size of the light source (float)
                - "SoftSourceRadius": Size of the soft light source border (float)
                - "CastShadows": Whether the light casts shadows (boolean)
            property_value: Value to set the property to
            
        Returns:
            Dict containing response information
            
        Examples:
            # Set light intensity
            set_light_property(
                name="MyPointLight",
                property_name="Intensity",
                property_value=5000.0
            )
            
            # Set light color to red
            set_light_property(
                name="MyPointLight",
                property_name="LightColor",
                property_value=[1.0, 0.0, 0.0]
            )
            
            # Set light attenuation radius
            set_light_property(
                name="MyPointLight",
                property_name="AttenuationRadius",
                property_value=500.0
            )
        """
        return set_light_property_impl(ctx, name, property_name, property_value)

    # @mcp.tool() commented out because it's buggy
    def focus_viewport(
        ctx: Context,
        target: str = None,
        location: List[float] = None,
        distance: float = 1000.0,
        orientation: List[float] = None
    ) -> Dict[str, Any]:
        """
        Focus the viewport on a specific actor or location.
        
        Args:
            target: Name of the actor to focus on (if provided, location is ignored)
            location: [X, Y, Z] coordinates to focus on (used if target is None)
            distance: Distance from the target/location
            orientation: Optional [Pitch, Yaw, Roll] for the viewport camera
            
        Returns:
            Response from Unreal Engine
            
        Examples:
            # Focus on an actor named "MyCube"
            focus_viewport(target="MyCube")
            
            # Focus on a specific location
            focus_viewport(location=[100, 200, 50])
            
            # Focus on an actor from a specific orientation
            focus_viewport(target="MyCube", orientation=[45, 0, 0])
        """
        return focus_viewport_impl(ctx, target, location, distance, orientation)

    @mcp.tool()
    def spawn_blueprint_actor(
        ctx: Context,
        blueprint_name: str,
        actor_name: str,
        location: List[float] = None,
        rotation: List[float] = None
    ) -> Dict[str, Any]:
        """
        Spawn an actor from a Blueprint class in the current level.
        This function is used for spawning custom Blueprint actors that can have:
        - Custom components and hierarchies
        - Visual scripting logic
        - Custom variables and events
        - Complex behaviors and interactions
        
        Args:
            blueprint_name: Path to the Blueprint to spawn from. Can be:
                          - Absolute path: "/Game/Blueprints/BP_Character"
                          - Relative path: "BP_Character" (will be prefixed with "/Game/Blueprints/")
            actor_name: Name to give the spawned actor instance (must be unique)
            location: The [x, y, z] world location to spawn at
            rotation: The [pitch, yaw, roll] rotation in degrees
            
        Returns:
            Dict containing the spawned actor's properties
            
        Examples:
            # Spawn a blueprint actor with a relative path (looks in /Game/Blueprints/)
            spawn_blueprint_actor(
                blueprint_name="BP_Character",
                actor_name="MyCharacter_1"
            )
            
            # Spawn a blueprint actor with a full path
            spawn_blueprint_actor(
                blueprint_name="/Game/Characters/BP_Enemy",
                actor_name="Enemy_1",
                location=[100, 200, 50],
                rotation=[0, 45, 0]
            )
            
            # For ThirdPerson template project character
            spawn_blueprint_actor(
                blueprint_name="/Game/ThirdPerson/Blueprints/BP_ThirdPersonCharacter",
                actor_name="Player1",
                location=[0, 0, 100]
            )
            
        Note:
            This function requires the Blueprint to exist and be properly compiled.
            For spawning basic actor types (lights, static meshes, etc.), use spawn_actor() instead.
        """
        return spawn_blueprint_actor_impl(ctx, blueprint_name, actor_name, location, rotation)

    @mcp.tool()
    def get_ue5_viewport_screenshot(
        ctx: Context
    ) -> Image:
        """
        Get the screenshot of the viewport of currently selected level.
        This screenshot is of the resolution 1920, 1080. 

        Requires editor "Use less CPU when in Background" option to be disabled. If this option is disabled screenshot will fail.
        Addionally in unreal engine viewport should be visible.
        
        Args:
            
        Returns:
            Image of the viewport screenshot
            
        Examples:
            # Spawn a blueprint actor with a relative path (looks in /Game/Blueprints/)
            get_ue5_viewport_screenshot()
        """
        code = '''import unreal
import uuid
import time
import os

suffix = uuid.uuid4().hex[:10]

automation_library = unreal.AutomationLibrary


screenshot_dir = unreal.SystemLibrary.get_project_directory() + "FridayWorkspace/Screenshots/"
screenshot_path = f"{screenshot_dir}viewport_{suffix}.png"

# Ensure the Screenshots directory exists
#unreal.EditorAssetLibrary.make_directory(screenshot_dir)

# this resolution is not accurate and may NOT show exactly what the user is seeing
task_info = automation_library.take_high_res_screenshot(1920, 1080, screenshot_path)

if task_info.is_valid_task():
    # screenshot can take a few more seconds to complete. Additionally if time.sleep is used it will pause the unreal engine.
    print(f"Screenshot taken at>>>{screenshot_path}")
else:
    print("Failed to start screenshot task.")
        '''
        # requires editor "Use less CPU when in Background" option to be disabled 
        output = execute_python_code_impl(ctx, code)

        lines = []
        if 'status' in output and output['status'] == 'success':
            result = output['result']
            if 'success' in result and result['success'] == True:
                lines = result['result'].splitlines()

        pattern = r"Screenshot taken at>>>"

        matching_lines = []
        for line in lines:
            if re.search(pattern, line):
                matching_lines.append(line)
        screenshot_path = ""
        if len(matching_lines) > 0:
            screenshot_path = matching_lines[-1].replace('Screenshot taken at>>>', '').strip()
        else:
            raise Exception("No screenshot found, output: ", output)

        timer = 0
        while(not os.path.exists(screenshot_path)):
            if (timer > 10):
                raise Exception("Screenshot file was not created")
            time.sleep(0.2)
            timer += 0.2
        
        # Read the file
        with open(screenshot_path, 'rb') as f:
            image_bytes = f.read()
        
        # Delete the temp file
        os.remove(screenshot_path)

        return Image(data=image_bytes, format="png")



    logger.info("Editor tools registered successfully")
