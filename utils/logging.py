import logging

def setup_logging(log_file="paragon_ai.log"):
    """Sets up the logging configuration."""
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
    print("Logging initialized.")

def log(message, level="info"):
    """Logs a message to the configured logger."""
    levels = {
        "info": logging.info,
        "warning": logging.warning,
        "error": logging.error,
        "debug": logging.debug
    }
    if level in levels:
        levels[level](message)
        print(f"[{level.upper()}]: {message}")
    else:
        logging.info(message)
        print(f"[INFO]: {message}")
