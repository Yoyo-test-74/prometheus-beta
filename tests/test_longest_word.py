import pytest
from src.longest_word import find_longest_word

def test_basic_sentence():
    """Test finding the longest word in a basic sentence."""
    assert find_longest_word("The quick brown fox jumps over") == "quick"

def test_multiple_longest_words():
    """Test that the first longest word is returned when multiple exist."""
    assert find_longest_word("cat banana apple longest") == "banana"

def test_single_word():
    """Test with a single word."""
    assert find_longest_word("hello") == "hello"

def test_words_with_numbers():
    """Test words that include numbers."""
    assert find_longest_word("hello world python3 programming") == "programming"

def test_sentence_with_punctuation():
    """Test sentence with punctuation."""
    assert find_longest_word("Hello, world! How are you?") == "Hello"

def test_multiple_whitespaces():
    """Test sentence with multiple whitespace characters."""
    assert find_longest_word("  the   quick   brown   fox  ") == "quick"

def test_empty_string_raises_error():
    """Test that empty string raises a ValueError."""
    with pytest.raises(ValueError, match="Input sentence cannot be empty"):
        find_longest_word("")

def test_whitespace_only_raises_error():
    """Test that whitespace-only input raises a ValueError."""
    with pytest.raises(ValueError, match="Input sentence contains no valid words"):
        find_longest_word("   \t\n  ")

def test_non_string_input_raises_error():
    """Test that non-string input raises a TypeError."""
    with pytest.raises(TypeError, match="Input must be a string"):
        find_longest_word(123)

def test_unicode_words():
    """Test finding longest word with unicode characters."""
    assert find_longest_word("café résumé longer") == "résumé"