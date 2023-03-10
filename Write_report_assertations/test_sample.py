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


def myfunc(): # You can pass a match keyword parameter to the context-manager(pytest.raises) to test that a reg-exp matches on the string representation of an exception
    raise ValueError("Exception 123 raised")

def test_match():
    with pytest.raises(ValueError, match=r".* 123 .*"): # The regexp param of the match method is matched with the re.search func, so in this e.g, match='123' would worked.
        myfunc()

# an alternate form of the pytest.raises() function where you pass a function that will be executed with the given *args and **kwargs and assert that the given exception is raised:
# pytest.raises(ExpectedException, func, *args, **kwargs)
#
#
# that it is also possible to specify a “raises” argument to pytest.mark.xfail, which checks that the test is failing in a more specific way than just having any exception raised:
# @pytest.mark.xfail(raises=IndexError)
# def test_f():
#    f()


# Assertions about expected warnings ( research PYTEST.WARNS)



# Making use of context-sensitive comparisons ( in test_comparison.py )



# Defining your own explanation for failed assertions ( in conftest.py and test_foocompare.py )


# ASSERTION INSPECTION DETAILS
# You can manually enable assertion rewriting for an imported module by calling register_assert_rewrite before you import it (a good place to do that is in your root conftest.py).

# Assertion rewriting caches files on disk:
# pytest will write back the rewritten modules to disk for caching. You can disable this behavior (for example to avoid leaving stale .pyc files around in projects that move files around a lot) by adding this to the top of your conftest.py file:
# import sys
# sys.dont_write_bytecode = True

# Disabling assert rewriting:
# pytest rewrites test modules on import by using an import hook to write new pyc files. Most of the time this works transparently. However, if you are working with the import machinery yourself, the import hook may interfere. If this is the case you have two options: 
# Disable rewriting for a specific module by adding the string PYTEST_DONT_REWRITE to its docstring.
# Disable rewriting for all modules by using --assert=plain.