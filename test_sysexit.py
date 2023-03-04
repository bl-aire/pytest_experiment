# Assert that a certain exception is raised
# pytest -q test_sysexit.py............-q/--quiet gives a brief output on terminal
import pytest

def f():
    raise SystemExit(1)

def test_sysexit():
    with pytest.raises(SystemExit):
        f()