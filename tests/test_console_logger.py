import pytest
from src.console_logger import ConsoleLogger, UserPermissionLevel

def test_logger_default_guest_permission(capsys):
    """Test logging behavior for default guest user."""
    logger = ConsoleLogger()
    
    # Guest-level message should log
    result = logger.log("Guest message")
    captured = capsys.readouterr()
    assert result == "Guest message"
    assert "Guest message" in captured.out
    
    # Guest-level log with default permission
    result = logger.log("Another guest message", UserPermissionLevel.GUEST)
    captured = capsys.readouterr()
    assert result == "Another guest message"
    assert "Another guest message" in captured.out

def test_logger_user_permission(capsys):
    """Test logging behavior for user-level permissions."""
    logger = ConsoleLogger(UserPermissionLevel.USER)
    
    # User can log guest and user-level messages
    result = logger.log("Guest message")
    assert result == "Guest message"
    
    result = logger.log("User message", UserPermissionLevel.USER)
    captured = capsys.readouterr()
    assert result == "User message"
    assert "User message" in captured.out
    
    # Cannot log admin-level messages
    result = logger.log("Admin message", UserPermissionLevel.ADMIN)
    captured = capsys.readouterr()
    assert result is None
    assert "Admin message" not in captured.out

def test_logger_admin_permission(capsys):
    """Test logging behavior for admin-level permissions."""
    logger = ConsoleLogger(UserPermissionLevel.ADMIN)
    
    # Admin can log all levels of messages
    result = logger.log("Guest message")
    assert result == "Guest message"
    
    result = logger.log("User message", UserPermissionLevel.USER)
    assert result == "User message"
    
    result = logger.log("Admin message", UserPermissionLevel.ADMIN)
    captured = capsys.readouterr()
    assert result == "Admin message"
    assert "Admin message" in captured.out

def test_logger_invalid_input():
    """Test error handling for invalid input types."""
    logger = ConsoleLogger()
    
    # Test invalid message type
    with pytest.raises(TypeError, match="Message must be a string"):
        logger.log(123)
    
    # Test invalid permission type
    with pytest.raises(TypeError, match="Minimum permission must be a UserPermissionLevel"):
        logger.log("Test", "INVALID")  # type: ignore