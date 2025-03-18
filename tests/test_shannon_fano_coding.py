import pytest
import sys
import os

# Ensure the src directory is in the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from shannon_fano_coding import shannon_fano_encode, shannon_fano_decode

def test_shannon_fano_basic_encoding():
    """Test basic encoding functionality"""
    data = "AABBBCCCC"
    code_map, encoded = shannon_fano_encode(data)
    
    # Check that code map is generated
    assert len(code_map) > 0
    
    # Verify unique codes
    assert len(set(code_map.values())) == len(code_map)
    
    # Decode and verify
    decoded = shannon_fano_decode(code_map, encoded)
    assert decoded == data

def test_shannon_fano_decode():
    """Test decoding functionality"""
    data = "HELLO WORLD"
    code_map, encoded = shannon_fano_encode(data)
    decoded = shannon_fano_decode(code_map, encoded)
    assert decoded == data

def test_shannon_fano_empty_input():
    """Test handling of empty input"""
    with pytest.raises(ValueError, match="Input data cannot be empty"):
        shannon_fano_encode("")

def test_shannon_fano_single_char():
    """Test encoding and decoding with a single character"""
    data = "AAAA"
    code_map, encoded = shannon_fano_encode(data)
    decoded = shannon_fano_decode(code_map, encoded)
    assert decoded == data

def test_shannon_fano_complex_string():
    """Test encoding and decoding with a complex string"""
    data = "The quick brown fox jumps over the lazy dog"
    code_map, encoded = shannon_fano_encode(data)
    decoded = shannon_fano_decode(code_map, encoded)
    assert decoded == data

def test_shannon_fano_invalid_decoding():
    """Test handling of invalid decoding"""
    data = "HELLO"
    code_map, encoded = shannon_fano_encode(data)
    
    # Modify encoded string to make it undecadable
    invalid_encoded = encoded + "1"
    
    with pytest.raises(ValueError, match="Could not decode entire input string"):
        shannon_fano_decode(code_map, invalid_encoded)

def test_shannon_fano_unicode():
    """Test encoding and decoding with unicode characters"""
    data = "こんにちは世界"
    code_map, encoded = shannon_fano_encode(data)
    decoded = shannon_fano_decode(code_map, encoded)
    assert decoded == data