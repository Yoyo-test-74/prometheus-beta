import pytest
from src.second_highest_value import find_second_highest

def test_ascending_list():
    assert find_second_highest([1, 2, 3, 4, 5]) == 4

def test_descending_list():
    assert find_second_highest([5, 4, 3, 2, 1]) == 4

def test_list_with_duplicates():
    assert find_second_highest([1, 2, 2, 3, 3, 4, 5]) == 4

def test_single_unique_value():
    assert find_second_highest([1, 1, 1, 1]) is None

def test_two_unique_values():
    assert find_second_highest([1, 2]) == 1

def test_raises_type_error_on_non_list():
    with pytest.raises(TypeError):
        find_second_highest("not a list")

def test_raises_value_error_on_empty_list():
    with pytest.raises(ValueError):
        find_second_highest([])