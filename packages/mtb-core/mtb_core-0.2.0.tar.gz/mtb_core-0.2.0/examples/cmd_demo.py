#!/usr/bin/env python3
"""
Example usage of the MTB CommandRunner.

This example demonstrates the async command runner that provides real-time output
streaming via the observer pattern.
"""

import asyncio

from mtb.core.cmd import CollectorObserver, CommandRunner, PrintObserver
from rich.console import Console

console = Console()


async def demo_basic_command():
    """Demonstrate basic command execution with real-time output."""
    console.print("\n[bold blue]Demo: Basic Command Execution[/bold blue]")

    runner = CommandRunner()
    observer = PrintObserver("[BASIC] ")

    # Add observer to see real-time output
    runner.subscribe(observer)

    # Run a simple command
    console.print("Running: [cyan]echo 'Hello World!'[/cyan]")
    return_code = await runner.run_command("echo 'Hello World!'")

    console.print(f"[green]Command completed with return code: {return_code}[/green]")


async def demo_long_running_command():
    """Demonstrate a command that produces output over time."""
    console.print("\n[bold blue]Demo: Long Running Command[/bold blue]")

    runner = CommandRunner()
    observer = PrintObserver("[LONG] ")
    runner.subscribe(observer)

    # Run a command that produces output over time
    console.print('Running: [cyan]for i in {1..5}; do echo "Line $i"; sleep 1; done[/cyan]')
    return_code = await runner.run_command('for i in {1..5}; do echo "Line $i"; sleep 1; done')

    console.print(f"[green]Command completed with return code: {return_code}[/green]")


async def demo_command_with_error():
    """Demonstrate command that produces both stdout and stderr."""
    console.print("\n[bold blue]Demo: Command with Error Output[/bold blue]")

    runner = CommandRunner()
    observer = PrintObserver("[ERROR] ")
    runner.subscribe(observer)

    # Command that writes to both stdout and stderr
    console.print("Running: [cyan]echo 'Success' && echo 'Warning' >&2[/cyan]")
    return_code = await runner.run_command("echo 'Success' && echo 'Warning' >&2")

    console.print(f"[green]Command completed with return code: {return_code}[/green]")


async def demo_collector_observer():
    """Demonstrate collecting all output for later processing."""
    console.print("\n[bold blue]Demo: Output Collection[/bold blue]")

    runner = CommandRunner()
    collector = CollectorObserver()
    runner.subscribe(collector)

    # Run multiple commands
    commands = ["echo 'First command'", "echo 'Second command'", "ls /tmp | head -3"]

    for i, cmd in enumerate(commands, 1):
        console.print(f"Running command {i}: [cyan]{cmd}[/cyan]")
        await runner.run_command(cmd)

    # Show collected results
    console.print("\n[bold green]Collected Results:[/bold green]")
    for i, (return_code, stdout, stderr) in enumerate(collector.completed_commands, 1):
        console.print(f"Command {i} (exit {return_code}):")
        if stdout:
            for line in stdout:
                console.print(f"  [green]OUT:[/green] {line}")
        if stderr:
            for line in stderr:
                console.print(f"  [red]ERR:[/red] {line}")


async def demo_timeout():
    """Demonstrate command timeout handling."""
    console.print("\n[bold blue]Demo: Command Timeout[/bold blue]")

    runner = CommandRunner()
    observer = PrintObserver("[TIMEOUT] ")
    runner.subscribe(observer)

    console.print("Running: [cyan]sleep 5[/cyan] with 2 second timeout")

    try:
        return_code = await runner.run_command("sleep 5", timeout=2.0)
        console.print(f"[green]Command completed with return code: {return_code}[/green]")
    except asyncio.TimeoutError:
        console.print("[red]Command timed out as expected![/red]")


async def demo_list_command():
    """Demonstrate running command from a list of arguments."""
    console.print("\n[bold blue]Demo: List Command Format[/bold blue]")

    runner = CommandRunner()
    observer = PrintObserver("[LIST] ")
    runner.subscribe(observer)

    # Command as list (safer for complex arguments)
    cmd_list = ["echo", "Hello from list command!"]
    console.print(f"Running: [cyan]{' '.join(cmd_list)}[/cyan]")
    return_code = await runner.run_command(cmd_list)

    console.print(f"[green]Command completed with return code: {return_code}[/green]")


async def main():
    """Run all command runner demonstrations."""
    console.print("[bold green]MTB CommandRunner Demo[/bold green]")
    console.print("This demo shows async command execution with real-time output streaming.\n")

    demos = [
        ("Basic Command", demo_basic_command),
        ("Long Running Command", demo_long_running_command),
        ("Command with Error", demo_command_with_error),
        ("Output Collection", demo_collector_observer),
        ("Timeout Handling", demo_timeout),
        ("List Command Format", demo_list_command),
    ]

    for name, demo_func in demos:
        console.print(f"\n[dim]Press Enter to run: {name}[/dim]")
        input()
        await demo_func()

    console.print("\n[green]All demos completed![/green]")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        console.print("\n\n[yellow]Demo cancelled. Goodbye![/yellow]")
