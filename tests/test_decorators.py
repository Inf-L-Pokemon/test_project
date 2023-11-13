import os.path
from datetime import datetime

import pytest

from src.decorators import log


@pytest.mark.parametrize(
    "filename, arg_1, arg_2, expected_result",
    [
        ("test_log", 1, 2, " foo ok"),
        ("test_log", 1, "2", " foo error: unsupported operand type(s) for +: 'int' and 'str'. Inputs: (1, '2'), {}"),
    ],
)
def test_log_in_file(filename, arg_1, arg_2, expected_result):
    @log(filename)
    def foo(x, y):
        return x + y

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    foo(arg_1, arg_2)

    with open(filename) as file:
        log_message = file.read().strip()

    os.remove(filename)

    expected_log = now + expected_result

    assert log_message == expected_log


@pytest.mark.parametrize(
    "arg_1, arg_2, expected_result",
    [
        (1, 2, " foo ok"),
        (1, "2", " foo error: unsupported operand type(s) for +: 'int' and 'str'. Inputs: (1, '2'), {}"),
    ],
)
def test_log_in_console(arg_1, arg_2, expected_result, capsys):
    @log()
    def foo(x, y):
        return x + y

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    foo(arg_1, arg_2)

    log_message = capsys.readouterr()

    expected_log = now + expected_result

    assert log_message.out.strip() == expected_log
