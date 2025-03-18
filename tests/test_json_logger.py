import pytest
import logging
import json
from io import StringIO
from src.json_logger import log_json

class TestJSONLogger:
    @pytest.fixture
    def logger(self):
        """Create a logger that captures log output to a StringIO buffer."""
        logger = logging.getLogger('test_logger')
        logger.setLevel(logging.DEBUG)
        stream_handler = logging.StreamHandler(StringIO())
        stream_handler.setLevel(logging.DEBUG)
        logger.addHandler(stream_handler)
        return logger, stream_handler.stream

    def test_log_json_basic(self, logger):
        """Test basic JSON logging functionality."""
        log_logger, log_stream = logger
        test_obj = {"name": "John", "age": 30}
        log_json(log_logger, logging.INFO, "User details:", test_obj)
        log_output = log_stream.getvalue()
        
        assert "User details:" in log_output
        assert json.dumps(test_obj, indent=2) in log_output

    def test_log_json_custom_indent(self, logger):
        """Test JSON logging with custom indentation."""
        log_logger, log_stream = logger
        test_obj = {"name": "Jane", "hobbies": ["reading", "swimming"]}
        log_json(log_logger, logging.DEBUG, "User profile:", test_obj, indent=4)
        log_output = log_stream.getvalue()
        
        assert "User profile:" in log_output
        assert json.dumps(test_obj, indent=4) in log_output

    def test_log_json_invalid_input_type(self, logger):
        """Test logging with invalid input type raises TypeError."""
        log_logger, _ = logger
        with pytest.raises(TypeError, match="Input must be a dictionary"):
            log_json(log_logger, logging.ERROR, "Invalid input:", "not a dict")

    def test_log_json_invalid_indent(self, logger):
        """Test logging with invalid indent value raises ValueError."""
        log_logger, _ = logger
        test_obj = {"key": "value"}
        with pytest.raises(ValueError, match="Indent must be a non-negative integer"):
            log_json(log_logger, logging.WARNING, "Invalid indent:", test_obj, indent=-1)

    def test_log_json_complex_object(self, logger):
        """Test logging a complex, nested JSON object."""
        log_logger, log_stream = logger
        test_obj = {
            "user": {
                "name": "Alice",
                "address": {
                    "street": "123 Main St",
                    "city": "Wonderland"
                }
            },
            "active": True
        }
        log_json(log_logger, logging.INFO, "Complex user data:", test_obj)
        log_output = log_stream.getvalue()
        
        assert "Complex user data:" in log_output
        assert json.dumps(test_obj, indent=2) in log_output