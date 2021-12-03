import contextlib
import threading


class Locks:
    def __init__(self):
        self._threading_lock = threading.Lock()

    @contextlib.contextmanager
    def exclusive_lock(self, *args, **kwargs):
        print(f"trying to get lock using inputs ({args}, {kwargs})")
        self._threading_lock.acquire()
        print("lock acquired")
        yield
        print("releasing lock")
        self._threading_lock.release()
        print("lock released")


class InterestingThing:
    def __init__(self):
        self._lock_manager = Locks()

    def interesting_method(self):
        print("hello world!")
        with self._lock_manager.exclusive_lock(5, 6, taters="precious"):
            print("my code running while locked!")
        print("goodbye world!")
