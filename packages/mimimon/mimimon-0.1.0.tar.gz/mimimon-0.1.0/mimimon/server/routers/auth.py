"""
Authentication API Routes

Handles user authentication, registration, and token management.
"""

from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel, validator
from typing import Optional
import re

from ..auth import auth_manager, get_current_user_from_token, AuthenticationError
from ..database import UserRepository
from ..demo_auth import authenticate_demo_user, create_demo_token, verify_demo_token

router = APIRouter(prefix="/auth", tags=["authentication"])
security = HTTPBearer()


class UserLogin(BaseModel):
    """User login request model."""
    username: str  # Can be username or email
    password: str


class UserRegister(BaseModel):
    """User registration request model."""
    username: str
    email: str
    password: str
    full_name: Optional[str] = None
    
    @validator('email')
    def validate_email(cls, v):
        """Simple email validation."""
        if not re.match(r'^[^@]+@[^@]+\.[^@]+$', v):
            raise ValueError('Invalid email format')
        return v


class TokenResponse(BaseModel):
    """Token response model."""
    access_token: str
    token_type: str
    expires_in: int
    user: dict


async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """Dependency to get current authenticated user."""
    token = credentials.credentials
    
    # Try demo authentication first
    demo_user = verify_demo_token(token)
    if demo_user:
        return demo_user
    
    # Fall back to regular authentication
    try:
        user = await get_current_user_from_token(token)
        if user:
            return user
    except Exception:
        pass
    
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid authentication credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )


@router.post("/login", response_model=TokenResponse)
async def login(user_data: UserLogin):
    """Authenticate user and return access token."""
    # Try demo authentication first
    demo_user = authenticate_demo_user(user_data.username, user_data.password)
    if demo_user:
        return create_demo_token(demo_user)
    
    # Fall back to regular authentication if available
    try:
        user = await auth_manager.authenticate_user(user_data.username, user_data.password)
        if user:
            return auth_manager.create_token_response(user)
    except Exception:
        pass
    
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect username or password",
        headers={"WWW-Authenticate": "Bearer"},
    )


@router.post("/register", response_model=TokenResponse)
async def register(user_data: UserRegister):
    """Register a new user."""
    try:
        user = await auth_manager.create_user(
            username=user_data.username,
            email=user_data.email,
            password=user_data.password,
            full_name=user_data.full_name
        )
        
        if not user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Failed to create user"
            )
        
        return auth_manager.create_token_response(user)
        
    except AuthenticationError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )


@router.get("/me")
async def get_current_user_info(current_user: dict = Depends(get_current_user)):
    """Get current user information."""
    return {
        "user": current_user,
        "message": "User authenticated successfully"
    }


@router.post("/demo-login", response_model=TokenResponse)
async def demo_login(user_data: UserLogin):
    """Demo login endpoint (redirects to main login)."""
    return await login(user_data)


@router.post("/refresh")
async def refresh_token(current_user: dict = Depends(get_current_user)):
    """Refresh access token."""
    return auth_manager.create_token_response(current_user)