"""
MiMiMON Client

Main client class for interacting with AI agents and the MiMiMON platform.
This client provides similar functionality to OmnaraClient.
"""

import asyncio
import json
from typing import Dict, List, Optional, Any, Callable
from datetime import datetime

import httpx
import websockets
from pydantic import BaseModel, Field
from rich.console import Console

console = Console()


class AgentSession(BaseModel):
    """Represents an active agent monitoring session."""
    agent_id: str
    agent_type: str
    start_time: datetime = Field(default_factory=datetime.now)
    status: str = "active"
    metadata: Dict[str, Any] = Field(default_factory=dict)


class MiMiMONClient:
    """
    Main client for MiMiMON platform interactions.
    
    Provides functionality to:
    - Monitor AI agents across platforms
    - Communicate with agents remotely
    - Track agent activities and performance
    - Manage agent sessions
    """
    
    def __init__(
        self, 
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
        debug: bool = False
    ):
        self.api_key = api_key
        self.base_url = base_url or "https://api.mimimon.ai"
        self.debug = debug
        self.sessions: Dict[str, AgentSession] = {}
        self._websocket = None
        self._http_client = httpx.AsyncClient()
        
        if debug:
            console.print(f"[debug]MiMiMONClient initialized with base_url: {self.base_url}")
    
    async def authenticate(self) -> bool:
        """Authenticate with MiMiMON platform."""
        if not self.api_key:
            if self.debug:
                console.print("[debug]No API key provided, using demo mode")
            return True
        
        try:
            response = await self._http_client.post(
                f"{self.base_url}/auth/verify",
                headers={"Authorization": f"Bearer {self.api_key}"}
            )
            return response.status_code == 200
        except Exception as e:
            if self.debug:
                console.print(f"[debug]Authentication failed: {e}")
            return False
    
    async def start_monitoring_session(
        self, 
        agent: str = "claude",
        track_git: bool = False
    ) -> str:
        """Start a new agent monitoring session."""
        session_id = f"session_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        session = AgentSession(
            agent_id=session_id,
            agent_type=agent,
            metadata={
                "track_git": track_git,
                "platform": "cli"
            }
        )
        
        self.sessions[session_id] = session
        
        console.print(f"[green]✓[/green] Started monitoring session: {session_id}")
        console.print(f"[blue]ℹ[/blue] Agent type: {agent}")
        
        # Simulate monitoring
        console.print("[cyan]📡[/cyan] Monitoring agent activity...")
        console.print("[cyan]🔄[/cyan] Session active. Press Ctrl+C to stop.")
        
        try:
            # Keep session alive
            while True:
                await asyncio.sleep(1)
        except KeyboardInterrupt:
            self.stop_session(session_id)
            
        return session_id
    
    def stop_session(self, session_id: str) -> bool:
        """Stop an active monitoring session."""
        if session_id in self.sessions:
            self.sessions[session_id].status = "stopped"
            console.print(f"[yellow]⚠[/yellow] Stopped session: {session_id}")
            return True
        return False
    
    async def send_message(
        self, 
        session_id: str, 
        message: str,
        message_type: str = "user"
    ) -> Dict[str, Any]:
        """Send a message to an agent session."""
        if session_id not in self.sessions:
            raise ValueError(f"Session {session_id} not found")
        
        message_data = {
            "session_id": session_id,
            "message": message,
            "type": message_type,
            "timestamp": datetime.now().isoformat()
        }
        
        if self.debug:
            console.print(f"[debug]Sending message: {message_data}")
        
        return message_data
    
    async def get_session_history(self, session_id: str) -> List[Dict[str, Any]]:
        """Get the message history for a session."""
        # Placeholder implementation
        return [
            {
                "timestamp": datetime.now().isoformat(),
                "type": "system",
                "message": f"Session {session_id} started"
            }
        ]
    
    def list_sessions(self) -> List[AgentSession]:
        """List all active sessions."""
        return list(self.sessions.values())
    
    async def connect_websocket(self, on_message: Optional[Callable] = None):
        """Connect to MiMiMON WebSocket for real-time updates."""
        ws_url = self.base_url.replace("https://", "wss://").replace("http://", "ws://")
        ws_url += "/ws"
        
        try:
            self._websocket = await websockets.connect(ws_url)
            console.print("[green]✓[/green] WebSocket connected")
            
            if on_message:
                async for message in self._websocket:
                    await on_message(json.loads(message))
                    
        except Exception as e:
            if self.debug:
                console.print(f"[debug]WebSocket connection failed: {e}")
    
    async def close(self):
        """Clean up client resources."""
        if self._websocket:
            await self._websocket.close()
        await self._http_client.aclose()
    
    def __del__(self):
        """Ensure cleanup on deletion."""
        try:
            # Try to close gracefully if event loop exists
            import asyncio
            try:
                loop = asyncio.get_running_loop()
                loop.create_task(self.close())
            except RuntimeError:
                # No running loop, create new one
                asyncio.run(self.close())
        except:
            pass