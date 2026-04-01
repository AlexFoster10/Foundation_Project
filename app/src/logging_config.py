import logging
from venv import logger
import os
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
log_path = os.path.join(BASE_DIR, "app", "tests", "logs", "main.log")
os.makedirs(os.path.dirname(log_path), exist_ok=True)

main_logger = logging.getLogger("main_logger")
main_logger.setLevel(logging.INFO)
handler = logging.FileHandler(log_path, mode="a")    
handler.setFormatter(formatter)

logger = logging.getLogger("main_logger")
logger.setLevel(logging.INFO)
logger.addHandler(handler)


def setup_logger(name, log_file, level=logging.INFO):

    handler = logging.FileHandler(log_file, mode="w")      
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger