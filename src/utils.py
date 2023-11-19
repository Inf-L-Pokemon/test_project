import json
from typing import Any


def return_transaction_from_json(filepath: str) -> list | Any:
    """
    Принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список.
    :param filepath: Путь до JSON-файла.
    :return: Список транзакций (опционально - пустой список).
    """
    try:
        with open(filepath, "r", encoding="utf-8") as jf:
            list_transaction = json.load(jf)
            return list_transaction
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return []


def transaction_in_rubles(transaction: dict) -> float | ValueError:
    """
    Принимает на вход одну транзакцию и возвращает сумму транзакции в рублях.
    :param transaction: Транзакция в виде словаря.
    :return: Сумма транзакции в рублях (выдаёт ошибку ValueError с сообщением
    "Транзакция выполнена не в рублях. Укажите транзакцию в рублях", если транзакция была совершена в другой валюте).
    """
    if transaction["operationAmount"]["currency"]["code"] == "RUB":
        return float(transaction["operationAmount"]["amount"])
    else:
        raise ValueError("Транзакция выполнена не в рублях. Укажите транзакцию в рублях")
