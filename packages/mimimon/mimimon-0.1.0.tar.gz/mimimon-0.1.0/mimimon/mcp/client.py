"""
MCP (Model Context Protocol) Client

Implements Model Context Protocol support for MiMiMON,
enabling communication with various AI models and agents.
"""

import asyncio
import json
from typing import Dict, Any, Optional, List
from datetime import datetime

import websockets
from rich.console import Console

console = Console()


class MCPMessage:
    """Represents an MCP protocol message."""
    
    def __init__(self, method: str, params: Dict[str, Any], id: Optional[str] = None):
        self.method = method
        self.params = params
        self.id = id or f"mcp_{datetime.now().strftime('%Y%m%d_%H%M%S_%f')}"
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert message to dictionary format."""
        return {
            "jsonrpc": "2.0",
            "method": self.method,
            "params": self.params,
            "id": self.id
        }
    
    def to_json(self) -> str:
        """Convert message to JSON string."""
        return json.dumps(self.to_dict())


class MCPClient:
    """
    Client for Model Context Protocol interactions.
    
    Supports communication with MCP-compatible AI models and agents.
    """
    
    def __init__(self, endpoint: Optional[str] = None, transport: str = "websocket"):
        self.endpoint = endpoint or "ws://localhost:8080/mcp"
        self.transport = transport
        self.connection = None
        self.session_id = None
        self.message_handlers: Dict[str, callable] = {}
        
        # Register default handlers
        self._register_default_handlers()
    
    def _register_default_handlers(self):
        """Register default message handlers."""
        self.message_handlers["ping"] = self._handle_ping
        self.message_handlers["initialize"] = self._handle_initialize
        self.message_handlers["notification"] = self._handle_notification
    
    async def connect(self) -> bool:
        """Connect to MCP endpoint."""
        try:
            if self.transport == "websocket":
                self.connection = await websockets.connect(self.endpoint)
                console.print(f"[green]✓[/green] Connected to MCP endpoint: {self.endpoint}")
                return True
            else:
                console.print(f"[red]✗[/red] Unsupported transport: {self.transport}")
                return False
        except Exception as e:
            console.print(f"[red]✗[/red] Failed to connect to MCP endpoint: {e}")
            return False
    
    async def initialize(self, client_info: Dict[str, Any]) -> Dict[str, Any]:
        """Initialize MCP session."""
        message = MCPMessage(
            method="initialize",
            params={
                "protocolVersion": "1.0.0",
                "clientInfo": client_info,
                "capabilities": {
                    "tools": {"listChanged": True},
                    "resources": {"subscribe": True, "listChanged": True}
                }
            }
        )
        
        return await self.send_request(message)
    
    async def send_request(self, message: MCPMessage) -> Dict[str, Any]:
        """Send an MCP request and wait for response."""
        if not self.connection:
            raise RuntimeError("Not connected to MCP endpoint")
        
        await self.connection.send(message.to_json())
        console.print(f"[blue]→[/blue] Sent MCP request: {message.method}")
        
        # Wait for response
        response_text = await self.connection.recv()
        response = json.loads(response_text)
        
        console.print(f"[blue]←[/blue] Received MCP response: {response.get('result', {}).get('protocolVersion', 'unknown')}")
        
        return response
    
    async def send_notification(self, method: str, params: Dict[str, Any]):
        """Send an MCP notification (no response expected)."""
        if not self.connection:
            raise RuntimeError("Not connected to MCP endpoint")
        
        message = {
            "jsonrpc": "2.0",
            "method": method,
            "params": params
        }
        
        await self.connection.send(json.dumps(message))
        console.print(f"[blue]→[/blue] Sent MCP notification: {method}")
    
    async def list_tools(self) -> List[Dict[str, Any]]:
        """List available tools from the MCP server."""
        message = MCPMessage(method="tools/list", params={})
        response = await self.send_request(message)
        return response.get("result", {}).get("tools", [])
    
    async def call_tool(self, name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """Call a tool on the MCP server."""
        message = MCPMessage(
            method="tools/call",
            params={
                "name": name,
                "arguments": arguments
            }
        )
        
        return await self.send_request(message)
    
    async def list_resources(self) -> List[Dict[str, Any]]:
        """List available resources from the MCP server."""
        message = MCPMessage(method="resources/list", params={})
        response = await self.send_request(message)
        return response.get("result", {}).get("resources", [])
    
    async def read_resource(self, uri: str) -> Dict[str, Any]:
        """Read a resource from the MCP server."""
        message = MCPMessage(
            method="resources/read",
            params={"uri": uri}
        )
        
        return await self.send_request(message)
    
    async def listen_for_messages(self):
        """Listen for incoming messages from the MCP server."""
        if not self.connection:
            raise RuntimeError("Not connected to MCP endpoint")
        
        try:
            async for message_text in self.connection:
                message = json.loads(message_text)
                await self._handle_message(message)
        except websockets.exceptions.ConnectionClosed:
            console.print("[yellow]⚠[/yellow] MCP connection closed")
        except Exception as e:
            console.print(f"[red]✗[/red] Error listening for messages: {e}")
    
    async def _handle_message(self, message: Dict[str, Any]):
        """Handle incoming MCP message."""
        method = message.get("method")
        if method and method in self.message_handlers:
            await self.message_handlers[method](message)
        else:
            console.print(f"[yellow]⚠[/yellow] Unhandled MCP message: {method}")
    
    async def _handle_ping(self, message: Dict[str, Any]):
        """Handle ping message."""
        console.print("[blue]🏓[/blue] Received MCP ping")
    
    async def _handle_initialize(self, message: Dict[str, Any]):
        """Handle initialize message."""
        console.print("[green]✓[/green] MCP session initialized")
    
    async def _handle_notification(self, message: Dict[str, Any]):
        """Handle notification message."""
        console.print(f"[blue]🔔[/blue] MCP notification: {message.get('method')}")
    
    async def close(self):
        """Close MCP connection."""
        if self.connection:
            await self.connection.close()
            console.print("[yellow]⚠[/yellow] MCP connection closed")


def start_mcp_session(
    protocol: str = "1.0",
    endpoint: Optional[str] = None,
    transport: str = "websocket"
):
    """Start an MCP session with the specified parameters."""
    async def run_session():
        client = MCPClient(endpoint=endpoint, transport=transport)
        
        try:
            # Connect to MCP server
            if await client.connect():
                # Initialize session
                client_info = {
                    "name": "MiMiMON",
                    "version": "0.1.0"
                }
                
                await client.initialize(client_info)
                
                # List available tools and resources
                tools = await client.list_tools()
                resources = await client.list_resources()
                
                console.print(f"[green]✓[/green] Available tools: {len(tools)}")
                console.print(f"[green]✓[/green] Available resources: {len(resources)}")
                
                # Start listening for messages
                await client.listen_for_messages()
                
        except KeyboardInterrupt:
            console.print("\n[yellow]⚠[/yellow] MCP session interrupted by user")
        except Exception as e:
            console.print(f"[red]✗[/red] MCP session error: {e}")
        finally:
            await client.close()
    
    # Run the session
    try:
        asyncio.run(run_session())
    except KeyboardInterrupt:
        console.print("\n[yellow]⚠[/yellow] MCP session stopped")