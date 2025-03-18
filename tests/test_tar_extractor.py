import os
import pytest
import tarfile
import tempfile
from src.tar_extractor import extract_tar_archive

@pytest.fixture
def sample_tar_archive():
    """Create a sample tar archive for testing"""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create a tar archive with sample files
        tar_path = os.path.join(temp_dir, 'sample.tar')
        with tarfile.open(tar_path, 'w') as tar:
            # Create sample files
            files = {
                'file1.txt': b'Content of file 1',
                'file2.txt': b'Content of file 2',
                'nested/file3.txt': b'Content of nested file'
            }
            
            for filename, content in files.items():
                full_path = os.path.join(temp_dir, filename)
                os.makedirs(os.path.dirname(full_path), exist_ok=True)
                
                with open(full_path, 'wb') as f:
                    f.write(content)
                
                tar.add(full_path, arcname=filename)
        
        yield tar_path

def test_extract_all_files(sample_tar_archive):
    """Test extracting all files from a tar archive"""
    with tempfile.TemporaryDirectory() as extract_dir:
        extracted = extract_tar_archive(sample_tar_archive, extract_dir)
        
        assert len(extracted) == 3
        assert all(os.path.exists(path) for path in extracted)
        assert set(os.path.basename(f) for f in extracted) == {'file1.txt', 'file2.txt', 'file3.txt'}

def test_extract_specific_files(sample_tar_archive):
    """Test extracting specific files from a tar archive"""
    with tempfile.TemporaryDirectory() as extract_dir:
        extracted = extract_tar_archive(sample_tar_archive, extract_dir, 'file1.txt')
        
        assert len(extracted) == 1
        assert extracted[0].endswith('file1.txt')
        assert os.path.exists(extracted[0])

def test_extract_multiple_specific_files(sample_tar_archive):
    """Test extracting multiple specific files"""
    with tempfile.TemporaryDirectory() as extract_dir:
        extracted = extract_tar_archive(sample_tar_archive, extract_dir, ['file1.txt', 'nested/file3.txt'])
        
        assert len(extracted) == 2
        assert set(os.path.basename(f) for f in extracted) == {'file1.txt', 'file3.txt'}

def test_nonexistent_tar_file():
    """Test handling of nonexistent tar file"""
    with pytest.raises(FileNotFoundError):
        extract_tar_archive('/path/to/nonexistent/archive.tar')

def test_nonexistent_specific_file(sample_tar_archive):
    """Test extracting a file that doesn't exist in the archive"""
    with tempfile.TemporaryDirectory() as extract_dir:
        with pytest.raises(ValueError, match="File nonexistent.txt not found in archive"):
            extract_tar_archive(sample_tar_archive, extract_dir, 'nonexistent.txt')

def test_extract_to_default_path(sample_tar_archive):
    """Test extraction to default path"""
    with tempfile.TemporaryDirectory() as temp_dir:
        original_cwd = os.getcwd()
        os.chdir(temp_dir)
        
        try:
            # Copy tar to current directory
            import shutil
            tar_copy = os.path.join(temp_dir, 'sample.tar')
            shutil.copy(sample_tar_archive, tar_copy)
            
            # Extract with default path
            extracted = extract_tar_archive(tar_copy)
            
            assert len(extracted) == 3
            assert all(os.path.exists(path) for path in extracted)
        finally:
            os.chdir(original_cwd)