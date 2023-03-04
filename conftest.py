# It is possible to add your own detailed explanations by implementing the pytest_assertrepr_compare hook....pytest_assertrepr_compare(config, op, left, right)....pytest config object, operator, left operand, right operand
#
# Return None for no custom explanation, otherwise return a list of strings. The strings will be joined by newlines but any newlines in a string will be escaped. Note that all but the first line will be indented slightly, the intention is for the first line to be a summary.
#
# Run pytest -q test_foocompare.py on the CLI to test


from test_foocompare import Foo 

def pytest_assertrepr_compare(op, left, right):
    if isinstance(left, Foo) and isinstance(right, Foo) and op == "==":
        return[
            "Comparing Foo instances:",
            f" vals: {left.val}  != {right.val}",
        ]