import re
from datetime import datetime
import pytest
from src.current_time_formatter import get_current_time_formatted

def test_current_time_format():
    """Test that the returned time string matches the expected format."""
    current_time = get_current_time_formatted()
    
    # Check that the time string matches HH:MM:SS format
    assert re.match(r'^\d{2}:\d{2}:\d{2}$', current_time), \
        f"Time format is incorrect. Got: {current_time}"

def test_time_components():
    """Test that each component of the time is within valid ranges."""
    current_time = get_current_time_formatted()
    hours, minutes, seconds = map(int, current_time.split(':'))
    
    # Validate hour is between 0 and 23
    assert 0 <= hours <= 23, f"Invalid hours: {hours}"
    
    # Validate minutes are between 0 and 59
    assert 0 <= minutes <= 59, f"Invalid minutes: {minutes}"
    
    # Validate seconds are between 0 and 59
    assert 0 <= seconds <= 59, f"Invalid seconds: {seconds}"

def test_consistency():
    """Verify that multiple calls return valid times."""
    times = set()
    for _ in range(5):
        times.add(get_current_time_formatted())
    
    # Ensure all times are valid strings
    assert all(re.match(r'^\d{2}:\d{2}:\d{2}$', time) for time in times), \
        "Not all times were in the correct format"