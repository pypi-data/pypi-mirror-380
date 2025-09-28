import logging
import os
import shutil
import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path


class SubprocessPoolError(Exception):
    """Base exception for all subprocess pool errors."""

    pass


class TaskFailureError(SubprocessPoolError):
    """Raised when a task fails and early_fail is True."""

    pass


class Signal:
    """Simple event signal for task notifications."""

    def __init__(self):
        self._subscribers = []

    def connect(self, func):
        """Connect a callback function to this signal."""
        self._subscribers.append(func)

    def emit(self, *args, **kwargs):
        """Emit the signal, calling all connected callbacks."""
        for subscriber in self._subscribers:
            try:
                subscriber(*args, **kwargs)
            except Exception as e:
                logging.warning(f"Signal callback failed: {e}")


class Task:
    """Represents a command to be executed in the subprocess pool."""

    def __init__(self, command: str, shell: str | None = None):
        self.command = command
        self.shell = shell
        self.on_done = Signal()
        self.on_failure = Signal()
        self.on_std_out = Signal()
        self.on_std_err = Signal()
        self.result_code: int | None = None
        self.stdout_lines: list[str] = []
        self.stderr_lines: list[str] = []


class SubprocessPool:
    """A pool for executing shell commands concurrently with configurable shell support."""

    def __init__(
        self,
        max_concurrent: int = 4,
        *,
        early_fail: bool = False,
        shell: str | None = None,
        logger: logging.Logger | None = None
    ):
        """
        Initialize the subprocess pool.

        Args
        ----
        max_concurrent : int
            Maximum number of concurrent tasks
        early_fail : bool
            Whether to cancel remaining tasks if one fails
        shell : str, optional
            Shell to use for command execution (auto-detected if None)
        logger : logging.Logger, optional
            Logger instance for debugging
        """
        self.max_concurrent = max_concurrent
        self.tasks: list[Task] = []
        self.early_fail = early_fail
        self.executor = ThreadPoolExecutor(max_concurrent)
        self.futures = []
        self.logger = logger or logging.getLogger(__name__)
        self.shell = shell or self._detect_shell()

    def _detect_shell(self) -> str:
        """Detect the appropriate shell to use based on environment and availability."""
        # Check environment variable first
        if default_shell := os.environ.get("SHELL"):
            shell_name = Path(default_shell).name
            if shell_path := shutil.which(shell_name):
                self.logger.debug(f"Using shell from SHELL env var: {shell_path}")
                return shell_path

        # Try common shells in order of preference for the user's setup
        preferred_shells = ["nu", "zsh", "bash", "fish", "sh"]

        for shell_name in preferred_shells:
            if shell_path := shutil.which(shell_name):
                self.logger.debug(f"Found shell: {shell_path}")
                return shell_path

        # Fallback to system shell
        fallback = "/bin/sh"
        self.logger.warning(f"No preferred shell found, using fallback: {fallback}")
        return fallback

    def _get_shell_command(self, command: str, shell: str) -> list[str]:
        """Format a command for the specified shell."""
        shell_name = Path(shell).name

        if shell_name in ["nu", "bash", "zsh", "fish", "sh"]:
            return [shell, "-c", command]
        else:
            # Generic shell command format
            return [shell, "-c", command]

    def add_task(self, command: str, shell: str | None = None) -> Task:
        """
        Add a task to the pool.

        Parameters
        ----------
        command : str
            Shell command to execute
        shell : str, optional
            Override shell for this specific task

        Returns
        -------
        Task
            Task instance for connecting to signals
        """
        task = Task(command, shell or self.shell)
        self.tasks.append(task)
        return task

    def _execute_task(self, task: Task) -> None:
        """Execute a single task subprocess with proper error handling."""
        shell_cmd = self._get_shell_command(task.command, task.shell or self.shell)
        self.logger.debug(f"Executing: {shell_cmd}")

        process = subprocess.Popen(
            shell_cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            env=os.environ.copy(),
            text=True,
            encoding="utf-8",
            bufsize=1,  # Line buffered
            universal_newlines=True
        )

        # Read stdout line by line
        if process.stdout:
            for line in iter(process.stdout.readline, ''):
                if not line:
                    break
                line = line.strip()
                if line:  # Only emit non-empty lines
                    task.stdout_lines.append(line)
                    task.on_std_out.emit(line)

        # Wait for process to complete and get stderr
        _, stderr = process.communicate()
        task.result_code = process.returncode

        # Process stderr
        if stderr:
            stderr_lines = stderr.strip().split('\n')
            task.stderr_lines.extend(stderr_lines)
            for line in stderr_lines:
                if line.strip():
                    task.on_std_err.emit(line.strip())

        # Handle completion
        self._handle_task_completion(task, process.returncode)

    def _handle_task_completion(self, task: Task, return_code: int) -> None:
        """Handle task completion and error conditions."""
        if return_code == 0:
            self.logger.debug(f"Task completed successfully: {task.command}")
            task.on_done.emit(task)
        else:
            self.logger.warning(f"Task failed with code {return_code}: {task.command}")
            task.on_failure.emit(task)
            if self.early_fail:
                self.cancel()
                raise TaskFailureError(f"Task '{task.command}' failed with code {return_code}")

    def run_subprocess(self, task: Task) -> None:
        """Execute a single task subprocess."""
        try:
            self._execute_task(task)
        except TaskFailureError:
            # Re-raise task failures
            raise
        except Exception as e:
            task.result_code = -1
            self.logger.error(f"Exception executing task '{task.command}': {e}")
            task.on_failure.emit(task)
            if self.early_fail:
                self.cancel()
                raise TaskFailureError(f"Task '{task.command}' failed with exception: {e}") from e

    def run(self) -> None:
        """Execute all tasks concurrently."""
        self.logger.debug(
            f"Starting {len(self.tasks)} tasks with {self.max_concurrent} max concurrent"
        )

        for task in self.tasks:
            future = self.executor.submit(self.run_subprocess, task)
            self.futures.append(future)

    def wait(self) -> None:
        """Wait for all tasks to complete."""
        for future in as_completed(self.futures):
            try:
                future.result()  # This will raise any exceptions that occurred
            except TaskFailureError:
                # Re-raise task failures
                raise
            except Exception as e:
                self.logger.error(f"Unexpected error in task execution: {e}")
                if self.early_fail:
                    self.cancel()
                    raise

    def cancel(self) -> None:
        """Cancel all pending tasks."""
        self.logger.debug("Cancelling remaining tasks")
        cancelled_count = 0
        for future in self.futures:
            if future.cancel():
                cancelled_count += 1
        self.logger.debug(f"Cancelled {cancelled_count} pending tasks")

    def __enter__(self):
        """Context manager entry."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit - ensures cleanup."""
        self.cancel()
        self.executor.shutdown(wait=True)
