import pytest
from src.symmetric_difference import symmetric_difference

def test_symmetric_difference_basic():
    """Test basic symmetric difference between two lists"""
    assert sorted(symmetric_difference([1, 2, 3], [3, 4, 5])) == [1, 2, 4, 5]

def test_symmetric_difference_empty_lists():
    """Test symmetric difference with empty lists"""
    assert symmetric_difference([], []) == []

def test_symmetric_difference_one_empty_list():
    """Test symmetric difference with one empty list"""
    assert sorted(symmetric_difference([1, 2, 3], [])) == [1, 2, 3]

def test_symmetric_difference_duplicate_elements():
    """Test symmetric difference with duplicate elements"""
    assert sorted(symmetric_difference([1, 1, 2, 3], [3, 3, 4, 5])) == [1, 2, 4, 5]

def test_symmetric_difference_same_lists():
    """Test symmetric difference of identical lists"""
    assert symmetric_difference([1, 2, 3], [1, 2, 3]) == []

def test_symmetric_difference_invalid_input():
    """Test that TypeError is raised for non-list inputs"""
    with pytest.raises(TypeError):
        symmetric_difference(1, [1, 2, 3])
    
    with pytest.raises(TypeError):
        symmetric_difference([1, 2, 3], "not a list")

def test_symmetric_difference_complex_types():
    """Test symmetric difference with complex types"""
    result = symmetric_difference([1, "a"], ["a", 2])
    assert sorted(result) == [1, 2]