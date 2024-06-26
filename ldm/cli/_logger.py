from typing import Callable
from ..logger import Logger, ClickLogger


def create_logger(debug: bool) -> ClickLogger:
    level = 1 if debug else 2
    return ClickLogger(level=level)


def error_boundary(func: Callable, logger: Logger):
    try:
        func()
    except Exception as e:
        for line in str(e).split("\n"):
            logger.error(line)
        exit(1)
