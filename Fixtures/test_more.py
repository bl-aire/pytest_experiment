# A FIXTURE CAN REQUEST MORE THAN ONE FIXTURE AT A TIME


import pytest

#Arrange
@pytest.fixture
def first_entry():
    return "a"

# Arrange
@pytest.fixture
def second_entry():
    return "b"

#Arrange
@pytest.fixture
def order(first_entry, second_entry):
    return [first_entry, second_entry]

#Arrange
@pytest.fixture
def expected_list():
    return ["a", "b", 3.0]

def test_string(order, expected_list):
    # Act 
    order.append(3.0)

    # Assert
    assert order == expected_list