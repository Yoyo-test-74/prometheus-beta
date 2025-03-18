import os
import pytest
import logging
from src.keystroke_logger import KeystrokeLogger

def test_log_single_keystroke(tmp_path):
    """Test logging a single keystroke"""
    log_file = os.path.join(tmp_path, 'test_keystrokes.log')
    logger = KeystrokeLogger(log_file=log_file)
    
    logger.log_keystroke('a')
    
    # Verify log file contains the keystroke
    with open(log_file, 'r') as f:
        log_content = f.read()
        assert 'Keystroke: a' in log_content

def test_log_multiple_keystrokes(tmp_path):
    """Test logging multiple keystrokes"""
    log_file = os.path.join(tmp_path, 'test_keystrokes.log')
    logger = KeystrokeLogger(log_file=log_file)
    
    logger.log_keystrokes(['a', 'b', 'c'])
    
    # Verify log file contains all keystrokes
    with open(log_file, 'r') as f:
        log_content = f.read()
        assert 'Keystroke: a' in log_content
        assert 'Keystroke: b' in log_content
        assert 'Keystroke: c' in log_content

def test_sensitive_mode(tmp_path):
    """Test sensitive mode masking"""
    log_file = os.path.join(tmp_path, 'test_keystrokes.log')
    logger = KeystrokeLogger(log_file=log_file, sensitive_mode=True)
    
    logger.log_keystroke('password')
    
    # Verify log file masks the keystroke
    with open(log_file, 'r') as f:
        log_content = f.read()
        assert 'Keystroke: ********' in log_content

def test_invalid_keystroke_input():
    """Test handling of invalid keystroke inputs"""
    logger = KeystrokeLogger()
    
    # Test empty string
    with pytest.raises(ValueError, match="Keystroke cannot be an empty string"):
        logger.log_keystroke('')
    
    # Test non-string input
    with pytest.raises(ValueError, match="Keystroke must be a string"):
        logger.log_keystroke(123)

def test_invalid_keystrokes_input():
    """Test handling of invalid keystrokes list input"""
    logger = KeystrokeLogger()
    
    # Test non-list input
    with pytest.raises(ValueError, match="Input must be a list of keystrokes"):
        logger.log_keystrokes('not a list')

def test_clear_log(tmp_path):
    """Test clearing the log file"""
    log_file = os.path.join(tmp_path, 'test_keystrokes.log')
    logger = KeystrokeLogger(log_file=log_file)
    
    # Log some keystrokes
    logger.log_keystroke('a')
    logger.log_keystroke('b')
    
    # Clear the log
    logger.clear_log()
    
    # Verify log file is empty or contains only the clear log message
    with open(log_file, 'r') as f:
        log_content = f.read()
        assert 'Log file cleared' in log_content
        assert 'Keystroke: a' not in log_content
        assert 'Keystroke: b' not in log_content