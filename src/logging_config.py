import logging
from venv import logger
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')


main_logger = logging.getLogger("main_logger")
main_logger.setLevel(logging.INFO)


def setup_logger(name, log_file, level=logging.INFO):

    handler = logging.FileHandler(log_file, mode="w")      
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger