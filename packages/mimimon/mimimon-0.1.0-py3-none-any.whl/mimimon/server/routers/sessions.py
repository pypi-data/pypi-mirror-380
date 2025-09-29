"""
Session Management API Routes

Handles agent monitoring sessions, CRUD operations, and session lifecycle.
"""

from fastapi import APIRouter, HTTPException, Depends, status
from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime
import uuid

from ..database import SessionRepository, AgentRepository
from ..routers.auth import get_current_user

router = APIRouter(prefix="/sessions", tags=["sessions"])


class SessionCreate(BaseModel):
    """Session creation request model."""
    agent_type: str
    agent_id: Optional[int] = None
    metadata: Optional[Dict[str, Any]] = None


class SessionUpdate(BaseModel):
    """Session update request model."""
    status: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


class SessionResponse(BaseModel):
    """Session response model."""
    id: int
    session_id: str
    user_id: int
    agent_id: Optional[int]
    status: str
    metadata: Dict[str, Any]
    start_time: datetime
    end_time: Optional[datetime]
    last_activity: datetime
    username: Optional[str] = None
    agent_name: Optional[str] = None
    agent_type: Optional[str] = None


@router.post("/", response_model=SessionResponse)
async def create_session(
    session_data: SessionCreate,
    current_user: dict = Depends(get_current_user)
):
    """Create a new agent monitoring session."""
    
    # Get or create agent
    agent_id = session_data.agent_id
    if not agent_id:
        # Find existing agent of the requested type or create one
        agents = await AgentRepository.get_agents_by_type(session_data.agent_type)
        if agents:
            agent_id = agents[0]["id"]
        else:
            # Create default agent for this type
            agent = await AgentRepository.create_agent(
                name=f"Default {session_data.agent_type.title()} Agent",
                agent_type=session_data.agent_type,
                description=f"Default agent for {session_data.agent_type} monitoring",
                created_by=current_user["id"]
            )
            if agent:
                agent_id = agent["id"]
    
    if not agent_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Could not find or create agent"
        )
    
    # Generate unique session ID
    session_id = f"session_{uuid.uuid4().hex[:12]}"
    
    # Create session
    session = await SessionRepository.create_session(
        session_id=session_id,
        user_id=current_user["id"],
        agent_id=agent_id,
        metadata=session_data.metadata or {}
    )
    
    if not session:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create session"
        )
    
    # Get full session details
    full_session = await SessionRepository.get_session_by_id(session_id)
    return full_session


@router.get("/", response_model=List[SessionResponse])
async def list_sessions(
    status: Optional[str] = None,
    current_user: dict = Depends(get_current_user)
):
    """List user's sessions, optionally filtered by status."""
    if status == "active":
        sessions = await SessionRepository.get_active_sessions(current_user["id"])
    else:
        # For now, just get active sessions; can be extended later
        sessions = await SessionRepository.get_active_sessions(current_user["id"])
    
    return sessions


@router.get("/{session_id}", response_model=SessionResponse)
async def get_session(
    session_id: str,
    current_user: dict = Depends(get_current_user)
):
    """Get session details."""
    session = await SessionRepository.get_session_by_id(session_id)
    
    if not session:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Session not found"
        )
    
    # Check if user has access to this session
    if session["user_id"] != current_user["id"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied to this session"
        )
    
    return session


@router.put("/{session_id}", response_model=SessionResponse)
async def update_session(
    session_id: str,
    session_update: SessionUpdate,
    current_user: dict = Depends(get_current_user)
):
    """Update session details."""
    # Verify session exists and user has access
    session = await SessionRepository.get_session_by_id(session_id)
    if not session:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Session not found"
        )
    
    if session["user_id"] != current_user["id"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied to this session"
        )
    
    # Update status if provided
    if session_update.status:
        await SessionRepository.update_session_status(session_id, session_update.status)
    
    # Get updated session
    updated_session = await SessionRepository.get_session_by_id(session_id)
    return updated_session


@router.delete("/{session_id}")
async def stop_session(
    session_id: str,
    current_user: dict = Depends(get_current_user)
):
    """Stop/end a session."""
    # Verify session exists and user has access
    session = await SessionRepository.get_session_by_id(session_id)
    if not session:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Session not found"
        )
    
    if session["user_id"] != current_user["id"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied to this session"
        )
    
    # Update session status to stopped
    await SessionRepository.update_session_status(session_id, "stopped")
    
    return {
        "session_id": session_id,
        "status": "stopped",
        "message": "Session stopped successfully"
    }