import logging
import pathlib
from logging.handlers import RotatingFileHandler

logging_file = pathlib.Path(__file__).parent.parent.parent.joinpath("logging", "counter_errors.log")

def setup_logger() -> logging.Logger:
    formater = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    handler = RotatingFileHandler(logging_file, mode="a", encoding="utf-8", maxBytes=5 * 1024 * 1024, backupCount=5)
    handler.setFormatter(formater)
    logger = logging.getLogger(pathlib.Path(__name__).name)
    logger.setLevel(logging.WARNING)
    if not logger.hasHandlers():
        logger.addHandler(handler)
    return logger