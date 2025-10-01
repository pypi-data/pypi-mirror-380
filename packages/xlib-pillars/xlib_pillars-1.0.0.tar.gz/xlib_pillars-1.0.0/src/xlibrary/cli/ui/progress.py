"""
Docker-style progress bars with multi-line display and rich formatting.

Provides advanced progress tracking similar to Docker's multi-line progress
display with colors, transfer speeds, and ETA calculations.
"""

import sys
import time
import threading
from enum import Enum
from typing import Dict, List, Optional, Callable, Any, TextIO, Union
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from pathlib import Path

# Optional Rich import
try:
    from rich.console import Console
    from rich.progress import (
        Progress, TaskID, BarColumn, TextColumn, TimeRemainingColumn,
        DownloadColumn, TransferSpeedColumn, SpinnerColumn
    )
    from rich.live import Live
    from rich.table import Table
    from rich.panel import Panel
    from rich.text import Text
    RICH_AVAILABLE = True
except ImportError:
    RICH_AVAILABLE = False
    TaskID = str  # Fallback type


class ProgressStyle(Enum):
    """Different progress bar styles."""
    SIMPLE = "simple"           # Basic single-line progress
    DOCKER = "docker"           # Docker-style multi-line
    DASHBOARD = "dashboard"     # Live dashboard format
    COMPACT = "compact"         # Compact multi-progress
    SPINNER = "spinner"         # Spinner for indeterminate


@dataclass
class ProgressTask:
    """Individual progress task information."""
    id: str
    description: str
    total: Optional[int] = None
    current: int = 0
    start_time: datetime = field(default_factory=datetime.now)
    status: str = "running"
    error: Optional[str] = None
    metadata: Dict[str, Any] = field(default_factory=dict)

    @property
    def elapsed(self) -> timedelta:
        """Time elapsed since task started."""
        return datetime.now() - self.start_time

    @property
    def percent(self) -> float:
        """Completion percentage."""
        if self.total is None or self.total == 0:
            return 0.0
        return min(100.0, (self.current / self.total) * 100)

    @property
    def rate(self) -> float:
        """Processing rate per second."""
        elapsed_seconds = self.elapsed.total_seconds()
        if elapsed_seconds == 0:
            return 0.0
        return self.current / elapsed_seconds

    @property
    def eta(self) -> Optional[timedelta]:
        """Estimated time to completion."""
        if self.total is None or self.current == 0 or self.status != "running":
            return None

        remaining = self.total - self.current
        if remaining <= 0:
            return timedelta(0)

        rate = self.rate
        if rate == 0:
            return None

        return timedelta(seconds=remaining / rate)


class ProgressManager:
    """
    Advanced progress manager with multiple display styles.

    Supports Docker-style multi-line progress, live dashboards,
    and automatic fallback to basic text progress.
    """

    def __init__(
        self,
        style: ProgressStyle = ProgressStyle.DOCKER,
        console: Optional[Console] = None,
        file: TextIO = sys.stderr,
        refresh_rate: float = 0.1
    ):
        """
        Initialize progress manager.

        Args:
            style: Progress display style
            console: Rich console instance (created if None)
            file: Output file stream
            refresh_rate: Update refresh rate in seconds
        """
        self.style = style
        self.file = file
        self.refresh_rate = refresh_rate
        self.use_rich = RICH_AVAILABLE and style != ProgressStyle.SIMPLE

        if self.use_rich and console is None:
            console = Console(file=file, force_terminal=True)

        self.console = console
        self.tasks: Dict[str, ProgressTask] = {}
        self.task_order: List[str] = []

        # Rich progress components
        self._rich_progress: Optional[Progress] = None
        self._rich_tasks: Dict[str, TaskID] = {}
        self._live_display: Optional[Live] = None

        # Threading for live updates
        self._update_thread: Optional[threading.Thread] = None
        self._stop_updates = threading.Event()
        self._lock = threading.Lock()

        # Last update tracking for basic mode
        self._last_update = time.time()
        self._update_interval = 1.0  # Basic mode update interval

    @classmethod
    def docker_style(
        cls,
        console: Optional[Console] = None,
        file: TextIO = sys.stderr
    ) -> 'ProgressManager':
        """Create Docker-style progress manager."""
        return cls(ProgressStyle.DOCKER, console, file)

    @classmethod
    def dashboard_style(
        cls,
        console: Optional[Console] = None,
        file: TextIO = sys.stderr
    ) -> 'ProgressManager':
        """Create dashboard-style progress manager."""
        return cls(ProgressStyle.DASHBOARD, console, file)

    @classmethod
    def simple_style(
        cls,
        file: TextIO = sys.stderr
    ) -> 'ProgressManager':
        """Create simple text progress manager."""
        return cls(ProgressStyle.SIMPLE, None, file)

    def add_task(
        self,
        description: str,
        total: Optional[int] = None,
        task_id: Optional[str] = None,
        **metadata
    ) -> str:
        """
        Add a new progress task.

        Args:
            description: Task description
            total: Total units of work (None for indeterminate)
            task_id: Optional custom task ID
            **metadata: Additional task metadata

        Returns:
            Task ID string
        """
        if task_id is None:
            task_id = f"task_{len(self.tasks) + 1}"

        with self._lock:
            # Create progress task
            task = ProgressTask(
                id=task_id,
                description=description,
                total=total,
                metadata=metadata
            )

            self.tasks[task_id] = task
            self.task_order.append(task_id)

            # Add to Rich progress if using Rich
            if self._rich_progress:
                rich_task_id = self._rich_progress.add_task(
                    description,
                    total=total,
                    start=False
                )
                self._rich_tasks[task_id] = rich_task_id

        return task_id

    def update(
        self,
        task_id: str,
        advance: int = 1,
        description: Optional[str] = None,
        status: Optional[str] = None,
        error: Optional[str] = None,
        **metadata
    ):
        """
        Update progress task.

        Args:
            task_id: Task ID to update
            advance: Amount to advance progress
            description: New description
            status: New status
            error: Error message if task failed
            **metadata: Additional metadata updates
        """
        with self._lock:
            if task_id not in self.tasks:
                return

            task = self.tasks[task_id]
            task.current += advance

            if description:
                task.description = description
            if status:
                task.status = status
            if error:
                task.error = error
                task.status = "error"

            task.metadata.update(metadata)

            # Update Rich progress
            if self._rich_progress and task_id in self._rich_tasks:
                rich_task_id = self._rich_tasks[task_id]
                update_kwargs = {"advance": advance}

                if description:
                    update_kwargs["description"] = description

                self._rich_progress.update(rich_task_id, **update_kwargs)

        # Force update in basic mode
        if not self.use_rich:
            self._maybe_update_basic()

    def complete_task(self, task_id: str, status: str = "completed", message: Optional[str] = None):
        """Mark task as completed."""
        with self._lock:
            if task_id not in self.tasks:
                return

            task = self.tasks[task_id]
            task.status = status

            if task.total and task.current < task.total:
                task.current = task.total

            if message:
                task.description = message

            # Complete Rich task
            if self._rich_progress and task_id in self._rich_tasks:
                rich_task_id = self._rich_tasks[task_id]
                if task.total:
                    self._rich_progress.update(rich_task_id, completed=task.total)

    def start(self):
        """Start the progress display."""
        if self.use_rich:
            self._setup_rich_display()
        else:
            self._print_header()

    def stop(self):
        """Stop the progress display."""
        self._stop_updates.set()

        if self._update_thread and self._update_thread.is_alive():
            self._update_thread.join(timeout=1.0)

        if self._live_display:
            self._live_display.stop()

        if not self.use_rich:
            self._print_summary()

    def _setup_rich_display(self):
        """Setup Rich progress display."""
        if self.style == ProgressStyle.DOCKER:
            self._setup_docker_style()
        elif self.style == ProgressStyle.DASHBOARD:
            self._setup_dashboard_style()
        else:
            self._setup_standard_rich()

    def _setup_docker_style(self):
        """Setup Docker-style multi-line progress."""
        self._rich_progress = Progress(
            TextColumn("{task.description}"),
            BarColumn(),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            TransferSpeedColumn(),
            TimeRemainingColumn(),
            console=self.console,
            transient=False
        )

        self._live_display = Live(
            self._generate_docker_display(),
            console=self.console,
            refresh_per_second=1/self.refresh_rate
        )
        self._live_display.start()

    def _setup_dashboard_style(self):
        """Setup dashboard-style display."""
        self._live_display = Live(
            self._generate_dashboard_display(),
            console=self.console,
            refresh_per_second=1/self.refresh_rate
        )
        self._live_display.start()

    def _setup_standard_rich(self):
        """Setup standard Rich progress."""
        self._rich_progress = Progress(
            SpinnerColumn(),
            TextColumn("{task.description}"),
            BarColumn(),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            TimeRemainingColumn(),
            console=self.console
        )
        self._rich_progress.start()

    def _generate_docker_display(self) -> Panel:
        """Generate Docker-style display panel."""
        if not self.tasks:
            return Panel("No active tasks", title="Progress")

        lines = []
        for task_id in self.task_order:
            task = self.tasks[task_id]
            line = self._format_docker_line(task)
            lines.append(line)

        content = "\n".join(lines)
        return Panel(
            content,
            title="🚀 xlibrary Operations",
            border_style="blue"
        )

    def _format_docker_line(self, task: ProgressTask) -> str:
        """Format single Docker-style progress line."""
        # Status icon
        if task.status == "completed":
            icon = "✅"
            color = "green"
        elif task.status == "error":
            icon = "❌"
            color = "red"
        elif task.status == "running":
            icon = "🔄"
            color = "blue"
        else:
            icon = "⏸️"
            color = "yellow"

        # Progress bar
        if task.total:
            bar_width = 20
            filled = int((task.percent / 100) * bar_width)
            bar = "▓" * filled + "░" * (bar_width - filled)
            progress_text = f"[{bar}] {task.percent:5.1f}%"
        else:
            progress_text = "[----------] ???%"

        # Rate and ETA
        rate_text = ""
        if task.rate > 0:
            if task.rate > 1024**2:
                rate_text = f"({task.rate/1024**2:.1f} MB/s)"
            elif task.rate > 1024:
                rate_text = f"({task.rate/1024:.1f} KB/s)"
            else:
                rate_text = f"({task.rate:.1f} B/s)"

        eta_text = ""
        if task.eta:
            if task.eta.total_seconds() < 60:
                eta_text = f"ETA: {task.eta.total_seconds():.0f}s"
            else:
                eta_text = f"ETA: {task.eta.total_seconds()/60:.1f}m"

        # Combine line
        line_parts = [
            f"[{color}]{icon}[/{color}]",
            progress_text,
            task.description[:40],
            rate_text,
            eta_text
        ]

        return " ".join(filter(None, line_parts))

    def _generate_dashboard_display(self) -> Table:
        """Generate dashboard-style display."""
        table = Table(title="🎛️ xlibrary Dashboard")
        table.add_column("Task", style="cyan")
        table.add_column("Progress", style="magenta")
        table.add_column("Status", style="green")
        table.add_column("Rate", style="blue")
        table.add_column("ETA", style="yellow")

        for task_id in self.task_order:
            task = self.tasks[task_id]

            # Progress column
            if task.total:
                progress = f"{task.percent:.1f}%"
            else:
                progress = "N/A"

            # Status column
            status_color = {
                "completed": "green",
                "error": "red",
                "running": "blue"
            }.get(task.status, "white")

            status = f"[{status_color}]{task.status}[/{status_color}]"

            # Rate column
            if task.rate > 0:
                rate = f"{task.rate:.1f} ops/s"
            else:
                rate = "---"

            # ETA column
            if task.eta:
                eta = f"{task.eta.total_seconds():.0f}s"
            else:
                eta = "---"

            table.add_row(
                task.description[:30],
                progress,
                status,
                rate,
                eta
            )

        return table

    def _print_header(self):
        """Print basic mode header."""
        print("\n🚀 xlibrary Progress", file=self.file)
        print("=" * 50, file=self.file)

    def _maybe_update_basic(self):
        """Update basic progress if enough time has passed."""
        now = time.time()
        if now - self._last_update >= self._update_interval:
            self._print_basic_progress()
            self._last_update = now

    def _print_basic_progress(self):
        """Print basic text progress."""
        for task_id in self.task_order:
            task = self.tasks[task_id]

            if task.total:
                progress = f"{task.current}/{task.total} ({task.percent:.1f}%)"
            else:
                progress = f"{task.current} processed"

            status_icon = {
                "completed": "✅",
                "error": "❌",
                "running": "🔄"
            }.get(task.status, "⏸️")

            print(f"\r{status_icon} {task.description}: {progress}", end="", file=self.file)

        print(file=self.file)  # New line

    def _print_summary(self):
        """Print final summary."""
        print("\n📊 Summary:", file=self.file)
        completed = sum(1 for t in self.tasks.values() if t.status == "completed")
        errored = sum(1 for t in self.tasks.values() if t.status == "error")
        total = len(self.tasks)

        print(f"   Completed: {completed}/{total}", file=self.file)
        if errored > 0:
            print(f"   Errors: {errored}", file=self.file)

    def __enter__(self):
        """Context manager entry."""
        self.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.stop()


class DockerProgress:
    """Simplified Docker-style progress for single operations."""

    def __init__(
        self,
        description: str,
        total: Optional[int] = None,
        console: Optional[Console] = None
    ):
        """Initialize Docker-style progress."""
        self.manager = ProgressManager.docker_style(console)
        self.task_id = None
        self.description = description
        self.total = total

    def start(self) -> str:
        """Start progress tracking."""
        self.manager.start()
        self.task_id = self.manager.add_task(self.description, self.total)
        return self.task_id

    def update(self, advance: int = 1, description: Optional[str] = None):
        """Update progress."""
        if self.task_id:
            self.manager.update(self.task_id, advance, description)

    def complete(self, message: Optional[str] = None):
        """Complete progress."""
        if self.task_id:
            self.manager.complete_task(self.task_id, "completed", message)

    def stop(self):
        """Stop progress."""
        self.manager.stop()

    def __enter__(self):
        """Context manager entry."""
        self.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        if exc_type is None:
            self.complete()
        else:
            if self.task_id:
                self.manager.complete_task(self.task_id, "error", "Failed")
        self.stop()


# Convenience functions
def docker_progress(description: str, total: Optional[int] = None) -> DockerProgress:
    """Create Docker-style progress bar."""
    return DockerProgress(description, total)


def simple_progress(description: str, total: Optional[int] = None):
    """Create simple progress bar."""
    manager = ProgressManager.simple_style()
    with manager:
        task_id = manager.add_task(description, total)
        yield manager, task_id