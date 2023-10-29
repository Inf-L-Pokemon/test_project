from masks import hidden_card_number, hidden_account_number


def type_and_hidden_number(type_number: str) -> str:
    """
    Принимает на вход строку с информацией тип карты/счета и номер карты/счета,
    возвращает эту строку с замаскированным номером карты/счета
    :param type_number: Строка с информацией "тип карты/счета и номер карты/счета"
    :return: Тип карты/счета с замаскированным номером карты/счета
    """
    for i, w in enumerate(type_number):
        if w in "0123456789":
            if len(type_number[i:]) == 16:
                return type_number[:i] + hidden_card_number(type_number[i:])
            elif len(type_number[i:]) == 20:
                return type_number[:i] + hidden_account_number(type_number[i:])
            else:
                quit("Неправильно введен номер счета/карты")


def return_date(str_datetime: str) -> str:
    """
    Принимает на вход строку, вида "2018-07-11T02:26:18.671407"
    и возвращает строку с датой в виде "11.07.2018"
    :param str_datetime: Дата и время в виде "2018-07-11T02:26:18.671407"
    :return: Дата в виде "11.07.2018"
    """
    return f"{str_datetime[8:10]}.{str_datetime[5:7]}.{str_datetime[0:4]}"
