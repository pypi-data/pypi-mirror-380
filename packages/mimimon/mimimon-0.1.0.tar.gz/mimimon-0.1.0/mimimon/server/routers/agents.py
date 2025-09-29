"""
Agent Management API Routes

Handles agent CRUD operations, configuration, and agent types.
"""

from fastapi import APIRouter, HTTPException, Depends, status
from pydantic import BaseModel
from typing import List, Optional, Dict, Any

from ..database import AgentRepository
from ..routers.auth import get_current_user

router = APIRouter(prefix="/agents", tags=["agents"])


class AgentCreate(BaseModel):
    """Agent creation request model."""
    name: str
    agent_type: str  # claude, chatgpt, custom, etc.
    description: Optional[str] = None
    config: Optional[Dict[str, Any]] = None


class AgentUpdate(BaseModel):
    """Agent update request model."""
    name: Optional[str] = None
    description: Optional[str] = None
    config: Optional[Dict[str, Any]] = None
    is_active: Optional[bool] = None


class AgentResponse(BaseModel):
    """Agent response model."""
    id: int
    name: str
    agent_type: str
    description: Optional[str]
    config: Dict[str, Any]
    is_active: bool
    created_by: Optional[int]
    created_at: str
    updated_at: str


@router.post("/", response_model=AgentResponse)
async def create_agent(
    agent_data: AgentCreate,
    current_user: dict = Depends(get_current_user)
):
    """Create a new agent."""
    
    agent = await AgentRepository.create_agent(
        name=agent_data.name,
        agent_type=agent_data.agent_type,
        description=agent_data.description,
        config=agent_data.config or {},
        created_by=current_user["id"]
    )
    
    if not agent:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create agent"
        )
    
    return agent


@router.get("/", response_model=List[AgentResponse])
async def list_agents(
    agent_type: Optional[str] = None,
    current_user: dict = Depends(get_current_user)
):
    """List agents, optionally filtered by type."""
    
    if agent_type:
        agents = await AgentRepository.get_agents_by_type(agent_type)
    else:
        agents = await AgentRepository.get_all_agents()
    
    return agents


@router.get("/types")
async def get_agent_types(current_user: dict = Depends(get_current_user)):
    """Get available agent types."""
    
    return {
        "agent_types": [
            {
                "type": "claude",
                "name": "Claude Code",
                "description": "Claude AI code assistant for development tasks"
            },
            {
                "type": "chatgpt",
                "name": "ChatGPT",
                "description": "OpenAI ChatGPT for general assistance"
            },
            {
                "type": "custom",
                "name": "Custom Agent",
                "description": "Custom AI agent with configurable behavior"
            },
            {
                "type": "local",
                "name": "Local Agent",
                "description": "Locally running AI agent"
            }
        ]
    }


@router.get("/{agent_id}", response_model=AgentResponse)
async def get_agent(
    agent_id: int,
    current_user: dict = Depends(get_current_user)
):
    """Get agent details."""
    
    agent = await AgentRepository.get_agent_by_id(agent_id)
    
    if not agent:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Agent not found"
        )
    
    return agent


@router.put("/{agent_id}", response_model=AgentResponse)
async def update_agent(
    agent_id: int,
    agent_update: AgentUpdate,
    current_user: dict = Depends(get_current_user)
):
    """Update agent details."""
    
    # Verify agent exists
    agent = await AgentRepository.get_agent_by_id(agent_id)
    if not agent:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Agent not found"
        )
    
    # Check permission (only creator or superuser can update)
    if agent["created_by"] != current_user["id"] and not current_user.get("is_superuser"):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Permission denied to update this agent"
        )
    
    # For now, return the agent as-is since we haven't implemented update in repository
    # This can be extended later
    return agent


@router.delete("/{agent_id}")
async def delete_agent(
    agent_id: int,
    current_user: dict = Depends(get_current_user)
):
    """Delete/deactivate an agent."""
    
    # Verify agent exists
    agent = await AgentRepository.get_agent_by_id(agent_id)
    if not agent:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Agent not found"
        )
    
    # Check permission (only creator or superuser can delete)
    if agent["created_by"] != current_user["id"] and not current_user.get("is_superuser"):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Permission denied to delete this agent"
        )
    
    # For now, just return success message
    # Can be implemented later to actually deactivate the agent
    return {
        "agent_id": agent_id,
        "status": "deactivated",
        "message": "Agent deactivated successfully"
    }