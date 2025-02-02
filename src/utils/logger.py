import logging

def setup_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # Create a file handler
    fh = logging.FileHandler('app.log')
    fh.setLevel(logging.DEBUG)

    # Create a console handler (optional)
    ch = logging.StreamHandler()
    ch.setLevel(logging.ERROR)

    # Create a formatter and set it for both handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    # Add the handlers to the logger
    logger.addHandler(fh)
    logger.addHandler(ch)

    return logger

logger = setup_logger()
