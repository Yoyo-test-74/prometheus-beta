import logging
import os
from typing import Optional, List

class KeystrokeLogger:
    """
    A class to log keystrokes entered by the user with configurable logging options.
    
    Attributes:
        log_file (str): Path to the log file where keystrokes will be recorded.
        sensitive_mode (bool): Flag to mask sensitive input if enabled.
    """
    
    def __init__(self, log_file: Optional[str] = None, sensitive_mode: bool = False):
        """
        Initialize the KeystrokeLogger.
        
        Args:
            log_file (str, optional): Path to the log file. 
                                      Defaults to 'keystrokes.log' in the current directory.
            sensitive_mode (bool, optional): If True, masks sensitive input. 
                                             Defaults to False.
        """
        # Set default log file if not provided
        self.log_file = log_file or os.path.join(os.getcwd(), 'keystrokes.log')
        self.sensitive_mode = sensitive_mode
        
        # Configure logging
        logging.basicConfig(
            filename=self.log_file, 
            level=logging.INFO, 
            format='%(asctime)s - %(message)s'
        )
    
    def log_keystroke(self, key: str) -> None:
        """
        Log a single keystroke.
        
        Args:
            key (str): The keystroke to log.
        
        Raises:
            ValueError: If the input key is invalid or empty.
        """
        # Validate input
        if not isinstance(key, str):
            raise ValueError("Keystroke must be a string")
        
        if len(key) == 0:
            raise ValueError("Keystroke cannot be an empty string")
        
        # Log the keystroke, applying sensitive mode if enabled
        log_message = key if not self.sensitive_mode else '*' * len(key)
        logging.info(f"Keystroke: {log_message}")
    
    def log_keystrokes(self, keys: List[str]) -> None:
        """
        Log multiple keystrokes.
        
        Args:
            keys (List[str]): List of keystrokes to log.
        
        Raises:
            ValueError: If the input list is invalid or contains invalid keystrokes.
        """
        # Validate input
        if not isinstance(keys, list):
            raise ValueError("Input must be a list of keystrokes")
        
        # Log each keystroke
        for key in keys:
            self.log_keystroke(key)
    
    def clear_log(self) -> None:
        """
        Clear the existing log file.
        """
        try:
            open(self.log_file, 'w').close()
            logging.info("Log file cleared")
        except IOError as e:
            logging.error(f"Failed to clear log file: {e}")