import pytest

# WRITING AND REPORTING ASSERTATIONS IN TESTS



# Asserting with the assert statement(used to cerify expectations and values in Python)
def func(x):
    return x + 3

def test_answer():
    assert func(4) == 7



# Assertions about expected exceptions

def test_zero_division():
    with pytest.raises(ZeroDivisionError): # a built-in Python exception thrown when a number is divided by 0.
        2/0


def test_recursion_depth():
    with pytest.raises(RuntimeError) as excinfo:

        def f():
            f()

        f()
    assert "maximum recursion" in str(excinfo.value) # if you need to have access to the actual exception info (.type, .value, .traceback)