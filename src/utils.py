import json
from typing import Any

from src.logger import logger_set

logger_utils = logger_set()


def return_transaction_from_json(filepath: str) -> list | Any:
    """
    Принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список.
    :param filepath: Путь до JSON-файла.
    :return: Список транзакций (опционально - пустой список).
    """
    logger_utils.info("Составляем список словарей с транзакциями...")
    try:
        with open(filepath, "r", encoding="utf-8") as jf:
            list_transaction = json.load(jf)
            logger_utils.info(f"Найдено {len(list_transaction)} транзакций.")
            return list_transaction
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        logger_utils.error(f"Файл по адресу {filepath} не найден или содержит текст не в формате json")
        return []


def transaction_in_rubles(transaction: dict) -> float | ValueError:
    """
    Принимает на вход одну транзакцию и возвращает сумму транзакции в рублях.
    :param transaction: Транзакция в виде словаря.
    :return: Сумма транзакции в рублях (выдаёт ошибку ValueError с сообщением
    "Транзакция выполнена не в рублях. Укажите транзакцию в рублях", если транзакция была совершена в другой валюте).
    """
    logger_utils.info("Возвращаем сумму транзакции в рублях...")
    if transaction["operationAmount"]["currency"]["code"] == "RUB":
        logger_utils.info("Получена сумма транзакции в рублях.")
        return float(transaction["operationAmount"]["amount"])
    else:
        logger_utils.error(f"Транзакция id: {transaction['id']} выполнена не в рублях")
        raise ValueError("Транзакция выполнена не в рублях. Укажите транзакцию в рублях")
