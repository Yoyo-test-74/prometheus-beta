import pytest
from src.palindrome_mirror import palindrome_mirror

def test_basic_string():
    """Test palindrome mirror with a basic string."""
    assert palindrome_mirror("hello") == "helloolleh"

def test_empty_string():
    """Test palindrome mirror with an empty string."""
    assert palindrome_mirror("") == ""

def test_single_character():
    """Test palindrome mirror with a single character."""
    assert palindrome_mirror("A") == "AA"

def test_numbers_and_special_characters():
    """Test palindrome mirror with numbers and special characters."""
    assert palindrome_mirror("A1B2!") == "A1B2!!2B1A"

def test_spaces():
    """Test palindrome mirror with spaces."""
    assert palindrome_mirror("hello world") == "hello worlddlrow olleh"

def test_invalid_input():
    """Test error handling for non-string input."""
    with pytest.raises(TypeError):
        palindrome_mirror(123)
    
    with pytest.raises(TypeError):
        palindrome_mirror(None)

def test_mixed_characters():
    """Test palindrome mirror with mixed character types."""
    assert palindrome_mirror("123 abc !@#") == "123 abc !@##@! cba 321"