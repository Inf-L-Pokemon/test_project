import logging


def logger_set(name: str = __name__) -> logging.Logger:
    """
    Получает имя регистратора и создает регистратор с именем name
    :param name: Имя регистратора
    :return: Регистратор
    """
    logger = logging.getLogger(name)

    file_handler = logging.FileHandler(r"data\logs.log", encoding="utf-8", mode="w")
    file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)

    logger.setLevel(logging.INFO)

    return logger
