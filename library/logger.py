import logging


def log_event():
    logging.basicConfig(filename="test" + __name__ + ".log", level=logging.INFO,
                        format="%(asctime)s - %(levelname)s - %(message)s")
    return logging
