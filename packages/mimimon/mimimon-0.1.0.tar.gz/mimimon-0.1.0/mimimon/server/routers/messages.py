"""
Message API Routes

Handles message operations, agent communication, and message history.
"""

from fastapi import APIRouter, HTTPException, Depends, status
from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime

from ..database import MessageRepository, SessionRepository
from ..routers.auth import get_current_user

router = APIRouter(prefix="/messages", tags=["messages"])


class MessageCreate(BaseModel):
    """Message creation request model."""
    session_id: str
    content: str
    message_type: str = "user"  # user, agent, system, error
    metadata: Optional[Dict[str, Any]] = None


class AgentMessageCreate(BaseModel):
    """Agent message creation request model for /api/v1/messages/agent endpoint."""
    session_id: str
    content: str
    metadata: Optional[Dict[str, Any]] = None


class MessageResponse(BaseModel):
    """Message response model."""
    id: int
    session_id: int
    message_type: str
    content: str
    metadata: Dict[str, Any]
    timestamp: datetime
    parent_message_id: Optional[int]
    is_edited: bool


@router.post("/", response_model=MessageResponse)
async def create_message(
    message_data: MessageCreate,
    current_user: dict = Depends(get_current_user)
):
    """Create a new message in a session."""
    
    # Verify session exists and user has access
    session = await SessionRepository.get_session_by_id(message_data.session_id)
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
    
    # Create message
    message = await MessageRepository.create_message(
        session_id=session["id"],  # Use internal session ID
        message_type=message_data.message_type,
        content=message_data.content,
        metadata=message_data.metadata or {}
    )
    
    if not message:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create message"
        )
    
    # Update session last activity
    await SessionRepository.update_session_status(message_data.session_id, session["status"])
    
    return message


@router.post("/agent", response_model=MessageResponse)
async def create_agent_message(
    message_data: AgentMessageCreate,
    current_user: dict = Depends(get_current_user)
):
    """Create a message from an agent (special endpoint for /api/v1/messages/agent)."""
    
    # Verify session exists and user has access
    session = await SessionRepository.get_session_by_id(message_data.session_id)
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
    
    # Create agent message
    message = await MessageRepository.create_message(
        session_id=session["id"],  # Use internal session ID
        message_type="agent",
        content=message_data.content,
        metadata=message_data.metadata or {}
    )
    
    if not message:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create agent message"
        )
    
    # Update session last activity
    await SessionRepository.update_session_status(message_data.session_id, session["status"])
    
    return message


@router.get("/session/{session_id}", response_model=List[MessageResponse])
async def get_session_messages(
    session_id: str,
    limit: int = 50,
    offset: int = 0,
    current_user: dict = Depends(get_current_user)
):
    """Get messages for a specific session."""
    
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
    
    # Get messages
    messages = await MessageRepository.get_session_messages(
        session_id=session["id"],  # Use internal session ID
        limit=limit,
        offset=offset
    )
    
    return messages


@router.get("/recent", response_model=List[MessageResponse])
async def get_recent_messages(
    limit: int = 100,
    current_user: dict = Depends(get_current_user)
):
    """Get recent messages across all user's sessions."""
    
    # Get recent messages
    messages = await MessageRepository.get_recent_messages(limit=limit)
    
    # Filter messages for current user's sessions only
    user_messages = [
        msg for msg in messages 
        if msg.get("user_id") == current_user["id"]
    ]
    
    return user_messages


@router.get("/{message_id}", response_model=MessageResponse)
async def get_message(
    message_id: int,
    current_user: dict = Depends(get_current_user)
):
    """Get a specific message by ID."""
    
    # This would require additional database queries to verify access
    # For now, return a simple implementation
    
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Individual message retrieval not yet implemented"
    )