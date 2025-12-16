import sys
from network_security.logging.logger import logging


class NetworkSecurityException(Exception):
    def __init__(self, error_message, error_details: sys):
        super().__init__(error_message)
        self.error_message = NetworkSecurityException.get_detailed_error_message(
            error_message, error_details
        )

    @staticmethod
    def get_detailed_error_message(error_message, error_details: sys):
        _, _, exc_tb = error_details.exc_info()

        file_name = exc_tb.tb_frame.f_code.co_filename
        line_number = exc_tb.tb_lineno

        detailed_message = (
            f"Error occurred in file [{file_name}] "
            f"at line [{line_number}] "
            f"with error message [{error_message}]"
        )

        return detailed_message

    def __str__(self):
        return self.error_message


