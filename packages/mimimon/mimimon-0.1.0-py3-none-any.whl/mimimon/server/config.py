"""
Environment Configuration for MiMiMON Server

Manages environment variables and application settings using Pydantic.
"""

import os
from typing import Optional, List
from pydantic import BaseModel, Field


class DatabaseConfig(BaseModel):
    """Database configuration settings."""
    url: str = Field(default_factory=lambda: os.getenv("DATABASE_URL", "postgresql://localhost/mimimon"))
    echo: bool = Field(default=False)
    pool_size: int = Field(default=10)
    max_overflow: int = Field(default=20)


class AuthConfig(BaseModel):
    """Authentication configuration settings."""
    secret_key: str = Field(default_factory=lambda: os.getenv("SECRET_KEY", "your-secret-key-change-in-production"))
    algorithm: str = Field(default="HS256")
    access_token_expire_minutes: int = Field(default=30)
    refresh_token_expire_days: int = Field(default=7)
    

class ServerConfig(BaseModel):
    """Server configuration settings."""
    host: str = Field(default="0.0.0.0")
    port: int = Field(default=8000)
    debug: bool = Field(default=False)
    reload: bool = Field(default=False)
    cors_origins: List[str] = Field(default_factory=lambda: 
        os.getenv("CORS_ORIGINS", "http://localhost:3000,http://localhost:5000").split(",")
    )


class Settings(BaseModel):
    """Main application settings."""
    
    # Application metadata
    app_name: str = "MiMiMON API"
    app_version: str = "0.1.0"
    app_description: str = "AI Agent Monitoring and Communication Platform API"
    
    # Environment
    environment: str = Field(default_factory=lambda: os.getenv("ENVIRONMENT", "development"))
    
    # Configuration sections
    database: DatabaseConfig = Field(default_factory=DatabaseConfig)
    auth: AuthConfig = Field(default_factory=AuthConfig)
    server: ServerConfig = Field(default_factory=ServerConfig)
    
    # API configuration
    api_v1_prefix: str = "/api/v1"
    docs_url: str = "/docs"
    redoc_url: str = "/redoc"
    
    # Monitoring settings
    enable_metrics: bool = Field(default=True)
    log_level: str = Field(default_factory=lambda: os.getenv("LOG_LEVEL", "INFO"))
    
    # Real-time features
    max_websocket_connections: int = Field(default=100)
    sse_heartbeat_interval: int = Field(default=30)
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False


def get_settings() -> Settings:
    """Get application settings instance."""
    return Settings()


# Global settings instance
settings = get_settings()