import pytest
from pytest_mock import mocker

from src.table_integration import get_transactions_from_csv_file, get_transactions_from_excel_file


def test_get_transactions_from_csv_file_ok():
    """Тестирование вызова ф-ии получения информации из
    .csv файла в нормальных условиях"""
    result = get_transactions_from_csv_file("data/transactions.csv")[0]
    assert result == {
        "id": 650703.0,
        "state": "EXECUTED",
        "date": "2023-09-05T11:30:32Z",
        "operationAmount": {"amount": 16210.0, "currency": {"name": "Sol", "code": "PEN"}},
        "description": "Перевод организации",
        "from": "Счет 58803664561298323391",
        "to": "Счет 39745660563456619397",
    }


def test_get_transactions_from_csv_file_not_existed_file():
    """Тестирование вызова ф-ии получения информации из
    несуществующего .csv файла"""
    result = get_transactions_from_csv_file("data/not_existed.csv")
    assert result == []


def test_get_transactions_from_csv_file_empty_file(mocker):
    """Тестирование вызова ф-ии получения информации из пустого
    .csv файла"""
    mocker.patch("pandas.read_csv", return_value=None)
    assert get_transactions_from_csv_file("data/transactions_emptyes.csv") == []


def test_get_transactions_from_csv_file_absent_file():
    """Тестирование вызова ф-ии получения информации из пустого
    .csv файла"""
    assert get_transactions_from_csv_file("data/transactions_absent.csv") == []


def test_get_transactions_from_excel_file_ok():
    """Тестирование вызова ф-ии получения информации из
    .csv файла в нормальных условиях"""
    result = get_transactions_from_excel_file("data/transactions_excel.xlsx")[0]
    assert result == {
        "id": 650703.0,
        "state": "EXECUTED",
        "date": "2023-09-05T11:30:32Z",
        "operationAmount": {"amount": 16210.0, "currency": {"name": "Sol", "code": "PEN"}},
        "description": "Перевод организации",
        "from": "Счет 58803664561298323391",
        "to": "Счет 39745660563456619397",
    }


def test_get_transactions_from_excel_file_not_existed_file():
    """Тестирование вызова ф-ии получения информации из
    несуществующего .csv файла"""
    result = get_transactions_from_excel_file("data/not_existed.xlsx")
    assert result == []


def test_get_transactions_from_excel_file_empty_file(mocker):
    """Тестирование вызова ф-ии получения информации из пустого
    .csv файла"""
    mocker.patch("pandas.read_csv", return_value=None)
    assert get_transactions_from_excel_file("data/transactions_emptyes.xlsx") == []


def test_get_transactions_from_excel_file_absent_file():
    """Тестирование вызова ф-ии получения информации из пустого
    .csv файла"""
    assert get_transactions_from_excel_file("data/transactions_absent.xlsx") == []
