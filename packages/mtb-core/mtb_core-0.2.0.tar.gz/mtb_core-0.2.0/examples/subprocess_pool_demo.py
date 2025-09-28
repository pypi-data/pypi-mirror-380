"""
Example usage of the improved SubprocessPool.

This example demonstrates how to use the new, more robust SubprocessPool
that automatically detects shells and handles errors properly.
"""

from mtb.core.SubprocessPool import SubprocessPool
from rich.console import Console

console = Console()


def example_basic_usage():
    """Demonstrate basic usage example."""
    console.print("=== Basic Usage Example ===")

    # Create pool with context manager for automatic cleanup
    with SubprocessPool(max_concurrent=2) as pool:
        # Add some tasks
        task1 = pool.add_task("echo 'Hello from task 1'")
        task2 = pool.add_task("echo 'Hello from task 2'")
        task3 = pool.add_task("ls -la /tmp | head -5")

        # Connect to signals to see output
        task1.on_std_out.connect(lambda line: console.print(f"Task1 output: {line}"))
        task2.on_std_out.connect(lambda line: console.print(f"Task2 output: {line}"))
        task3.on_std_out.connect(lambda line: console.print(f"Task3 output: {line}"))

        # Connect to completion signals
        task1.on_done.connect(lambda task: console.print(f"Task1 completed: {task.command}"))
        task2.on_done.connect(lambda task: console.print(f"Task2 completed: {task.command}"))
        task3.on_done.connect(lambda task: console.print(f"Task3 completed: {task.command}"))

        # Run all tasks
        pool.run()
        pool.wait()  # Wait for completion

        console.print(f"All tasks completed. Task1 exit code: {task1.result_code}")


def example_with_shell_detection():
    """Demonstrate shell auto-detection functionality."""
    console.print("\n=== Shell Auto-Detection Example ===")

    with SubprocessPool() as pool:
        # Let the pool auto-detect the shell
        task1 = pool.add_task("echo 'Auto-detected shell command'")
        task2 = pool.add_task("pwd")

        # Show which shell was detected
        console.print(f"Detected shell: {pool.shell}")

        # Connect signals
        task1.on_std_out.connect(lambda line: console.print(f"Shell task 1: {line}"))
        task2.on_std_out.connect(lambda line: console.print(f"Shell task 2: {line}"))

        pool.run()
        pool.wait()


def example_error_handling():
    """Demonstrate error handling with early_fail."""
    console.print("\n=== Error Handling Example ===")

    try:
        with SubprocessPool(max_concurrent=2, early_fail=True) as pool:
            good_task = pool.add_task("echo 'This will work'")
            bad_task = pool.add_task("this-command-does-not-exist-12345")
            another_task = pool.add_task("echo 'This might not run due to early_fail'")

            # Connect signals
            good_task.on_std_out.connect(lambda line: console.print(f"Good task: {line}"))
            good_task.on_done.connect(
                lambda task: console.print("Good task completed successfully")
            )

            bad_task.on_failure.connect(
                lambda task: console.print(f"[red]Bad task failed as expected: {task.command}[/]")
            )
            bad_task.on_std_err.connect(lambda line: console.print(f"[red]Bad task error: {line}[/]"))

            another_task.on_std_out.connect(lambda line: console.print(f"Another task: {line}"))

            pool.run()
            pool.wait()

    except Exception as e:
        console.print(f"Pool execution failed as expected: {e}")


def example_without_early_fail():
    """Demonstrate running tasks without early failure mode."""
    console.print("\n=== No Early Fail Example ===")

    with SubprocessPool(max_concurrent=3, early_fail=False) as pool:
        good_task1 = pool.add_task("echo 'First good task'")
        bad_task = pool.add_task("this-command-does-not-exist-67890")
        good_task2 = pool.add_task("echo 'Second good task runs despite failure'")

        # Connect signals
        good_task1.on_std_out.connect(lambda line: console.print(f"Good task 1: {line}"))
        good_task1.on_done.connect(lambda task: console.print("Good task 1 completed"))

        bad_task.on_failure.connect(
            lambda task: console.print(f"[red]Bad task failed: exit code {task.result_code}[/]")
        )

        good_task2.on_std_out.connect(lambda line: console.print(f"Good task 2: {line}"))
        good_task2.on_done.connect(lambda task: console.print("Good task 2 completed"))

        pool.run()
        pool.wait()

        console.print("All tasks processed (some may have failed)")


if __name__ == "__main__":
    example_basic_usage()
    example_with_shell_detection()
    example_error_handling()
    example_without_early_fail()
