"""
Tests for the LZ78 compression and decompression algorithm.
"""

import pytest
from src.lz78_compression import lz78_compress, lz78_decompress

def test_lz78_basic_compression():
    """Test basic compression and decompression"""
    test_string = "TOBEORNOTTOBEORTOBEORNOT"
    compressed = lz78_compress(test_string)
    decompressed = lz78_decompress(compressed)
    assert decompressed == test_string

def test_lz78_repeated_sequence():
    """Test compression with repeated sequences"""
    test_string = "ababababab"
    compressed = lz78_compress(test_string)
    decompressed = lz78_decompress(compressed)
    assert decompressed == test_string

def test_lz78_single_character():
    """Test compression with single character string"""
    test_string = "a"
    compressed = lz78_compress(test_string)
    decompressed = lz78_decompress(compressed)
    assert decompressed == test_string

def test_lz78_long_string():
    """Test compression with a longer, complex string"""
    test_string = "hello world hello world hello python"
    compressed = lz78_compress(test_string)
    decompressed = lz78_decompress(compressed)
    assert decompressed == test_string

def test_lz78_empty_string_raises_error():
    """Test that empty string raises ValueError"""
    with pytest.raises(ValueError):
        lz78_compress("")

def test_lz78_invalid_input_type():
    """Test that non-string input raises TypeError"""
    with pytest.raises(TypeError):
        lz78_compress(123)
    with pytest.raises(TypeError):
        lz78_compress(None)

def test_lz78_invalid_compressed_data():
    """Test error handling for invalid compressed data"""
    # Invalid index
    with pytest.raises(ValueError):
        lz78_decompress([(10, 'a')])
    
    # Invalid tuple type
    with pytest.raises(ValueError):
        lz78_decompress(["not a tuple"])

def test_lz78_compression_properties():
    """Test some properties of the compression"""
    test_string = "mississippi"
    compressed = lz78_compress(test_string)
    
    # Verify first few dictionary entries
    assert lz78_decompress(compressed) == test_string
    
    # Compressed data should always be list of tuples
    assert isinstance(compressed, list)
    assert all(isinstance(item, tuple) and len(item) == 2 for item in compressed)