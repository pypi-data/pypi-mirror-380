"""
Blueprint Operations for Unreal MCP.

This module provides utility functions for working with Blueprints in Unreal Engine.
"""

import logging
from typing import Dict, List, Any, Tuple
from mcp.server.fastmcp import Context
from utils.unreal_connection_utils import send_unreal_command


from mcp.server.fastmcp import Context
from ..blueprint_actions.blueprint_action_operations import create_node_by_action_name as create_node_by_action_name_impl
from ..nodes.node_operations import connect_nodes_impl

# Get logger
logger = logging.getLogger("UnrealMCP")

def list_all_blueprints(ctx: Context) -> List[Dict[str, Any]]:
    """Implementation for getting a list of all blueprints in the project."""
    return send_unreal_command("list_all_blueprints", {})

def search_blueprints(ctx: Context, query: str) -> List[Dict[str, Any]]:
    """Implementation for searching blueprints matching a query string."""
    params = {"query": query}
    return send_unreal_command("search_blueprints", params)

def get_blueprint_details(ctx: Context, blueprint_path: str) -> Dict[str, Any]:
    """Implementation for getting detailed information about a specific blueprint."""
    params = {"blueprint_path": blueprint_path}
    return send_unreal_command("get_blueprint_details", params)

def create_blueprint_from_actor(
    ctx: Context,
    actor_name: str,
    blueprint_name: str,
    folder_path: str = "/Game/Blueprints"
) -> Dict[str, Any]:
    """Implementation for creating a new blueprint from an existing actor."""
    params = {
        "actor_name": actor_name,
        "blueprint_name": blueprint_name,
        "folder_path": folder_path
    }
    return send_unreal_command("create_blueprint_from_actor", params)

def create_blank_blueprint(
    ctx: Context,
    blueprint_name: str,
    parent_class: str = "Actor",
    folder_path: str = "/Game/Blueprints"
) -> Dict[str, Any]:
    """Implementation for creating a new blank blueprint."""
    params = {
        "blueprint_name": blueprint_name,
        "parent_class": parent_class,
        "folder_path": folder_path
    }
    return send_unreal_command("create_blank_blueprint", params)

def compile_blueprint(ctx: Context, blueprint_name: str) -> Dict[str, Any]:
    """Implementation for compiling a blueprint."""
    # The C++ side will handle finding the path from the name, 
    # assuming it expects the 'blueprint_name' key.
    params = {"blueprint_name": blueprint_name} 
    return send_unreal_command("compile_blueprint", params)

def save_blueprint(ctx: Context, blueprint_path: str) -> Dict[str, Any]:
    """Implementation for saving a blueprint to disk."""
    params = {"blueprint_path": blueprint_path}
    return send_unreal_command("save_blueprint", params)

def get_blueprint_variables(ctx: Context, blueprint_path: str) -> List[Dict[str, Any]]:
    """Implementation for getting a list of variables defined in a blueprint."""
    params = {"blueprint_path": blueprint_path}
    return send_unreal_command("get_blueprint_variables", params)

def add_blueprint_variable(
    ctx: Context,
    blueprint_name: str,
    var_name: str,
    var_type: str,
    default_value: Any = None,
    is_instance_editable: bool = True,
    is_blueprint_read_only: bool = False,
    category: str = "Default"
) -> Dict[str, Any]:
    """Implementation for adding a new variable to a blueprint."""
    params = {
        "blueprint_name": blueprint_name,
        "variable_name": var_name,
        "variable_type": var_type,
        "is_exposed": is_instance_editable,
        "is_blueprint_read_only": is_blueprint_read_only,
        "category": category
    }
    
    # Only include default value if provided
    if default_value is not None:
        params["default_value"] = default_value
    
    return send_unreal_command("add_blueprint_variable", params)

def get_blueprint_functions(ctx: Context, blueprint_path: str) -> List[Dict[str, Any]]:
    """Implementation for getting a list of functions defined in a blueprint."""
    params = {"blueprint_path": blueprint_path}
    return send_unreal_command("get_blueprint_functions", params)

def add_blueprint_function(
    ctx: Context,
    blueprint_path: str,
    function_name: str,
    inputs: List[Dict[str, Any]] = None,
    outputs: List[Dict[str, Any]] = None,
    pure: bool = False,
    static: bool = False,
    category: str = "Default"
) -> Dict[str, Any]:
    """Implementation for adding a new function to a blueprint."""
    if inputs is None:
        inputs = []
    if outputs is None:
        outputs = []
    
    params = {
        "blueprint_path": blueprint_path,
        "function_name": function_name,
        "inputs": inputs,
        "outputs": outputs,
        "pure": pure,
        "static": static,
        "category": category
    }
    
    return send_unreal_command("add_blueprint_function", params)

def connect_graph_nodes(
    ctx: Context,
    blueprint_path: str,
    function_name: str,
    source_node_name: str,
    source_pin_name: str,
    target_node_name: str,
    target_pin_name: str
) -> Dict[str, Any]:
    """Implementation for connecting two nodes in a blueprint graph."""
    params = {
        "blueprint_path": blueprint_path,
        "function_name": function_name,
        "source_node_name": source_node_name,
        "source_pin_name": source_pin_name,
        "target_node_name": target_node_name,
        "target_pin_name": target_pin_name
    }
    
    return send_unreal_command("connect_graph_nodes", params)

def create_blueprint(
    ctx: Context,
    name: str,
    parent_class: str,
    folder_path: str = ""
) -> Dict[str, Any]:
    """Implementation for creating a new Blueprint class."""
    params = {
        "name": name,
        "parent_class": parent_class
    }
    
    if folder_path:
        params["folder_path"] = folder_path
        
    return send_unreal_command("create_blueprint", params)

def add_component_to_blueprint(
    ctx: Context,
    blueprint_name: str,
    component_type: str,
    component_name: str,
    location: List[float] = None,
    rotation: List[float] = None,
    scale: List[float] = None,
    component_properties: Dict[str, Any] = None
) -> Dict[str, Any]:
    """Implementation for adding a component to a Blueprint."""
    params = {
        "blueprint_name": blueprint_name,
        "component_type": component_type,
        "component_name": component_name
    }
    
    if location is not None:
        params["location"] = location
        
    if rotation is not None:
        params["rotation"] = rotation
        
    if scale is not None:
        params["scale"] = scale
        
    if component_properties is not None:
        params["component_properties"] = component_properties
        
    return send_unreal_command("add_component_to_blueprint", params)

def set_static_mesh_properties(
    ctx: Context,
    blueprint_name: str,
    component_name: str,
    static_mesh: str = "/Engine/BasicShapes/Cube.Cube"
) -> Dict[str, Any]:
    """Implementation for setting static mesh properties on a StaticMeshComponent."""
    params = {
        "blueprint_name": blueprint_name,
        "component_name": component_name,
        "static_mesh": static_mesh
    }
    
    return send_unreal_command("set_static_mesh_properties", params)

def set_component_property(
    ctx: Context,
    blueprint_name: str,
    component_name: str,
    **kwargs
) -> Dict[str, Any]:
    """
    Set one or more properties on a component in a Blueprint.

    Args:
        ctx: MCP context
        blueprint_name: Name of the target Blueprint
        component_name: Name of the component
        kwargs: Properties to set. You can pass properties as direct keyword arguments (recommended),
            or as a single dict using kwargs={...}. If double-wrapped (kwargs={'kwargs': {...}}),
            the function will automatically flatten it for convenience. This matches the widget property setter pattern.

    Returns:
        Response indicating success or failure for each property.

    Example:
        # Preferred usage (direct keyword arguments):
        set_component_property(ctx, "MyActor", "Mesh", StaticMesh="/Game/StarterContent/Shapes/Shape_Cube.Shape_Cube", Mobility="Movable")

        # Also supported (dict):
        set_component_property(ctx, "MyActor", "Mesh", kwargs={"StaticMesh": "/Game/StarterContent/Shapes/Shape_Cube.Shape_Cube", "Mobility": "Movable"})

    """
    # Debug: Log all incoming arguments
    logger.info(f"[DEBUG] set_component_property called with: blueprint_name={blueprint_name}, component_name={component_name}, kwargs={kwargs}")

    # Flatten if kwargs is double-wrapped (i.e., kwargs={'kwargs': {...}})
    if (
        len(kwargs) == 1 and
        'kwargs' in kwargs and
        isinstance(kwargs['kwargs'], dict)
    ):
        logger.info("[DEBUG] Flattening double-wrapped kwargs in set_component_property")
        kwargs = kwargs['kwargs']

    # Argument validation
    if not blueprint_name or not isinstance(blueprint_name, str):
        logger.error("[ERROR] 'blueprint_name' is required and must be a string.")
        raise ValueError("'blueprint_name' is required and must be a string.")
    if not component_name or not isinstance(component_name, str):
        logger.error("[ERROR] 'component_name' is required and must be a string.")
        raise ValueError("'component_name' is required and must be a string.")
    if not kwargs or not isinstance(kwargs, dict):
        logger.error("[ERROR] At least one property must be provided as a keyword argument.")
        raise ValueError("At least one property must be provided as a keyword argument.")

    params = {
        "blueprint_name": blueprint_name,
        "component_name": component_name,
        "kwargs": kwargs
    }
    logger.info(f"[DEBUG] Sending set_component_property params: {params}")
    return send_unreal_command("set_component_property", params)

def set_physics_properties(
    ctx: Context,
    blueprint_name: str,
    component_name: str,
    simulate_physics: bool = True,
    gravity_enabled: bool = True,
    mass: float = 1.0,
    linear_damping: float = 0.01,
    angular_damping: float = 0.0
) -> Dict[str, Any]:
    """Implementation for setting physics properties on a component."""
    params = {
        "blueprint_name": blueprint_name,
        "component_name": component_name,
        "simulate_physics": simulate_physics,
        "gravity_enabled": gravity_enabled,
        "mass": mass,
        "linear_damping": linear_damping,
        "angular_damping": angular_damping
    }
    
    return send_unreal_command("set_physics_properties", params)

def set_blueprint_property(
    ctx: Context,
    blueprint_name: str,
    property_name: str,
    property_value: Any
) -> Dict[str, Any]:
    """Implementation for setting a property on a Blueprint class default object."""
    params = {
        "blueprint_name": blueprint_name,
        "property_name": property_name,
        "property_value": property_value
    }
    
    return send_unreal_command("set_blueprint_property", params)

def set_pawn_properties(
    ctx: Context,
    blueprint_name: str,
    auto_possess_player: str = "",
    use_controller_rotation_yaw: bool = None,
    use_controller_rotation_pitch: bool = None,
    use_controller_rotation_roll: bool = None,
    can_be_damaged: bool = None
) -> Dict[str, Any]:
    """Implementation for setting common Pawn properties on a Blueprint."""
    params = {
        "blueprint_name": blueprint_name
    }
    
    if auto_possess_player:
        params["auto_possess_player"] = auto_possess_player
        
    if use_controller_rotation_yaw is not None:
        params["use_controller_rotation_yaw"] = use_controller_rotation_yaw
        
    if use_controller_rotation_pitch is not None:
        params["use_controller_rotation_pitch"] = use_controller_rotation_pitch
        
    if use_controller_rotation_roll is not None:
        params["use_controller_rotation_roll"] = use_controller_rotation_roll
        
    if can_be_damaged is not None:
        params["can_be_damaged"] = can_be_damaged
        
    return send_unreal_command("set_pawn_properties", params)

def add_interface_to_blueprint(
    ctx: Context,
    blueprint_name: str,
    interface_name: str
) -> Dict[str, Any]:
    """Implementation for adding an interface to a blueprint."""
    params = {
        "blueprint_name": blueprint_name,
        "interface_name": interface_name
    }
    return send_unreal_command("add_interface_to_blueprint", params)

def create_blueprint_interface(
    ctx: Context,
    name: str,
    folder_path: str = ""
) -> Dict[str, Any]:
    """Implementation for creating a Blueprint Interface asset."""
    params = {
        "name": name,
        "folder_path": folder_path
    }
    return send_unreal_command("create_blueprint_interface", params)

def list_blueprint_components(ctx: Context, blueprint_name: str) -> Dict[str, Any]:
    """Implementation for listing components in a blueprint."""
    params = {"blueprint_name": blueprint_name}
    return send_unreal_command("list_blueprint_components", params)

def create_custom_blueprint_function(
    ctx: Context,
    blueprint_name: str,
    function_name: str,
    inputs: List[Dict[str, str]] = None,
    outputs: List[Dict[str, str]] = None,
    is_pure: bool = False,
    is_const: bool = False,
    access_specifier: str = "Public",
    category: str = "Default"
) -> Dict[str, Any]:
    """Implementation for creating a custom user-defined function in a blueprint.
    
    Args:
        blueprint_name: Name of the target Blueprint
        function_name: Name of the custom function to create
        inputs: List of input parameters, each with 'name' and 'type' keys
        outputs: List of output parameters, each with 'name' and 'type' keys  
        is_pure: Whether the function is pure (no execution pins)
        is_const: Whether the function is const
        access_specifier: Access level ("Public", "Protected", "Private")
        category: Category for organization in the functions list
        
    Returns:
        Dictionary containing success status and function information
    """
    params = {
        "blueprint_name": blueprint_name,
        "function_name": function_name,
        "is_pure": is_pure,
        "is_const": is_const,
        "access_specifier": access_specifier,
        "category": category
    }
    
    if inputs is not None:
        params["inputs"] = inputs
        
    if outputs is not None:
        params["outputs"] = outputs
        
    return send_unreal_command("create_custom_blueprint_function", params)

def post_blueprint_from_json(
    ctx: Context,
    blueprint_path: str,
    parent_class: str,
    blueprint_data: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Implementation for creating or overwriting a Blueprint from a full JSON structure.
    """
    logger.info(f"Sending command to create/update blueprint from JSON at: {blueprint_path}")
    
    params = {
        "blueprint_path": blueprint_path,
        "parent_class": parent_class,
        "blueprint_data": blueprint_data 
    }

    command_type = "post_blueprint_json"
    
    return send_unreal_command(command_type, params)

def build_blueprint_from_definition(
    ctx: Context,
    blueprint_name: str,
    parent_class: str,
    definition: Dict[str, Any],
    folder_path: str = "/Game/Blueprints"
) -> Dict[str, Any]:
    """
    Orchestrates the creation of a complete Blueprint from a JSON definition by calling
    other low-level implementation functions.
    """
    logger.info(f"BUILDER: Starting construction of Blueprint '{blueprint_name}' from definition.")

    # Step 1: Create the Blueprint Asset
    try:
        # CORRECTED: Calls the function defined in this file directly, no _impl suffix.
        bp_result = create_blueprint(ctx, name=blueprint_name, parent_class=parent_class, folder_path=folder_path)
        if not bp_result.get("success", True):
            logger.error(f"BUILDER: Failed to create Blueprint asset. Reason: {bp_result.get('message')}")
            return bp_result
        blueprint_path = bp_result.get('path')
        logger.info(f"BUILDER: Blueprint asset created or found at '{blueprint_path}'.")
    except Exception as e:
        return {"success": False, "message": f"An exception occurred during Blueprint asset creation: {e}"}

    # Step 2: Details (Interfaces, Replication)
    details = definition.get("details", {})
    if details:
        logger.info("BUILDER: Processing 'details'...")
        for interface_path in details.get("interfaces", []):
            # CORRECTED: Calls the function defined in this file.
            add_interface_to_blueprint(ctx, blueprint_name, interface_path)
        if details.get("bReplicates"):
            # CORRECTED: Calls the function defined in this file.
            set_blueprint_property(ctx, blueprint_name, "bReplicates", True)

    # Step 3: Scene (Components)
    scene = definition.get("scene", {})
    if scene:
        logger.info("BUILDER: Processing 'scene' component hierarchy...")
        # A more robust version would be recursive to handle parenting.
        if root_info := scene.get("RootComponent"):
            add_component_to_blueprint(ctx, blueprint_name, root_info['Type'], root_info['Name'])
        for child in scene.get("Children", []):
            if child_info := child.get("Component"):
                add_component_to_blueprint(ctx, blueprint_name, child_info['Type'], child_info['Name'])

    # Step 4: Variables
    for var_def in definition.get("variables", []):
        logger.info(f"BUILDER: Creating variable '{var_def['Name']}' of type '{var_def['Type']}'.")
        # CORRECTED: Calls the function defined in this file.
        add_blueprint_variable(ctx, blueprint_name, var_def["Name"], var_def["Type"], is_instance_editable=var_def.get("IsExposed", False))

    # Step 5: Defaults
    for var_name, default_value in definition.get("defaults", {}).items():
        logger.info(f"BUILDER: Setting default value for '{var_name}'.")
        # CORRECTED: Calls the function defined in this file.
        set_blueprint_property(ctx, blueprint_name, var_name, default_value)

    # Step 6: Graphs
    for graph_data in definition.get("graphs", []):
        graph_def = graph_data.get("BlueprintGraph", {})
        graph_name = graph_def.get("Name", "EventGraph")
        nodes = graph_def.get("Nodes", [])
        connections = graph_def.get("Connections", [])
        
        node_id_map = {}

        # PASS 1: Create all nodes
        logger.info(f"BUILDER: Creating {len(nodes)} nodes in graph '{graph_name}'...")
        for node_def in nodes:
            json_node_id = node_def["NodeID"]
            node_type = node_def["NodeType"]
            properties = node_def.get("Properties", {})
            
            params_for_tool = {"target_graph": graph_name}
            # CORRECTED: Added more robust logic for variable get/set and macros
            if node_type == "Event":
                params_for_tool['function_name'] = properties.get("Event")
            elif node_type == "CallFunction":
                params_for_tool['function_name'] = properties.get("Function")
            elif node_type == "VariableGet":
                params_for_tool['function_name'] = f"Get {properties.get('variable_name')}"
            elif node_type == "VariableSet":
                params_for_tool['function_name'] = f"Set {properties.get('variable_name')}"
            elif node_type == "ForEachLoop":
                params_for_tool['function_name'] = "ForEachLoop"
            elif node_type == "Branch":
                params_for_tool['function_name'] = "Branch"
            elif node_type == "Macro": # Added support for Macro nodes like FlipFlop
                params_for_tool['function_name'] = properties.get("Macro")
            
            if params_for_tool.get('function_name'):
                try:
                    # CORRECTED: Calls the imported function correctly.
                    node_result = create_node_by_action_name(ctx, blueprint_name=blueprint_name, **params_for_tool)
                    if node_result.get("success") and (real_node_id := node_result.get("node_id")):
                        node_id_map[json_node_id] = real_node_id
                    else:
                        logger.error(f"BUILDER: Failed to create node '{params_for_tool['function_name']}': {node_result.get('message')}")
                except Exception as e:
                    logger.error(f"BUILDER: Exception creating node '{params_for_tool['function_name']}': {e}")

        # PASS 2: Connect all nodes
        if connections and node_id_map:
            connection_batch = [
                {
                    "source_node_id": node_id_map.get(conn["from_node"]),
                    "source_pin": conn["from_pin"],
                    "target_node_id": node_id_map.get(conn["to_node"]),
                    "target_pin": conn["to_pin"],
                }
                for conn in connections
                if node_id_map.get(conn["from_node"]) and node_id_map.get(conn["to_node"])
            ]
            if connection_batch:
                # CORRECTED: Calls the imported function correctly.
                connect_blueprint_nodes(ctx, blueprint_name=blueprint_name, connections=connection_batch)

    # Step 7: Final Compilation
    logger.info("BUILDER: Performing final compilation...")
    # CORRECTED: Calls the function defined in this file.
    compile_result = compile_blueprint(ctx, blueprint_name)
    if compile_result.get("num_errors", 0) > 0:
        return {"success": False, "message": "Blueprint created but failed to compile.", "details": compile_result}

    logger.info(f"BUILDER: Blueprint '{blueprint_name}' built successfully.")
    return {"success": True, "message": f"Blueprint '{blueprint_name}' built successfully.", "path": blueprint_path}