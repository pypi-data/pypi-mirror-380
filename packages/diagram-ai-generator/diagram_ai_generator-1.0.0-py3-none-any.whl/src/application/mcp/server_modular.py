"""
Servidor MCP modular para Diagram AI Generator
"""
import sys
import time
from pathlib import Path
from typing import Callable, Dict

try:
    from mcp.server.fastmcp import FastMCP
    MCP_AVAILABLE = True
except ImportError:
    class FastMCP:
        def __init__(self, name: str): pass
        def tool(self): return lambda f: f
        def prompt(self): return lambda f: f
        def resource(self, pattern: str): return lambda f: f
        def run(self): pass
    MCP_AVAILABLE = False

# Añadir el directorio del proyecto al path para importaciones relativas
project_root = Path(__file__).parent.parent.parent.parent
sys.path.insert(0, str(project_root))

from src.application.services.diagram_service import DiagramService
from src.application.mcp.tools.registry import ToolRegistry

# Crear instancia del servicio de diagramas
diagram_service = DiagramService()

# Crear instancia del registro de herramientas
tool_registry = ToolRegistry(diagram_service)

# Crear instancia del servidor MCP
mcp = FastMCP("diagram-ai-generator")

# Registrar todas las herramientas dinámicamente
for tool_name, tool_method in tool_registry.get_tool_methods().items():
    mcp.tool()(tool_method)

# Función principal para ejecutar el servidor
def main():
    """Función principal para ejecutar el servidor MCP"""
    if MCP_AVAILABLE:
        print("🚀 Iniciando servidor MCP modular...")
        print(f"📋 Herramientas registradas: {list(tool_registry.get_tool_methods().keys())}")
        print("🔗 Servidor listo para recibir conexiones MCP...")
        print("💡 Para conectar desde Claude Desktop, usa:")
        print(f"   - Comando: python3 {Path(__file__).resolve()}")
        print("   - O ejecuta: docker-compose exec diagram-ai-generator python3 scripts/run_mcp_server.py")
        print("")
        print("⏳ Servidor esperando conexiones (Ctrl+C para detener)...")
        
        try:
            # Intentar ejecutar el servidor MCP
            mcp.run()
        except KeyboardInterrupt:
            print("\n🛑 Servidor detenido por el usuario")
            return 0
        except Exception as e:
            print(f"❌ Error en el servidor: {e}")
            # Si falla, mantener el contenedor activo para debugging
            print("🔄 Manteniendo contenedor activo para debugging...")
            import time
            try:
                while True:
                    time.sleep(60)
                    print("💓 Servidor en espera... (Ctrl+C para detener)")
            except KeyboardInterrupt:
                print("\n🛑 Servidor detenido")
                return 0
    else:
        print("❌ MCP no está disponible. Instala con: pip install 'mcp[cli]'")
        print("💡 Manteniendo contenedor activo para debugging...")
        import time
        try:
            while True:
                time.sleep(60)
                print("⚠️  MCP no disponible, contenedor en espera...")
        except KeyboardInterrupt:
            return 1
    
    return 0

if __name__ == "__main__":
    main()