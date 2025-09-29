"""
Claude Code Wrapper

Provides wrapper functionality similar to omnara's claude_wrapper_v3,
enabling monitoring and communication with Claude Code sessions.
"""

import os
import sys
import asyncio
import subprocess
from typing import Dict, List, Optional, Any, Union
from datetime import datetime
from pathlib import Path

from rich.console import Console

from .file_watcher import ClaudeFileWatcher
from .log_parser import ClaudeLogParser, MessageType
from .session_tracker import SessionTracker, SessionStatus
from .terminal_monitor import TerminalMonitor

console = Console()


class ClaudeWrapper:
    """
    Wrapper for Claude Code sessions providing monitoring and communication.
    
    Similar to omnara's claude_wrapper_v3, this class:
    - Monitors Claude Code activity
    - Parses logs and interactions
    - Provides real-time session tracking
    - Enables remote communication with Claude sessions
    """
    
    def __init__(
        self,
        project_path: Optional[str] = None,
        session_callback: Optional[callable] = None,
        debug: bool = False
    ):
        self.project_path = project_path
        self.debug = debug
        self.session_callback = session_callback
        
        # Initialize monitoring components
        self.file_watcher = ClaudeFileWatcher(callback=self._on_file_change)
        self.log_parser = ClaudeLogParser()
        self.session_tracker = SessionTracker()
        self.terminal_monitor = TerminalMonitor(callback=self._on_terminal_output)
        
        # Current session
        self.current_session = None
        self.is_active = False
        
        # Message buffer for real-time processing
        self.message_buffer = []
        self.last_processed_time = datetime.now()
        
        # Register session callbacks
        self._register_callbacks()
        
        console.print("[blue]🔧[/blue] Claude wrapper initialized")
        if project_path:
            console.print(f"[blue]📁[/blue] Project path: {project_path}")
    
    def _register_callbacks(self):
        """Register callbacks for session events."""
        self.session_tracker.register_callback("question_detected", self._on_question_detected)
        self.session_tracker.register_callback("activity_detected", self._on_activity_detected)
        self.session_tracker.register_callback("error_detected", self._on_error_detected)
    
    def start_monitoring(self) -> bool:
        """Start monitoring Claude Code sessions."""
        try:
            console.print("[cyan]🚀[/cyan] Starting Claude monitoring...")
            
            # Start file watcher
            if not self.file_watcher.start_watching():
                console.print("[red]❌[/red] Failed to start file watcher")
                return False
            
            # Start terminal monitor
            if not self.terminal_monitor.start_monitoring():
                console.print("[red]❌[/red] Failed to start terminal monitor")
                return False
            
            # Create monitoring session
            self.current_session = self.session_tracker.create_session(
                agent_type="claude",
                project_path=self.project_path,
                metadata={
                    "wrapper_version": "1.0.0",
                    "start_method": "manual",
                    "debug_mode": self.debug
                }
            )
            
            self.session_tracker.update_session_status(
                self.current_session.session_id, 
                SessionStatus.ACTIVE
            )
            
            self.is_active = True
            
            # Scan for existing sessions
            existing_sessions = self.file_watcher.get_existing_sessions()
            if existing_sessions:
                console.print(f"[green]📋[/green] Found {len(existing_sessions)} existing Claude sessions")
                for session in existing_sessions:
                    self._process_existing_session(session)
            
            console.print("[green]✅[/green] Claude monitoring started successfully")
            return True
            
        except Exception as e:
            console.print(f"[red]❌[/red] Failed to start monitoring: {e}")
            return False
    
    def stop_monitoring(self):
        """Stop monitoring."""
        console.print("[yellow]⏹️[/yellow] Stopping Claude monitoring...")
        
        self.is_active = False
        
        # Stop monitoring components
        self.file_watcher.stop_watching()
        self.terminal_monitor.stop_monitoring()
        
        # End current session
        if self.current_session:
            self.session_tracker.end_session(
                self.current_session.session_id, 
                reason="manual_stop"
            )
        
        console.print("[yellow]⏹️[/yellow] Claude monitoring stopped")
    
    def _on_file_change(self, file_path: str, event_type: str):
        """Handle file change events."""
        if self.debug:
            console.print(f"[debug]File {event_type}: {file_path}")
        
        # Parse the file if it's a log file
        if file_path.endswith('.log') or '.claude' in file_path:
            self._process_log_file(file_path, event_type)
    
    def _process_log_file(self, file_path: str, event_type: str):
        """Process a Claude log file."""
        try:
            # Read recent content (last 50 lines for efficiency)
            content = self.file_watcher.read_file_content(file_path, tail_lines=50)
            if not content.strip():
                return
            
            # Parse the content
            lines = content.strip().split('\n')
            for line_num, line in enumerate(lines, 1):
                parsed = self.log_parser.parse_line(line, line_num)
                if parsed:
                    self._process_parsed_message(parsed, file_path)
                    
        except Exception as e:
            console.print(f"[red]❌[/red] Error processing log file {file_path}: {e}")
    
    def _process_parsed_message(self, message, file_path: str):
        """Process a parsed message from Claude logs."""
        if not self.current_session:
            return
        
        # Add to message buffer
        self.message_buffer.append(message)
        
        # Record activity in session tracker
        activity_type = "message"
        if message.message_type == MessageType.AGENT_QUESTION:
            activity_type = "question"
        elif message.message_type == MessageType.ERROR:
            activity_type = "error"
        
        self.session_tracker.record_activity(
            self.current_session.session_id,
            activity_type,
            {
                "message_type": message.message_type.value,
                "content": message.content,
                "file_path": file_path,
                "metadata": message.metadata
            }
        )
        
        # Check if agent needs input
        if self.log_parser.detect_agent_needs_input([message]):
            self._handle_agent_needs_input(message)
    
    def _on_terminal_output(self, output):
        """Handle terminal output from monitoring."""
        if not output.is_relevant or not self.current_session:
            return
        
        # Analyze the output
        analysis = self.terminal_monitor.analyze_output(output.content)
        
        if analysis["is_relevant"]:
            self.session_tracker.record_activity(
                self.current_session.session_id,
                "terminal_output",
                {
                    "content": output.content,
                    "output_type": output.output_type,
                    "analysis": analysis,
                    "process_id": output.process_id
                }
            )
    
    def _process_existing_session(self, session_info: Dict[str, Any]):
        """Process an existing Claude session found during startup."""
        if self.debug:
            console.print(f"[debug]Processing existing session: {session_info['project_name']}")
        
        # Parse recent log files
        for log_file in session_info.get("log_files", []):
            try:
                messages = self.log_parser.parse_log_file(log_file["path"])
                if messages:
                    # Generate summary
                    summary = self.log_parser.generate_session_summary(messages)
                    console.print(f"[blue]📊[/blue] Session summary: {summary.total_messages} messages, {summary.questions_asked} questions")
                    
                    # Check if agent needs input
                    if self.log_parser.detect_agent_needs_input(messages):
                        latest_question = self.log_parser.extract_latest_question(messages)
                        if latest_question:
                            console.print(f"[yellow]❓[/yellow] Agent waiting for input: {latest_question[:100]}...")
                            
            except Exception as e:
                console.print(f"[red]❌[/red] Error processing log file: {e}")
    
    def _handle_agent_needs_input(self, message):
        """Handle when agent needs user input."""
        console.print(f"[yellow]🤔[/yellow] Agent question detected: {message.content[:100]}...")
        
        if self.session_callback:
            try:
                self.session_callback({
                    "type": "agent_question",
                    "session_id": self.current_session.session_id,
                    "question": message.content,
                    "timestamp": message.timestamp.isoformat(),
                    "metadata": message.metadata
                })
            except Exception as e:
                console.print(f"[red]❌[/red] Callback error: {e}")
    
    def _on_question_detected(self, session, extra_data):
        """Handle question detection callback."""
        console.print(f"[yellow]❓[/yellow] Question detected in session {session.session_id}")
        
    def _on_activity_detected(self, session, extra_data):
        """Handle activity detection callback."""
        if self.debug:
            activity_type = extra_data.get("type", "unknown")
            console.print(f"[debug]Activity detected: {activity_type}")
    
    def _on_error_detected(self, session, extra_data):
        """Handle error detection callback."""
        console.print(f"[red]❌[/red] Error detected in session {session.session_id}")
    
    def send_message_to_agent(self, message: str) -> bool:
        """Send a message to the Claude agent (placeholder implementation)."""
        if not self.current_session:
            console.print("[red]❌[/red] No active session")
            return False
        
        console.print(f"[green]📤[/green] Sending message to agent: {message[:50]}...")
        
        # In a real implementation, this would interact with Claude Code's input mechanism
        # For now, we'll just record it as activity
        self.session_tracker.record_activity(
            self.current_session.session_id,
            "user_message",
            {
                "content": message,
                "timestamp": datetime.now().isoformat(),
                "source": "wrapper"
            }
        )
        
        return True
    
    def get_session_status(self) -> Optional[Dict[str, Any]]:
        """Get current session status."""
        if not self.current_session:
            return None
        
        return {
            "session": self.current_session.to_dict(),
            "stats": self.session_tracker.get_session_stats(),
            "process_stats": self.terminal_monitor.get_process_stats(),
            "message_buffer_size": len(self.message_buffer),
            "is_active": self.is_active
        }
    
    def get_recent_messages(self, limit: int = 10) -> List[Dict[str, Any]]:
        """Get recent messages from the buffer."""
        recent = self.message_buffer[-limit:] if self.message_buffer else []
        return [msg.to_dict() for msg in recent]
    
    def clear_message_buffer(self):
        """Clear the message buffer."""
        self.message_buffer.clear()
        console.print("[cyan]🗑️[/cyan] Message buffer cleared")
    
    def __enter__(self):
        """Context manager entry."""
        self.start_monitoring()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.stop_monitoring()