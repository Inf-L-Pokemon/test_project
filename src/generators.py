from typing import Generator


def filter_by_currency(transactions: list[dict], code_currency: str) -> Generator:
    """
    Принимает список словарей и возвращает итератор
    с операциями в которых указана заданная валюта.
    :param transactions: Список словарей с операциями
    :param code_currency: Код валюты
    :return: Операции с заданной валютой
    """
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == code_currency:
            yield transaction


def transaction_descriptions(transactions: list[dict]) -> Generator:
    """
    Принимает список словарей и возвращает описание каждой операции по очереди.
    :param transactions: Список словарей с операциями
    :return: Описание операций по очереди
    """
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int, stop: int) -> Generator:
    """
    Принимает начальный и конечный диапазон
    для генерирования номеров банковских карт
    :param start: Начальное значение
    :param stop: Конечное значение
    :return: Номера банковских карт из диапазона
    """
    for i in range(start, stop + 1):
        card_number = str(i).zfill(16)
        yield f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:16]}"
