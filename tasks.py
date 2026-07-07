import time


def add(x, y):
    """Trivial example job."""
    return x + y


def slow_task(seconds=5):
    """Example long-running job."""
    time.sleep(seconds)
    return f"slept for {seconds}s"
