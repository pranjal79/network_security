# network_security/logging/logger.py
import logging
import os
from datetime import datetime
from logging import Logger

# Create logs directory at project root (one level up from this file)
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
LOG_DIR = os.path.join(ROOT_DIR, "logs")
os.makedirs(LOG_DIR, exist_ok=True)

def get_log_file_path() -> str:
    """Generate a timestamped log filename in the logs directory."""
    ts = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
    return os.path.join(LOG_DIR, f"network_security_{ts}.log")

# Configure the root logger for the package
_log_file = get_log_file_path()
LOG_FORMAT = "%(asctime)s — %(filename)s:%(lineno)d — %(name)s — %(levelname)s — %(message)s"

logging.basicConfig(
    filename=_log_file,
    filemode="a",
    format=LOG_FORMAT,
    level=logging.INFO,
)

# Optional: also add a console handler (useful during development)
_console_handler = logging.StreamHandler()
_console_handler.setLevel(logging.INFO)
_console_handler.setFormatter(logging.Formatter(LOG_FORMAT))
logging.getLogger().addHandler(_console_handler)

def get_logger(name: str) -> Logger:
    """
    Return a logger configured for the given name.
    Use this in modules: from network_security.logging.logger import get_logger
    logger = get_logger(__name__)
    """
    return logging.getLogger(name)
