from datetime import datetime
from functools import wraps
from typing import Any, Callable, Optional


def log(filename: str | None = None) -> Optional[Callable]:
    """
    Декоратор ведет лог вызова функции и ее результата в файл или в консоль.
    Если вызов функции закончился ошибкой, то записывается сообщение об ошибке и входные параметры функции.
    Если задан параметр filename - записывает лог в файл с именем filename.
    Если параметр filename не задан - выводит лог в консоль.
    :param filename: Имя файла для логов
    :return: Лог вызова функции
    """
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
