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
