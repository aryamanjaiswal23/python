import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%m-%d-%Y %H:%M:%S",
)
logging.debug("this is debug message")
logging.warning("this is a warning message")
logging.critical("this is a critical message")
logging.error("this is an error message")
