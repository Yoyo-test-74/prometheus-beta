import pytest
from src.find_pairs_sum_to_target import find_pairs_sum_to_target

def test_basic_pairs():
    """Test finding pairs that sum to a target"""
    result = find_pairs_sum_to_target([1, 2, 3, 4, 5], 7)
    assert result == [(2, 5), (3, 4)]

def test_list_with_duplicates():
    """Test handling lists with duplicate numbers"""
    result = find_pairs_sum_to_target([1, 1, 2, 3, 4, 5], 6)
    assert result == [(1, 5), (2, 4)]

def test_empty_list():
    """Test behavior with an empty list"""
    result = find_pairs_sum_to_target([], 10)
    assert result == []

def test_no_pairs_found():
    """Test when no pairs sum to the target"""
    result = find_pairs_sum_to_target([1, 2, 3, 4], 10)
    assert result == []

def test_single_element_list():
    """Test list with single element"""
    result = find_pairs_sum_to_target([5], 10)
    assert result == []

def test_multiple_same_pairs():
    """Test list with multiple ways to form the same pair"""
    result = find_pairs_sum_to_target([2, 2, 3, 3, 5, 5], 7)
    # Check that all pairs in the result sum to 7
    assert all(sum(pair) == 7 for pair in result)
    # Check that the pairs involve unique numbers in the result set
    assert len(set(sum(pair) for pair in result)) == len(result)

def test_negative_numbers():
    """Test with negative numbers"""
    result = find_pairs_sum_to_target([-1, 0, 1, 2, 3], 2)
    assert result == [(-1, 3), (0, 2)]

def test_invalid_input_type():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError, match="Input must be a list"):
        find_pairs_sum_to_target("not a list", 10)
    
    with pytest.raises(TypeError, match="Target must be a number"):
        find_pairs_sum_to_target([1, 2, 3], "not a number")

def test_floating_point_target():
    """Test with floating point target"""
    result = find_pairs_sum_to_target([1.5, 2.5, 3.5, 4.5], 6.0)
    assert result == [(1.5, 4.5), (2.5, 3.5)]