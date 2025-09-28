import datetime
import inspect
import sys
from functools import wraps
from pprint import pformat

from loguru import logger as global_logger
from loguru._logger import Logger  # type:ignore


class GlobalLogger(Logger):
    def __init__(self) -> None:
        pass

    def __getattr__(self, name):
        return getattr(global_logger, name)


def get_real_logger():
    return global_logger


def set_real_logger(logger_):
    global global_logger
    global_logger = logger_


logger = GlobalLogger()


def timeit(*, log_level: str = "DEBUG", log_args: bool | set[str] = True):
    def decorator(func):
        sig = inspect.signature(func)
        if isinstance(log_args, set):
            for arg in log_args:
                assert arg in sig.parameters, f"Argument '{arg}' not found in function `{func.__name__}` signature."

        @wraps(func)
        def wrapper(*args, **kwargs):
            func_name = f"<yellow>{func.__qualname__:<20}</yellow>"
            has_args = len(args) > 0 or len(kwargs) > 0

            logger_ = logger.opt(colors=True, depth=1)

            if log_args and has_args:
                # https://stackoverflow.com/a/69170441
                bound = sig.bind(*args, **kwargs)
                bound.apply_defaults()

                args_dict = bound.arguments
                if isinstance(log_args, set):
                    args_dict = {k: v for k, v in args_dict.items() if k in log_args}

                args_message = "\n<magenta>" + pformat(args_dict) + "</magenta>"
            else:
                args_message = ""

            logger_.log(log_level, f"enter {func_name}{args_message}")
            sys.stdout.flush()

            start = datetime.datetime.now()
            result = func(*args, **kwargs)
            end = datetime.datetime.now()

            duration = end - start
            duration_message = f"duration=<yellow>{duration.total_seconds():.6f}s</yellow>"
            logger_.log(log_level, f"exit  {func_name} {duration_message}{args_message}")
            sys.stdout.flush()

            return result

        return wrapper

    return decorator
