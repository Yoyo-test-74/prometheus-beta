import os
import pytest

from src.write_to_file import write_string_to_file

def test_write_string_to_file_normal_case(tmp_path):
    """Test writing a normal string to a file."""
    test_file = tmp_path / "test_file.txt"
    test_content = "Hello, World!"
    
    write_string_to_file(str(test_file), test_content)
    
    assert test_file.exists()
    with open(test_file, 'r', encoding='utf-8') as file:
        assert file.read() == test_content

def test_write_string_to_file_empty_string(tmp_path):
    """Test writing an empty string to a file."""
    test_file = tmp_path / "empty_file.txt"
    test_content = ""
    
    write_string_to_file(str(test_file), test_content)
    
    assert test_file.exists()
    with open(test_file, 'r', encoding='utf-8') as file:
        assert file.read() == ""

def test_write_string_to_file_unicode(tmp_path):
    """Test writing a file with unicode characters."""
    test_file = tmp_path / "unicode_file.txt"
    test_content = "Héllo, 世界!"
    
    write_string_to_file(str(test_file), test_content)
    
    assert test_file.exists()
    with open(test_file, 'r', encoding='utf-8') as file:
        assert file.read() == test_content

def test_write_string_to_file_invalid_filepath_type():
    """Test passing non-string file path raises TypeError."""
    with pytest.raises(TypeError, match="file_path must be a string"):
        write_string_to_file(123, "test content")

def test_write_string_to_file_invalid_content_type():
    """Test passing non-string content raises TypeError."""
    with pytest.raises(TypeError, match="content must be a string"):
        write_string_to_file("test.txt", 123)

def test_write_string_to_file_empty_filepath():
    """Test passing an empty file path raises ValueError."""
    with pytest.raises(ValueError, match="file_path cannot be an empty string"):
        write_string_to_file("   ", "test content")
        write_string_to_file("", "test content")