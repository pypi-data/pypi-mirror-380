# Unreal MCP (Model Context Protocol)

🚀 **The most advanced and powerful server for Unreal Engine integration via the Model Context Protocol (MCP).**

Transform your Unreal Engine workflow with AI-powered automation, blueprint generation, and intelligent development assistance.

## 🎯 Quick Setup

### Prerequisites
- **Python 3.10+** 
- **Unreal Engine 5+** 
- **uvx installed**
- **MCP Client** (Claude Desktop, Cursor, or Windsurf)

### Installation

1. **Download Unreal Engine Plugin:**
   > 📦 **Plugin Download:** https://www.fab.com/listings/df091518-23de-4f9d-9dac-bbe6f4bff0e9

2. **Configure MCP Client:**
   
   Add this configuration to your MCP client settings:
   
   ```json
   {
     "mcpServers": {
       "unreal-mcp": {
         "command": "uvx",
         "args": [
            "--from",
            "gamewave-unreal-mcp",
            "unreal-mcp"
         ]
       }
     }
   }
   ```

   **For Friday** Already configured. Download it here: https://apps.microsoft.com/detail/9p5mdsrjhdc8?hl=en-US&gl=US.


4. **Launch Unreal Engine** and start your MCP client!

## ✨ Features

### 🖥️ Client Support
- **✅ Friday Custom Desktop App Support**

### 🤖 PCG Tools
- **✅ Create PCG Graph** Creates the entire PCG graph
- **✅ Get PCG Graph** Gets the PCG graph based on file path

### 🤖 PCG Tools
- **✅ Create Material Graph** Creates the entire material graph
- **✅ Get Mateiral Graph** Gets the Material graph based on file path - Beta.

### 🎨 Download Tools
- **✅ Download & import 3d assets** Objaverse models - Non commercial Recommended
- **✅ Download & import Textures** Download ai generated textures 

### 🛠️ Blueprint Development
- **✅ Create blueprints** with custom parent classes
- **✅ Add & configure components** (StaticMesh, Camera, Light, etc.)
- **✅ Set component properties** and static mesh assets
- **✅ Configure physics properties** (simulation, gravity, mass, damping)
- **✅ Set Pawn-specific properties** (auto possess, rotation control, damageability)
- **✅ Compile Blueprints** and set class default properties
- **✅ Add variables** of any type (Boolean, Integer, Float, Vector, Struct, Array, Delegate, Blueprint references)
- **✅ Add interfaces** to Blueprints and create Blueprint Interfaces
- **✅ Add custom event nodes** and call BlueprintCallable functions by name
- **✅ List all components** (including inherited) for inspection and automation
- **✅ Dynamic Blueprint Action Discovery** - discover available actions for specific pin types, classes, and hierarchies
- **✅ Intelligent Node Creation** - create Blueprint nodes using discovered action names from Unreal's action database
- **✅ Pin Requirement Analysis** - get detailed information about node pins and their type requirements
- **✅ Class Hierarchy Exploration** - explore complete functionality across inheritance chains

### 🔗 Blueprint Node Graph
- **✅ Add event nodes** for standard events (BeginPlay, Tick) and input actions
- **✅ Add custom event nodes** and create function call nodes with target components and parameters
- **✅ Connect nodes** with proper pin linkages for execution and data flow
- **✅ Add variables** with various types (Boolean, Integer, Float, Vector, Struct, etc.)
- **✅ Create component references** and self references in the graph
- **✅ Find and identify nodes** in the Blueprint graph by type/event
- **✅ Get variable type information** for automation
- **✅ Build complete gameplay logic chains** through the Blueprint visual scripting system

### 🎮 Actor/Level/Scene Control
- **✅ Spawn/Delete Actors** and shapes
- **✅ Move, rotate and scale** objects
- **✅ Query actor properties** and find actors by name or pattern
- **✅ List all actors** in the current level
- **✅ Set and query light properties** (intensity, color, attenuation, shadows, source size)
- **✅ Spawn actors** from Blueprint classes with custom transforms
- **✅ viewport Screenshot** Get screenshot of the viewport 

### 🤖 AI Integration
- **🛠️ Prompt to 3D model** fetch and spawn (in development)

### ⚙️ Control Systems
- **✅ Run Python scripts** directly in Unreal
- **🚧 Run Console Commands** (coming soon)

### 🎨 UI Development
- **✅ Create UMG Widget Blueprints** for building user interfaces
- **✅ Add and customize UI components** (text, buttons, images, checkboxes, sliders, etc.)
- **✅ Add any widget component type** to a widget
- **✅ Create complex layouts** with scrollboxes, borders, containers, and nested hierarchies
- **✅ Set up event bindings** and property bindings for dynamic UI
- **✅ Add widgets to viewport** with z-ordering control
- **✅ Set and query widget component properties** (text, color, brush, etc.)
- **✅ Change widget placement, size, and alignment**
- **✅ Check for component existence** and get hierarchical layout information
- **✅ Get container dimensions** for layout automation

### 📁 Project Management
- **✅ Create and organize** content browser folders for asset management
- **✅ Create project folders** for non-content files (logs, intermediate, etc.)
- **✅ Set up input mappings** for keyboard, mouse, and gamepad controls
- **✅ Enhanced Input System:** Create Input Action assets with value types (Digital, Analog, Axis2D, Axis3D)
- **✅ Enhanced Input System:** Create Input Mapping Context assets for organized input handling
- **✅ Enhanced Input System:** Add key mappings between contexts and actions with modifier support
- **✅ Enhanced Input System:** List and query Enhanced Input Actions and Mapping Contexts with metadata
- **✅ Enhanced Input System:** Full integration with UE 5.5+ Enhanced Input architecture
- **✅ Create, update, and inspect** Unreal structs
- **✅ List folder contents** for project and content folders

### 🎛️ Editor Controls
- **✅ Focus viewport** on specific actors or locations with custom distance
- **✅ Control viewport camera** orientation with precise angle settings
- **✅ Find actors in the scene** using name pattern matching and wildcards
- **✅ Access and modify** actor properties through the editor interface
- **✅ Create and configure** different light types (Point, Spot, Directional)
- **✅ Adjust light properties** (intensity, color, attenuation, shadows, source size)
- **✅ Spawn Blueprint actors** with custom logic and components

## Full Setup with the most powerful agent for Unreal Engine

- **visit gamewave.dev** 

## 📝 License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

## 🤝 Support

- **Email:** fridayue5@gmail.com
- **Issues:** Create an issue in this repository
- **Documentation:** Check the `/docs` folder for detailed guides

---

**⚡ Transform your Unreal Engine development with the power of AI!** 

Made with ❤️ by GameWave