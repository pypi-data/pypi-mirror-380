"""
Session Tracker for Claude Code Monitoring

Manages active monitoring sessions with unique IDs and real-time tracking.
"""

import uuid
import asyncio
from typing import Dict, List, Optional, Any, Callable
from datetime import datetime, timedelta
from dataclasses import dataclass, field
from enum import Enum

from rich.console import Console

console = Console()


class SessionStatus(Enum):
    """Possible session statuses."""
    STARTING = "starting"
    ACTIVE = "active"
    IDLE = "idle"
    PAUSED = "paused"
    ENDED = "ended"
    ERROR = "error"


@dataclass
class MonitoringSession:
    """Represents an active monitoring session."""
    session_id: str
    agent_type: str
    project_path: Optional[str]
    start_time: datetime = field(default_factory=datetime.now)
    last_activity: datetime = field(default_factory=datetime.now)
    status: SessionStatus = SessionStatus.STARTING
    message_count: int = 0
    question_count: int = 0
    error_count: int = 0
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert session to dictionary for API communication."""
        return {
            "session_id": self.session_id,
            "agent_type": self.agent_type,
            "project_path": self.project_path,
            "start_time": self.start_time.isoformat(),
            "last_activity": self.last_activity.isoformat(),
            "status": self.status.value,
            "message_count": self.message_count,
            "question_count": self.question_count,
            "error_count": self.error_count,
            "duration_seconds": (datetime.now() - self.start_time).total_seconds(),
            "metadata": self.metadata
        }
    
    def update_activity(self):
        """Update last activity timestamp."""
        self.last_activity = datetime.now()
    
    def is_idle(self, idle_threshold_minutes: int = 10) -> bool:
        """Check if session has been idle for too long."""
        threshold = datetime.now() - timedelta(minutes=idle_threshold_minutes)
        return self.last_activity < threshold


class SessionTracker:
    """
    Tracks active Claude Code monitoring sessions.
    
    Manages session lifecycle, status updates, and provides
    APIs for querying session information.
    """
    
    def __init__(self):
        self.sessions: Dict[str, MonitoringSession] = {}
        self.callbacks: Dict[str, List[Callable]] = {
            "session_started": [],
            "session_updated": [],
            "session_ended": [],
            "activity_detected": [],
            "question_detected": [],
            "error_detected": []
        }
        self._cleanup_task = None
        self._start_cleanup_task()
    
    def generate_session_id(self, prefix: str = "mimimon") -> str:
        """Generate a unique session ID."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        unique_id = str(uuid.uuid4())[:8]
        return f"{prefix}_{timestamp}_{unique_id}"
    
    def create_session(
        self, 
        agent_type: str = "claude",
        project_path: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None
    ) -> MonitoringSession:
        """Create a new monitoring session."""
        session_id = self.generate_session_id()
        
        session = MonitoringSession(
            session_id=session_id,
            agent_type=agent_type,
            project_path=project_path,
            metadata=metadata or {}
        )
        
        self.sessions[session_id] = session
        
        console.print(f"[green]✅[/green] Created session: {session_id}")
        console.print(f"[blue]📍[/blue] Agent: {agent_type}")
        if project_path:
            console.print(f"[blue]📁[/blue] Project: {project_path}")
        
        self._trigger_callbacks("session_started", session)
        return session
    
    def get_session(self, session_id: str) -> Optional[MonitoringSession]:
        """Get a session by ID."""
        return self.sessions.get(session_id)
    
    def list_active_sessions(self) -> List[MonitoringSession]:
        """List all active sessions."""
        return [
            session for session in self.sessions.values()
            if session.status in [SessionStatus.ACTIVE, SessionStatus.IDLE, SessionStatus.STARTING]
        ]
    
    def update_session_status(self, session_id: str, status: SessionStatus) -> bool:
        """Update session status."""
        session = self.sessions.get(session_id)
        if not session:
            return False
        
        old_status = session.status
        session.status = status
        session.update_activity()
        
        console.print(f"[cyan]🔄[/cyan] Session {session_id}: {old_status.value} → {status.value}")
        
        self._trigger_callbacks("session_updated", session)
        
        if status == SessionStatus.ENDED:
            self._trigger_callbacks("session_ended", session)
        
        return True
    
    def record_activity(
        self, 
        session_id: str, 
        activity_type: str,
        details: Optional[Dict[str, Any]] = None
    ) -> bool:
        """Record activity for a session."""
        session = self.sessions.get(session_id)
        if not session:
            return False
        
        session.update_activity()
        session.message_count += 1
        
        # Update status to active if it was idle
        if session.status == SessionStatus.IDLE:
            session.status = SessionStatus.ACTIVE
        
        # Track specific activity types
        if activity_type == "question":
            session.question_count += 1
            self._trigger_callbacks("question_detected", session, details)
        elif activity_type == "error":
            session.error_count += 1
            self._trigger_callbacks("error_detected", session, details)
        
        self._trigger_callbacks("activity_detected", session, {"type": activity_type, "details": details})
        return True
    
    def end_session(self, session_id: str, reason: str = "manual") -> bool:
        """End a monitoring session."""
        session = self.sessions.get(session_id)
        if not session:
            return False
        
        session.status = SessionStatus.ENDED
        session.metadata["end_reason"] = reason
        session.metadata["end_time"] = datetime.now().isoformat()
        
        console.print(f"[yellow]⏹️[/yellow] Session ended: {session_id} (reason: {reason})")
        
        self._trigger_callbacks("session_ended", session)
        return True
    
    def cleanup_old_sessions(self, max_age_hours: int = 24) -> int:
        """Clean up old ended sessions."""
        cutoff_time = datetime.now() - timedelta(hours=max_age_hours)
        sessions_to_remove = []
        
        for session_id, session in self.sessions.items():
            if (session.status == SessionStatus.ENDED and 
                session.last_activity < cutoff_time):
                sessions_to_remove.append(session_id)
        
        for session_id in sessions_to_remove:
            del self.sessions[session_id]
        
        if sessions_to_remove:
            console.print(f"[cyan]🧹[/cyan] Cleaned up {len(sessions_to_remove)} old sessions")
        
        return len(sessions_to_remove)
    
    def mark_idle_sessions(self, idle_threshold_minutes: int = 10) -> int:
        """Mark sessions as idle if they haven't had activity."""
        idle_count = 0
        
        for session in self.sessions.values():
            if (session.status == SessionStatus.ACTIVE and 
                session.is_idle(idle_threshold_minutes)):
                session.status = SessionStatus.IDLE
                idle_count += 1
                console.print(f"[yellow]😴[/yellow] Session {session.session_id} marked as idle")
        
        return idle_count
    
    def get_session_stats(self) -> Dict[str, Any]:
        """Get overall session statistics."""
        total_sessions = len(self.sessions)
        active_sessions = len([s for s in self.sessions.values() if s.status == SessionStatus.ACTIVE])
        idle_sessions = len([s for s in self.sessions.values() if s.status == SessionStatus.IDLE])
        ended_sessions = len([s for s in self.sessions.values() if s.status == SessionStatus.ENDED])
        
        total_messages = sum(s.message_count for s in self.sessions.values())
        total_questions = sum(s.question_count for s in self.sessions.values())
        total_errors = sum(s.error_count for s in self.sessions.values())
        
        return {
            "total_sessions": total_sessions,
            "active_sessions": active_sessions,
            "idle_sessions": idle_sessions,
            "ended_sessions": ended_sessions,
            "total_messages": total_messages,
            "total_questions": total_questions,
            "total_errors": total_errors,
            "timestamp": datetime.now().isoformat()
        }
    
    def register_callback(self, event_type: str, callback: Callable) -> bool:
        """Register a callback for session events."""
        if event_type not in self.callbacks:
            return False
        
        self.callbacks[event_type].append(callback)
        return True
    
    def _trigger_callbacks(self, event_type: str, session: MonitoringSession, extra_data: Optional[Any] = None):
        """Trigger callbacks for a specific event."""
        for callback in self.callbacks.get(event_type, []):
            try:
                if extra_data is not None:
                    callback(session, extra_data)
                else:
                    callback(session)
            except Exception as e:
                console.print(f"[red]❌[/red] Callback error for {event_type}: {e}")
    
    def _start_cleanup_task(self):
        """Start background cleanup task."""
        async def cleanup_loop():
            while True:
                try:
                    await asyncio.sleep(300)  # Run every 5 minutes
                    self.mark_idle_sessions()
                    self.cleanup_old_sessions()
                except Exception as e:
                    console.print(f"[red]❌[/red] Cleanup task error: {e}")
        
        try:
            self._cleanup_task = asyncio.create_task(cleanup_loop())
        except RuntimeError:
            # No event loop running, skip background task
            pass
    
    def stop_cleanup_task(self):
        """Stop the background cleanup task."""
        if self._cleanup_task:
            self._cleanup_task.cancel()
    
    def __del__(self):
        """Cleanup when tracker is destroyed."""
        self.stop_cleanup_task()