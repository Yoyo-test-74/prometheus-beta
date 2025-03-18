import pytest
from src.bubble_sort import bubble_sort

def test_bubble_sort_basic():
    """Test basic sorting of integers."""
    assert bubble_sort([5, 2, 9, 1, 7]) == [1, 2, 5, 7, 9]

def test_bubble_sort_already_sorted():
    """Test list that is already sorted."""
    assert bubble_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_bubble_sort_reverse_sorted():
    """Test list in reverse order."""
    assert bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_bubble_sort_duplicate_elements():
    """Test list with duplicate elements."""
    assert bubble_sort([3, 1, 4, 1, 5, 9, 2, 6, 5]) == [1, 1, 2, 3, 4, 5, 5, 6, 9]

def test_bubble_sort_empty_list():
    """Test empty list."""
    assert bubble_sort([]) == []

def test_bubble_sort_single_element():
    """Test list with a single element."""
    assert bubble_sort([42]) == [42]

def test_bubble_sort_floating_point():
    """Test sorting of floating point numbers."""
    assert bubble_sort([3.14, 2.71, 1.41, 0.58]) == [0.58, 1.41, 2.71, 3.14]

def test_bubble_sort_mixed_numeric():
    """Test sorting of mixed numeric types."""
    assert bubble_sort([5, 2.5, 7, 1.2, 3]) == [1.2, 2.5, 3, 5, 7]

def test_bubble_sort_non_list_input():
    """Test that non-list input raises TypeError."""
    with pytest.raises(TypeError):
        bubble_sort("not a list")

def test_bubble_sort_non_comparable_elements():
    """Test that non-comparable elements raise TypeError."""
    with pytest.raises(TypeError):
        bubble_sort([1, 2, "3", 4])

def test_bubble_sort_original_list_unchanged():
    """Test that the original list is not modified."""
    original = [5, 2, 9, 1, 7]
    bubble_sort(original)
    assert original == [5, 2, 9, 1, 7]