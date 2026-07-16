"""Structured logging utilities for mobile automation tests."""
import logging
import os
import time
import config


def setup_logger(name: str) -> logging.Logger:
    """Set up a logger with file and console handlers."""
    os.makedirs(config.LOG_DIR, exist_ok=True)
    ts = time.strftime("%Y%m%d")

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    if logger.handlers:
        return logger

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    fh = logging.FileHandler(
        os.path.join(config.LOG_DIR, f"automation_{ts}.log")
    )
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(formatter)

    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    ch.setFormatter(formatter)

    logger.addHandler(fh)
    logger.addHandler(ch)

    return logger
