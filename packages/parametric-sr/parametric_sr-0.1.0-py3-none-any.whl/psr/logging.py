"""
logging module
"""

import logging
import os
import sys
from typing import Optional


def _create_logger(name: str | None = None) -> logging.Logger:
    """
    Create a logger for the given name.

    Parameters
    ----------
    name : str | None
        The name of the logger. If None, the logger will be named "PSR".

    Returns
    -------
    logging.Logger
        The created logger.
    """
    logger = logging.getLogger(name or "PSR")
    logger.setLevel(logging.DEBUG)  # Set the default logging level

    # Create a handler that writes log messages to stdout
    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setLevel(logging.DEBUG)  # Set the handler's logging level

    # Create a formatter and set it for the handler
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    stdout_handler.setFormatter(formatter)

    logger.addHandler(stdout_handler)

    return logger


def add_file_handler(
    log_file: str,
    level: int = logging.INFO,
    formatter: Optional[logging.Formatter] = None,
    mode: str = "a",
) -> logging.Handler:
    """
    Add a FileHandler to the module logger.

    - Reuses the existing StreamHandler formatter by default.
    - Avoids adding the same file handler twice.

    Returns the handler (existing or newly created).

    Parameters
    ----------
    log_file : str
        The path to the log file.
    level : int
        The logging level for the file handler.
    formatter : Optional[logging.Formatter]
        The formatter to use for the file handler.
    mode : str
        The file mode for the file handler.

    Returns
    -------
    logging.Handler
        The file handler.
    """
    # avoid duplicate handlers for the same file
    abs_path = os.path.abspath(log_file)
    for h in logger.handlers:
        if (
            isinstance(h, logging.FileHandler)
            and getattr(h, "baseFilename", None) == abs_path
        ):
            return h

    # pick formatter from first StreamHandler if none provided
    if formatter is None:
        for h in logger.handlers:
            if isinstance(h, logging.StreamHandler) and h.formatter is not None:
                formatter = h.formatter
                break
    if formatter is None:
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

    fh = logging.FileHandler(abs_path, mode=mode)
    fh.setLevel(level)
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    return fh


logger = _create_logger()
"""
The global logger instance for the `psr` module.
"""
