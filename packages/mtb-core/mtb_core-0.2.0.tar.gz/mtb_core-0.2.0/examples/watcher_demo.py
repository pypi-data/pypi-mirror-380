"""Demo for the Watcher utility.

Creates a temporary directory, starts a Watcher that watches for '*.txt'
files, then touches and writes a file several times quickly to show
that debounce coalesces the events.
"""

# import logging
import tempfile
import time
from pathlib import Path

from mtb.core.watcher import Watcher


def run_demo():
    """Run the watcher demo: create files and show collected events."""
    with tempfile.TemporaryDirectory() as td:
        d = Path(td)
        print("Watching directory:", d)

        # enable debug logging so the watcher internals are visible
        # logging.basicConfig(level=logging.DEBUG)

        events = []

        def cb(ev):
            print("EVENT:", ev.event_type, ev.src_path)
            events.append((ev.event_type, ev.src_path))

        # watch only .txt files and debounce by 0.1s
        w = Watcher(d, patterns=("*.txt",), debounce=0.1)
        w.add_callback(cb)

        try:
            w.start()
            # allow observer thread to start
            time.sleep(0.2)

            f = d / "test.txt"

            # Rapid writes - these should coalesce to a single dispatched event
            for i in range(4):
                f.write_text(f"{i}\n")
                time.sleep(0.02)

            # write a non-matching file - should be ignored
            (d / "ignore.log").write_text("noisy")

            # give debounce a chance to fire
            time.sleep(0.5)

        finally:
            w.close()

        print("collected events:", events)


if __name__ == "__main__":
    run_demo()
