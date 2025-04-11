from functools import wraps
from typing import Callable
from .logger import logger

def catch_error(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.error(f"{func.__name__}")
            raise e
    return wrapper