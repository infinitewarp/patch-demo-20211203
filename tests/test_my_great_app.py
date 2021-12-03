import contextlib
from unittest.mock import patch

from my_great_app import InterestingThing, Locks


def test_patching_whole_locks_class():
    @contextlib.contextmanager
    def fake_exclusive_lock(*args, **kwargs):
        print(f"fake_exclusive_lock entering with inputs ({args}, {kwargs})")
        assert args == (5, 6)
        assert kwargs == {"taters": "precious"}
        yield
        print("fake_exclusive_lock exiting")

    with patch("my_great_app.Locks") as mock_locks_class:
        mock_locks_class.return_value.exclusive_lock.side_effect = fake_exclusive_lock

        thing = InterestingThing()
        thing.interesting_method()

    mock_locks_class.return_value.exclusive_lock.assert_called_once_with(5, 6, taters="precious")


def test_patching_only_the_exclusive_lock_function():
    @contextlib.contextmanager
    def fake_exclusive_lock(*args, **kwargs):
        print(f"fake_exclusive_lock entering with inputs ({args}, {kwargs})")
        assert args == (5, 6)
        assert kwargs == {"taters": "precious"}
        yield
        print("fake_exclusive_lock exiting")

    with patch.object(Locks, "exclusive_lock") as mock_exclusive_lock_function:
        mock_exclusive_lock_function.side_effect = fake_exclusive_lock

        thing = InterestingThing()
        thing.interesting_method()

    mock_exclusive_lock_function.assert_called_once_with(5, 6, taters="precious")
