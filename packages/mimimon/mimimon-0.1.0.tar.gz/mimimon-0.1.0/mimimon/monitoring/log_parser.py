"""
Claude Code Log Parser

Parses Claude Code session logs to extract agent interactions,
questions, progress updates, and important events.
"""

import re
import json
from typing import Dict, List, Optional, Any, Union
from datetime import datetime
from dataclasses import dataclass
from enum import Enum

from rich.console import Console

console = Console()


class MessageType(Enum):
    """Types of messages found in Claude logs."""
    USER_INPUT = "user_input"
    AGENT_RESPONSE = "agent_response"
    AGENT_QUESTION = "agent_question"
    PROGRESS_UPDATE = "progress_update"
    ERROR = "error"
    TOOL_USAGE = "tool_usage"
    FILE_OPERATION = "file_operation"
    SYSTEM_MESSAGE = "system_message"
    UNKNOWN = "unknown"


@dataclass
class ParsedMessage:
    """Represents a parsed message from Claude logs."""
    timestamp: datetime
    message_type: MessageType
    content: str
    metadata: Dict[str, Any]
    raw_line: str
    line_number: int
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON serialization."""
        return {
            "timestamp": self.timestamp.isoformat(),
            "message_type": self.message_type.value,
            "content": self.content,
            "metadata": self.metadata,
            "raw_line": self.raw_line,
            "line_number": self.line_number
        }


@dataclass
class SessionSummary:
    """Summary of a Claude session."""
    session_id: str
    start_time: datetime
    end_time: Optional[datetime]
    total_messages: int
    user_messages: int
    agent_responses: int
    questions_asked: int
    tools_used: int
    files_modified: int
    errors_encountered: int
    last_activity: datetime
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON serialization."""
        return {
            "session_id": self.session_id,
            "start_time": self.start_time.isoformat(),
            "end_time": self.end_time.isoformat() if self.end_time else None,
            "total_messages": self.total_messages,
            "user_messages": self.user_messages,
            "agent_responses": self.agent_responses,
            "questions_asked": self.questions_asked,
            "tools_used": self.tools_used,
            "files_modified": self.files_modified,
            "errors_encountered": self.errors_encountered,
            "last_activity": self.last_activity.isoformat()
        }


class ClaudeLogParser:
    """
    Parser for Claude Code session logs.
    
    Extracts structured information from log files including:
    - User inputs and agent responses
    - Questions asked by the agent
    - Progress updates and status changes
    - Tool usage and file operations
    - Error messages and warnings
    """
    
    def __init__(self):
        self.patterns = self._compile_patterns()
        self.message_buffer = []
        self.current_session = None
    
    def _compile_patterns(self) -> Dict[str, re.Pattern]:
        """Compile regex patterns for log parsing."""
        return {
            # Timestamp patterns
            "timestamp": re.compile(r"(\d{4}-\d{2}-\d{2}[T\s]\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+-]\d{2}:\d{2})?)"),
            "simple_timestamp": re.compile(r"(\d{2}:\d{2}:\d{2})"),
            
            # User input patterns
            "user_input": re.compile(r"(?:User(?:\s+(?:says|input|message))?|Human):\s*(.+)", re.IGNORECASE),
            "user_prompt": re.compile(r"(?:>>|>)\s*(.+)"),
            
            # Agent response patterns  
            "agent_response": re.compile(r"(?:Assistant|Claude|Agent):\s*(.+)", re.IGNORECASE),
            "agent_thinking": re.compile(r"(?:thinking|reasoning):\s*(.+)", re.IGNORECASE),
            
            # Questions from agent
            "agent_question": re.compile(r"(.+\?)\s*$"),
            "clarification": re.compile(r"(?:could you|can you|would you|do you|should i|what|how|which|where|when|why)\b.+\?", re.IGNORECASE),
            
            # Progress and status
            "progress": re.compile(r"(?:progress|step|stage|phase|completing|finished|started|working on)\s*:?\s*(.+)", re.IGNORECASE),
            "status_update": re.compile(r"(?:status|state|current)\s*:?\s*(.+)", re.IGNORECASE),
            
            # Tool usage
            "tool_call": re.compile(r"(?:using tool|calling|executing|running)\s*:?\s*(.+)", re.IGNORECASE),
            "tool_result": re.compile(r"(?:tool result|output|result)\s*:?\s*(.+)", re.IGNORECASE),
            
            # File operations
            "file_read": re.compile(r"(?:reading|read|loading)\s+file\s*:?\s*(.+)", re.IGNORECASE),
            "file_write": re.compile(r"(?:writing|wrote|saving|created)\s+file\s*:?\s*(.+)", re.IGNORECASE),
            "file_modify": re.compile(r"(?:modifying|modified|updating|edited)\s+file\s*:?\s*(.+)", re.IGNORECASE),
            
            # Errors and warnings
            "error": re.compile(r"(?:error|exception|failed|failure)\s*:?\s*(.+)", re.IGNORECASE),
            "warning": re.compile(r"(?:warning|warn)\s*:?\s*(.+)", re.IGNORECASE),
            
            # System messages
            "system": re.compile(r"(?:system|info|debug)\s*:?\s*(.+)", re.IGNORECASE),
            
            # JSON-like structures
            "json_block": re.compile(r"\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\}"),
        }
    
    def parse_log_file(self, file_path: str) -> List[ParsedMessage]:
        """Parse a complete log file and return structured messages."""
        messages = []
        
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                lines = f.readlines()
            
            for line_num, line in enumerate(lines, 1):
                line = line.strip()
                if not line:
                    continue
                
                parsed = self.parse_line(line, line_num)
                if parsed:
                    messages.append(parsed)
                    
        except Exception as e:
            console.print(f"[red]Error parsing log file {file_path}: {e}[/red]")
        
        return messages
    
    def parse_line(self, line: str, line_number: int = 0) -> Optional[ParsedMessage]:
        """Parse a single log line and return structured information."""
        # Extract timestamp if present
        timestamp = self._extract_timestamp(line)
        if not timestamp:
            timestamp = datetime.now()
        
        # Clean the line for content extraction
        clean_line = self._clean_line(line)
        
        # Determine message type and extract content
        message_type, content, metadata = self._classify_message(clean_line)
        
        if message_type == MessageType.UNKNOWN and not content:
            return None
        
        return ParsedMessage(
            timestamp=timestamp,
            message_type=message_type,
            content=content,
            metadata=metadata,
            raw_line=line,
            line_number=line_number
        )
    
    def _extract_timestamp(self, line: str) -> Optional[datetime]:
        """Extract timestamp from a log line."""
        # Try full timestamp first
        match = self.patterns["timestamp"].search(line)
        if match:
            timestamp_str = match.group(1)
            try:
                # Handle various timestamp formats
                for fmt in [
                    "%Y-%m-%dT%H:%M:%S.%fZ",
                    "%Y-%m-%dT%H:%M:%SZ", 
                    "%Y-%m-%d %H:%M:%S.%f",
                    "%Y-%m-%d %H:%M:%S",
                    "%Y-%m-%dT%H:%M:%S"
                ]:
                    try:
                        return datetime.strptime(timestamp_str, fmt)
                    except ValueError:
                        continue
            except:
                pass
        
        # Try simple time format
        match = self.patterns["simple_timestamp"].search(line)
        if match:
            time_str = match.group(1)
            try:
                time_obj = datetime.strptime(time_str, "%H:%M:%S")
                # Use today's date with the extracted time
                now = datetime.now()
                return now.replace(
                    hour=time_obj.hour, 
                    minute=time_obj.minute, 
                    second=time_obj.second,
                    microsecond=0
                )
            except:
                pass
        
        return None
    
    def _clean_line(self, line: str) -> str:
        """Clean a log line by removing timestamps and prefixes."""
        # Remove timestamp
        line = self.patterns["timestamp"].sub("", line).strip()
        line = self.patterns["simple_timestamp"].sub("", line).strip()
        
        # Remove common prefixes
        prefixes_to_remove = ["[INFO]", "[DEBUG]", "[ERROR]", "[WARN]", "[WARNING]"]
        for prefix in prefixes_to_remove:
            if line.startswith(prefix):
                line = line[len(prefix):].strip()
        
        return line
    
    def _classify_message(self, line: str) -> tuple[MessageType, str, Dict[str, Any]]:
        """Classify a message and extract relevant content."""
        metadata = {}
        
        # Check for user input
        match = self.patterns["user_input"].search(line)
        if match:
            return MessageType.USER_INPUT, match.group(1).strip(), metadata
        
        match = self.patterns["user_prompt"].search(line)
        if match:
            return MessageType.USER_INPUT, match.group(1).strip(), metadata
        
        # Check for agent responses
        match = self.patterns["agent_response"].search(line)
        if match:
            content = match.group(1).strip()
            # Check if it's a question
            if self.patterns["agent_question"].search(content) or self.patterns["clarification"].search(content):
                return MessageType.AGENT_QUESTION, content, metadata
            return MessageType.AGENT_RESPONSE, content, metadata
        
        # Check for progress updates
        match = self.patterns["progress"].search(line)
        if match:
            return MessageType.PROGRESS_UPDATE, match.group(1).strip(), metadata
        
        match = self.patterns["status_update"].search(line)
        if match:
            return MessageType.PROGRESS_UPDATE, match.group(1).strip(), metadata
        
        # Check for tool usage
        match = self.patterns["tool_call"].search(line)
        if match:
            metadata["tool_action"] = "call"
            return MessageType.TOOL_USAGE, match.group(1).strip(), metadata
        
        match = self.patterns["tool_result"].search(line)
        if match:
            metadata["tool_action"] = "result"
            return MessageType.TOOL_USAGE, match.group(1).strip(), metadata
        
        # Check for file operations
        for pattern_name in ["file_read", "file_write", "file_modify"]:
            match = self.patterns[pattern_name].search(line)
            if match:
                metadata["operation"] = pattern_name.replace("file_", "")
                return MessageType.FILE_OPERATION, match.group(1).strip(), metadata
        
        # Check for errors
        match = self.patterns["error"].search(line)
        if match:
            metadata["severity"] = "error"
            return MessageType.ERROR, match.group(1).strip(), metadata
        
        match = self.patterns["warning"].search(line)
        if match:
            metadata["severity"] = "warning"
            return MessageType.ERROR, match.group(1).strip(), metadata
        
        # Check for system messages
        match = self.patterns["system"].search(line)
        if match:
            return MessageType.SYSTEM_MESSAGE, match.group(1).strip(), metadata
        
        # Check for questions (fallback)
        if self.patterns["agent_question"].search(line):
            return MessageType.AGENT_QUESTION, line, metadata
        
        # Return as unknown with the full line as content
        return MessageType.UNKNOWN, line, metadata
    
    def generate_session_summary(self, messages: List[ParsedMessage]) -> SessionSummary:
        """Generate a summary of a session from parsed messages."""
        if not messages:
            return SessionSummary(
                session_id="empty",
                start_time=datetime.now(),
                end_time=None,
                total_messages=0,
                user_messages=0,
                agent_responses=0,
                questions_asked=0,
                tools_used=0,
                files_modified=0,
                errors_encountered=0,
                last_activity=datetime.now()
            )
        
        # Count message types
        type_counts = {}
        for msg in messages:
            type_counts[msg.message_type] = type_counts.get(msg.message_type, 0) + 1
        
        return SessionSummary(
            session_id=f"session_{messages[0].timestamp.strftime('%Y%m%d_%H%M%S')}",
            start_time=messages[0].timestamp,
            end_time=messages[-1].timestamp if len(messages) > 1 else None,
            total_messages=len(messages),
            user_messages=type_counts.get(MessageType.USER_INPUT, 0),
            agent_responses=type_counts.get(MessageType.AGENT_RESPONSE, 0),
            questions_asked=type_counts.get(MessageType.AGENT_QUESTION, 0),
            tools_used=type_counts.get(MessageType.TOOL_USAGE, 0),
            files_modified=type_counts.get(MessageType.FILE_OPERATION, 0),
            errors_encountered=type_counts.get(MessageType.ERROR, 0),
            last_activity=messages[-1].timestamp
        )
    
    def detect_agent_needs_input(self, messages: List[ParsedMessage]) -> bool:
        """Detect if the agent is waiting for user input."""
        if not messages:
            return False
        
        # Look at the last few messages
        recent_messages = messages[-5:]
        
        for msg in reversed(recent_messages):
            # If the last message is a question, agent likely needs input
            if msg.message_type == MessageType.AGENT_QUESTION:
                return True
            
            # If there's a user input after the question, agent doesn't need input
            if msg.message_type == MessageType.USER_INPUT:
                return False
        
        return False
    
    def extract_latest_question(self, messages: List[ParsedMessage]) -> Optional[str]:
        """Extract the latest question asked by the agent."""
        for msg in reversed(messages):
            if msg.message_type == MessageType.AGENT_QUESTION:
                return msg.content
        return None