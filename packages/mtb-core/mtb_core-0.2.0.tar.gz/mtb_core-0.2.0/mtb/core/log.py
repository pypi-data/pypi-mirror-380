import datetime
import json
import logging
import os
import sys
from contextlib import contextmanager
from logging.handlers import RotatingFileHandler

# from pathlib import Path


def _is_testing():
    """Check if the current execution environment is a pytest test run."""
    return any("pytest" in x for x in sys.modules)


@contextmanager
def suppress_std():
    """
    Context manager that redirects stdout and stderr to /dev/null.

    This is useful when you want to suppress console output from a specific section of your code.

    Examples
    --------
    >>> with suppress_std():
    ...     print('This text will not appear in the console')
    """
    with open(os.devnull, "w") as devnull:
        old_stdout = sys.stdout
        old_stderr = sys.stderr
        sys.stdout = devnull
        sys.stderr = devnull

        try:
            yield
        finally:
            sys.stdout = old_stdout
            sys.stderr = old_stderr


class ConsoleFormatter(logging.Formatter):
    """A custom log formatter that adds color to log messages."""

    COLORS = {
        logging.DEBUG: "\x1b[35;20m",  # purple
        logging.INFO: "\x1b[36;20m",  # cyan
        logging.WARNING: "\x1b[33;20m",  # yellow
        logging.ERROR: "\x1b[31;20m",  # red
        logging.CRITICAL: "\x1b[31;1m",  # bold red
    }
    RESET = "\x1b[0m"
    # FORMATS = {
    #     logging.DEBUG: f"{purple}{format}{RESET}",
    #     logging.INFO: f"{cyan}{format}{RESET}",
    #     logging.WARNING: f"{yellow}{format}{RESET}",
    #     logging.ERROR: f"{red}{format}{RESET}",
    #     logging.CRITICAL: f"{bold_red}{format}{RESET}",
    # }

    def format(self, record):
        message = super().format(record)
        log_color = self.COLORS.get(record.levelno, self.RESET)

        # ANSI escape code for hyperlink: OSC 8 ; params ; URI ST text OSC 8 ; ; ST
        # file://{record.pathname} is the URI
        # {record.filename}:{record.lineno} is the display text
        hyperlink = f"\x1b]8;;file://{record.pathname}\a{record.filename}:{record.lineno}\x1b]8;;\a"
        return f"{log_color}{message}{self.RESET} ({hyperlink})"

    # DEPRECATED: It can break message formatting (e.g., logger.info("User %s", name)
    # will be broken because you override before formatting is applied).
    def format_prev(self, record):
        """Format the log message with color and include a hyperlink to the source code."""
        log_color = self.COLORS.get(record.levelno, self.RESET)

        # filepath = Path(record.pathname)
        hyperlink = f"\x1b]8;;file://{record.pathname}\a{record.filename}:{record.lineno}\x1b]8;;\a"
        record.msg = f"{log_color}{record.msg}{self.RESET} ({hyperlink})"

        # formatted_message = f"[{record.name}]({record.levelname}) | {self.formatTime(record, '%H:%M:%S')} -> {record.msg}"

        return super().format(record)

        # NOTE: I just changed it it was forcing this...?
        # return f"{log_color}[{record.name}]({record.levelname}){self.RESET} | {self.formatTime(record, self.datefmt)} -> {record.msg}"


class FileFormatter(logging.Formatter):
    """
    A custom log formatter for file output.

    designed to be parsed by the log syntax of bat.
    It formats timestamps to YYYY-MM-DDTHH:MM:SS.ms and uses a structured plain text format.
    """

    def formatTime(self, record, datefmt=None):  # noqa: N802
        """
        Override to format asctime to YYYY-MM-DDTHH:MM:SS.ms.

        The default asctime format from logging.Formatter is "YYYY-MM-DD HH:MM:SS,ms".
        """
        s = super().formatTime(record, datefmt)
        # replace space with 'T' and comma with dot for milliseconds
        return s.replace(" ", "T").replace(",", ".")


class JsonFormatter(logging.Formatter):
    """
    A custom log formatter for JSON file output.

    It serializes log records into a single JSON object per line.
    """

    def format(self, record):
        # Use record.getMessage() to ensure 'msg % args' formatting is applied
        message = record.getMessage()

        # Prepare basic log entry with common attributes
        log_entry = {
            "timestamp": datetime.datetime.fromtimestamp(record.created).isoformat(
                timespec="milliseconds"
            ),
            "level": record.levelname,
            "logger_name": record.name,
            "message": message,
            "file": record.pathname,
            "line": record.lineno,
            "function": record.funcName,
            "process_id": record.process,
            "process_name": record.processName,
            "thread_id": record.thread,
            "thread_name": record.threadName,
        }

        # Add exception info if present
        if record.exc_info:
            # formatException returns a string with traceback
            log_entry["exception"] = self.formatException(record.exc_info)

        # Add stack info if present
        if record.stack_info:
            # formatStack returns a string with stack trace
            log_entry["stack_trace"] = self.formatStack(record.stack_info)

        # Add any extra attributes passed to the logger via `extra` dict
        # Filter out standard LogRecord attributes to avoid duplication or non-serializable types
        standard_log_record_attrs = {
            "name",
            "levelname",
            "levelno",
            "pathname",
            "filename",
            "module",
            "lineno",
            "funcName",
            "created",
            "asctime",
            "msecs",
            "relativeCreated",
            "thread",
            "threadName",
            "process",
            "processName",
            "msg",
            "args",
            "exc_info",
            "exc_text",
            "stack_info",
            "message",
        }

        for key, value in record.__dict__.items():
            if key not in standard_log_record_attrs and not key.startswith("_"):
                try:
                    # Attempt to serialize directly. If it fails, convert to string.
                    json.dumps(value)  # Check if serializable
                    log_entry[key] = value
                except TypeError:
                    log_entry[key] = str(value)  # Fallback for non-serializable types
                except Exception:
                    # Catch any other unexpected errors during serialization check
                    log_entry[key] = repr(value)  # Use repr for more detailed representation

        return json.dumps(log_entry)


def mklog(
    name,
    level=logging.INFO,
    *,
    use_rich=False,
    file_path=None,
    max_files: int = 5,
    rotate_threshold_kb: int = 1024,
) -> logging.Logger:
    """
    Create and configure a logger with the specified name and log level.

    Supports console output (with optional Rich formatting) and file output (plain text or JSON).
    Includes log rotation for file handlers.

    Parameters
    ----------
    name : str
        The name of the logger.
    level : int
        The logging level (e.g., logging.DEBUG, logging.INFO).
    use_rich : bool, optional
        If True, use RichHandler for console output if stderr is a TTY and not testing.
        Defaults to False.
    file_path : str, optional
        If provided, log messages will also be written to this file.
        The file format depends on the extension:
        - If ends with ".jlog", output will be JSON.
        - Otherwise (e.g., ".log"), output will be plain text optimized for Sublime Text syntax.

    max_files : int, optional
        The maximum number of rotated log files to keep (including the current active one).
        Defaults to 5. Must be >= 1.
    rotate_threshold_kb : int, optional
        The size in kilobytes at which a log file rotation is initiated.
        Defaults to 1024 KB (1 MB). Must be >= 0.

    Returns
    -------
    logging.Logger
        The configured logger instance.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # for handler in logger.handlers[:]:
    # logger.removeHandler(handler)

    logger.handlers.clear()
    ch = None

    if use_rich and sys.stderr.isatty():
        try:
            from rich.console import Console
            from rich.logging import RichHandler

            ch = RichHandler(
                show_time=True,
                show_level=True,
                show_path=False,
                rich_tracebacks=True,
                markup=True,
                console=Console(file=sys.stderr, stderr=True),
            )
            ch.setLevel(level)
            # RichHandler handles its own formatting and coloring
            # a simple message format is often sufficient.
            ch.setFormatter(logging.Formatter("%(message)s", datefmt="[%X]"))
        except ImportError:
            # Fallback to standard StreamHandler if rich is not installed
            print(
                "Warning: rich library not found. Falling back to standard console logging.",
                file=sys.stderr,
            )
            ch = logging.StreamHandler(sys.stderr)
            ch.setLevel(level)
            ch.setFormatter(ConsoleFormatter("%(message)s", datefmt="%H:%M:%S"))

    else:
        ch = logging.StreamHandler(sys.stderr)
        ch.setLevel(level)
        ch.setFormatter(
            ConsoleFormatter(
                "%(message)s",
                # "[%(name)s](%(levelname)s) | %(asctime)s -> %(message)s",
                datefmt="%H:%M:%S",
            )
        )

    if ch:
        logger.addHandler(ch)

    # --- File Handler ---
    if file_path:
        try:
            # Ensure the directory for the log file exists
            os.makedirs(os.path.dirname(file_path), exist_ok=True)

            max_bytes = max(0, rotate_threshold_kb) * 1024
            backup_count = max(0, max_files - 1)
            fh = RotatingFileHandler(
                file_path, maxBytes=max_bytes, backupCount=backup_count, encoding="utf-8"
            )
            # fh = logging.FileHandler(file_path, encoding="utf-8")
            fh.setLevel(level)

            if file_path.endswith(".jlog"):
                fh.setFormatter(JsonFormatter())
            else:  # Default to plain text for .log or other extensions
                # Format string for plain text file output, optimized for Sublime Text syntax
                file_format_string = (
                    "%(asctime)s %(levelname)s %(name)s: %(message)s (file=%(pathname)s:%(lineno)d)"
                )
                fh.setFormatter(FileFormatter(file_format_string))
            logger.addHandler(fh)

        except Exception as e:
            # Log an error if file handler setup fails, but don't crash the application
            # Use a basic print to stderr as the logger itself might not be fully functional yet
            print(f"ERROR: Could not set up file logger at '{file_path}': {e}", file=sys.stderr)

    # disable log propagation to prevent duplicate logs, unless running in a pytest environment
    logger.propagate = _is_testing()

    return logger


def getLogger(name=None, level=logging.DEBUG) -> logging.Logger:
    """Retrieve an existing logger or create a new one if it doesn't exist."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    logger.handlers.clear()
    # for h in logger.handlers[:]:
    #     logger.removeHandler(h)
    #     h.close()
    # for handler in logger.handlers[:]:
    #     logger.removeHandler(handler)

    # if not logger.handlers:
    ch = logging.StreamHandler(sys.stderr)
    ch.setLevel(level)
    ch.setFormatter(
        ConsoleFormatter(
            "%(message)s",
            # "[%(name)s](%(levelname)s) | %(asctime)s -> %(message)s",
            datefmt="%H:%M:%S",
        )
    )
    logger.addHandler(ch)

    # Disable log propagation to prevent duplicate logs
    logger.propagate = _is_testing()

    return logger
