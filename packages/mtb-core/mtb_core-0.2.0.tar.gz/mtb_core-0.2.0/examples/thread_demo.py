"""Demo for ThreadManager cooperative stop API.

Run the `run_demo()` function from your test runner or import it and call it
from a REPL. This demo does not use `if __name__ == '__main__'` per repo style.
"""

import threading
import time
from threading import Event

from mtb.core.thread import ThreadManager


def long_running_task(task_id: int, stop_event=None):
    """Run a long-running task that cooperatively checks stop_event."""
    print(f"task-{task_id}: starting")
    i = 0
    try:
        while not (stop_event and stop_event.is_set()):
            print(f"task-{task_id}: tick {i}")
            i += 1
            time.sleep(0.2)
    finally:
        print(f"task-{task_id}: exiting")


def run_demo():
    """Run a short demo of ThreadManager cooperative stop semantics."""
    tm = ThreadManager()

    # subscribe to lifecycle events
    tm.events.connect("started", lambda p: print("EVENT started ->", p))
    tm.events.connect("finished", lambda p: print("EVENT finished ->", p))
    tm.events.connect("error", lambda p: print("EVENT error ->", p))

    # add 2 cooperating tasks
    tm.add_task(long_running_task, 1, name="task-1")
    tm.add_task(long_running_task, 2, name="task-2")

    # add an external stoppable thread (Thread subclass with stop_event attr)
    class ExtThread(threading.Thread):
        def __init__(self, *a, **kw):
            super().__init__(*a, **kw)
            self.stop_event = Event()

        def run(self):
            print(f"{self.name}: external starting")
            while not self.stop_event.is_set():
                print(f"{self.name}: external tick")
                time.sleep(0.25)
            print(f"{self.name}: external exiting")

    ext = ExtThread(name="external-1")
    tm.add_thread(ext)

    # add a non-cooperative task (ignores stop_event)
    def non_cooperative(task_id: int):
        print(f"noncoop-{task_id}: starting")
        time.sleep(2.0)
        print(f"noncoop-{task_id}: exiting")

    tm.add_task(non_cooperative, 99, name="noncoop-99")

    # add a task that raises an exception to demonstrate the error event
    def error_task(stop_event=None):
        raise RuntimeError("boom")

    tm.add_task(error_task, name="err-1")

    print("starting tasks")
    tm.start_all()

    time.sleep(1.0)

    # show active count
    print("active_count before stop:", tm.active_count())

    print("stopping task-1 only (cooperative)")
    tm.stop("task-1", join=True, timeout=0.5)
    print("active_count after stopping task-1:", tm.active_count())

    print("stopping all (cooperative)")
    tm.stop_all(join=True, timeout=1.0)

    print("join results:", tm.join_all(timeout=0.1))

    print("demo complete")


if __name__ == "__main__":
    run_demo()
