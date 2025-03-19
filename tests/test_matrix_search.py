import pytest
from src.matrix_search import search_matrix

def test_search_matrix_basic_found():
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ]
    assert search_matrix(matrix, 3) == True
    assert search_matrix(matrix, 13) == False

def test_search_matrix_edge_cases():
    # Empty matrix
    assert search_matrix([], 5) == False
    assert search_matrix([[]], 5) == False

    # Single element matrix
    matrix = [[5]]
    assert search_matrix(matrix, 5) == True
    assert search_matrix(matrix, 6) == False

def test_search_matrix_boundary_values():
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ]
    # Test first and last elements
    assert search_matrix(matrix, 1) == True
    assert search_matrix(matrix, 60) == True

def test_search_matrix_invalid_input():
    # Invalid matrix type
    with pytest.raises(TypeError):
        search_matrix("not a matrix", 5)
    
    # Invalid matrix row type
    with pytest.raises(TypeError):
        search_matrix([[1, 2], "not a row"], 5)
    
    # Non-integer matrix
    with pytest.raises(ValueError):
        search_matrix([[1, 2], [3, "4"]], 5)

def test_search_matrix_sorted_property():
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ]
    # Each row is sorted
    # Each row's first element is greater than previous row's last element
    for i in range(1, len(matrix)):
        assert matrix[i][0] > matrix[i-1][-1]

def test_search_matrix_large_matrix():
    # Create a large sorted matrix
    large_matrix = [[i * 10 + j for j in range(10)] for i in range(50)]
    
    # Test finding elements
    assert search_matrix(large_matrix, 42) == True
    assert search_matrix(large_matrix, 100) == True
    assert search_matrix(large_matrix, 501) == False

def test_search_matrix_negative_elements():
    matrix = [
        [-5, -3, 0],
        [2, 5, 7],
        [10, 15, 20]
    ]
    assert search_matrix(matrix, -3) == True
    assert search_matrix(matrix, -4) == False
    assert search_matrix(matrix, 20) == True
    assert search_matrix(matrix, 21) == False