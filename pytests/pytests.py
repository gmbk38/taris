import pytest
def add(x, y):
    return x + y

def test_addition():
    assert add(1, 2) == 3
    assert add(0, 0) == 0
    assert add(-1, 1) == 0

def add(x, y):
    return x + y

@pytest.mark.parametrize("x, y, expected", [(1, 2, 3), (0, 0, 0), (-1, 1, 0)])
def test_addition(x, y, expected):
    assert add(x, y) == expected

@pytest.fixture
def sample_list():
    return [1, 2, 3, 4, 5]

def test_list_length(sample_list):
    assert len(sample_list) == 5

def test_list_contains_element(sample_list):
    assert 3 in sample_list

def divide(x, y):
    if y == 0:
        raise ValueError("Division by zero is not allowed")
    return x / y

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Division by zero is not allowed"):
        divide(10, 0)

@pytest.mark.smoke
def test_feature_1():
    assert True

@pytest.mark.regression
def test_feature_2():
    assert True
