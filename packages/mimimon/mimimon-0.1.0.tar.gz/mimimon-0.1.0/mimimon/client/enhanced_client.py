"""
Enhanced MiMiMON Client

Enhanced client with real-time monitoring, error handling, and retry logic.
Integrates with Claude Code monitoring functionality.
"""

import asyncio
import json
import time
from typing import Dict, List, Optional, Any, Callable
from datetime import datetime
from pathlib import Path

import httpx
import websockets
from pydantic import BaseModel, Field
from rich.console import Console

from ..monitoring import ClaudeWrapper, SessionStatus

console = Console()


class AgentSession(BaseModel):
    """Represents an active agent monitoring session."""
    agent_id: str
    agent_type: str
    start_time: datetime = Field(default_factory=datetime.now)
    status: str = "active"
    metadata: Dict[str, Any] = Field(default_factory=dict)


class EnhancedMiMiMONClient:
    """
    Enhanced MiMiMON client with real-time monitoring capabilities.
    
    Features:
    - Real Claude Code monitoring via ClaudeWrapper
    - WebSocket communication with retry logic
    - Automatic message detection and API communication
    - Error handling and exponential backoff
    - Session management and tracking
    """
    
    def __init__(
        self, 
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
        debug: bool = False,
        max_retries: int = 3,
        retry_delay: float = 1.0,
        auto_send_enabled: bool = True
    ):
        self.api_key = api_key
        self.base_url = base_url or "https://api.mimimon.ai"
        self.debug = debug
        self.max_retries = max_retries
        self.retry_delay = retry_delay
        self.auto_send_enabled = auto_send_enabled
        
        # Session management
        self.sessions: Dict[str, AgentSession] = {}
        
        # Network components
        self._websocket = None
        self._http_client = httpx.AsyncClient(timeout=30.0)
        self._connected = False
        self._reconnect_attempts = 0
        self._message_queue = []
        
        # Claude monitoring
        self.claude_wrapper: Optional[ClaudeWrapper] = None
        self._monitoring_task = None
        
        if debug:
            console.print(f"[debug]Enhanced MiMiMON client initialized")
    
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
            
            if response.status_code == 200:
                console.print("[green]✅[/green] Authentication successful")
                return True
            else:
                console.print(f"[red]❌[/red] Authentication failed: {response.status_code}")
                return False
                
        except Exception as e:
            if self.debug:
                console.print(f"[debug]Authentication error: {e}")
            return False
    
    def start_monitoring_session(
        self, 
        agent: str = "claude",
        track_git: bool = False,
        project_path: Optional[str] = None
    ) -> str:
        """Start a new agent monitoring session with real Claude monitoring (legacy sync method)."""
        
        try:
            # Initialize Claude wrapper for real monitoring
            self.claude_wrapper = ClaudeWrapper(
                project_path=project_path,
                session_callback=self._on_claude_event,
                debug=self.debug
            )
            
            # Start monitoring
            if not self.claude_wrapper.start_monitoring():
                console.print("[red]❌[/red] Failed to start Claude monitoring")
                return ""
            
            if not self.claude_wrapper.current_session:
                console.print("[red]❌[/red] Failed to create monitoring session")
                return ""
            
            session_id = self.claude_wrapper.current_session.session_id
            
            # Create AgentSession for backward compatibility
            session = AgentSession(
                agent_id=session_id,
                agent_type=agent,
                metadata={
                    "track_git": track_git,
                    "platform": "cli",
                    "project_path": project_path,
                    "real_monitoring": True
                }
            )
            
            self.sessions[session_id] = session
            
            console.print(f"[green]✅[/green] Started real monitoring session: {session_id}")
            console.print(f"[blue]🤖[/blue] Agent type: {agent}")
            
            console.print("[cyan]📡[/cyan] Monitoring Claude Code activity...")
            console.print("[cyan]🔄[/cyan] Session active. Press Ctrl+C to stop.")
            
            try:
                # Keep session alive with real monitoring
                while self.claude_wrapper and self.claude_wrapper.is_active:
                    time.sleep(1)
            except KeyboardInterrupt:
                self.stop_session(session_id)
                
            return session_id
            
        except Exception as e:
            console.print(f"[red]❌[/red] Failed to start monitoring session: {e}")
            if self.debug:
                import traceback
                traceback.print_exc()
            return ""
    
    async def start_monitoring_session_async(
        self, 
        agent: str = "claude",
        track_git: bool = False,
        project_path: Optional[str] = None
    ) -> str:
        """Start a new agent monitoring session with real Claude monitoring (async version)."""
        
        try:
            # Initialize Claude wrapper for real monitoring
            self.claude_wrapper = ClaudeWrapper(
                project_path=project_path,
                session_callback=self._on_claude_event,
                debug=self.debug
            )
            
            # Start monitoring
            if not self.claude_wrapper.start_monitoring():
                console.print("[red]❌[/red] Failed to start Claude monitoring")
                return ""
            
            if not self.claude_wrapper.current_session:
                console.print("[red]❌[/red] Failed to create monitoring session")
                return ""
            
            session_id = self.claude_wrapper.current_session.session_id
            
            # Create AgentSession for backward compatibility
            session = AgentSession(
                agent_id=session_id,
                agent_type=agent,
                metadata={
                    "track_git": track_git,
                    "platform": "cli",
                    "project_path": project_path,
                    "real_monitoring": True
                }
            )
            
            self.sessions[session_id] = session
            
            console.print(f"[green]✅[/green] Started real monitoring session: {session_id}")
            console.print(f"[blue]🤖[/blue] Agent type: {agent}")
            
            # Start real-time communication in background
            self._monitoring_task = asyncio.create_task(
                self._start_realtime_communication(session_id)
            )
            
            console.print("[cyan]📡[/cyan] Monitoring Claude Code activity...")
            console.print("[cyan]🔄[/cyan] Session active. Press Ctrl+C to stop.")
            
            try:
                # Keep session alive with real monitoring
                while self.claude_wrapper and self.claude_wrapper.is_active:
                    await asyncio.sleep(1)  # Use async sleep
            except KeyboardInterrupt:
                self.stop_session(session_id)
                
            return session_id
            
        except Exception as e:
            console.print(f"[red]❌[/red] Failed to start monitoring session: {e}")
            if self.debug:
                import traceback
                traceback.print_exc()
            return ""
    
    def stop_session(self, session_id: str) -> bool:
        """Stop an active monitoring session."""
        if session_id in self.sessions:
            self.sessions[session_id].status = "stopped"
            
            # Stop Claude wrapper if active
            if self.claude_wrapper:
                self.claude_wrapper.stop_monitoring()
                self.claude_wrapper = None
            
            # Cancel monitoring task
            if self._monitoring_task:
                self._monitoring_task.cancel()
                self._monitoring_task = None
            
            console.print(f"[yellow]⏹️[/yellow] Stopped session: {session_id}")
            return True
        return False
    
    async def _start_realtime_communication(self, session_id: str):
        """Start real-time communication with backend."""
        try:
            # Authenticate first
            if not await self.authenticate():
                console.print("[yellow]⚠️[/yellow] Authentication failed, continuing in offline mode")
                return
            
            # Create session on backend
            await self._create_backend_session(session_id)
            
            # Connect WebSocket
            await self.connect_websocket_with_retry()
            
        except Exception as e:
            console.print(f"[red]❌[/red] Real-time communication error: {e}")
            if self.debug:
                import traceback
                traceback.print_exc()
    
    async def _create_backend_session(self, session_id: str) -> bool:
        """Create session on backend API."""
        session_data = {
            "agent_type": "claude",
            "metadata": {
                "session_id": session_id,
                "client_version": "1.0.0",
                "monitoring_type": "real_time",
                "auto_send_enabled": self.auto_send_enabled
            }
        }
        
        result = await self._api_call_with_retry("POST", "/sessions", json=session_data)
        if result:
            console.print("[green]✅[/green] Backend session created")
            return True
        return False
    
    async def _api_call_with_retry(
        self, 
        method: str, 
        endpoint: str, 
        **kwargs
    ) -> Optional[Dict[str, Any]]:
        """Make API call with retry logic and exponential backoff."""
        
        for attempt in range(self.max_retries):
            try:
                headers = kwargs.get("headers", {})
                if self.api_key:
                    headers["Authorization"] = f"Bearer {self.api_key}"
                kwargs["headers"] = headers
                
                response = await self._http_client.request(
                    method,
                    f"{self.base_url}{endpoint}",
                    **kwargs
                )
                
                if response.status_code < 400:
                    return response.json() if response.content else {}
                elif response.status_code == 401:
                    console.print("[red]❌[/red] Authentication failed")
                    return None
                elif response.status_code >= 500:
                    # Server error - retry
                    raise httpx.HTTPStatusError(
                        f"Server error: {response.status_code}",
                        request=response.request,
                        response=response
                    )
                else:
                    console.print(f"[yellow]⚠️[/yellow] API error {response.status_code}: {response.text}")
                    return None
                    
            except (httpx.ConnectError, httpx.TimeoutException, httpx.HTTPStatusError) as e:
                if self.debug:
                    console.print(f"[debug]API call attempt {attempt + 1} failed: {e}")
                
                if attempt < self.max_retries - 1:
                    delay = self.retry_delay * (2 ** attempt)  # Exponential backoff
                    console.print(f"[cyan]🔄[/cyan] Retrying in {delay:.1f}s...")
                    await asyncio.sleep(delay)
                else:
                    console.print(f"[red]❌[/red] API call failed after {self.max_retries} attempts: {e}")
                    
            except Exception as e:
                console.print(f"[red]❌[/red] Unexpected API error: {e}")
                break
        
        return None
    
    async def connect_websocket_with_retry(self, on_message: Optional[Callable] = None):
        """Connect to WebSocket with retry logic."""
        
        for attempt in range(self.max_retries):
            try:
                ws_url = self.base_url.replace("https://", "wss://").replace("http://", "ws://")
                ws_url += "/ws"
                
                if self.debug:
                    console.print(f"[debug]Connecting to WebSocket: {ws_url}")
                
                self._websocket = await websockets.connect(
                    ws_url,
                    ping_interval=30,
                    ping_timeout=10
                )
                
                self._connected = True
                self._reconnect_attempts = 0
                console.print("[green]✅[/green] WebSocket connected")
                
                # Start message handler
                asyncio.create_task(self._websocket_message_handler(on_message))
                
                # Send queued messages
                await self._send_queued_messages()
                
                return True
                
            except Exception as e:
                self._connected = False
                if self.debug:
                    console.print(f"[debug]WebSocket connection attempt {attempt + 1} failed: {e}")
                
                if attempt < self.max_retries - 1:
                    delay = self.retry_delay * (2 ** attempt)
                    await asyncio.sleep(delay)
                else:
                    console.print(f"[red]❌[/red] WebSocket connection failed after {self.max_retries} attempts")
        
        return False
    
    async def _websocket_message_handler(self, callback: Optional[Callable] = None):
        """Handle incoming WebSocket messages with reconnection."""
        try:
            if not self._websocket:
                console.print("[red]❌[/red] WebSocket not connected")
                return
            
            async for message in self._websocket:
                try:
                    data = json.loads(message)
                    
                    if callback:
                        await callback(data)
                    else:
                        await self._default_websocket_handler(data)
                        
                except json.JSONDecodeError as e:
                    console.print(f"[red]❌[/red] Invalid JSON received: {e}")
                    
        except websockets.exceptions.ConnectionClosed:
            self._connected = False
            console.print("[yellow]⚠️[/yellow] WebSocket connection closed")
            
            # Attempt reconnection
            if self._reconnect_attempts < self.max_retries:
                self._reconnect_attempts += 1
                console.print(f"[cyan]🔄[/cyan] Reconnecting... (attempt {self._reconnect_attempts})")
                await asyncio.sleep(self.retry_delay)
                await self.connect_websocket_with_retry()
        
        except Exception as e:
            self._connected = False
            console.print(f"[red]❌[/red] WebSocket handler error: {e}")
    
    async def _default_websocket_handler(self, data: Dict[str, Any]):
        """Default WebSocket message handler."""
        message_type = data.get("type")
        
        if message_type == "ping":
            await self._send_websocket_message({"type": "pong"})
        elif message_type == "session_update":
            if self.debug:
                console.print(f"[debug]Session update: {data}")
        elif message_type == "agent_response":
            content = data.get("content", "")
            console.print(f"[blue]📨[/blue] Remote response: {content[:100]}...")
        elif message_type == "user_message":
            # Handle incoming user message from remote
            content = data.get("content", "")
            console.print(f"[green]📥[/green] Remote message: {content}")
            await self._forward_to_claude(content)
    
    async def _forward_to_claude(self, message: str):
        """Forward a message to the Claude agent."""
        if self.claude_wrapper:
            success = self.claude_wrapper.send_message_to_agent(message)
            if success:
                console.print("[green]✅[/green] Message forwarded to Claude")
            else:
                console.print("[red]❌[/red] Failed to forward message to Claude")
    
    async def _send_websocket_message(self, message: Dict[str, Any]) -> bool:
        """Send message via WebSocket with error handling."""
        if not self._connected or not self._websocket:
            # Queue message for later
            self._message_queue.append(message)
            if self.debug:
                console.print("[debug]Message queued (WebSocket not connected)")
            return False
        
        try:
            await self._websocket.send(json.dumps(message))
            return True
        except Exception as e:
            console.print(f"[red]❌[/red] WebSocket send error: {e}")
            self._message_queue.append(message)  # Queue for retry
            return False
    
    async def _send_queued_messages(self):
        """Send queued messages after reconnection."""
        if self.debug and self._message_queue:
            console.print(f"[debug]Sending {len(self._message_queue)} queued messages")
        
        while self._message_queue and self._connected:
            message = self._message_queue.pop(0)
            success = await self._send_websocket_message(message)
            if not success:
                # Put message back at front of queue
                self._message_queue.insert(0, message)
                break
    
    def _on_claude_event(self, event_data: Dict[str, Any]):
        """Handle events from Claude wrapper."""
        event_type = event_data.get("type")
        session_id = event_data.get("session_id")
        
        if self.debug:
            console.print(f"[debug]Claude event: {event_type}")
        
        if event_type == "agent_question" and self.auto_send_enabled:
            # Automatically send notification to backend
            asyncio.create_task(self._send_agent_question(event_data))
        elif event_type == "agent_response":
            # Send agent response to backend
            asyncio.create_task(self._send_agent_response(event_data))
        elif event_type == "error":
            # Send error notification
            asyncio.create_task(self._send_error_notification(event_data))
    
    async def _send_agent_question(self, event_data: Dict[str, Any]):
        """Send agent question to backend API."""
        session_id = event_data.get("session_id")
        question = event_data.get("question")
        
        if not session_id or not question:
            return
        
        message_data = {
            "session_id": session_id,
            "content": question,
            "type": "agent_question",
            "timestamp": event_data.get("timestamp", datetime.now().isoformat()),
            "metadata": event_data.get("metadata", {})
        }
        
        # Send via API
        result = await self._api_call_with_retry(
            "POST", 
            f"/sessions/{session_id}/messages",
            json=message_data
        )
        
        if result:
            console.print("[green]📤[/green] Agent question sent to backend")
        
        # Send via WebSocket for real-time updates
        await self._send_websocket_message({
            "type": "agent_question",
            "data": message_data
        })
    
    async def _send_agent_response(self, event_data: Dict[str, Any]):
        """Send agent response to backend."""
        session_id = event_data.get("session_id")
        response = event_data.get("response")
        
        if not session_id or not response:
            return
        
        message_data = {
            "session_id": session_id,
            "content": response,
            "type": "agent_response",
            "timestamp": event_data.get("timestamp", datetime.now().isoformat()),
            "metadata": event_data.get("metadata", {})
        }
        
        # Send via WebSocket for real-time updates
        await self._send_websocket_message({
            "type": "agent_response",
            "data": message_data
        })
    
    async def _send_error_notification(self, event_data: Dict[str, Any]):
        """Send error notification to backend."""
        session_id = event_data.get("session_id")
        error = event_data.get("error")
        
        if not session_id or not error:
            return
        
        message_data = {
            "session_id": session_id,
            "content": error,
            "type": "error",
            "timestamp": event_data.get("timestamp", datetime.now().isoformat()),
            "metadata": event_data.get("metadata", {})
        }
        
        # Send via WebSocket for real-time updates
        await self._send_websocket_message({
            "type": "error",
            "data": message_data
        })
    
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
        
        # Send via API
        result = await self._api_call_with_retry(
            "POST",
            f"/sessions/{session_id}/messages",
            json=message_data
        )
        
        # Send via WebSocket
        await self._send_websocket_message({
            "type": "user_message",
            "data": message_data
        })
        
        if self.debug:
            console.print(f"[debug]Message sent: {message[:50]}...")
        
        return message_data
    
    async def get_session_history(self, session_id: str) -> List[Dict[str, Any]]:
        """Get the message history for a session."""
        result = await self._api_call_with_retry("GET", f"/sessions/{session_id}/messages")
        
        if result:
            return result.get("messages", [])
        
        # Fallback to local history if available
        if self.claude_wrapper:
            recent_messages = self.claude_wrapper.get_recent_messages()
            return recent_messages
        
        return []
    
    def list_sessions(self) -> List[AgentSession]:
        """List all active sessions."""
        return list(self.sessions.values())
    
    def get_session_status(self) -> Optional[Dict[str, Any]]:
        """Get comprehensive session status."""
        if self.claude_wrapper:
            return self.claude_wrapper.get_session_status()
        return None
    
    async def close(self):
        """Clean up client resources."""
        console.print("[yellow]👋[/yellow] Shutting down MiMiMON client...")
        
        # Stop Claude wrapper
        if self.claude_wrapper:
            self.claude_wrapper.stop_monitoring()
            self.claude_wrapper = None
        
        # Cancel monitoring task
        if self._monitoring_task:
            self._monitoring_task.cancel()
            try:
                await self._monitoring_task
            except asyncio.CancelledError:
                pass
        
        # Close WebSocket
        if self._websocket:
            await self._websocket.close()
        
        # Close HTTP client
        await self._http_client.aclose()
        
        console.print("[green]✅[/green] MiMiMON client closed")
    
    def __del__(self):
        """Ensure cleanup on deletion."""
        try:
            asyncio.run(self.close())
        except:
            pass