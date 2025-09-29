"""
MiMiMON CLI Entry Point

Enables running MiMiMON via `python -m mimimon` command.
"""

from .cli.main import app

if __name__ == "__main__":
    app()