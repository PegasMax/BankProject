import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions
from tests.conftest import call_transactions_list

# Тестирование функции filter_by_currency


def test_filter_by_currency_basic(call_transactions_list: dict) -> None:
    """Проверка базового функционала"""
    assert (
        list(filter_by_currency(call_transactions_list["all_transactions"], "USD"))
        == call_transactions_list["USD_transactions"]
    )

    assert (
        list(filter_by_currency(call_transactions_list["all_transactions"], "RUB"))
        == call_transactions_list["RUB_transactions"]
    )


def test_filter_by_currency_upset(call_transactions_list: dict) -> None:
    """Проверка отработки ситуации когда требуемая валюта отсутствует"""
    assert list(filter_by_currency(call_transactions_list["all_transactions"], "EUR")) == []


def test_filter_by_currency_empty_list() -> None:
    """Проверка отсутствия ошибки в случае получения на вход пустого списка"""
    assert list(filter_by_currency([], "RUB")) == []


# Тестирование функции transaction_descriptions


def test_transaction_descriptions_basic(call_transactions_list: dict) -> None:
    """Проверка на то, что функция возвращает корректные описания для каждой транзакции"""
    assert (
        list(transaction_descriptions(call_transactions_list["all_transactions"]))
        == call_transactions_list["all_transactions_descriptions"]
    )


def test_transaction_descriptions_empty() -> None:
    """Проверка отработки функции при пустом списке во входных данных"""
    assert list(transaction_descriptions([])) == []


# Тестирование функции card_number_generator


@pytest.mark.parametrize(
    "start_number, finish_number, expected_result",
    [
        (
            2200404533221000,
            2200404533221010,
            [
                "2200 4045 3322 1000",
                "2200 4045 3322 1001",
                "2200 4045 3322 1002",
                "2200 4045 3322 1003",
                "2200 4045 3322 1004",
                "2200 4045 3322 1005",
                "2200 4045 3322 1006",
                "2200 4045 3322 1007",
                "2200 4045 3322 1008",
                "2200 4045 3322 1009",
                "2200 4045 3322 1010",
            ],
        ),
        (1, 2, ["0000 0000 0000 0001", "0000 0000 0000 0002"]),
    ],
)
def test_card_number_generator_basic(start_number, finish_number, expected_result) -> None:
    """Проверка выдачи номеров в заданном диапазоне и корректности форматирования номеров карт"""
    assert list(card_number_generator(start_number, finish_number)) == expected_result


@pytest.mark.parametrize(
    "start_number, finish_number, expected_first, expected_last",
    [
        (
            2200404533221000,
            2200404533221010,
            "2200 4045 3322 1000",
            "2200 4045 3322 1010",
        ),
        (1, 1000000, "0000 0000 0000 0001", "0000 0000 0100 0000"),
    ],
)
def test_card_number_generator_extreme(start_number, finish_number, expected_first, expected_last) -> None:
    """Проверка корректности крайних значений диапазона"""
    card_generator = card_number_generator(start_number, finish_number)

    # Сравниваем первое генерируемое значение
    assert next(card_generator) == expected_first

    # Ищем и сравниваем последнее генерируемое значение
    card_number = ""
    while True:
        try:
            card_number = next(card_generator)
        except StopIteration:
            break
    assert card_number == expected_last
