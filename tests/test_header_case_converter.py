import pytest
from src.header_case_converter import convert_to_header_case

def test_basic_string_conversion():
    """Test basic string conversion to header case."""
    assert convert_to_header_case("hello world") == "Hello World"

def test_mixed_case_string():
    """Test conversion of mixed case string."""
    assert convert_to_header_case("hello_WORLD-test") == "Hello World Test"

def test_string_with_multiple_separators():
    """Test string with multiple types of separators."""
    assert convert_to_header_case("hello__world-test_case") == "Hello World Test Case"

def test_empty_string():
    """Test conversion of an empty string."""
    assert convert_to_header_case("") == ""

def test_single_word():
    """Test conversion of a single word."""
    assert convert_to_header_case("hello") == "Hello"

def test_string_with_numbers():
    """Test string containing numbers."""
    assert convert_to_header_case("hello2world3test") == "Hello2world3test"

def test_input_with_special_characters():
    """Test string with special characters."""
    assert convert_to_header_case("hello!@#world") == "Hello World"

def test_invalid_input_type():
    """Test that TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_header_case(123)
        
def test_string_with_extra_whitespace():
    """Test string with extra whitespace."""
    assert convert_to_header_case("  hello   world  ") == "Hello World"