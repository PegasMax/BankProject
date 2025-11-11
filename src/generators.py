def filter_by_currency(transactions: list[dict], currency:str) -> iter(dict):
    """Принимает на вход список словарей, представляющих транзакции. Возвращает итератор,
    который поочередно выдает транзакции, где валюта операции соответствует заданной (например, USD)"""

    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction


def transaction_descriptions(transactions: list[dict]) -> iter(str) :
    """Принимает список словарей с транзакциями и возвращает описание каждой операции по очереди"""

    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start_number, finish_number) -> iter(str):
    """Выдает номера банковских карт в формате XXXX XXXX XXXX XXXX,
    где X — цифра номера карты.
    Генератор может сгенерировать номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999."""

    for number in range(start_number, finish_number + 1):

        number_str = str(number)

        # При необходимости добавляем нолики в начало номера карты
        result_str = "0" * (16-len(number_str)) + number_str
        result_with_spaces = ""

        # Дополняем номер карты разделителями
        for i, x in enumerate(result_str):
            result_with_spaces += x
            if i + 1 % 4 == 0 and i !=16:
                result_with_spaces += " "

        yield result_with_spaces
