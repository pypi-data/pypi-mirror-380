"""
Unified Streaming Interface for Metis Agent.

This module consolidates the duplicate streaming interfaces into a single,
configurable streaming system with all features from both implementations.
"""

import click
import os
import sys
import time
import asyncio
import threading
from pathlib import Path
from typing import Dict, List, Any, Optional, Generator, AsyncGenerator, Union
import subprocess
import json
from dataclasses import dataclass, field
from enum import Enum
from contextlib import contextmanager

# Optional Rich imports
try:
    from rich.console import Console
    from rich.live import Live
    from rich.table import Table
    from rich.panel import Panel
    from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskID
    from rich.text import Text
    from rich.syntax import Syntax
    from rich.markdown import Markdown
    from rich.tree import Tree
    RICH_AVAILABLE = True
except ImportError:
    RICH_AVAILABLE = False
    Console = None

# Optional status system imports
try:
    from .status_manager import MetisStatusManager, StatusLevel, get_status_manager
    from .progress_display import OperationContext, SimpleSpinner, SimpleProgressBar, StatusIndicator
    STATUS_SYSTEM_AVAILABLE = True
except ImportError:
    STATUS_SYSTEM_AVAILABLE = False

# Fix Windows console encoding
if sys.platform == "win32":
    try:
        import codecs
        sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
        sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')
    except Exception:
        pass


class StreamingMode(Enum):
    """Different streaming modes for output."""
    CHARACTER = "character"  # Character-by-character like Claude Code
    WORD = "word"           # Word-by-word like Gemini
    CHUNK = "chunk"         # Chunk-based for performance
    INSTANT = "instant"     # No streaming for debugging


class TaskStatus(Enum):
    """Task execution status."""
    PENDING = "pending"
    THINKING = "thinking"
    EXECUTING = "executing"
    COMPLETED = "completed"
    FAILED = "failed"


class InterfaceMode(Enum):
    """Interface complexity levels."""
    SIMPLE = "simple"      # Basic output
    ADVANCED = "advanced"  # Rich formatting
    EXPERT = "expert"      # Full features


@dataclass
class StreamingConfig:
    """Configuration for streaming interface."""
    mode: StreamingMode = StreamingMode.CHARACTER
    interface_mode: InterfaceMode = InterfaceMode.ADVANCED
    operation_mode: str = 'balanced'  # 'fast', 'balanced', 'thorough'
    confirmation_level: str = 'normal'  # 'minimal', 'normal', 'verbose'
    auto_write_files: bool = False
    auto_execute_commands: bool = False
    show_reasoning: bool = True
    show_progress: bool = True
    use_colors: bool = True
    chunk_delay: float = 0.05  # Delay between chunks in seconds
    character_delay: float = 0.01  # Delay between characters


@dataclass
class StreamingTask:
    """A task being executed with streaming output."""
    id: str
    description: str
    status: TaskStatus = TaskStatus.PENDING
    start_time: Optional[float] = None
    end_time: Optional[float] = None
    output: List[str] = field(default_factory=list)
    files_created: List[str] = field(default_factory=list)
    files_modified: List[str] = field(default_factory=list)
    reasoning: List[str] = field(default_factory=list)

    @property
    def duration(self) -> Optional[float]:
        if self.start_time and self.end_time:
            return self.end_time - self.start_time
        return None


class UnifiedStreamingInterface:
    """
    Unified streaming interface combining features from both implementations.
    """

    def __init__(
        self,
        agent,
        workspace_path: str = None,
        config: Optional[StreamingConfig] = None,
        tools_registry: Dict = None
    ):
        self.agent = agent
        self.current_agent = agent
        self.current_agent_id = None
        self.workspace_path = workspace_path or os.getcwd()
        self.config = config or StreamingConfig()
        self.tools_registry = tools_registry or {}

        # Session state
        self.session_active = True
        self.files_created = []
        self.files_modified = []
        self.current_task: Optional[StreamingTask] = None
        self.task_history: List[StreamingTask] = []

        # Multi-agent support
        self._initialize_multi_agent_support()

        # Tools initialization
        self._initialize_tools()

        # Interface components
        self._initialize_interface()

        # Status system
        self._initialize_status_system()

    def _initialize_multi_agent_support(self):
        """Initialize multi-agent support if available."""
        try:
            from ..core.agent_manager import get_agent_manager
            self.agent_manager = get_agent_manager()
            self.multi_agent_available = True
        except Exception:
            self.agent_manager = None
            self.multi_agent_available = False

    def _initialize_tools(self):
        """Initialize tool references."""
        self.write_tool = self.tools_registry.get('WriteTool')
        self.project_tool = self.tools_registry.get('ProjectManagementTool')
        self.read_tool = self.tools_registry.get('ReadTool')
        self.grep_tool = self.tools_registry.get('GrepTool')
        self.file_manager_tool = self.tools_registry.get('FileManagerTool')
        self.bash_tool = self.tools_registry.get('BashTool')
        self.e2b_tool = self.tools_registry.get('E2BCodeSandboxTool')

    def _initialize_interface(self):
        """Initialize interface components based on configuration."""
        if RICH_AVAILABLE and self.config.interface_mode != InterfaceMode.SIMPLE:
            self.console = Console(color_system="auto" if self.config.use_colors else None)
            self.use_rich = True
        else:
            self.console = None
            self.use_rich = False

        # Progress tracking
        self.progress = None
        if self.use_rich and self.config.show_progress:
            self.progress = Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                BarColumn(),
                TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
                console=self.console
            )

    def _initialize_status_system(self):
        """Initialize status management system."""
        if STATUS_SYSTEM_AVAILABLE:
            self.status_manager = get_status_manager()
        else:
            self.status_manager = None

    def start_task(self, description: str, task_id: str = None) -> StreamingTask:
        """Start a new streaming task."""
        if task_id is None:
            task_id = f"task_{len(self.task_history) + 1}"

        task = StreamingTask(
            id=task_id,
            description=description,
            start_time=time.time()
        )

        self.current_task = task
        self.task_history.append(task)

        if self.use_rich:
            self._display_task_start_rich(task)
        else:
            self._display_task_start_plain(task)

        return task

    def stream_response(self, response_generator: Generator[str, None, None],
                       task: Optional[StreamingTask] = None) -> str:
        """Stream response with configured mode."""
        if task is None:
            task = self.current_task

        if task:
            task.status = TaskStatus.THINKING

        full_response = ""

        if self.config.mode == StreamingMode.INSTANT:
            # No streaming, just collect and display
            full_response = "".join(response_generator)
            if self.use_rich:
                self._display_response_rich(full_response, task)
            else:
                self._display_response_plain(full_response)
        else:
            # Streaming display
            if self.use_rich:
                full_response = self._stream_response_rich(response_generator, task)
            else:
                full_response = self._stream_response_plain(response_generator, task)

        if task:
            task.output.append(full_response)
            task.status = TaskStatus.COMPLETED
            task.end_time = time.time()

        return full_response

    def _stream_response_rich(self, response_generator: Generator[str, None, None],
                             task: Optional[StreamingTask]) -> str:
        """Stream response using Rich interface."""
        full_response = ""

        with Live(self._create_live_panel(""), console=self.console, refresh_per_second=20) as live:
            for chunk in response_generator:
                if self.config.mode == StreamingMode.CHARACTER:
                    for char in chunk:
                        full_response += char
                        live.update(self._create_live_panel(full_response))
                        time.sleep(self.config.character_delay)
                elif self.config.mode == StreamingMode.WORD:
                    words = chunk.split()
                    for word in words:
                        full_response += word + " "
                        live.update(self._create_live_panel(full_response))
                        time.sleep(self.config.chunk_delay)
                else:  # CHUNK mode
                    full_response += chunk
                    live.update(self._create_live_panel(full_response))
                    time.sleep(self.config.chunk_delay)

        return full_response

    def _stream_response_plain(self, response_generator: Generator[str, None, None],
                              task: Optional[StreamingTask]) -> str:
        """Stream response using plain text interface."""
        full_response = ""

        for chunk in response_generator:
            if self.config.mode == StreamingMode.CHARACTER:
                for char in chunk:
                    print(char, end='', flush=True)
                    full_response += char
                    time.sleep(self.config.character_delay)
            elif self.config.mode == StreamingMode.WORD:
                words = chunk.split()
                for word in words:
                    print(word + " ", end='', flush=True)
                    full_response += word + " "
                    time.sleep(self.config.chunk_delay)
            else:  # CHUNK mode
                print(chunk, end='', flush=True)
                full_response += chunk
                time.sleep(self.config.chunk_delay)

        print()  # New line at end
        return full_response

    def _create_live_panel(self, content: str) -> Panel:
        """Create a Rich panel for live updates."""
        if self.current_task:
            title = f"🤖 {self.current_task.description}"
        else:
            title = "🤖 Metis Agent"

        # Truncate content for display if too long
        display_content = content
        if len(content) > 2000:
            display_content = content[:2000] + "\n\n... (output truncated) ..."

        return Panel(
            display_content,
            title=title,
            title_align="left",
            border_style="blue"
        )

    def _display_task_start_rich(self, task: StreamingTask):
        """Display task start with Rich formatting."""
        panel = Panel(
            f"Starting: {task.description}",
            title="🚀 New Task",
            title_align="left",
            border_style="green"
        )
        self.console.print(panel)

    def _display_task_start_plain(self, task: StreamingTask):
        """Display task start with plain text."""
        print(f"🚀 Starting: {task.description}")
        print("-" * 50)

    def _display_response_rich(self, response: str, task: Optional[StreamingTask]):
        """Display complete response with Rich formatting."""
        if task:
            title = f"✅ {task.description}"
        else:
            title = "✅ Response"

        panel = Panel(
            response,
            title=title,
            title_align="left",
            border_style="green"
        )
        self.console.print(panel)

    def _display_response_plain(self, response: str):
        """Display complete response with plain text."""
        print(response)
        print("-" * 50)

    async def stream_async(self, response_generator: AsyncGenerator[str, None],
                          task: Optional[StreamingTask] = None) -> str:
        """Handle async streaming response."""
        if task is None:
            task = self.current_task

        if task:
            task.status = TaskStatus.THINKING

        full_response = ""

        if self.use_rich:
            full_response = await self._stream_async_rich(response_generator, task)
        else:
            full_response = await self._stream_async_plain(response_generator, task)

        if task:
            task.output.append(full_response)
            task.status = TaskStatus.COMPLETED
            task.end_time = time.time()

        return full_response

    async def _stream_async_rich(self, response_generator: AsyncGenerator[str, None],
                                task: Optional[StreamingTask]) -> str:
        """Handle async streaming with Rich interface."""
        full_response = ""

        with Live(self._create_live_panel(""), console=self.console, refresh_per_second=20) as live:
            async for chunk in response_generator:
                if self.config.mode == StreamingMode.CHARACTER:
                    for char in chunk:
                        full_response += char
                        live.update(self._create_live_panel(full_response))
                        await asyncio.sleep(self.config.character_delay)
                else:
                    full_response += chunk
                    live.update(self._create_live_panel(full_response))
                    await asyncio.sleep(self.config.chunk_delay)

        return full_response

    async def _stream_async_plain(self, response_generator: AsyncGenerator[str, None],
                                 task: Optional[StreamingTask]) -> str:
        """Handle async streaming with plain text."""
        full_response = ""

        async for chunk in response_generator:
            if self.config.mode == StreamingMode.CHARACTER:
                for char in chunk:
                    print(char, end='', flush=True)
                    full_response += char
                    await asyncio.sleep(self.config.character_delay)
            else:
                print(chunk, end='', flush=True)
                full_response += chunk
                await asyncio.sleep(self.config.chunk_delay)

        print()  # New line at end
        return full_response

    def show_file_operations(self, files_created: List[str], files_modified: List[str]):
        """Display file operations summary."""
        if not files_created and not files_modified:
            return

        if self.use_rich:
            self._show_file_operations_rich(files_created, files_modified)
        else:
            self._show_file_operations_plain(files_created, files_modified)

    def _show_file_operations_rich(self, files_created: List[str], files_modified: List[str]):
        """Show file operations with Rich formatting."""
        if files_created or files_modified:
            table = Table(title="📁 File Operations")
            table.add_column("Operation", style="cyan")
            table.add_column("File", style="white")

            for file in files_created:
                table.add_row("✨ Created", file)
            for file in files_modified:
                table.add_row("📝 Modified", file)

            self.console.print(table)

    def _show_file_operations_plain(self, files_created: List[str], files_modified: List[str]):
        """Show file operations with plain text."""
        print("\n📁 File Operations:")
        for file in files_created:
            print(f"  ✨ Created: {file}")
        for file in files_modified:
            print(f"  📝 Modified: {file}")
        print()

    def show_task_summary(self):
        """Display summary of all tasks in the session."""
        if not self.task_history:
            return

        if self.use_rich:
            self._show_task_summary_rich()
        else:
            self._show_task_summary_plain()

    def _show_task_summary_rich(self):
        """Show task summary with Rich formatting."""
        table = Table(title="📊 Session Summary")
        table.add_column("Task", style="cyan")
        table.add_column("Status", style="white")
        table.add_column("Duration", style="yellow")
        table.add_column("Files", style="green")

        for task in self.task_history:
            status_emoji = {
                TaskStatus.COMPLETED: "✅",
                TaskStatus.FAILED: "❌",
                TaskStatus.EXECUTING: "⏳",
                TaskStatus.PENDING: "⏸️"
            }.get(task.status, "❓")

            duration = f"{task.duration:.2f}s" if task.duration else "N/A"
            files_count = len(task.files_created) + len(task.files_modified)
            files_str = f"{files_count} files" if files_count > 0 else "No files"

            table.add_row(
                task.description[:50] + ("..." if len(task.description) > 50 else ""),
                f"{status_emoji} {task.status.value}",
                duration,
                files_str
            )

        self.console.print(table)

    def _show_task_summary_plain(self):
        """Show task summary with plain text."""
        print("\n📊 Session Summary:")
        print("-" * 60)
        for i, task in enumerate(self.task_history, 1):
            status_emoji = {
                TaskStatus.COMPLETED: "✅",
                TaskStatus.FAILED: "❌",
                TaskStatus.EXECUTING: "⏳",
                TaskStatus.PENDING: "⏸️"
            }.get(task.status, "❓")

            duration = f"{task.duration:.2f}s" if task.duration else "N/A"
            files_count = len(task.files_created) + len(task.files_modified)

            print(f"{i}. {status_emoji} {task.description}")
            print(f"   Duration: {duration} | Files: {files_count}")
        print("-" * 60)

    @contextmanager
    def task_context(self, description: str, task_id: str = None):
        """Context manager for task execution."""
        task = self.start_task(description, task_id)
        try:
            yield task
            task.status = TaskStatus.COMPLETED
        except Exception as e:
            task.status = TaskStatus.FAILED
            task.output.append(f"Error: {str(e)}")
            raise
        finally:
            task.end_time = time.time()

    def configure(self, **kwargs):
        """Update configuration dynamically."""
        for key, value in kwargs.items():
            if hasattr(self.config, key):
                setattr(self.config, key, value)

    def close_session(self):
        """Close the streaming session and show summary."""
        self.session_active = False

        if self.use_rich:
            self.console.print("\n[bold green]Session completed! 🎉[/bold green]")
        else:
            print("\nSession completed! 🎉")

        self.show_task_summary()


# Convenience functions for different modes
def create_streaming_interface(
    agent,
    workspace_path: str = None,
    mode: str = "advanced",
    streaming_mode: str = "character",
    **kwargs
) -> UnifiedStreamingInterface:
    """Create a streaming interface with common configurations."""

    config = StreamingConfig(
        mode=StreamingMode(streaming_mode),
        interface_mode=InterfaceMode(mode),
        **kwargs
    )

    return UnifiedStreamingInterface(
        agent=agent,
        workspace_path=workspace_path,
        config=config
    )


# Legacy compatibility functions
def create_gemini_interface(agent, **kwargs) -> UnifiedStreamingInterface:
    """Create interface compatible with old GeminiStreamingInterface."""
    return create_streaming_interface(
        agent,
        mode="advanced",
        streaming_mode="word",
        **kwargs
    )


def create_enhanced_interface(agent, **kwargs) -> UnifiedStreamingInterface:
    """Create interface compatible with old EnhancedStreamingInterface."""
    return create_streaming_interface(
        agent,
        mode="expert",
        streaming_mode="character",
        **kwargs
    )