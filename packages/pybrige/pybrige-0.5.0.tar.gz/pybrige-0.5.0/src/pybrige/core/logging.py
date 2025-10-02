import logging
from typing import Optional


class ColoredFormatter(logging.Formatter):
    """
    Custom log formatter with colors for terminal output.
    Format changes depending on the log level.
    """
    GREY = "\x1b[38;20m"
    GREEN = "\x1b[32;20m"
    YELLOW = "\x1b[33;20m"
    RED = "\x1b[31;20m"
    BOLD_RED = "\x1b[31;1m"
    RESET = "\x1b[0m"

    BASE_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"

    def __init__(self, datefmt: Optional[str] = "%H:%M:%S"):
        super().__init__(datefmt=datefmt)
        self.formatters = {
            logging.DEBUG: logging.Formatter(self.GREY + self.BASE_FORMAT + self.RESET, datefmt),
            logging.INFO: logging.Formatter(self.GREEN + self.BASE_FORMAT + self.RESET, datefmt),
            logging.WARNING: logging.Formatter(self.YELLOW + self.BASE_FORMAT + self.RESET, datefmt),
            logging.ERROR: logging.Formatter(self.RED + self.BASE_FORMAT + self.RESET, datefmt),
            logging.CRITICAL: logging.Formatter(self.BOLD_RED + self.BASE_FORMAT + self.RESET, datefmt),
        }

    def format(self, record: logging.LogRecord) -> str:
        formatter = self.formatters.get(record.levelno, self.formatters[logging.INFO])
        return formatter.format(record)


def setup_logging(
    level: int = logging.INFO, 
    colors: bool = False, 
    file: Optional[str] = None,
    logger_name: Optional[str] = None
) -> None:
    """
    Configure logging for your application.

    Args:
        level (int, optional): Minimum logging level. Default: logging.INFO.
        colors (bool, optional): Enable colored logs in terminal. Default: False.
        file (str, optional): If provided, logs will also be written to this file.
        logger_name (str, optional): Name of the logger to configure. 
                                     If None, root logger is used.
    """
    logger = logging.getLogger(logger_name)
    logger.setLevel(level)

    # Remove existing handlers
    for handler in list(logger.handlers):
        logger.removeHandler(handler)

    # Choose formatter
    if colors:
        formatter = ColoredFormatter()
    else:
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s", datefmt="%H:%M:%S")

    # Console handler
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    # File handler (optional)
    if file:
        file_handler = logging.FileHandler(file)
        file_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
        logger.addHandler(file_handler)
