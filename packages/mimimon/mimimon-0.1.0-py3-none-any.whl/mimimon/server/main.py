"""
Enhanced MiMiMON Server Application

Complete FastAPI backend server with PostgreSQL database integration,
JWT authentication, real-time features, and comprehensive API endpoints.
"""

import asyncio
import logging
import json
from contextlib import asynccontextmanager
from typing import Dict, Any, Optional

from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Depends, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse
from pydantic import BaseModel, ValidationError, Field

from .config import settings
from .database import db_manager
from .realtime import connection_manager, sse_manager, SSEManager
from .routers import auth, sessions, messages, agents
from .routers.auth import get_current_user


# Pydantic models for WebSocket message validation
class WebSocketMessage(BaseModel):
    """Pydantic model for validating WebSocket messages."""
    type: str = Field(..., description="Message type")
    session_id: Optional[str] = Field(None, description="Session ID for session-related messages")
    content: Optional[str] = Field(None, description="Message content")
    metadata: Optional[Dict[str, Any]] = Field(default_factory=dict, description="Additional metadata")

# Configure logging
logging.basicConfig(level=getattr(logging, settings.log_level))
logger = logging.getLogger(__name__)


class LoggingMiddleware(BaseHTTPMiddleware):
    """Middleware to log requests and responses."""
    
    async def dispatch(self, request: Request, call_next):
        start_time = asyncio.get_event_loop().time()
        
        response = await call_next(request)
        
        process_time = asyncio.get_event_loop().time() - start_time
        logger.info(
            f"{request.method} {request.url.path} - "
            f"{response.status_code} - {process_time:.3f}s"
        )
        
        return response


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Manage application lifespan events."""
    # Startup
    logger.info("Starting MiMiMON server...")
    
    # Initialize background task variable
    heartbeat_task = None
    
    # Initialize database
    try:
        await db_manager.initialize()
        logger.info("Database initialized successfully")
    except Exception as e:
        logger.error(f"Database initialization failed: {e}")
    
    # Start SSE heartbeat task
    if settings.enable_metrics:
        heartbeat_task = asyncio.create_task(sse_manager.heartbeat_task())
        logger.info("SSE heartbeat task started")
    
    yield
    
    # Shutdown
    logger.info("Shutting down MiMiMON server...")
    
    # Close database connections
    await db_manager.close()
    
    # Cancel background tasks
    if heartbeat_task is not None:
        heartbeat_task.cancel()
    
    logger.info("Server shutdown complete")


# Create FastAPI application
app = FastAPI(
    title=settings.app_name,
    description=settings.app_description,
    version=settings.app_version,
    docs_url=settings.docs_url,
    redoc_url=settings.redoc_url,
    lifespan=lifespan
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.server.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add logging middleware
if settings.server.debug:
    app.add_middleware(LoggingMiddleware)

# Include API routers
app.include_router(auth.router, prefix=settings.api_v1_prefix)
app.include_router(sessions.router, prefix=settings.api_v1_prefix)
app.include_router(messages.router, prefix=settings.api_v1_prefix)
app.include_router(agents.router, prefix=settings.api_v1_prefix)


@app.get("/")
async def root():
    """Root endpoint with API information."""
    return {
        "service": settings.app_name,
        "version": settings.app_version,
        "description": settings.app_description,
        "status": "operational",
        "api_docs": settings.docs_url,
        "api_version": "v1",
        "features": [
            "JWT Authentication",
            "PostgreSQL Database",
            "Real-time WebSocket",
            "Server-Sent Events",
            "Session Management",
            "Agent Communication",
            "Message History"
        ]
    }


@app.get("/health")
async def health_check():
    """Health check endpoint with system status."""
    try:
        # Check database connectivity
        await db_manager.execute_query("SELECT 1")
        db_status = "healthy"
    except Exception as e:
        db_status = f"unhealthy: {str(e)}"
    
    # Get connection stats
    ws_stats = connection_manager.get_stats()
    
    return {
        "status": "healthy" if db_status == "healthy" else "degraded",
        "timestamp": asyncio.get_event_loop().time(),
        "database": db_status,
        "websocket_connections": ws_stats,
        "environment": settings.environment,
        "version": settings.app_version
    }


@app.get("/api/v1/stats")
async def get_system_stats(current_user: dict = Depends(get_current_user)):
    """Get system statistics (authenticated endpoint)."""
    
    # Get WebSocket connection stats
    ws_stats = connection_manager.get_stats()
    
    # Get database stats (example queries)
    try:
        user_count = await db_manager.execute_query("SELECT COUNT(*) as count FROM users")
        session_count = await db_manager.execute_query("SELECT COUNT(*) as count FROM sessions")
        message_count = await db_manager.execute_query("SELECT COUNT(*) as count FROM messages")
        agent_count = await db_manager.execute_query("SELECT COUNT(*) as count FROM agents")
        
        db_stats = {
            "users": user_count[0]["count"] if user_count else 0,
            "sessions": session_count[0]["count"] if session_count else 0,
            "messages": message_count[0]["count"] if message_count else 0,
            "agents": agent_count[0]["count"] if agent_count else 0
        }
    except Exception as e:
        db_stats = {"error": str(e)}
    
    return {
        "websocket": ws_stats,
        "database": db_stats,
        "system": {
            "environment": settings.environment,
            "debug_mode": settings.server.debug,
            "max_ws_connections": settings.max_websocket_connections
        }
    }


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    """WebSocket endpoint for real-time communication."""
    
    # Get user from query parameters (in production, use proper token validation)
    user_id = websocket.query_params.get("user_id")
    if not user_id:
        await websocket.close(code=4001, reason="Missing user_id parameter")
        return
    
    # Initialize user_id_int with default value
    user_id_int = 0
    
    try:
        user_id_int = int(user_id)
        await connection_manager.connect(websocket, user_id_int)
        
        while True:
            # Receive messages from client
            try:
                data = await websocket.receive_text()
                
                # Parse and validate WebSocket message safely
                try:
                    raw_message = json.loads(data) if data else {}
                    message = WebSocketMessage(**raw_message)
                except json.JSONDecodeError as e:
                    logger.error(f"Invalid JSON in WebSocket message: {e}")
                    await connection_manager.send_personal_message({
                        "type": "error",
                        "message": "Invalid JSON format",
                        "timestamp": asyncio.get_event_loop().time()
                    }, websocket)
                    continue
                except ValidationError as e:
                    logger.error(f"Invalid message format: {e}")
                    await connection_manager.send_personal_message({
                        "type": "error",
                        "message": "Invalid message format",
                        "errors": str(e),
                        "timestamp": asyncio.get_event_loop().time()
                    }, websocket)
                    continue
                
                # Handle different message types
                message_type = message.type
                
                if message_type == "subscribe_session":
                    session_id = message.session_id
                    if session_id:
                        await connection_manager.subscribe_to_session(websocket, session_id)
                
                elif message_type == "unsubscribe_session":
                    session_id = message.session_id
                    if session_id:
                        await connection_manager.unsubscribe_from_session(websocket, session_id)
                
                elif message_type == "ping":
                    # Respond to ping with pong
                    await connection_manager.send_personal_message({
                        "type": "pong",
                        "timestamp": asyncio.get_event_loop().time()
                    }, websocket)
                
                elif message_type == "echo":
                    # Echo the message back to sender for testing
                    await connection_manager.send_personal_message({
                        "type": "echo",
                        "original_message": message.dict(),
                        "timestamp": asyncio.get_event_loop().time()
                    }, websocket)
                
            except Exception as e:
                logger.error(f"Error processing WebSocket message: {e}")
                break
                
    except WebSocketDisconnect:
        logger.info(f"WebSocket disconnected for user {user_id}")
    except Exception as e:
        logger.error(f"WebSocket error for user {user_id}: {e}")
    finally:
        connection_manager.disconnect(websocket, user_id_int)


@app.get("/api/v1/events/stream")
async def sse_endpoint(request: Request, current_user: dict = Depends(get_current_user)):
    """Server-Sent Events endpoint for real-time updates."""
    
    user_id = current_user["id"]
    session_id = request.query_params.get("session_id")
    
    # Create event stream
    event_generator = sse_manager.create_event_stream(user_id, session_id)
    
    return StreamingResponse(
        event_generator,
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "Cache-Control"
        }
    )


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    """Global exception handler for better error responses."""
    logger.error(f"Unhandled exception: {exc}", exc_info=True)
    
    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal server error",
            "detail": str(exc) if settings.server.debug else "An unexpected error occurred",
            "timestamp": asyncio.get_event_loop().time()
        }
    )


# Additional API endpoints for specific MiMiMON functionality
@app.post("/api/v1/messages/agent")
async def agent_message_endpoint(
    message_data: dict,
    current_user: dict = Depends(get_current_user)
):
    """Special endpoint for agent communication (/api/v1/messages/agent)."""
    
    # This endpoint is specifically mentioned in the requirements
    # Route it to the messages router
    from .routers.messages import create_agent_message, AgentMessageCreate
    
    try:
        agent_message = AgentMessageCreate(**message_data)
        return await create_agent_message(agent_message, current_user)
    except Exception as e:
        logger.error(f"Error in agent message endpoint: {e}")
        return JSONResponse(
            status_code=400,
            content={"error": "Invalid message data", "detail": str(e)}
        )


if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(
        "mimimon.server.main:app",
        host=settings.server.host,
        port=settings.server.port,
        reload=settings.server.reload,
        log_level=settings.log_level.lower()
    )