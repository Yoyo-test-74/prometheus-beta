import pytest
from src.library_sort import library_sort

def test_library_sort_empty_list():
    """Test sorting an empty list."""
    assert library_sort([]) == []

def test_library_sort_single_element():
    """Test sorting a list with a single element."""
    assert library_sort([5]) == [5]

def test_library_sort_sorted_list():
    """Test sorting an already sorted list."""
    input_list = [1, 2, 3, 4, 5]
    assert library_sort(input_list) == input_list

def test_library_sort_reverse_sorted_list():
    """Test sorting a reverse sorted list."""
    input_list = [5, 4, 3, 2, 1]
    assert library_sort(input_list) == [1, 2, 3, 4, 5]

def test_library_sort_random_list():
    """Test sorting a random list of integers."""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert library_sort(input_list) == sorted(input_list)

def test_library_sort_with_duplicates():
    """Test sorting a list with duplicate elements."""
    input_list = [3, 3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert library_sort(input_list) == sorted(input_list)

def test_library_sort_with_floats():
    """Test sorting a list of floating-point numbers."""
    input_list = [3.14, 2.71, 1.41, 0.58, 2.23]
    assert library_sort(input_list) == sorted(input_list)

def test_library_sort_with_strings():
    """Test sorting a list of strings."""
    input_list = ['banana', 'apple', 'cherry', 'date']
    assert library_sort(input_list) == sorted(input_list)

def test_library_sort_none_input():
    """Test that sorting None raises a TypeError."""
    with pytest.raises(TypeError, match="Input cannot be None"):
        library_sort(None)

def test_library_sort_preserves_original_list():
    """Test that the original list is not modified."""
    original_list = [3, 1, 4, 1, 5]
    sorted_list = library_sort(original_list)
    assert original_list != sorted_list
    assert original_list == [3, 1, 4, 1, 5]  # Original list remains unchanged