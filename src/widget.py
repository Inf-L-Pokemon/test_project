from masks import hidden_card_number, hidden_account_number


def type_and_hidden_number(type_number: str) -> str:
    """
    Принимает на вход строку с информацией тип карты/счета и номер карты/счета,
    возвращает эту строку с замаскированным номером карты/счета
    :param type_number: Строка с информацией "тип карты/счета и номер карты/счета"
    :return: Тип карты/счета с замаскированным номером карты/счета
    """
    index_start_number = type_number.index(str(range(10)))
    if len(type_number[index_start_number:]) == 16:
        return type_number[:index_start_number] + hidden_card_number(type_number[index_start_number:])
    elif len(type_number[index_start_number:]) == 20:
        return type_number[:index_start_number] + hidden_account_number(type_number[index_start_number:])
