from unittest.mock import Mock, mock_open

import src.external_api
from src.utils import get_transaction_amount_rub, get_transactions_from_json_file
from tests.conftest import coll_usd_transaction


def test_get_transactions_from_json_file_not_exist():
    """Проверка корректной реакции на открытие отсутствующего файла"""
    assert get_transactions_from_json_file("not_existed_file.json") == []


def test_get_transactions_from_json_file_empty(mocker):
    """Проверка корректной реакции на открытие пустого файла"""
    mocker.patch("json.load", return_value=None)
    assert get_transactions_from_json_file("../data/operations.json") == []


def test_get_transactions_from_json_file_not_list(mocker):
    """Проверка корректной реакции на открытие файла, содержащего не список"""
    mocker.patch("json.load", return_value="Not_list")
    assert get_transactions_from_json_file("../data/operations.json") == []


def test_get_transactions_from_json_file_ok_data(mocker):
    """Проверка корректной реакции на открытие файла, содержащего корректные данные"""
    test_data = """[
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 587085106,
            "state": "EXECUTED",
            "date": "2018-03-23T10:45:06.972075",
            "operationAmount": {
                "amount": "48223.05",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 41421565395219882431"
        }]"""

    mocker.patch("builtins.open", mock_open(read_data=test_data))
    result = get_transactions_from_json_file("../data/operations.json")
    assert result[1] == {
        "id": 587085106,
        "state": "EXECUTED",
        "date": "2018-03-23T10:45:06.972075",
        "operationAmount": {
            "amount": "48223.05",
            "currency": {"name": "руб.", "code": "RUB"},
        },
        "description": "Открытие вклада",
        "to": "Счет 41421565395219882431",
    }


# Тестирование функции get_transaction_amount_rub
def test_get_transaction_amount_rub(coll_rub_transaction):
    """Проверка работы ф-ии при нормальном входном значении в рублях"""
    assert get_transaction_amount_rub(coll_rub_transaction) == 48223.05


def test_get_transaction_amount_rub_usd_or_eur(coll_usd_transaction):
    """Тестирование вызова ф-ии конвертации при получении долларовой
    или евро операции на вход"""
    mock_convert = Mock(return_value=713.8)
    src.external_api.rub_conversion = mock_convert
    assert get_transaction_amount_rub(coll_usd_transaction) == 713.8


def test_get_transaction_amount_rub_strange_valute():
    """Тестирование вызова ф-ии конвертации при получении операции
    в непредусмотренной валюте на вход"""
    transaction_invalid = {
        "operationAmount": {"amount": 100.00, "currency": {"code": "JPY"}}
    }
    result = get_transaction_amount_rub(transaction_invalid)
    assert result == 0.00
