import os
import pytest
import tempfile
import shutil

from src.directory_file_size import calculate_directory_total_size

def test_calculate_directory_total_size_empty_directory():
    """Test total size calculation for an empty directory."""
    with tempfile.TemporaryDirectory() as temp_dir:
        assert calculate_directory_total_size(temp_dir) == 0

def test_calculate_directory_total_size_single_file():
    """Test total size calculation for a directory with a single file."""
    with tempfile.TemporaryDirectory() as temp_dir:
        test_file_path = os.path.join(temp_dir, 'test.txt')
        with open(test_file_path, 'w') as f:
            f.write('Hello, World!')
        
        assert calculate_directory_total_size(temp_dir) == len('Hello, World!')

def test_calculate_directory_total_size_multiple_files():
    """Test total size calculation for a directory with multiple files."""
    with tempfile.TemporaryDirectory() as temp_dir:
        file_contents = ['Test 1', 'Another test', 'Third file']
        total_size = 0
        
        for i, content in enumerate(file_contents, 1):
            file_path = os.path.join(temp_dir, f'test_{i}.txt')
            with open(file_path, 'w') as f:
                f.write(content)
            total_size += len(content)
        
        assert calculate_directory_total_size(temp_dir) == total_size

def test_calculate_directory_total_size_nested_directory():
    """Test total size calculation for nested directories."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create nested directory structure
        os.makedirs(os.path.join(temp_dir, 'subdir1', 'subsubdir'))
        os.makedirs(os.path.join(temp_dir, 'subdir2'))
        
        files_and_contents = [
            (os.path.join(temp_dir, 'file1.txt'), 'Root file'),
            (os.path.join(temp_dir, 'subdir1', 'file2.txt'), 'Subdir file'),
            (os.path.join(temp_dir, 'subdir1', 'subsubdir', 'file3.txt'), 'Nested file'),
            (os.path.join(temp_dir, 'subdir2', 'file4.txt'), 'Another subdir file')
        ]
        
        total_size = 0
        for path, content in files_and_contents:
            with open(path, 'w') as f:
                f.write(content)
            total_size += len(content)
        
        assert calculate_directory_total_size(temp_dir) == total_size

def test_calculate_directory_total_size_invalid_input():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        calculate_directory_total_size(123)
    
    with pytest.raises(TypeError):
        calculate_directory_total_size(None)

def test_calculate_directory_total_size_nonexistent_directory():
    """Test error handling for nonexistent directory."""
    with pytest.raises(FileNotFoundError):
        calculate_directory_total_size('/path/to/nonexistent/directory')

def test_calculate_directory_total_size_not_a_directory():
    """Test error handling when path is not a directory."""
    with tempfile.NamedTemporaryFile() as temp_file:
        with pytest.raises(NotADirectoryError):
            calculate_directory_total_size(temp_file.name)