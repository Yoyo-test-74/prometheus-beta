import os
import pytest
from src.file_string_search import search_string_in_file

@pytest.fixture
def temp_file(tmp_path):
    """Create a temporary file with some content for testing."""
    file_path = tmp_path / "test_search_file.txt"
    file_path.write_text("Hello world\nThis is a test\nAnother line with WORLD\nLast line")
    return str(file_path)

def test_basic_string_search(temp_file):
    """Test basic string search functionality."""
    results = search_string_in_file(temp_file, "world")
    assert results == [1, 3]

def test_case_sensitive_search(temp_file):
    """Test case-sensitive search."""
    results = search_string_in_file(temp_file, "World")
    assert results == []

def test_multiple_occurrences(temp_file):
    """Test finding multiple occurrences of a string."""
    results = search_string_in_file(temp_file, "line")
    assert results == [2, 4]

def test_no_matches(temp_file):
    """Test when no matches are found."""
    results = search_string_in_file(temp_file, "python")
    assert results == []

def test_full_line_match(temp_file):
    """Test matching a full line."""
    results = search_string_in_file(temp_file, "This is a test")
    assert results == [2]

def test_file_not_found():
    """Test handling of non-existent file."""
    with pytest.raises(FileNotFoundError):
        search_string_in_file("non_existent_file.txt", "test")

def test_invalid_file_path_type():
    """Test handling of invalid file path type."""
    with pytest.raises(TypeError):
        search_string_in_file(123, "test")

def test_invalid_search_string_type():
    """Test handling of invalid search string type."""
    with pytest.raises(TypeError):
        search_string_in_file("some_file.txt", 123)

def test_empty_search_string(temp_file):
    """Test handling of empty search string."""
    with pytest.raises(ValueError):
        search_string_in_file(temp_file, "")