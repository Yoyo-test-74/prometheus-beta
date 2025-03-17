import pytest
from src.word_count import count_words

def test_count_words_normal_case():
    """Test counting words in a normal sentence."""
    assert count_words("Hello world") == 2

def test_count_words_multiple_spaces():
    """Test counting words with multiple spaces between words."""
    assert count_words("Hello   world    python") == 3

def test_count_words_leading_trailing_spaces():
    """Test counting words with leading and trailing spaces."""
    assert count_words("  Hello world  ") == 2

def test_count_words_empty_string():
    """Test counting words in an empty string."""
    assert count_words("") == 0

def test_count_words_whitespace_only():
    """Test counting words in a string with only whitespace."""
    assert count_words("   \t\n  ") == 0

def test_count_words_single_word():
    """Test counting words in a single word."""
    assert count_words("python") == 1

def test_count_words_none_input():
    """Test handling of None input."""
    assert count_words(None) == 0