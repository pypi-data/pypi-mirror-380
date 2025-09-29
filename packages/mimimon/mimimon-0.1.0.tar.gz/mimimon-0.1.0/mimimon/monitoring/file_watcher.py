"""
File Watcher for Claude Code Sessions

Monitors ~/.claude/projects/ directory for log changes and new sessions.
"""

import os
import time
import asyncio
from pathlib import Path
from typing import Dict, List, Optional, Callable, Any
from datetime import datetime
import json

try:
    from watchdog.observers import Observer
    from watchdog.events import FileSystemEventHandler
    WATCHDOG_AVAILABLE = True
except ImportError:
    print("Warning: watchdog not available. Using polling fallback.")
    Observer = None
    FileSystemEventHandler = object  # Use object as base class when watchdog unavailable
    WATCHDOG_AVAILABLE = False

from rich.console import Console

console = Console()


class ClaudeLogEventHandler(FileSystemEventHandler):
    """Handler for Claude Code log file events."""
    
    def __init__(self, callback: Callable[[str, str], None]):
        self.callback = callback
        self.last_modified = {}
        
    def on_modified(self, event):
        """Handle file modification events."""
        if event.is_directory:
            return
            
        # Only process .log files or specific Claude files
        if not (event.src_path.endswith('.log') or 
                event.src_path.endswith('.claude') or
                'session' in event.src_path.lower()):
            return
            
        # Debounce rapid file changes
        now = time.time()
        if event.src_path in self.last_modified:
            if now - self.last_modified[event.src_path] < 0.5:  # 500ms debounce
                return
                
        self.last_modified[event.src_path] = now
        
        try:
            self.callback(event.src_path, "modified")
        except Exception as e:
            console.print(f"[red]Error processing file change: {e}[/red]")
    
    def on_created(self, event):
        """Handle file creation events."""
        if not event.is_directory:
            try:
                self.callback(event.src_path, "created")
            except Exception as e:
                console.print(f"[red]Error processing file creation: {e}[/red]")


class ClaudeFileWatcher:
    """
    File watcher for Claude Code sessions.
    
    Monitors the ~/.claude/projects/ directory for changes and
    triggers callbacks when log files are modified or created.
    """
    
    def __init__(self, callback: Optional[Callable[[str, str], None]] = None):
        self.claude_dir = Path.home() / ".claude" / "projects"
        self.callback = callback or self._default_callback
        self.observer = None
        self.is_running = False
        self.watched_files: Dict[str, datetime] = {}
        
        # Ensure Claude directory exists
        self.claude_dir.mkdir(parents=True, exist_ok=True)
        
        console.print(f"[blue]📁[/blue] Watching Claude directory: {self.claude_dir}")
    
    def _default_callback(self, file_path: str, event_type: str):
        """Default callback for file events."""
        console.print(f"[cyan]📝[/cyan] {event_type}: {file_path}")
    
    def start_watching(self) -> bool:
        """Start watching the Claude directory."""
        if not WATCHDOG_AVAILABLE:
            console.print("[yellow]⚠️[/yellow] Watchdog not available. Using polling fallback.")
            return self._start_polling()
        
        try:
            self.observer = Observer()
            event_handler = ClaudeLogEventHandler(self.callback)
            
            # Watch the main Claude directory and subdirectories
            self.observer.schedule(
                event_handler, 
                str(self.claude_dir), 
                recursive=True
            )
            
            self.observer.start()
            self.is_running = True
            
            console.print(f"[green]✅[/green] Started watching {self.claude_dir}")
            return True
            
        except Exception as e:
            console.print(f"[red]❌[/red] Failed to start file watcher: {e}")
            console.print("[yellow]⚠️[/yellow] Falling back to polling mode")
            return self._start_polling()
    
    def _start_polling(self) -> bool:
        """Fallback polling method when watchdog is not available."""
        async def poll_files():
            while self.is_running:
                try:
                    await self._check_files()
                    await asyncio.sleep(2)  # Poll every 2 seconds
                except Exception as e:
                    console.print(f"[red]Error during polling: {e}[/red]")
        
        self.is_running = True
        asyncio.create_task(poll_files())
        console.print("[green]✅[/green] Started polling for file changes")
        return True
    
    async def _check_files(self):
        """Check for file changes during polling."""
        if not self.claude_dir.exists():
            return
        
        for file_path in self.claude_dir.rglob("*"):
            if file_path.is_file() and (
                file_path.suffix in ['.log', '.claude'] or 
                'session' in file_path.name.lower()
            ):
                try:
                    current_mtime = datetime.fromtimestamp(file_path.stat().st_mtime)
                    file_str = str(file_path)
                    
                    if file_str not in self.watched_files:
                        self.watched_files[file_str] = current_mtime
                        self.callback(file_str, "created")
                    elif self.watched_files[file_str] < current_mtime:
                        self.watched_files[file_str] = current_mtime
                        self.callback(file_str, "modified")
                        
                except Exception as e:
                    console.print(f"[red]Error checking file {file_path}: {e}[/red]")
    
    def stop_watching(self):
        """Stop the file watcher."""
        self.is_running = False
        
        if self.observer:
            self.observer.stop()
            self.observer.join()
            
        console.print("[yellow]⏹️[/yellow] Stopped file watching")
    
    def get_existing_sessions(self) -> List[Dict[str, Any]]:
        """Get information about existing Claude sessions."""
        sessions = []
        
        if not self.claude_dir.exists():
            return sessions
        
        try:
            for project_dir in self.claude_dir.iterdir():
                if project_dir.is_dir():
                    session_info = {
                        "project_name": project_dir.name,
                        "project_path": str(project_dir),
                        "created_time": datetime.fromtimestamp(project_dir.stat().st_ctime),
                        "modified_time": datetime.fromtimestamp(project_dir.stat().st_mtime),
                        "log_files": []
                    }
                    
                    # Find log files in the project
                    for log_file in project_dir.rglob("*.log"):
                        session_info["log_files"].append({
                            "path": str(log_file),
                            "size": log_file.stat().st_size,
                            "modified": datetime.fromtimestamp(log_file.stat().st_mtime)
                        })
                    
                    sessions.append(session_info)
                    
        except Exception as e:
            console.print(f"[red]Error scanning existing sessions: {e}[/red]")
        
        return sessions
    
    def read_file_content(self, file_path: str, tail_lines: Optional[int] = None) -> str:
        """Read content from a log file."""
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                if tail_lines:
                    lines = f.readlines()
                    return ''.join(lines[-tail_lines:])
                return f.read()
        except Exception as e:
            console.print(f"[red]Error reading file {file_path}: {e}[/red]")
            return ""
    
    def __enter__(self):
        """Context manager entry."""
        self.start_watching()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.stop_watching()