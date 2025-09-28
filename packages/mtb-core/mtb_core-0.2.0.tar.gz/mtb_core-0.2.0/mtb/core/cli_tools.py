#!/usr/bin/env python3
"""
Simple CLI tools for interactive command-line interfaces.

This module provides utilities for creating interactive CLI prompts and selections
using Rich for better formatting and user experience.
"""

from pathlib import Path
import logging
import sys
import tty
import termios

from rich.box import MINIMAL
from rich.console import Console
from rich.prompt import InvalidResponse, PromptBase
from rich.table import Table
from rich.live import Live
from collections.abc import Callable


class PathPrompt(PromptBase[Path]):
    """A prompt that returns a pathlib Path with validation."""

    response_type = Path
    validate_error_message = "[prompt.invalid]Please enter a valid path"

    def process_response(self, value: str) -> Path:
        """Convert str to Path and validate existence."""
        path = Path(value.strip()).expanduser()
        if not path.exists():
            raise InvalidResponse(self.validate_error_message)
        return path


def simple_select(
    console: Console,
    items: list[str],
    prompt: str = "Select an option"
) -> str | None:
    """Select an item from a list using numbered choices."""
    if not items:
        return None

    console.print(f"\n[bold]{prompt}:[/bold]")
    for i, item in enumerate(items, 1):
        console.print(f"  {i}. {item}")

    while True:
        try:
            choice = console.input("\nEnter your choice (number): ").strip()
            if not choice:
                return None

            idx = int(choice) - 1
            if 0 <= idx < len(items):
                return items[idx]
            else:
                console.print(f"[red]Please enter a number between 1 and {len(items)}[/red]")
        except ValueError:
            console.print("[red]Please enter a valid number[/red]")
        except KeyboardInterrupt:
            console.print("\n[yellow]Selection cancelled[/yellow]")
            return None


def select_from_table(
    console: Console,
    headers: list[str],
    items: list[list[str]],
    prompt: str = "Select an item"
) -> list[str] | None:
    """Select an item from a table display."""
    if not items:
        return None

    # Create and display table
    table = Table(box=MINIMAL, title=prompt)
    for header in headers:
        table.add_column(header)

    for i, row in enumerate(items, 1):
        table.add_row(str(i), *row)

    console.print(table)

    while True:
        try:
            choice = console.input(f"\nEnter your choice (1-{len(items)}): ").strip()
            if not choice:
                return None

            idx = int(choice) - 1
            if 0 <= idx < len(items):
                return items[idx]
            else:
                console.print(f"[red]Please enter a number between 1 and {len(items)}[/red]")
        except ValueError:
            console.print("[red]Please enter a valid number[/red]")
        except KeyboardInterrupt:
            console.print("\n[yellow]Selection cancelled[/yellow]")
            return None


def confirm(console: Console, message: str, *, default: bool = False) -> bool:
    """Prompt for yes/no confirmation."""
    suffix = " [Y/n]" if default else " [y/N]"

    while True:
        try:
            response = console.input(f"{message}{suffix}: ").strip().lower()
            if not response:
                return default
            if response in ['y', 'yes']:
                return True
            elif response in ['n', 'no']:
                return False
            else:
                console.print("[red]Please answer 'y' or 'n'[/red]")
        except KeyboardInterrupt:
            console.print("\n[yellow]Cancelled[/yellow]")
            return False


def add_argument_with_default(parser, *args, **kwargs):
    """Add an argument to argparse with default value shown in help text."""
    default = kwargs.get("default")
    if default is not None:
        help_text = kwargs.get('help', '')
        if help_text:
            kwargs["help"] = f"{help_text} (default: {default})"
        else:
            kwargs["help"] = f"(default: {default})"
    parser.add_argument(*args, **kwargs)


def select_table(
    console: Console,
    headers: list[str],
    items: list[list[str]],
    prompt: str = "Select an item",
    custom_actions: dict[str, Callable[[int, Live], None]] | None = None,
) -> list[str] | None:
    """Interactively select an item from a table using arrow keys when possible.

    Falls back to `select_from_table` (numbered input) if the optional `keyboard`
    package is not available or cannot be used in the current environment.

    Arguments:
        console: Rich Console to render to
        headers: column headers (excluding the index column)
        items: list of rows (each row is a list of string values)
        prompt: title shown above the table
        custom_actions: optional mapping from key name (e.g. 'f1', 'e') to a
            callable that receives the currently selected index and the Live
            instance. Return value ignored.
    """
    if not items:
        return None

    # If stdin isn't a tty, fall back to numbered table selection
    if not sys.stdin.isatty():
        return select_from_table(console, headers, items, prompt)

    # POSIX-safe key reader to avoid native-keyboard dependencies that crash on macOS
    def _read_key() -> str:
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch1 = sys.stdin.read(1)
            if ch1 == '\x1b':
                # Possible escape sequence
                ch2 = sys.stdin.read(1)
                if ch2 == '[':
                    ch3 = sys.stdin.read(1)
                    if ch3 == 'A':
                        return 'up'
                    if ch3 == 'B':
                        return 'down'
                    if ch3 == 'H':
                        return 'home'
                    if ch3 == 'F':
                        return 'end'
                return 'esc'
            if ch1 in ('\r', '\n'):
                return 'enter'
            return ch1
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    selected = 0
    custom_actions = custom_actions or {}

    # Helper to render the table with a highlighted selection window
    def _render_table(selected_idx: int) -> Table:
        table = Table(box=MINIMAL, title=prompt)
        table.add_column("#", justify="right")
        for header in headers:
            table.add_column(header)

        size = max(3, console.size.height - 6)
        total = len(items)

        if total <= size:
            window_start = 0
            window_rows = items
            visible_selected = selected_idx
        else:
            half = size // 2
            window_start = max(0, selected_idx - half)
            window_start = min(window_start, total - size)
            window_rows = items[window_start : window_start + size]
            visible_selected = selected_idx - window_start

        for i, row in enumerate(window_rows):
            index_label = str(window_start + i + 1)
            style = "reverse" if i == visible_selected else None
            table.add_row(index_label, *row, style=style)

        return table

    with Live(_render_table(selected), auto_refresh=False, screen=True) as live:
        try:
            while True:
                try:
                    key_name = _read_key()
                except KeyboardInterrupt:
                    return None

                # Allow custom action handlers to be invoked first
                if key_name in custom_actions:
                    try:
                        custom_actions[key_name](selected, live)
                    except Exception:
                        logging.exception("Error running custom action for key %s", key_name)
                    continue

                if key_name in ("up", "w"):
                    selected = max(0, selected - 1)
                elif key_name in ("down", "s"):
                    selected = min(len(items) - 1, selected + 1)
                elif key_name in ("home",):
                    selected = 0
                elif key_name in ("end",):
                    selected = len(items) - 1
                elif key_name in ("enter", "return"):
                    # User made a selection
                    return items[selected]
                elif key_name in ("esc", "q"):
                    # User cancelled
                    return None

                live.update(_render_table(selected), refresh=True)
        finally:
            # Ensure Live terminates cleanly; Live context will close automatically
            pass


__all__ = [
    "PathPrompt",
    "simple_select",
    "select_from_table",
    "confirm",
    "add_argument_with_default",
    "select_table",
]
