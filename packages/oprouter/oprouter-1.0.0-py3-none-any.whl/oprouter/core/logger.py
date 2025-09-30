"""Logging configuration for OpRouter."""

import logging
import sys
from pathlib import Path
from typing import Optional
from .config import get_config


def setup_logger(name: str = "oprouter", level: Optional[str] = None) -> logging.Logger:
    """Set up logger with file and console handlers."""
    config = get_config()

    # Create logger
    logger = logging.getLogger(name)

    # If logging is disabled, set to CRITICAL to suppress most messages
    if not config.enable_logging:
        logger.setLevel(logging.CRITICAL)
        # Return early with minimal setup
        if not logger.handlers:
            null_handler = logging.NullHandler()
            logger.addHandler(null_handler)
        return logger

    logger.setLevel(getattr(logging, level or config.log_level))

    # Avoid duplicate handlers
    if logger.handlers:
        return logger

    # Create formatters
    detailed_formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    simple_formatter = logging.Formatter(
        '%(levelname)s: %(message)s'
    )

    # File handler
    log_path = Path(config.log_file)
    log_path.parent.mkdir(exist_ok=True)
    file_handler = logging.FileHandler(log_path)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(detailed_formatter)

    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(getattr(logging, config.log_level))
    console_handler.setFormatter(simple_formatter)

    # Add handlers to logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


# Create default logger
logger = setup_logger()
