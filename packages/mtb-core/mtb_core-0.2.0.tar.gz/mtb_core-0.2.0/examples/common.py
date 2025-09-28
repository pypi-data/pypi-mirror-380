from rich.console import Console

console = Console()


def log(*msgs):
    console.print(*msgs)

def warn(message: str):
    console.print(f"[yellow]{message}[/yellow]")

