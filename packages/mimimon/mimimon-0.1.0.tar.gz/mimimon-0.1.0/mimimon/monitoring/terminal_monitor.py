"""
Terminal Output Monitor

Monitors terminal output and system processes to detect Claude Code
activity and extract relevant information for session tracking.
"""

import os
import re
import asyncio
import subprocess
from typing import Dict, List, Optional, Any, Callable
from datetime import datetime
from dataclasses import dataclass
from pathlib import Path

import psutil
from rich.console import Console

console = Console()


@dataclass
class ProcessInfo:
    """Information about a monitored process."""
    pid: int
    name: str
    cmdline: List[str]
    start_time: datetime
    cpu_percent: float = 0.0
    memory_percent: float = 0.0
    is_claude_related: bool = False


@dataclass
class TerminalOutput:
    """Captured terminal output with metadata."""
    timestamp: datetime
    process_id: int
    content: str
    output_type: str  # stdout, stderr
    is_relevant: bool = False
    metadata: Optional[Dict[str, Any]] = None


class TerminalMonitor:
    """
    Monitor terminal output and system processes for Claude Code activity.
    
    Detects:
    - Claude Code processes
    - Terminal output from Claude sessions
    - System commands executed by Claude
    - File operations and git activity
    """
    
    def __init__(self, callback: Optional[Callable[[TerminalOutput], None]] = None):
        self.callback = callback or self._default_callback
        self.monitored_processes: Dict[int, ProcessInfo] = {}
        self.is_monitoring = False
        self.output_patterns = self._compile_output_patterns()
        self._monitor_task = None
        
    def _compile_output_patterns(self) -> Dict[str, re.Pattern]:
        """Compile regex patterns for detecting relevant terminal output."""
        return {
            # Claude-related patterns
            "claude_command": re.compile(r"claude|anthropic", re.IGNORECASE),
            "ai_interaction": re.compile(r"(?:assistant|agent|ai|human|user):\s*(.+)", re.IGNORECASE),
            
            # File operation patterns
            "file_operation": re.compile(r"(?:created|modified|deleted|moved|copied)\s+(.+)", re.IGNORECASE),
            "git_operation": re.compile(r"git\s+(?:add|commit|push|pull|clone|checkout)\s*(.+)", re.IGNORECASE),
            
            # Progress indicators
            "progress_indicator": re.compile(r"(?:\d+%|\d+/\d+|progress|complete|finished|done)", re.IGNORECASE),
            "status_message": re.compile(r"(?:status|state|current|now|next):\s*(.+)", re.IGNORECASE),
            
            # Error patterns
            "error_message": re.compile(r"(?:error|exception|failed|failure|fatal):\s*(.+)", re.IGNORECASE),
            "warning_message": re.compile(r"(?:warning|warn):\s*(.+)", re.IGNORECASE),
            
            # Question patterns
            "question": re.compile(r"(.+\?)\s*$"),
            "user_prompt": re.compile(r"(?:please|can you|could you|would you|do you|should)\b.+", re.IGNORECASE),
            
            # Code execution
            "code_execution": re.compile(r"(?:running|executing|calling)\s+(.+)", re.IGNORECASE),
            "shell_command": re.compile(r"[\$#]\s*(.+)"),
        }
    
    def _default_callback(self, output: TerminalOutput):
        """Default callback for terminal output."""
        if output.is_relevant:
            console.print(f"[cyan]🖥️[/cyan] {output.output_type}: {output.content[:100]}...")
    
    def start_monitoring(self) -> bool:
        """Start monitoring terminal output and processes."""
        try:
            self.is_monitoring = True
            self._monitor_task = asyncio.create_task(self._monitor_loop())
            console.print("[green]✅[/green] Started terminal monitoring")
            return True
        except Exception as e:
            console.print(f"[red]❌[/red] Failed to start terminal monitoring: {e}")
            return False
    
    def stop_monitoring(self):
        """Stop monitoring."""
        self.is_monitoring = False
        if self._monitor_task:
            self._monitor_task.cancel()
        console.print("[yellow]⏹️[/yellow] Stopped terminal monitoring")
    
    async def _monitor_loop(self):
        """Main monitoring loop."""
        while self.is_monitoring:
            try:
                await self._scan_processes()
                await self._capture_output()
                await asyncio.sleep(1)  # Monitor every second
            except Exception as e:
                console.print(f"[red]❌[/red] Monitor loop error: {e}")
                await asyncio.sleep(5)  # Wait before retrying
    
    async def _scan_processes(self):
        """Scan for Claude-related processes."""
        current_pids = set()
        
        try:
            for proc in psutil.process_iter(['pid', 'name', 'cmdline', 'create_time']):
                try:
                    proc_info = proc.info
                    pid = proc_info['pid']
                    current_pids.add(pid)
                    
                    # Check if process is Claude-related
                    is_claude = self._is_claude_process(proc_info)
                    
                    if pid not in self.monitored_processes:
                        process_info = ProcessInfo(
                            pid=pid,
                            name=proc_info['name'] or "unknown",
                            cmdline=proc_info['cmdline'] or [],
                            start_time=datetime.fromtimestamp(proc_info['create_time']),
                            is_claude_related=is_claude
                        )
                        
                        if is_claude:
                            self.monitored_processes[pid] = process_info
                            console.print(f"[green]🔍[/green] Detected Claude process: {process_info.name} (PID: {pid})")
                    
                    # Update existing process info
                    elif pid in self.monitored_processes:
                        try:
                            self.monitored_processes[pid].cpu_percent = proc.cpu_percent()
                            self.monitored_processes[pid].memory_percent = proc.memory_percent()
                        except (psutil.NoSuchProcess, psutil.AccessDenied):
                            pass
                            
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    continue
        
        except Exception as e:
            console.print(f"[red]❌[/red] Process scanning error: {e}")
        
        # Remove dead processes
        dead_pids = set(self.monitored_processes.keys()) - current_pids
        for pid in dead_pids:
            process_info = self.monitored_processes.pop(pid)
            if process_info.is_claude_related:
                console.print(f"[yellow]👻[/yellow] Claude process ended: {process_info.name} (PID: {pid})")
    
    def _is_claude_process(self, proc_info: Dict[str, Any]) -> bool:
        """Check if a process is Claude-related."""
        name = (proc_info.get('name') or "").lower()
        cmdline = " ".join(proc_info.get('cmdline') or []).lower()
        
        claude_indicators = [
            "claude", "anthropic", "ai-assistant", "code-assistant",
            "llm", "gpt", "chatbot", "assistant"
        ]
        
        for indicator in claude_indicators:
            if indicator in name or indicator in cmdline:
                return True
        
        # Check for Python processes running Claude-related code
        if "python" in name and any(keyword in cmdline for keyword in ["claude", "anthropic", "assistant"]):
            return True
        
        return False
    
    async def _capture_output(self):
        """Capture output from monitored processes."""
        for pid, process_info in list(self.monitored_processes.items()):
            if not process_info.is_claude_related:
                continue
                
            try:
                # Get process object
                proc = psutil.Process(pid)
                
                # Try to capture recent output (this is limited on most systems)
                # In a real implementation, you might need to hook into the terminal
                # or use process tracing tools
                await self._check_process_files(proc, process_info)
                
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
            except Exception as e:
                console.print(f"[red]❌[/red] Output capture error for PID {pid}: {e}")
    
    async def _check_process_files(self, proc: psutil.Process, process_info: ProcessInfo):
        """Check for file operations by a process."""
        try:
            # Check open files
            open_files = proc.open_files()
            for file_info in open_files:
                file_path = file_info.path
                
                # Check if it's a relevant file (logs, projects, etc.)
                if self._is_relevant_file(file_path):
                    await self._process_file_activity(file_path, process_info)
                    
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
    
    def _is_relevant_file(self, file_path: str) -> bool:
        """Check if a file is relevant to Claude monitoring."""
        relevant_patterns = [
            r"\.claude",
            r"\.log$",
            r"\.py$",
            r"\.js$",
            r"\.ts$",
            r"\.json$",
            r"projects?/",
            r"workspace/",
        ]
        
        for pattern in relevant_patterns:
            if re.search(pattern, file_path, re.IGNORECASE):
                return True
        
        return False
    
    async def _process_file_activity(self, file_path: str, process_info: ProcessInfo):
        """Process file activity from a monitored process."""
        try:
            # Check if file was recently modified
            stat_info = os.stat(file_path)
            modified_time = datetime.fromtimestamp(stat_info.st_mtime)
            
            # If modified in the last few seconds, it's likely active
            if (datetime.now() - modified_time).total_seconds() < 10:
                output = TerminalOutput(
                    timestamp=modified_time,
                    process_id=process_info.pid,
                    content=f"File activity: {file_path}",
                    output_type="file_activity",
                    is_relevant=True,
                    metadata={
                        "file_path": file_path,
                        "process_name": process_info.name,
                        "activity_type": "file_modification"
                    }
                )
                
                self.callback(output)
                
        except (OSError, FileNotFoundError):
            pass
    
    def analyze_output(self, content: str) -> Dict[str, Any]:
        """Analyze terminal output for relevant patterns."""
        analysis = {
            "is_relevant": False,
            "patterns_found": [],
            "metadata": {}
        }
        
        for pattern_name, pattern in self.output_patterns.items():
            match = pattern.search(content)
            if match:
                analysis["is_relevant"] = True
                analysis["patterns_found"].append(pattern_name)
                
                # Extract specific information based on pattern
                if pattern_name == "question":
                    analysis["metadata"]["question"] = match.group(1)
                elif pattern_name in ["ai_interaction", "status_message", "error_message"]:
                    analysis["metadata"][pattern_name] = match.group(1)
                elif match.groups():
                    analysis["metadata"][pattern_name] = match.group(1)
        
        return analysis
    
    def get_claude_processes(self) -> List[ProcessInfo]:
        """Get all currently monitored Claude processes."""
        return [p for p in self.monitored_processes.values() if p.is_claude_related]
    
    def get_process_stats(self) -> Dict[str, Any]:
        """Get statistics about monitored processes."""
        claude_processes = self.get_claude_processes()
        
        return {
            "total_processes": len(self.monitored_processes),
            "claude_processes": len(claude_processes),
            "active_processes": len([p for p in claude_processes if p.cpu_percent > 0]),
            "total_cpu_usage": sum(p.cpu_percent for p in claude_processes),
            "total_memory_usage": sum(p.memory_percent for p in claude_processes),
            "timestamp": datetime.now().isoformat()
        }
    
    def __enter__(self):
        """Context manager entry."""
        self.start_monitoring()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.stop_monitoring()