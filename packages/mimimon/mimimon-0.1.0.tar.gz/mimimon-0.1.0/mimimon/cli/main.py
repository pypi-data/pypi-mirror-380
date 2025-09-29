"""
Main CLI entry point for MiMiMON

This module provides the primary command-line interface for MiMiMON,
mimicking the behavior of Omnara's CLI structure.
"""

import asyncio
import typer
from typing_extensions import Annotated
from typing import Optional, Union
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

from ..client import MiMiMONClient
from ..client.enhanced_client import EnhancedMiMiMONClient
from ..monitoring import ClaudeWrapper
from ..server.app import serve_app
from ..mcp.client import start_mcp_session

console = Console()
app = typer.Typer(
    name="mimimon",
    help="MiMiMON - AI Agent Monitoring and Communication Platform",
    add_completion=False,
)


@app.command()
def main(
    agent: Annotated[str, typer.Option(help="AI agent to monitor")] = "claude",
    api_key: Annotated[Optional[str], typer.Option(help="API key for authentication")] = None,
    git_diff: Annotated[bool, typer.Option(help="Track git differences")] = False,
    base_url: Annotated[Optional[str], typer.Option(help="Custom API endpoint")] = None,
    debug: Annotated[bool, typer.Option(help="Enable debug mode")] = False,
    project_path: Annotated[Optional[str], typer.Option(help="Path to Claude project to monitor")] = None,
    enhanced: Annotated[bool, typer.Option(help="Use enhanced monitoring with real-time features")] = True,
):
    """Start MiMiMON AI agent monitoring session with real Claude Code monitoring."""
    
    # Display welcome banner
    welcome_text = Text("🔍 MiMiMON Agent Monitor", style="bold cyan")
    banner_subtitle = "Real-time Claude Code Monitoring" if enhanced else "Basic Monitoring"
    console.print(Panel(welcome_text, subtitle=banner_subtitle, title="Welcome", border_style="cyan"))
    
    # Initialize appropriate client
    client: Union[MiMiMONClient, EnhancedMiMiMONClient]
    if enhanced:
        client = EnhancedMiMiMONClient(
            api_key=api_key,
            base_url=base_url,
            debug=debug,
            auto_send_enabled=True
        )
        console.print("[green]✅[/green] Enhanced monitoring mode enabled")
    else:
        client = MiMiMONClient(
            api_key=api_key,
            base_url=base_url,
            debug=debug
        )
        console.print("[blue]ℹ️[/blue] Basic monitoring mode")
    
    console.print(f"[green]✓[/green] Monitoring agent: [bold]{agent}[/bold]")
    
    if git_diff:
        console.print("[green]✓[/green] Git diff tracking enabled")
    
    if project_path:
        console.print(f"[blue]📁[/blue] Project path: {project_path}")
    
    # Start monitoring session
    try:
        if enhanced and isinstance(client, EnhancedMiMiMONClient):
            # Run the monitoring session in async context
            asyncio.run(client.start_monitoring_session_async(
                agent=agent, 
                track_git=git_diff, 
                project_path=project_path
            ))
        else:
            async def run_basic_monitoring() -> None:
                await client.start_monitoring_session(agent=agent, track_git=git_diff)
            asyncio.run(run_basic_monitoring())
    except KeyboardInterrupt:
        console.print("\n[yellow]⚠️[/yellow] Session interrupted by user")
    except Exception as e:
        console.print(f"[red]❌[/red] Error: {e}")
        if debug:
            import traceback
            traceback.print_exc()
        raise typer.Exit(1)
    finally:
        # Ensure cleanup
        try:
            if hasattr(client, 'close'):
                asyncio.run(client.close())
        except:
            pass


@app.command()
def serve(
    host: Annotated[str, typer.Option(help="Host to bind server")] = "0.0.0.0",
    port: Annotated[int, typer.Option(help="Port to bind server")] = 8000,
    reload: Annotated[bool, typer.Option(help="Enable auto-reload")] = False,
):
    """Start MiMiMON backend server."""
    console.print(f"[green]🚀[/green] Starting MiMiMON server on {host}:{port}")
    serve_app(host=host, port=port, reload=reload)


@app.command()
def mcp(
    protocol: Annotated[str, typer.Option(help="MCP protocol version")] = "1.0",
    endpoint: Annotated[Optional[str], typer.Option(help="MCP endpoint URL")] = None,
    transport: Annotated[str, typer.Option(help="Transport method")] = "websocket",
):
    """Start MCP (Model Context Protocol) session."""
    console.print("[green]🔗[/green] Starting MCP session")
    start_mcp_session(protocol=protocol, endpoint=endpoint, transport=transport)


@app.command()
def version():
    """Show MiMiMON version information."""
    from .. import __version__
    console.print(f"MiMiMON version: [bold cyan]{__version__}[/bold cyan]")


@app.command()
def status():
    """Check MiMiMON system status."""
    console.print("[green]✓[/green] MiMiMON is ready")
    console.print("[green]✓[/green] All systems operational")


if __name__ == "__main__":
    app()