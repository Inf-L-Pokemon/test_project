from src.logger import logger_set

logger_masks = logger_set()


def hidden_card_number(card_number: str) -> str:
    """
    Принимает на вход номер карты и возвращает ее маску
    :param card_number: Номер для маскирования
    :return: Маскированный по правилу номер
    """
    logger_masks.info("Скрываем номер карты...")
    logger_masks.info("Получен замаскированный номер карты.")
    return card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]


def hidden_account_number(account_number: str) -> str:
    """
    Принимает на вход номер счёта и возвращает его маску
    :param account_number: Номер для маскирования
    :return: Маскированный по правилу номер
    """
    logger_masks.info("Скрываем номер счёта...")
    logger_masks.info("Получен замаскированный номер счёта.")
    return "**" + account_number[-4:]
