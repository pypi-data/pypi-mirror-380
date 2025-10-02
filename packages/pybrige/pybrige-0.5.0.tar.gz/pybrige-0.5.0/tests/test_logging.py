import logging
from typing import Optional

class ColoredFormatter(logging.Formatter):
    
    GREY = "\x1b[38;20m"
    GREEN = "\x1b[32;20m"
    YELLOW = "\x1b[33;20m"
    RED = "\x1b[31;20m"
    BOLD_RED = "\x1b[31;1m"
    RESET = "\x1b[0m"
    BASE_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"

    def __init__(self, datefmt: Optional[str] = "%H:%M:%S"):
        super().__init__(datefmt=datefmt)
        self.FORMATS = {
            logging.DEBUG: self.GREY + self.BASE_FORMAT + self.RESET,
            logging.INFO: self.GREEN + self.BASE_FORMAT + self.RESET,
            logging.WARNING: self.YELLOW + self.BASE_FORMAT + self.RESET,
            logging.ERROR: self.RED + self.BASE_FORMAT + self.RESET,
            logging.CRITICAL: self.BOLD_RED + self.BASE_FORMAT + self.RESET,
        }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt, datefmt=self.datefmt)
        return formatter.format(record)

def setup_logging(level: int = logging.INFO, colors: bool = False) -> None:
    # Escolhe o formatador a ser usado
    if colors:
        formatter = ColoredFormatter()
    else:
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s", datefmt="%H:%M:%S"
        )
    
    # Cria um handler para o terminal
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    # Usa logging.basicConfig com force=True para substituir a configuração existente
    # de forma limpa e compatível com pytest.
    logging.basicConfig(
        level=level,
        handlers=[stream_handler],
        force=True
    )
