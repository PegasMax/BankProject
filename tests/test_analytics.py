from re import search

from src.analytics import process_bank_search, process_bank_operations
from tests.conftest import call_transactions_list

# тестирование функции process_bank_search


def test_process_bank_search_ok(call_transactions_list) -> None:
    """Проверка работы функции при нормальных условиях"""
    data = call_transactions_list["all_transactions"]
    search = "счета"

    assert len(process_bank_search(data, search)) == 2


def test_process_bank_search_empty_search(call_transactions_list) -> None:
    """Проверка работы функции при передаче пустой подстроки поиска"""
    data = call_transactions_list["all_transactions"]
    search = ""

    assert len(process_bank_search(data, search)) == 5


def test_process_bank_search_false_search(call_transactions_list) -> None:
    """Проверка работы функции при передаче строки поиска с заведомо несуществующей комбинацией сисмволов"""
    data = call_transactions_list["all_transactions"]
    search = "нет там такого текста"

    assert len(process_bank_search(data, search)) == 0


def test_process_bank_search_empty_data() -> None:
    """Проверка работы функции при передаче пустого списка поиска"""
    data = []
    search = "счета"

    assert process_bank_search(data, search) == []


def test_process_bank_search_no_descriptions(call_operations) -> None:
    """Проверка работы функции при передаче поискового списка с элементами без нужного поля"""
    data = call_operations
    search = "счета"

    assert process_bank_search(data, search) == []


def test_process_bank_search_wrong_case(call_transactions_list) -> None:
    """Проверка работы функции при передаче строки поиска с заведомо несуществующей комбинацией сисмволов"""
    data = call_transactions_list["all_transactions"]
    search = "счЕта"

    assert len(process_bank_search(data, search)) == 2


# Тестирование функции process_bank_operations()


def test_process_bank_operations_ok(call_transactions_list) -> None:
    """Проверка работы функции при нормальных условиях"""
    data = call_transactions_list["all_transactions"]
    categories = ["Перевод организации", "Перевод со счета на счет"]

    assert process_bank_operations(data, categories) == {"Перевод организации": 2, "Перевод со счета на счет": 2}


def test_process_bank_operations_empty_categories(call_transactions_list) -> None:
    """Проверка работы функции при пустом списке требуемых категорий"""
    data = call_transactions_list["all_transactions"]
    categories = []

    assert process_bank_operations(data, categories) == {}


def test_process_bank_operations_wrong_categories(call_transactions_list) -> None:
    """Проверка работы функции при наборе несуществующих категорий"""
    data = call_transactions_list["all_transactions"]
    categories = ["Перевод организациям", "со счета"]

    assert process_bank_operations(data, categories) == {}


def test_process_bank_operations_empty_data() -> None:
    """Проверка работы функции при пустом наборе данных для поиска"""
    data = []
    categories = ["Перевод организации", "Перевод со счета на счет"]

    assert process_bank_operations(data, categories) == {}
