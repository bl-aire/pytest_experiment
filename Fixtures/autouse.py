import pytest


@pytest.fixture
def first_entry():
    return "a"


@pytest.fixture
def order(first_entry):
    return []


@pytest.fixture(autouse=True)
def append_first(order, first_entry):
    return order.append(first_entry)


def test_string_only(order, first_entry):
    assert order == [first_entry] # Autouse” fixtures are a convenient way to make all tests automatically request them...(Array containing first order is returned in the auto use fixture but others after are affected though neither test requested it. THEY CAN BE REQUESTED )


def test_string_and_int(order, first_entry):
    order.append(2)
    assert order == [first_entry, 2] # Autouse” fixtures are a convenient way to make all tests automatically request them