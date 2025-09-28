#!/usr/bin/env python3
"""
Example usage of the MTB CLI tools.

This example demonstrates the simple, cross-platform CLI utilities
that work reliably without complex keyboard handling.
"""

import sys
from pathlib import Path

# Add the parent directory to the path so we can import mtb
sys.path.insert(0, str(Path(__file__).parent.parent))

from mtb.core.cli_tools import PathPrompt, confirm, select_table, simple_select
from rich.console import Console

console = Console()


def demo_simple_select():
    """Demonstrate simple list selection."""
    console.print("\n[bold blue]Demo: Simple Selection[/bold blue]")

    options = ["Option A", "Option B", "Option C", "Exit"]
    selected = simple_select(console, options, "Choose your favorite option")

    if selected:
        console.print(f"[green]You selected: {selected}[/green]")
    else:
        console.print("[yellow]No selection made[/yellow]")


def demo_table_select():
    """Demonstrate table-based selection."""
    console.print("\n[bold blue]Demo: Table Selection[/bold blue]")

    headers = ["Name", "Type", "Description"]
    items = [
        ["config.json", "File", "Configuration file"],
        ["data/", "Directory", "Data storage"],
        ["script.py", "File", "Python script"],
        ["README.md", "File", "Documentation"],
    ]

    selected = select_table(console, headers, items, "Select a file or directory")

    if selected:
        console.print(f"[green]You selected: {' | '.join(selected)}[/green]")
    else:
        console.print("[yellow]No selection made[/yellow]")


def demo_confirm():
    """Demonstrate confirmation prompts."""
    console.print("\n[bold blue]Demo: Confirmation[/bold blue]")

    # Default to Yes
    if confirm(console, "Do you want to continue", default=True):
        console.print("[green]Continuing...[/green]")
    else:
        console.print("[red]Cancelled[/red]")

    # Default to No
    if confirm(console, "Are you sure you want to delete everything", default=False):
        console.print("[red]Deleting everything... (just kidding!)[/red]")
    else:
        console.print("[green]Phew, nothing deleted![/green]")


def demo_path_prompt():
    """Demonstrate path prompts."""
    console.print("\n[bold blue]Demo: Path Prompt[/bold blue]")
    console.print("Enter a valid existing path (try your home directory: ~)")

    try:
        path = PathPrompt.ask("Please enter a path")
        console.print(f"[green]Valid path entered: {path}[/green]")
        console.print(f"[dim]Absolute path: {path.absolute()}[/dim]")
        console.print(f"[dim]Is directory: {path.is_dir()}[/dim]")
    except KeyboardInterrupt:
        console.print("\n[yellow]Path prompt cancelled[/yellow]")


def main():
    """Run all CLI tool demonstrations."""
    console.print("[bold green]MTB CLI Tools Demo[/bold green]")
    console.print("This demo shows simple, reliable CLI interaction tools.")

    while True:
        demos = [
            "Simple Selection",
            "Table Selection",
            "Confirmation Prompts",
            "Path Prompt",
            "Exit"
        ]

        choice = simple_select(console, demos, "Choose a demo to run")

        if not choice or choice == "Exit":
            console.print("\n[green]Thanks for trying the CLI tools demo![/green]")
            break
        elif choice == "Simple Selection":
            demo_simple_select()
        elif choice == "Table Selection":
            demo_table_select()
        elif choice == "Confirmation Prompts":
            demo_confirm()
        elif choice == "Path Prompt":
            demo_path_prompt()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n\n[yellow]Demo cancelled. Goodbye![/yellow]")
