from datetime import datetime
from functools import wraps
from typing import Any, Callable, Optional


def log(filename: str | None = None) -> Optional[Callable]:
    def wrapper(func: Callable) -> Optional[Callable]:
        @wraps(func)
        def inner(*args: Any, **kwargs: Any) -> Any:
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            try:
                result = func(*args, **kwargs)
                log_message = f"{now} {func.__name__} ok\n"
            except Exception as err:
                log_message = f"{now} {func.__name__} error: {err}. Inputs: {args}, {kwargs}\n"
                result = None
            if filename:
                with open(filename, "a", encoding="utf8") as log_file:
                    log_file.write(log_message)
            else:
                print(log_message)
            return result

        return inner

    return wrapper
