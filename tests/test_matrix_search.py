import pytest
import sys
sys.path.append('.')  # Ensure the src directory can be imported

from src.matrix_search import search_sorted_matrix

def test_matrix_search_basic_cases():
    # Test basic cases with different matrix configurations
    matrix1 = [[1, 3, 5], [7, 9, 11], [13, 15, 17]]
    assert search_sorted_matrix(matrix1, 9) == True
    assert search_sorted_matrix(matrix1, 12) == False

def test_matrix_search_edge_cases():
    # Test edge cases
    assert search_sorted_matrix([], 5) == False
    assert search_sorted_matrix([[]], 5) == False
    assert search_sorted_matrix([[1]], 1) == True
    assert search_sorted_matrix([[1]], 2) == False

def test_matrix_search_unsorted_rows():
    # Test matrix with unsorted rows but sorted inner lists
    matrix2 = [[10, 20, 30], [5, 15, 25], [35, 45, 55]]
    assert search_sorted_matrix(matrix2, 15) == True
    assert search_sorted_matrix(matrix2, 22) == False

def test_matrix_search_boundary_values():
    # Test boundary values
    matrix3 = [[1, 4, 7], [10, 14, 19], [23, 30, 34]]
    assert search_sorted_matrix(matrix3, 1) == True  # First element
    assert search_sorted_matrix(matrix3, 34) == True  # Last element
    assert search_sorted_matrix(matrix3, 0) == False  # Lower than first
    assert search_sorted_matrix(matrix3, 35) == False  # Higher than last

def test_matrix_search_invalid_inputs():
    # Test invalid input types and structures
    with pytest.raises(TypeError, match="Target must be an integer"):
        search_sorted_matrix([[1, 2], [3, 4]], "5")
    
    with pytest.raises(TypeError, match="Matrix must be a list of lists"):
        search_sorted_matrix("not a matrix", 5)
    
    with pytest.raises(ValueError, match="Matrix must contain only integers"):
        search_sorted_matrix([[1, 2], [3, 'a']], 5)

def test_matrix_search_large_matrix():
    # Test a larger matrix
    large_matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    assert search_sorted_matrix(large_matrix, 5) == True
    assert search_sorted_matrix(large_matrix, 20) == False