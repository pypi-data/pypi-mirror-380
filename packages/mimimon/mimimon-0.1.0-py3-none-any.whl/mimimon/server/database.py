"""
Database Layer for MiMiMON Server

Provides database connection management and CRUD operations
without SQLAlchemy dependency.
"""

import os
import asyncio
import json
from typing import Dict, List, Optional, Any, Union, TYPE_CHECKING
from datetime import datetime, timezone
from contextlib import asynccontextmanager
import logging
from functools import wraps

# Type checking imports
if TYPE_CHECKING:
    import psycopg2
    import psycopg2.extras
    from psycopg2.pool import ThreadedConnectionPool

try:
    import psycopg2
    import psycopg2.extras
    from psycopg2.pool import ThreadedConnectionPool
    HAS_PSYCOPG2 = True
except ImportError:
    HAS_PSYCOPG2 = False
    # Define fallback types
    psycopg2 = None  # type: ignore
    ThreadedConnectionPool = None  # type: ignore

from .config import settings

logger = logging.getLogger(__name__)


class DatabaseManager:
    """Database connection and operations manager."""
    
    def __init__(self, database_url: str):
        self.database_url = database_url
        self.pool = None
        
    async def initialize(self):
        """Initialize database connection pool."""
        if not HAS_PSYCOPG2:
            logger.warning("psycopg2 not available, using fallback database operations")
            return
            
        try:
            # Create connection pool
            if ThreadedConnectionPool is not None:
                self.pool = ThreadedConnectionPool(
                    minconn=1,
                    maxconn=settings.database.pool_size,
                    dsn=self.database_url
                )
            logger.info("Database connection pool initialized")
        except Exception as e:
            logger.error(f"Failed to initialize database pool: {e}")
            raise
    
    @asynccontextmanager
    async def get_connection(self):
        """Get a database connection from the pool."""
        if not self.pool:
            raise RuntimeError("Database pool not initialized")
        
        conn = None
        try:
            conn = self.pool.getconn()
            yield conn
        finally:
            if conn:
                self.pool.putconn(conn)
    
    async def execute_query(self, query: str, params: Optional[tuple] = None) -> List[Dict[str, Any]]:
        """Execute a SELECT query and return results."""
        if not HAS_PSYCOPG2:
            # Fallback implementation without psycopg2
            logger.warning("Database operation attempted without psycopg2")
            return []
        
        def _execute_blocking_query():
            if not self.pool:
                raise RuntimeError("Database pool not initialized")
            
            conn = None
            try:
                conn = self.pool.getconn()
                if psycopg2 is not None:
                    with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
                        cursor.execute(query, params)
                        results = cursor.fetchall()
                        return [dict(row) for row in results]
                else:
                    return []
            finally:
                if conn:
                    self.pool.putconn(conn)
        
        # Run the blocking operation in a thread pool
        return await asyncio.to_thread(_execute_blocking_query)
    
    async def execute_command(self, query: str, params: Optional[tuple] = None) -> int:
        """Execute an INSERT, UPDATE, or DELETE query."""
        if not HAS_PSYCOPG2:
            logger.warning("Database operation attempted without psycopg2")
            return 0
        
        def _execute_blocking_command():
            if not self.pool:
                raise RuntimeError("Database pool not initialized")
            
            conn = None
            try:
                conn = self.pool.getconn()
                with conn.cursor() as cursor:
                    cursor.execute(query, params)
                    conn.commit()
                    return cursor.rowcount
            finally:
                if conn:
                    self.pool.putconn(conn)
        
        # Run the blocking operation in a thread pool
        return await asyncio.to_thread(_execute_blocking_command)
    
    async def execute_returning(self, query: str, params: Optional[tuple] = None) -> Optional[Dict[str, Any]]:
        """Execute an INSERT/UPDATE query with RETURNING clause."""
        if not HAS_PSYCOPG2:
            logger.warning("Database operation attempted without psycopg2")
            return None
        
        def _execute_blocking_returning():
            if not self.pool:
                raise RuntimeError("Database pool not initialized")
            
            conn = None
            try:
                conn = self.pool.getconn()
                if psycopg2 is not None:
                    with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
                        cursor.execute(query, params)
                        conn.commit()
                        result = cursor.fetchone()
                        return dict(result) if result else None
                else:
                    return None
            finally:
                if conn:
                    self.pool.putconn(conn)
        
        # Run the blocking operation in a thread pool
        return await asyncio.to_thread(_execute_blocking_returning)
    
    async def close(self):
        """Close the database connection pool."""
        if self.pool:
            self.pool.closeall()
            logger.info("Database connection pool closed")


# Global database manager instance
db_manager = DatabaseManager(settings.database.url)


class UserRepository:
    """Repository for user operations."""
    
    @staticmethod
    async def create_user(username: str, email: str, password_hash: str, 
                         full_name: Optional[str] = None) -> Optional[Dict[str, Any]]:
        """Create a new user."""
        query = """
        INSERT INTO users (username, email, password_hash, full_name)
        VALUES (%s, %s, %s, %s)
        RETURNING id, username, email, full_name, is_active, created_at
        """
        return await db_manager.execute_returning(query, (username, email, password_hash, full_name))
    
    @staticmethod
    async def get_user_by_id(user_id: int) -> Optional[Dict[str, Any]]:
        """Get user by ID."""
        query = "SELECT id, username, email, full_name, is_active, created_at FROM users WHERE id = %s"
        results = await db_manager.execute_query(query, (user_id,))
        return results[0] if results else None
    
    @staticmethod
    async def get_user_by_email(email: str) -> Optional[Dict[str, Any]]:
        """Get user by email."""
        query = "SELECT * FROM users WHERE email = %s"
        results = await db_manager.execute_query(query, (email,))
        return results[0] if results else None
    
    @staticmethod
    async def get_user_by_username(username: str) -> Optional[Dict[str, Any]]:
        """Get user by username."""
        query = "SELECT * FROM users WHERE username = %s"
        results = await db_manager.execute_query(query, (username,))
        return results[0] if results else None


class SessionRepository:
    """Repository for session operations."""
    
    @staticmethod
    async def create_session(session_id: str, user_id: int, agent_id: int, 
                           metadata: Optional[Dict[str, Any]] = None) -> Optional[Dict[str, Any]]:
        """Create a new session."""
        query = """
        INSERT INTO sessions (session_id, user_id, agent_id, metadata)
        VALUES (%s, %s, %s, %s)
        RETURNING id, session_id, user_id, agent_id, status, metadata, start_time
        """
        metadata_json = json.dumps(metadata or {})
        return await db_manager.execute_returning(query, (session_id, user_id, agent_id, metadata_json))
    
    @staticmethod
    async def get_session_by_id(session_id: str) -> Optional[Dict[str, Any]]:
        """Get session by session_id."""
        query = """
        SELECT s.*, u.username, a.name as agent_name, a.agent_type
        FROM sessions s
        LEFT JOIN users u ON s.user_id = u.id
        LEFT JOIN agents a ON s.agent_id = a.id
        WHERE s.session_id = %s
        """
        results = await db_manager.execute_query(query, (session_id,))
        return results[0] if results else None
    
    @staticmethod
    async def update_session_status(session_id: str, status: str) -> bool:
        """Update session status."""
        query = "UPDATE sessions SET status = %s, last_activity = CURRENT_TIMESTAMP WHERE session_id = %s"
        rows_affected = await db_manager.execute_command(query, (status, session_id))
        return rows_affected > 0
    
    @staticmethod
    async def get_active_sessions(user_id: Optional[int] = None) -> List[Dict[str, Any]]:
        """Get active sessions, optionally filtered by user."""
        if user_id:
            query = """
            SELECT s.*, u.username, a.name as agent_name, a.agent_type
            FROM sessions s
            LEFT JOIN users u ON s.user_id = u.id
            LEFT JOIN agents a ON s.agent_id = a.id
            WHERE s.status = 'active' AND s.user_id = %s
            ORDER BY s.last_activity DESC
            """
            return await db_manager.execute_query(query, (user_id,))
        else:
            query = """
            SELECT s.*, u.username, a.name as agent_name, a.agent_type
            FROM sessions s
            LEFT JOIN users u ON s.user_id = u.id
            LEFT JOIN agents a ON s.agent_id = a.id
            WHERE s.status = 'active'
            ORDER BY s.last_activity DESC
            """
            return await db_manager.execute_query(query)


class MessageRepository:
    """Repository for message operations."""
    
    @staticmethod
    async def create_message(session_id: int, message_type: str, content: str,
                           metadata: Optional[Dict[str, Any]] = None) -> Optional[Dict[str, Any]]:
        """Create a new message."""
        query = """
        INSERT INTO messages (session_id, message_type, content, metadata)
        VALUES (%s, %s, %s, %s)
        RETURNING id, session_id, message_type, content, metadata, timestamp
        """
        metadata_json = json.dumps(metadata or {})
        return await db_manager.execute_returning(query, (session_id, message_type, content, metadata_json))
    
    @staticmethod
    async def get_session_messages(session_id: int, limit: int = 50, offset: int = 0) -> List[Dict[str, Any]]:
        """Get messages for a session."""
        query = """
        SELECT * FROM messages 
        WHERE session_id = %s 
        ORDER BY timestamp DESC 
        LIMIT %s OFFSET %s
        """
        return await db_manager.execute_query(query, (session_id, limit, offset))
    
    @staticmethod
    async def get_recent_messages(limit: int = 100) -> List[Dict[str, Any]]:
        """Get recent messages across all sessions."""
        query = """
        SELECT m.*, s.session_id, s.user_id
        FROM messages m
        JOIN sessions s ON m.session_id = s.id
        ORDER BY m.timestamp DESC
        LIMIT %s
        """
        return await db_manager.execute_query(query, (limit,))


class AgentRepository:
    """Repository for agent operations."""
    
    @staticmethod
    async def create_agent(name: str, agent_type: str, description: Optional[str] = None,
                          config: Optional[Dict[str, Any]] = None, created_by: Optional[int] = None) -> Optional[Dict[str, Any]]:
        """Create a new agent."""
        query = """
        INSERT INTO agents (name, agent_type, description, config, created_by)
        VALUES (%s, %s, %s, %s, %s)
        RETURNING id, name, agent_type, description, config, is_active, created_at
        """
        config_json = json.dumps(config or {})
        return await db_manager.execute_returning(query, (name, agent_type, description, config_json, created_by))
    
    @staticmethod
    async def get_agent_by_id(agent_id: int) -> Optional[Dict[str, Any]]:
        """Get agent by ID."""
        query = "SELECT * FROM agents WHERE id = %s"
        results = await db_manager.execute_query(query, (agent_id,))
        return results[0] if results else None
    
    @staticmethod
    async def get_agents_by_type(agent_type: str) -> List[Dict[str, Any]]:
        """Get agents by type."""
        query = "SELECT * FROM agents WHERE agent_type = %s AND is_active = true ORDER BY created_at DESC"
        return await db_manager.execute_query(query, (agent_type,))
    
    @staticmethod
    async def get_all_agents() -> List[Dict[str, Any]]:
        """Get all active agents."""
        query = "SELECT * FROM agents WHERE is_active = true ORDER BY created_at DESC"
        return await db_manager.execute_query(query)