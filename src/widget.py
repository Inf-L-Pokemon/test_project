from src.masks import hidden_account_number, hidden_card_number


def type_and_hidden_number(type_number: str) -> str:
    """
    Принимает на вход строку с информацией тип карты/счета и номер карты/счета,
    возвращает эту строку с замаскированным номером карты/счета
    :param type_number: Строка с информацией "тип карты/счета и номер карты/счета"
    :return: Тип карты/счета с замаскированным номером карты/счета
    """
    list_type_number = type_number.rsplit(maxsplit=1)
    if len(list_type_number[1]) == 16 and list_type_number[1].isdigit() and list_type_number[0] != "Счет":
        list_type_number[1] = hidden_card_number(list_type_number[1])
        return " ".join(list_type_number)
    elif len(list_type_number[1]) == 20 and list_type_number[1].isdigit() and list_type_number[0] == "Счет":
        list_type_number[1] = hidden_account_number(list_type_number[1])
        return " ".join(list_type_number)
    else:
        return "Неправильно введен номер счета/карты"


def return_date(str_datetime: str) -> str:
    """
    Принимает на вход строку, вида "2018-07-11T02:26:18.671407"
    и возвращает строку с датой в виде "11.07.2018"
    :param str_datetime: Дата и время в виде "2018-07-11T02:26:18.671407"
    :return: Дата в виде "11.07.2018"
    """
    return f"{str_datetime[8:10]}.{str_datetime[5:7]}.{str_datetime[0:4]}"
