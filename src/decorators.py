from datetime import datetime
from functools import wraps
from typing import Any, Callable, Optional


def log(filename: str | None = None) -> Optional[Callable]:
    def wrapper(func: Callable) -> Optional[Callable]:
        @wraps(func)
        def inner(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                if filename:
                    with open(filename, "a", encoding="utf8") as log_file:
                        log_file.write(f"{now} {func.__name__} ok\n")
                else:
                    print(f"{now} {func.__name__} ok")
                return result
            except Exception as err:
                now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                if filename:
                    with open(filename, "a", encoding="utf8") as log_file:
                        log_file.write(f"{now} {func.__name__} error: {err}. Inputs: {args}, {kwargs}\n")
                else:
                    print(f"{now} {func.__name__} error: {err}. Inputs: {args}, {kwargs}")

        return inner

    return wrapper
