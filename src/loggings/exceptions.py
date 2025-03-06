import sys
import logging
from loggings.logger import get_logger

logger = get_logger(__name__)

class CustomException(Exception):
    """Custom Exception class to provide detailed error logging."""

    def __init__(self, message, error_details: sys):
        """
        Initialize the custom exception with a message and system error details.
        
        Args:
            message (str): Custom error message.
            error_details (sys): System-specific error details.
        """
        super().__init__(message)
        self.error_message = self.get_detailed_error_message(message, error_details)

    def get_detailed_error_message(self, message, error_details: sys):
        """
        Extracts detailed error message including the error type, script name, and line number.

        Args:
            message (str): Custom error message.
            error_details (sys): System-specific error details.

        Returns:
            str: Formatted error message.
        """
        _, _, exc_tb = error_details.exc_info()
        file_name = exc_tb.tb_frame.f_code.co_filename
        line_number = exc_tb.tb_lineno

        error_message = (
            f"Error in script: [{file_name}] at line [{line_number}] | Message: {message}"
        )
        return error_message

    def __str__(self):
        return self.error_message


# Example Usage
if __name__ == "__main__":
    try:
        a = 1 / 0  # This will cause ZeroDivisionError
    except Exception as e:
        logger.error(CustomException("Division by zero error", sys))
