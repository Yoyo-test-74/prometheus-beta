import pytest
from src.unique_grid_paths import count_unique_paths

def test_standard_grid_sizes():
    """Test unique paths for typical grid sizes"""
    assert count_unique_paths(3, 7) == 28
    assert count_unique_paths(3, 2) == 3

def test_single_dimension_grids():
    """Test grids with one dimension being 1"""
    assert count_unique_paths(1, 5) == 1
    assert count_unique_paths(5, 1) == 1

def test_square_grids():
    """Test square grids"""
    assert count_unique_paths(2, 2) == 2
    assert count_unique_paths(4, 4) == 70

def test_large_grid():
    """Test a relatively large grid"""
    assert count_unique_paths(10, 10) > 48620

def test_invalid_grid_dimensions():
    """Test error handling for invalid grid dimensions"""
    with pytest.raises(ValueError, match="Grid dimensions must be at least 1x1"):
        count_unique_paths(0, 5)
    
    with pytest.raises(ValueError, match="Grid dimensions must be at least 1x1"):
        count_unique_paths(5, 0)
    
    with pytest.raises(ValueError, match="Grid dimensions must be at least 1x1"):
        count_unique_paths(-1, 3)
        
def test_minimal_grid():
    """Test 1x1 grid"""
    assert count_unique_paths(1, 1) == 1