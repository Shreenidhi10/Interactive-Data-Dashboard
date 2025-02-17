import logging
from logging.handlers import RotatingFileHandler

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            RotatingFileHandler("logs/app.log", maxBytes=100000, backupCount=5),
            RotatingFileHandler("logs/error.log", maxBytes=100000, backupCount=5),
            logging.StreamHandler()
        ]
    )

def log_info(message):
    logging.info(message)

def log_error(message):
    logging.error(message)
