# network_security/exception/test_exception.py
from network_security.logging.logger import get_logger
from network_security.exception.exception import NetworkSecurityException

logger = get_logger(__name__)

def cause_error():
    logger.info("About to cause a ZeroDivisionError (test).")
    # deliberate error
    return 1 / 0

if __name__ == "__main__":
    try:
        cause_error()
    except Exception as e:
        # Wrap, log, and re-raise as custom exception
        ne = NetworkSecurityException("Error while running cause_error()", e)
        # This will log the full traceback and raise the custom exception
        try:
            ne.log_and_raise()
        except NetworkSecurityException as final:
            # Final handler: show formatted message to console (or keep silent)
            logger.info("Custom exception caught in main: %s", final)
            # Optionally print to stdout for immediate feedback
            print("Caught:", final)
