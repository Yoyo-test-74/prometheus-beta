import pytest
from src.middle_range_indices import find_middle_range_indices

def test_odd_length_list_default_range():
    """Test with an odd-length list"""
    test_list = [1, 2, 3, 4, 5, 6, 7]
    result = find_middle_range_indices(test_list, 1)
    assert result == [2, 3, 4]

def test_even_length_list_default_range():
    """Test with an even-length list"""
    test_list = [1, 2, 3, 4, 5, 6]
    result = find_middle_range_indices(test_list, 1)
    assert result == [2, 3, 4]

def test_larger_range():
    """Test with a larger range"""
    test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = find_middle_range_indices(test_list, 2)
    assert result == [2, 3, 4, 5, 6]

def test_range_size_zero():
    """Test with zero range size"""
    test_list = [1, 2, 3, 4, 5]
    result = find_middle_range_indices(test_list, 0)
    assert result == [2]

def test_range_exceeds_list_bounds():
    """Test when range size would exceed list bounds"""
    test_list = [1, 2, 3, 4, 5]
    result = find_middle_range_indices(test_list, 10)
    assert result == list(range(5))

def test_invalid_input_types():
    """Test invalid input types"""
    with pytest.raises(TypeError):
        find_middle_range_indices("not a list", 1)
    
    with pytest.raises(TypeError):
        find_middle_range_indices([1, 2, 3], "not an int")

def test_negative_range_size():
    """Test negative range size"""
    with pytest.raises(ValueError):
        find_middle_range_indices([1, 2, 3], -1)

def test_empty_list():
    """Test empty list"""
    with pytest.raises(ValueError):
        find_middle_range_indices([], 1)