# Simple test showing a fixture

import pytest

class Fruit:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

@pytest.fixture
def my_fruit():
    return Fruit("apple")

@pytest.fixture
def fruit_basket(my_fruit):
    return [Fruit("banana"), my_fruit]

def test_my_fruit_in_basket(my_fruit, fruit_basket):
    assert my_fruit in fruit_basket



# Fixture errors

@pytest.fixture
def order():
    return []


@pytest.fixture
def append_first(order):
    order.append(1)


@pytest.fixture
def append_second(order, append_first):
    order.extend([2])


@pytest.fixture(autouse=True)
def append_third(order, append_second):
    order += [3]


def test_order(order):
    assert order == [1, 2, 3]

# If, for whatever reason, order.append(1) had a bug and it raises an exception, 
# we wouldn’t be able to know if order.extend([2]) or order += [3] would also have problems. 
# After append_first throws an exception, pytest won’t run any more fixtures for test_order, 
# and it won’t even try to run test_order itself. 
# The only things that would’ve run would be order and append_first
