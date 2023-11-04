import pytest

from src.widget import return_date, type_and_hidden_number


@pytest.mark.parametrize(
    "string, expected_result",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Счет 6831982476737658", "Неправильно введен номер счета/карты"),
        ("Visa Gold 5U994f4228426H53", "Неправильно введен номер счета/карты"),
        ("Счет 7365410843013587434", "Неправильно введен номер счета/карты"),
    ],
)
def test_type_and_hidden_number(string, expected_result):
    assert type_and_hidden_number(string) == expected_result


@pytest.mark.parametrize(
    "string, expected_result",
    [("2018-07-11T02:26:18.671407", "11.07.2018"), ("1999-07-03T18:35:29.512364", "03.07.1999")],
)
def test_return_date(string, expected_result):
    assert return_date(string) == expected_result
