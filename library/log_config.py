import logging
import os


def log_config(suite_name = "default"):

    # Create a logs directory, if not existing already
    os.makedirs("../results/logs", exist_ok=True)

    # Unique log file name
    log_file = f"../results/logs/{suite_name}.log"


    logging.basicConfig(filename=log_file,
                        level=logging.INFO,
                        format="%(asctime)s - %(levelname)s - %(message)s",
                        filemode='w') # Overwrite the log file on each run


    logger = logging.getLogger(__name__)
    logger.info(f"Logging initialized for test suite: {suite_name}")
    return logger
