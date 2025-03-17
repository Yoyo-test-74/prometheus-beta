import pytest
from src.digit_sum import sum_digits

def test_sum_digits_positive_numbers():
    """Test sum of digits for positive numbers."""
    assert sum_digits(123) == 6
    assert sum_digits(456) == 15
    assert sum_digits(9) == 9
    assert sum_digits(0) == 0

def test_sum_digits_large_number():
    """Test sum of digits for large numbers."""
    assert sum_digits(1234567890) == 45

def test_sum_digits_invalid_inputs():
    """Test error handling for invalid inputs."""
    # Negative number should raise ValueError
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        sum_digits(-123)
    
    # Non-integer input should raise TypeError
    with pytest.raises(TypeError, match="Input must be an integer"):
        sum_digits("123")
    with pytest.raises(TypeError, match="Input must be an integer"):
        sum_digits(3.14)
    with pytest.raises(TypeError, match="Input must be an integer"):
        sum_digits(None)