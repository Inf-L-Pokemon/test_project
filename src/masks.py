def hidden_card_number(card_number: str) -> str:
    """
    Принимает на вход номер карты и возвращает ее маску
    :param card_number: Номер для маскирования
    :return: Маскированный по правилу номер
    """
    return card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]


def hidden_account_number(account_number: str) -> str:
    """
    Принимает на вход номер счёта и возвращает его маску
    :param account_number: Номер для маскирования
    :return: Маскированный по правилу номер
    """
    return "**" + account_number[-4:]
