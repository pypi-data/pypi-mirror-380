"""
Authentication System for MiMiMON Server

Implements JWT-based authentication with user management.
"""

import hashlib
import hmac
import base64
import json
from typing import Optional, Dict, Any
from datetime import datetime, timedelta, timezone

from .config import settings
from .database import UserRepository


class AuthenticationError(Exception):
    """Authentication-related errors."""
    pass


class AuthManager:
    """Manages authentication and JWT tokens."""
    
    def __init__(self):
        self.secret_key = settings.auth.secret_key
        self.algorithm = settings.auth.algorithm
        self.access_token_expire_minutes = settings.auth.access_token_expire_minutes
    
    def hash_password(self, password: str) -> str:
        """Hash a password using HMAC-SHA256."""
        return base64.b64encode(
            hmac.new(
                self.secret_key.encode(), 
                password.encode(), 
                hashlib.sha256
            ).digest()
        ).decode()
    
    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        """Verify a password against its hash."""
        expected_hash = self.hash_password(plain_password)
        return hmac.compare_digest(expected_hash, hashed_password)
    
    def create_access_token(self, data: Dict[str, Any], expires_delta: Optional[timedelta] = None) -> str:
        """Create a JWT access token."""
        to_encode = data.copy()
        
        if expires_delta:
            expire = datetime.now(timezone.utc) + expires_delta
        else:
            expire = datetime.now(timezone.utc) + timedelta(minutes=self.access_token_expire_minutes)
        
        to_encode.update({"exp": expire.timestamp(), "iat": datetime.now(timezone.utc).timestamp()})
        
        # Simple JWT implementation without external dependencies
        header = base64.urlsafe_b64encode(
            json.dumps({"alg": self.algorithm, "typ": "JWT"}).encode()
        ).decode().rstrip("=")
        
        payload = base64.urlsafe_b64encode(
            json.dumps(to_encode).encode()
        ).decode().rstrip("=")
        
        signature = base64.urlsafe_b64encode(
            hmac.new(
                self.secret_key.encode(),
                f"{header}.{payload}".encode(),
                hashlib.sha256
            ).digest()
        ).decode().rstrip("=")
        
        return f"{header}.{payload}.{signature}"
    
    def verify_token(self, token: str) -> Optional[Dict[str, Any]]:
        """Verify and decode a JWT token."""
        try:
            parts = token.split(".")
            if len(parts) != 3:
                return None
            
            header, payload, signature = parts
            
            # Verify signature
            expected_signature = base64.urlsafe_b64encode(
                hmac.new(
                    self.secret_key.encode(),
                    f"{header}.{payload}".encode(),
                    hashlib.sha256
                ).digest()
            ).decode().rstrip("=")
            
            if not hmac.compare_digest(signature, expected_signature):
                return None
            
            # Decode payload
            padded_payload = payload + "=" * (4 - len(payload) % 4)
            decoded_payload = json.loads(base64.urlsafe_b64decode(padded_payload))
            
            # Check expiration
            if decoded_payload.get("exp", 0) < datetime.now(timezone.utc).timestamp():
                return None
            
            return decoded_payload
            
        except Exception:
            return None
    
    async def authenticate_user(self, username: str, password: str) -> Optional[Dict[str, Any]]:
        """Authenticate a user with username/email and password."""
        # Try to find user by username or email
        user = await UserRepository.get_user_by_username(username)
        if not user:
            user = await UserRepository.get_user_by_email(username)
        
        if not user or not user.get("is_active"):
            return None
        
        if not self.verify_password(password, user["password_hash"]):
            return None
        
        # Remove password hash from returned user data
        user_data = user.copy()
        user_data.pop("password_hash", None)
        return user_data
    
    async def create_user(self, username: str, email: str, password: str, 
                         full_name: Optional[str] = None) -> Optional[Dict[str, Any]]:
        """Create a new user."""
        # Check if user already exists
        existing_user = await UserRepository.get_user_by_username(username)
        if existing_user:
            raise AuthenticationError("Username already exists")
        
        existing_email = await UserRepository.get_user_by_email(email)
        if existing_email:
            raise AuthenticationError("Email already exists")
        
        # Hash password and create user
        password_hash = self.hash_password(password)
        user = await UserRepository.create_user(username, email, password_hash, full_name)
        
        return user
    
    def create_token_response(self, user: Dict[str, Any]) -> Dict[str, Any]:
        """Create a token response for a user."""
        access_token = self.create_access_token(
            data={"sub": str(user["id"]), "username": user["username"], "email": user["email"]}
        )
        
        return {
            "access_token": access_token,
            "token_type": "bearer",
            "expires_in": self.access_token_expire_minutes * 60,
            "user": {
                "id": user["id"],
                "username": user["username"],
                "email": user["email"],
                "full_name": user.get("full_name"),
                "is_active": user.get("is_active", True)
            }
        }


# Global auth manager instance
auth_manager = AuthManager()


async def get_current_user_from_token(token: str) -> Optional[Dict[str, Any]]:
    """Get current user from JWT token."""
    payload = auth_manager.verify_token(token)
    if not payload:
        return None
    
    user_id = payload.get("sub")
    if not user_id:
        return None
    
    try:
        user = await UserRepository.get_user_by_id(int(user_id))
        if user and user.get("is_active"):
            # Remove password hash
            user_data = user.copy()
            user_data.pop("password_hash", None)
            return user_data
    except Exception:
        pass
    
    return None