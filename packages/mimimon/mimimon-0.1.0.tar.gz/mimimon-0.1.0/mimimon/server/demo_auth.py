"""
Demo Authentication Module for Testing

Provides in-memory user storage and authentication for testing purposes
when the database is not available.
"""

from datetime import datetime, timedelta
from typing import Dict, Optional
from .config import settings
from .auth import auth_manager

# In-memory demo users
DEMO_USERS = {
    "demo": {
        "id": 1,
        "username": "demo",
        "email": "demo@mimimon.ai",
        "full_name": "Demo User",
        "password_hash": "demo123",  # In production, this would be hashed
        "is_active": True,
        "created_at": datetime.now().isoformat()
    }
}

def authenticate_demo_user(username: str, password: str) -> Optional[Dict]:
    """Authenticate a demo user."""
    user = DEMO_USERS.get(username)
    if user and user["password_hash"] == password:
        # Return user without password
        return {k: v for k, v in user.items() if k != "password_hash"}
    return None

def create_demo_token(user: Dict) -> Dict:
    """Create a JWT token for demo user using existing auth manager."""
    payload = {
        "sub": str(user["id"]),
        "username": user["username"],
        "user_id": user["id"]
    }
    
    token = auth_manager.create_access_token(payload)
    
    return {
        "access_token": token,
        "token_type": "bearer",
        "expires_in": settings.auth.access_token_expire_minutes * 60,
        "user": user
    }

def verify_demo_token(token: str) -> Optional[Dict]:
    """Verify a demo JWT token using existing auth manager."""
    try:
        payload = auth_manager.verify_token(token)
        if payload:
            username = payload.get("username")
            if username and username in DEMO_USERS:
                user = DEMO_USERS[username]
                return {k: v for k, v in user.items() if k != "password_hash"}
        return None
    except Exception:
        return None