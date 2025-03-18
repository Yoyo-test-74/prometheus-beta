import pytest
from src.fibonacci_memoized import fibonacci_memoized

def test_fibonacci_base_cases():
    """Test the base cases of Fibonacci sequence."""
    assert fibonacci_memoized(0) == 0
    assert fibonacci_memoized(1) == 1

def test_fibonacci_known_values():
    """Test known Fibonacci numbers."""
    test_cases = [
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (6, 8),
        (7, 13),
        (10, 55)
    ]
    
    for n, expected in test_cases:
        assert fibonacci_memoized(n) == expected

def test_fibonacci_negative_input():
    """Test that negative inputs raise a ValueError."""
    with pytest.raises(ValueError, match="Fibonacci index cannot be negative"):
        fibonacci_memoized(-1)

def test_fibonacci_non_integer_input():
    """Test that non-integer inputs raise a TypeError."""
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci_memoized(3.14)
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci_memoized("5")

def test_fibonacci_memoization():
    """Verify that memoization works correctly."""
    # Create a custom memo dict to track function calls
    memo = {}
    
    # First call should calculate and store
    result1 = fibonacci_memoized(10, memo)
    assert result1 == 55
    
    # Second call should retrieve from memo without additional calculations
    result2 = fibonacci_memoized(10, memo)
    assert result2 == 55
    
    # The memo should contain the expected keys
    expected_memoized_keys = set(range(11))
    assert set(memo.keys()) == expected_memoized_keys