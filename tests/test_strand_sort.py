import pytest
from src.strand_sort import strand_sort

def test_strand_sort_empty_list():
    """Test sorting an empty list"""
    assert strand_sort([]) == []

def test_strand_sort_single_element():
    """Test sorting a list with a single element"""
    assert strand_sort([5]) == [5]

def test_strand_sort_already_sorted():
    """Test sorting a list that is already sorted"""
    input_list = [1, 2, 3, 4, 5]
    assert strand_sort(input_list) == input_list

def test_strand_sort_reverse_sorted():
    """Test sorting a list in reverse order"""
    input_list = [5, 4, 3, 2, 1]
    assert strand_sort(input_list) == [1, 2, 3, 4, 5]

def test_strand_sort_unsorted_list():
    """Test sorting an unsorted list"""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    assert strand_sort(input_list) == [1, 1, 2, 3, 4, 5, 5, 6, 9]

def test_strand_sort_with_duplicates():
    """Test sorting a list with duplicate elements"""
    input_list = [3, 3, 1, 4, 1, 5, 9, 2, 6, 5]
    assert strand_sort(input_list) == [1, 1, 2, 3, 3, 4, 5, 5, 6, 9]

def test_strand_sort_type_error():
    """Test that a TypeError is raised for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        strand_sort("not a list")
    with pytest.raises(TypeError, match="Input must be a list"):
        strand_sort(123)
    with pytest.raises(TypeError, match="Input must be a list"):
        strand_sort(None)