from enum import Enum, auto
from typing import Optional, Any

class UserPermissionLevel(Enum):
    """Enumeration of user permission levels for logging."""
    GUEST = 0
    USER = 1
    ADMIN = 2

class ConsoleLogger:
    """
    A flexible console logging system that respects user permission levels.
    
    Allows logging messages based on the user's permission level, 
    with more sensitive or detailed logs only visible to higher-level users.
    """
    
    def __init__(self, user_level: UserPermissionLevel = UserPermissionLevel.GUEST):
        """
        Initialize the logger with a specific user permission level.
        
        Args:
            user_level (UserPermissionLevel): Permission level of the current user.
                Defaults to GUEST level.
        """
        self.user_level = user_level
    
    def log(self, message: str, min_permission: UserPermissionLevel = UserPermissionLevel.GUEST) -> Optional[str]:
        """
        Log a message if the user's permission level meets the minimum required level.
        
        Args:
            message (str): The message to log
            min_permission (UserPermissionLevel): Minimum permission level required to log the message
        
        Returns:
            Optional[str]: The logged message if permission is sufficient, None otherwise
        
        Raises:
            TypeError: If message is not a string or min_permission is not a UserPermissionLevel
        """
        # Type checking
        if not isinstance(message, str):
            raise TypeError("Message must be a string")
        
        if not isinstance(min_permission, UserPermissionLevel):
            raise TypeError("Minimum permission must be a UserPermissionLevel")
        
        # Check if user has sufficient permissions
        if self.user_level.value >= min_permission.value:
            # In a real-world scenario, this might use a proper logging framework
            print(message)
            return message
        
        return None