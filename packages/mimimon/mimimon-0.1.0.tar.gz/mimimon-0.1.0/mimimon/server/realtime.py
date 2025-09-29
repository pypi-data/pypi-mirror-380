"""
Real-time Communication Features

Implements WebSocket connections and Server-Sent Events for real-time updates.
"""

import json
import asyncio
from typing import Dict, List, Set, Any, Optional
from datetime import datetime
from fastapi import WebSocket, WebSocketDisconnect
from starlette.responses import StreamingResponse
import logging

from .config import settings

logger = logging.getLogger(__name__)


class ConnectionManager:
    """Manages WebSocket connections for real-time communication."""
    
    def __init__(self):
        # Store active connections by user ID
        self.active_connections: Dict[int, Set[WebSocket]] = {}
        # Store session subscriptions
        self.session_subscriptions: Dict[str, Set[WebSocket]] = {}
        
    async def connect(self, websocket: WebSocket, user_id: int):
        """Accept a WebSocket connection and associate it with a user."""
        await websocket.accept()
        
        if user_id not in self.active_connections:
            self.active_connections[user_id] = set()
        
        self.active_connections[user_id].add(websocket)
        logger.info(f"User {user_id} connected via WebSocket")
        
        # Send welcome message
        await self.send_personal_message({
            "type": "connection",
            "message": "Connected to MiMiMON real-time updates",
            "timestamp": datetime.now().isoformat(),
            "user_id": user_id
        }, websocket)
    
    def disconnect(self, websocket: WebSocket, user_id: int):
        """Remove a WebSocket connection."""
        if user_id in self.active_connections:
            self.active_connections[user_id].discard(websocket)
            if not self.active_connections[user_id]:
                del self.active_connections[user_id]
        
        # Remove from session subscriptions
        for session_id in list(self.session_subscriptions.keys()):
            self.session_subscriptions[session_id].discard(websocket)
            if not self.session_subscriptions[session_id]:
                del self.session_subscriptions[session_id]
        
        logger.info(f"User {user_id} disconnected from WebSocket")
    
    async def send_personal_message(self, message: dict, websocket: WebSocket):
        """Send a message to a specific WebSocket connection."""
        try:
            await websocket.send_text(json.dumps(message))
        except Exception as e:
            logger.error(f"Error sending message to WebSocket: {e}")
    
    async def send_user_message(self, message: dict, user_id: int):
        """Send a message to all connections for a specific user."""
        if user_id not in self.active_connections:
            return
        
        message_str = json.dumps(message)
        dead_connections = set()
        
        for websocket in self.active_connections[user_id].copy():
            try:
                await websocket.send_text(message_str)
            except Exception as e:
                logger.error(f"Error sending message to user {user_id}: {e}")
                dead_connections.add(websocket)
        
        # Clean up dead connections
        for websocket in dead_connections:
            self.active_connections[user_id].discard(websocket)
    
    async def subscribe_to_session(self, websocket: WebSocket, session_id: str):
        """Subscribe a WebSocket to session updates."""
        if session_id not in self.session_subscriptions:
            self.session_subscriptions[session_id] = set()
        
        self.session_subscriptions[session_id].add(websocket)
        
        # Send confirmation
        await self.send_personal_message({
            "type": "subscription",
            "message": f"Subscribed to session {session_id}",
            "session_id": session_id,
            "timestamp": datetime.now().isoformat()
        }, websocket)
    
    async def unsubscribe_from_session(self, websocket: WebSocket, session_id: str):
        """Unsubscribe a WebSocket from session updates."""
        if session_id in self.session_subscriptions:
            self.session_subscriptions[session_id].discard(websocket)
            if not self.session_subscriptions[session_id]:
                del self.session_subscriptions[session_id]
    
    async def broadcast_session_update(self, session_id: str, message: dict):
        """Broadcast a message to all subscribers of a session."""
        if session_id not in self.session_subscriptions:
            return
        
        message_str = json.dumps({
            **message,
            "session_id": session_id,
            "timestamp": datetime.now().isoformat()
        })
        
        dead_connections = set()
        
        for websocket in self.session_subscriptions[session_id].copy():
            try:
                await websocket.send_text(message_str)
            except Exception as e:
                logger.error(f"Error broadcasting to session {session_id}: {e}")
                dead_connections.add(websocket)
        
        # Clean up dead connections
        for websocket in dead_connections:
            self.session_subscriptions[session_id].discard(websocket)
    
    async def broadcast_to_all(self, message: dict):
        """Broadcast a message to all connected users."""
        message_str = json.dumps({
            **message,
            "timestamp": datetime.now().isoformat()
        })
        
        for user_id, connections in self.active_connections.items():
            dead_connections = set()
            
            for websocket in connections.copy():
                try:
                    await websocket.send_text(message_str)
                except Exception as e:
                    logger.error(f"Error broadcasting to user {user_id}: {e}")
                    dead_connections.add(websocket)
            
            # Clean up dead connections
            for websocket in dead_connections:
                connections.discard(websocket)
    
    def get_stats(self) -> dict:
        """Get connection statistics."""
        return {
            "total_users": len(self.active_connections),
            "total_connections": sum(len(connections) for connections in self.active_connections.values()),
            "active_sessions": len(self.session_subscriptions),
            "session_subscriptions": {
                session_id: len(connections) 
                for session_id, connections in self.session_subscriptions.items()
            }
        }


# Global connection manager instance
connection_manager = ConnectionManager()


class SSEManager:
    """Manages Server-Sent Events for real-time updates."""
    
    def __init__(self):
        self.active_streams: Dict[str, Set[asyncio.Queue]] = {}
    
    async def create_event_stream(self, user_id: int, session_id: Optional[str] = None):
        """Create an SSE event stream for a user."""
        stream_id = f"user_{user_id}"
        if session_id:
            stream_id += f"_session_{session_id}"
        
        if stream_id not in self.active_streams:
            self.active_streams[stream_id] = set()
        
        queue = asyncio.Queue()
        self.active_streams[stream_id].add(queue)
        
        # Send initial connection event
        await queue.put({
            "event": "connection",
            "data": json.dumps({
                "message": "Connected to MiMiMON SSE stream",
                "user_id": user_id,
                "session_id": session_id,
                "timestamp": datetime.now().isoformat()
            })
        })
        
        try:
            while True:
                # Wait for new events
                event = await queue.get()
                
                # Format as SSE
                sse_data = f"event: {event.get('event', 'message')}\n"
                sse_data += f"data: {event.get('data', '')}\n\n"
                
                yield sse_data
                
                # Send heartbeat every 30 seconds
                if event.get("event") == "heartbeat":
                    continue
                    
        except asyncio.CancelledError:
            # Clean up when stream is closed
            if stream_id in self.active_streams:
                self.active_streams[stream_id].discard(queue)
                if not self.active_streams[stream_id]:
                    del self.active_streams[stream_id]
            raise
    
    async def send_event(self, user_id: int, event_type: str, data: dict, session_id: Optional[str] = None):
        """Send an event to a user's SSE stream."""
        stream_id = f"user_{user_id}"
        if session_id:
            stream_id += f"_session_{session_id}"
        
        if stream_id not in self.active_streams:
            return
        
        event = {
            "event": event_type,
            "data": json.dumps({
                **data,
                "timestamp": datetime.now().isoformat()
            })
        }
        
        # Send to all queues for this stream
        dead_queues = set()
        for queue in self.active_streams[stream_id].copy():
            try:
                await queue.put(event)
            except Exception as e:
                logger.error(f"Error sending SSE event: {e}")
                dead_queues.add(queue)
        
        # Clean up dead queues
        for queue in dead_queues:
            self.active_streams[stream_id].discard(queue)
    
    async def heartbeat_task(self):
        """Send periodic heartbeat events to keep connections alive."""
        while True:
            await asyncio.sleep(settings.sse_heartbeat_interval)
            
            for stream_id in list(self.active_streams.keys()):
                heartbeat_event = {
                    "event": "heartbeat",
                    "data": json.dumps({
                        "timestamp": datetime.now().isoformat()
                    })
                }
                
                dead_queues = set()
                for queue in self.active_streams[stream_id].copy():
                    try:
                        await queue.put(heartbeat_event)
                    except Exception:
                        dead_queues.add(queue)
                
                # Clean up dead queues
                for queue in dead_queues:
                    self.active_streams[stream_id].discard(queue)


# Global SSE manager instance
sse_manager = SSEManager()


# Helper functions for broadcasting events
async def notify_message_created(session_id: str, message: dict, user_id: int):
    """Notify about a new message in a session."""
    # WebSocket notification
    await connection_manager.broadcast_session_update(session_id, {
        "type": "message_created",
        "message": message
    })
    
    # SSE notification
    await sse_manager.send_event(user_id, "message_created", {
        "message": message
    }, session_id)


async def notify_session_status_changed(session_id: str, status: str, user_id: int):
    """Notify about session status change."""
    # WebSocket notification
    await connection_manager.broadcast_session_update(session_id, {
        "type": "session_status_changed",
        "status": status
    })
    
    # SSE notification
    await sse_manager.send_event(user_id, "session_status_changed", {
        "session_id": session_id,
        "status": status
    })


async def notify_agent_activity(session_id: str, activity: dict, user_id: int):
    """Notify about agent activity."""
    # WebSocket notification
    await connection_manager.broadcast_session_update(session_id, {
        "type": "agent_activity",
        "activity": activity
    })
    
    # SSE notification
    await sse_manager.send_event(user_id, "agent_activity", {
        "session_id": session_id,
        "activity": activity
    })