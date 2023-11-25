import pytest

from src.utils import (
    return_transaction_from_csv,
    return_transaction_from_json,
    return_transaction_from_xls,
    transaction_in_rubles,
)


@pytest.mark.parametrize(
    "filepath, expected_result",
    [(r"data/operations.json", [441945886, 41428829, 939719570]), (r"data/nonexistent.json", [])],
)
def test_return_transaction_from_json(filepath, expected_result):
    list_transaction = return_transaction_from_json(filepath)
    assert [transaction["id"] for transaction in list_transaction[0:3]] == expected_result


@pytest.mark.parametrize(
    "filepath, expected_result",
    [(r"data/transactions.csv", [650703, 3598919, 593027]), (r"data/nonexistent.csv", [])],
)
def test_return_transaction_from_csv(filepath, expected_result):
    list_transaction = return_transaction_from_csv(filepath)
    assert [transaction["id"] for transaction in list_transaction[0:3]] == expected_result


@pytest.mark.parametrize(
    "filepath, expected_result",
    [(r"data/transactions_excel.xlsx", [650703, 3598919, 593027]), (r"data/nonexistent.xlsx", [])],
)
def test_return_transaction_from_xls(filepath, expected_result):
    list_transaction = return_transaction_from_xls(filepath)
    assert [transaction["id"] for transaction in list_transaction[0:3]] == expected_result


@pytest.mark.parametrize(
    "transaction_, expected_result",
    [
        (
            {
                "id": 441945886,
                "state": "EXECUTED",
                "date": "2019-08-26T10:50:58.294041",
                "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
                "description": "Перевод организации",
                "from": "Maestro 1596837868705199",
                "to": "Счет 64686473678894779589",
            },
            31957.58,
        ),
        (
            {
                "id": 41428829,
                "state": "EXECUTED",
                "date": "2019-07-03T18:35:29.512364",
                "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
                "description": "Перевод организации",
                "from": "MasterCard 7158300734726758",
                "to": "Счет 35383033474447895560",
            },
            ValueError("Транзакция выполнена не в рублях. Укажите транзакцию в рублях"),
        ),
    ],
)
def test_transaction_in_rubles(transaction_, expected_result):
    try:
        assert transaction_in_rubles(transaction_) == expected_result
    except ValueError:
        with pytest.raises(ValueError):
            raise ValueError("Транзакция выполнена не в рублях. Укажите транзакцию в рублях")
