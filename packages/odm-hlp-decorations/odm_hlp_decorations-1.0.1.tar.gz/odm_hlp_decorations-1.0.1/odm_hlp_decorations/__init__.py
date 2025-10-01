import os
from functools import wraps
from typing import Callable
import logging
import sys
from dotenv import dotenv_values

# take environment variables from .env.
config = dotenv_values(".env")

# logging setup
logformat = "%(asctime)s | %(levelname)s | %(message)s"
logging.basicConfig(filename=config['logs_path']+'python.log', encoding='utf-8', format=logformat, level=logging.WARNING)


def task(param1: str = None):
    def decorator(func: Callable):
                
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                ret = func(*args, **kwargs)
                return ret

            except Exception as e:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                file_origin = os.path.basename(sys.argv[0])
                logging.error(f" {file_origin}:{func.__module__}:{func.__name__} | {e}")
                #raise e # stop execution
                sys.exit(1) # stop execution
        
        return wrapper

    return decorator

