from typing import Generator


def filter_by_currency(transactions: list[dict], currency: str) -> Generator[dict]:
    """Принимает на вход список словарей, представляющих транзакции. Возвращает итератор,
    который поочередно выдает транзакции, где валюта операции соответствует заданной (например, USD)
    """

    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction


def transaction_descriptions(transactions: list[dict]) -> Generator[str]:
    """Принимает список словарей с транзакциями и возвращает описание каждой операции по очереди"""

    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start_number: int, finish_number: int) -> Generator[str]:
    """Выдает номера банковских карт в формате XXXX XXXX XXXX XXXX,
    где X — цифра номера карты.
    Генератор может сгенерировать номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999.
    """

    for number in range(start_number, finish_number + 1):

        number_str = str(number)

        # При необходимости добавляем нолики в начало номера карты
        result_str = "0" * (16 - len(number_str)) + number_str

        # Дополняем номер карты разделителями
        result_list = [x + " " if ((i + 1) % 4 == 0 and i != 15) else x for i, x in enumerate(result_str)]

        result_with_spaces = "".join(result_list)

        yield result_with_spaces
