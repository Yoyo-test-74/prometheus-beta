import pytest
from src.reverse_substring_vowels import reverse_substring_vowels

def test_basic_vowel_reversal():
    """Test basic vowel reversal in a substring"""
    assert reverse_substring_vowels("hello world", 0, 5) == "hollo werld"

def test_no_vowels_in_substring():
    """Test when no vowels are in the substring"""
    assert reverse_substring_vowels("hello world", 6, 11) == "hello world"

def test_all_vowels_in_substring():
    """Test when all characters in substring are vowels"""
    assert reverse_substring_vowels("hello iouae world", 6, 11) == "hello uoiea world"

def test_mixed_case_vowels():
    """Test with mixed case vowels"""
    assert reverse_substring_vowels("hEllO wOrld", 0, 5) == "hOllE wOrld"

def test_full_string_reversal():
    """Test reversing vowels in the entire string"""
    assert reverse_substring_vowels("hello world", 0, 11) == "hollo werld"

def test_invalid_start_index():
    """Test invalid start index"""
    with pytest.raises(ValueError):
        reverse_substring_vowels("hello", -1, 3)

def test_invalid_end_index():
    """Test invalid end index"""
    with pytest.raises(ValueError):
        reverse_substring_vowels("hello", 0, 6)

def test_start_greater_than_end():
    """Test when start index is greater than end index"""
    with pytest.raises(ValueError):
        reverse_substring_vowels("hello", 3, 2)

def test_non_string_input():
    """Test non-string input"""
    with pytest.raises(TypeError):
        reverse_substring_vowels(123, 0, 3)

def test_non_integer_indices():
    """Test non-integer indices"""
    with pytest.raises(TypeError):
        reverse_substring_vowels("hello", "0", 3)

def test_empty_string():
    """Test empty string"""
    assert reverse_substring_vowels("", 0, 0) == ""

def test_substring_with_no_modification():
    """Test substring where no reversing occurs"""
    assert reverse_substring_vowels("xyz", 0, 3) == "xyz"