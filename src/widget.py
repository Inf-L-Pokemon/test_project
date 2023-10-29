from masks import hidden_card_number, hidden_account_number


def type_and_hidden_number(type_number: str) -> str:
    index_start_number = type_number.index(str(range(10)))
    if len(type_number[index_start_number:]) == 16:
        return type_number[:index_start_number] + hidden_card_number(type_number[index_start_number:])
    elif len(type_number[index_start_number:]) == 20:
        return type_number[:index_start_number] + hidden_account_number(type_number[index_start_number:])
