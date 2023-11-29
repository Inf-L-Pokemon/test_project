import re
from collections import Counter


def state_sorting_transactions(list_transaction: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    Принимает на вход список словарей с транзакциями и значение для ключа state
    (опциональный параметр со значением по умолчанию EXECUTED)
    и возвращает новый список, содержащий только те словари,
    у которых ключ state содержит переданное в функцию значение
    :param list_transaction: Список словарей с транзакциями
    :param state: Состояние транзакции (по умолчанию "EXECUTED")
    :return: Список словарей с транзакциями по выбранному состоянию
    """
    return [transaction for transaction in list_transaction if transaction["state"] == state]


def date_sorting_transactions(list_transaction: list[dict], reverse_key: bool = True) -> list[dict]:
    """
    Принимает на вход список словарей и возвращает новый список,
    в котором исходные словари отсортированы по убыванию даты (ключ date).
    Функция принимает два аргумента, второй необязательный
    задает порядок сортировки (убывание, возрастание)
    :param list_transaction: Список словарей с транзакциями
    :param reverse_key: Параметр сортировки (по умолчанию True - по убыванию.)
    :return: Отсортированный список словарей с транзакциями
    """
    return sorted(list_transaction, key=lambda transaction: transaction["date"], reverse=reverse_key)


def search_transactions_by_description(list_transaction: list[dict], search_words: str) -> list:
    """
    Принимает список словарей с данными о банковских операциях и строку поиска,
    и возвращает список словарей, у которых в описании есть данная строка.
    :param list_transaction: Список словарей с транзакциями
    :param search_words: Строка поиска
    :return: Список словарей с транзакциями по поиску
    """
    # Я так и не понял зачем плодить сущности, если можно было сделать вот так:
    # return [transaction for transaction in list_transaction if transaction["description"] == search_words]
    # Ну или хотя бы вот так:
    # return [transaction for transaction in list_transaction if re.search(search_words, transaction["description"])]

    return [
        transaction for transaction in list_transaction if re.compile(search_words).search(transaction["description"])
    ]


def statistic_transactions_by_description(list_transaction: list[dict], description_dict: dict) -> dict:
    """
    Принимает список словарей с данными о банковских операциях и словарь категорий операций,
    и возвращает словарь, в котором ключи — это названия категорий,
    а значения — это количество операций в каждой категории.
    :param list_transaction: Список словарей с транзакциями
    :param description_dict: Словарь категорий операций
    :return: Словарь статистики транзакций по категориям
    """
    counter = dict(Counter([transaction["description"] for transaction in list_transaction]))
    description_dict.update(counter)
    return description_dict
