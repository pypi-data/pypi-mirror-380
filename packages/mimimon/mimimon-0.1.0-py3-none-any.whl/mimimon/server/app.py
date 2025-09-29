"""
MiMiMON Server Application

Enhanced FastAPI backend server with PostgreSQL database integration,
JWT authentication, real-time features, and comprehensive API endpoints.

This module provides backward compatibility while importing the enhanced server.
"""

# Import the enhanced application
from .main import app

# Import the serve function and update it to use the enhanced app
import uvicorn


def serve_app(host: str = "0.0.0.0", port: int = 8000, reload: bool = False):
    """Start the enhanced MiMiMON server."""
    uvicorn.run(
        "mimimon.server.main:app",
        host=host,
        port=port,
        reload=reload,
        log_level="info"
    )


# Export the enhanced app for backward compatibility
__all__ = ["app", "serve_app"]