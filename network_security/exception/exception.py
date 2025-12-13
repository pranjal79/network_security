import sys
from network_security.logging.logger import logger


class NetworkSecurityException(Exception):
    def __init__(self, error_message, error_details: sys):
        self.error_message = error_message

        _, _, exc_tb = error_details.exc_info()
        self.file_name = exc_tb.tb_frame.f_code.co_filename
        self.line_number = exc_tb.tb_lineno

    def __str__(self):
        return (
            f"Error occurred in file [{self.file_name}] "
            f"at line [{self.line_number}] "
            f"with message: {self.error_message}"
        )


# TESTING BLOCK (remove later)
if __name__ == "__main__":
    try:
        logger.info("Entered try block")
        a = 1 / 0   # intentional error
    except Exception as e:
        logger.error("Exception occurred")
        raise NetworkSecurityException(e, sys)
