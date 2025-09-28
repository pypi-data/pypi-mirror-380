import asyncio
from pathlib import Path
from typing import Any

from .log import mklog
from .observer import Observable, Observer

log = mklog(__name__)


class CommandRunner(Observable):
    """Async command runner with real-time output streaming via observer pattern."""

    def __init__(self):
        super().__init__()
        self.stdout_lines: list[str] = []
        self.stderr_lines: list[str] = []
        self.process: asyncio.subprocess.Process | None = None
        self.return_code: int | None = None
        log.debug("CommandRunner created")

    async def run_command(self, cmd: str | list[Any], timeout: float | None = None) -> int:
        """Execute a shell command asynchronously with real-time output.

        Parameters
        ----------
        cmd : str | list[Any]
            Command to run (string or list of arguments)
        timeout : float | None
            Optional timeout in seconds

        Returns
        -------
        int
            Process return code

        Raises
        ------
        ValueError
            If cmd argument is invalid
        asyncio.TimeoutError
            If command times out
        """
        # Clear previous results
        self.stdout_lines.clear()
        self.stderr_lines.clear()
        self.return_code = None

        # Prepare command
        shell_cmd = self._prepare_shell_cmd(cmd)
        log.debug(f"Running command: {shell_cmd}")

        # Create process
        self.process = await asyncio.create_subprocess_shell(
            shell_cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )

        try:
            # Read streams concurrently (handle None streams)
            tasks = []
            if self.process.stdout:
                tasks.append(self._read_stream(self.process.stdout, "stdout"))
            if self.process.stderr:
                tasks.append(self._read_stream(self.process.stderr, "stderr"))
            tasks.append(self.process.wait())

            await asyncio.wait_for(asyncio.gather(*tasks), timeout=timeout)
        except asyncio.TimeoutError:
            log.warning(f"Command timed out after {timeout}s: {shell_cmd}")
            self.process.terminate()
            await self.process.wait()
            raise

        self.return_code = self.process.returncode or 0
        log.debug(f"Command completed with return code: {self.return_code}")

        # Notify completion
        await self.notify_async("completed", self.return_code, self.stdout_lines, self.stderr_lines)

        return self.return_code

    async def _read_stream(self, stream: asyncio.StreamReader, stream_name: str):
        """Read lines from a stream and notify observers."""
        lines = self.stdout_lines if stream_name == "stdout" else self.stderr_lines

        while True:
            try:
                line = await stream.readline()
                if not line:
                    break

                line_str = line.decode("utf-8").rstrip()
                if line_str:  # Only process non-empty lines
                    lines.append(line_str)
                    log.debug(f"Output ({stream_name}): {line_str}")
                    await self.notify_async(stream_name, line_str)

            except Exception as e:
                log.error(f"Error reading {stream_name}: {e}")
                break

    def _prepare_shell_cmd(self, cmd: str | list[Any]) -> str:
        """Prepare shell command from various input types."""
        if isinstance(cmd, str):
            return cmd
        elif isinstance(cmd, list):
            # Convert Path objects and stringify all arguments
            parts = []
            for arg in cmd:
                if isinstance(arg, Path):
                    parts.append(str(arg))
                else:
                    parts.append(str(arg))
            return " ".join(parts)
        else:
            raise ValueError("Command must be a string or list of arguments")

    def get_output(self) -> tuple[list[str], list[str]]:
        """Get collected stdout and stderr lines."""
        return self.stdout_lines.copy(), self.stderr_lines.copy()

    async def terminate(self):
        """Terminate the running process if active."""
        if self.process and self.process.returncode is None:
            log.info("Terminating process")
            self.process.terminate()
            await self.process.wait()


class PrintObserver(Observer):
    """Simple observer that prints command output to console."""

    def __init__(self, prefix: str = ""):
        self.prefix = prefix

    async def update(self, observable: Observable, event_type: str, *args, **kwargs):
        """Handle async notifications from CommandRunner."""
        if event_type == "stdout":
            line = args[0]
            print(f"{self.prefix}[OUT] {line}")
        elif event_type == "stderr":
            line = args[0]
            print(f"{self.prefix}[ERR] {line}")
        elif event_type == "completed":
            return_code, stdout_lines, stderr_lines = args
            print(f"{self.prefix}[DONE] Process completed with code: {return_code}")


class CollectorObserver(Observer):
    """Observer that collects all output for later processing."""

    def __init__(self):
        self.all_stdout: list[str] = []
        self.all_stderr: list[str] = []
        self.completed_commands: list[tuple[int, list[str], list[str]]] = []

    async def update(self, observable: Observable, event_type: str, *args, **kwargs):
        """Collect command output and completion info."""
        if event_type == "stdout":
            self.all_stdout.append(args[0])
        elif event_type == "stderr":
            self.all_stderr.append(args[0])
        elif event_type == "completed":
            return_code, stdout_lines, stderr_lines = args
            self.completed_commands.append((return_code, stdout_lines.copy(), stderr_lines.copy()))

    def get_last_result(self) -> tuple[int, list[str], list[str]] | None:
        """Get the result of the last completed command."""
        return self.completed_commands[-1] if self.completed_commands else None
