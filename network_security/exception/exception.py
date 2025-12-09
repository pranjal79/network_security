# network_security/exception/exception.py
import sys
import traceback
from typing import Optional

from network_security.logging.logger import get_logger

logger = get_logger(__name__)

class NetworkSecurityException(Exception):
    """
    Custom exception that captures the original exception message + context.
    When raising, pass the original exception (or sys.exc_info()) so we can extract traceback.
    """

    def __init__(self, error_message: str, error_details: Optional[BaseException] = None):
        super().__init__(error_message)
        self.error_message = error_message
        self.error_details = error_details

        # Extract filename and line number from traceback if available
        tb = None
        if error_details is not None:
            # If passed an exception instance that has __traceback__
            tb = getattr(error_details, "__traceback__", None)
        else:
            # Fallback to current exception info if available
            tb = sys.exc_info()[2]

        if tb:
            last_tb = traceback.extract_tb(tb)[-1]
            self.filename = last_tb.filename
            self.lineno = last_tb.lineno
        else:
            self.filename = None
            self.lineno = None

    def __str__(self) -> str:
        file_info = f" in file: {self.filename}" if self.filename else ""
        line_info = f" at line: {self.lineno}" if self.lineno else ""
        base = f"{self.error_message}{file_info}{line_info}"
        return base

    def log_and_raise(self):
        """
        Log the exception with full traceback and re-raise as NetworkSecurityException.
        Use this in except blocks: raise NetworkSecurityException("msg", e).log_and_raise()
        """
        # Log full traceback
        if self.error_details:
            logger.error("An error occurred", exc_info=self.error_details)
        else:
            logger.error(self.error_message)
        # Re-raise this exception so calling code can handle it
        raise self
