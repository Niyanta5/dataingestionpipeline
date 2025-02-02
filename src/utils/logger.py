import logging
import sys


def setup_logger(name: str = "DataIngestion"):
    logger = logging.getLogger(name)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    #Console Handler

    ch = logging.StreamHandler(sys.stdout)
    ch.setFormatter(formatter)
    logger.addHandler(fh)

    return logger

logger = setup_logger()

