import pytest
from src.sum_even_indexed_elements import sum_even_indexed_elements

def test_sum_even_indexed_elements_normal_list():
    """Test with a normal list of positive integers."""
    assert sum_even_indexed_elements([1, 2, 3, 4, 5]) == 9

def test_sum_even_indexed_elements_mixed_integers():
    """Test with a list containing both positive and negative integers."""
    assert sum_even_indexed_elements([-1, 2, -3, 4, -5]) == -4

def test_sum_even_indexed_elements_empty_list():
    """Test with an empty list."""
    assert sum_even_indexed_elements([]) == 0

def test_sum_even_indexed_elements_single_element():
    """Test with a single-element list."""
    assert sum_even_indexed_elements([42]) == 42

def test_sum_even_indexed_elements_two_elements():
    """Test with a two-element list."""
    assert sum_even_indexed_elements([10, 20]) == 10

def test_sum_even_indexed_elements_zero_values():
    """Test with a list containing zero values."""
    assert sum_even_indexed_elements([0, 1, 0, 2, 0]) == 0