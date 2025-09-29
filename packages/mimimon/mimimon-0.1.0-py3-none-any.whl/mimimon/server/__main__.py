"""
Server module main entry point.

Allows running the server using: python -m mimimon.server
"""

from .app import serve_app

if __name__ == "__main__":
    serve_app()