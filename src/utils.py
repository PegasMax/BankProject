import json

from src.external_api import convert_amount_to_rub


def get_transactions_from_json_file(path: str) -> list[dict]:
    """Принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список
    """
    result_list = None

    # Проверки и исключения
    try:
        with open(path) as file:
            try:
                result_list = json.load(file)
                print(result_list[1])
            except json.JSONDecodeError:
                return []
    except FileNotFoundError:
        return []

    if type(result_list) is not list:
        return []

    return result_list


def get_transaction_amount_rub(transaction: dict) -> float:
    """Принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях, тип данных — float.
    Если транзакция была в USD или EUR, происходит обращение к внешнему API для получения текущего курса валют
    и конвертации суммы операции в рубли"""

    result = float(transaction["operationAmount"]["amount"])

    if transaction["operationAmount"]["currency"]["code"] == "RUB":
        return round(float(result), 2)
    elif transaction["operationAmount"]["currency"]["code"] in ["USD", "EUR"]:
        result = convert_amount_to_rub(transaction)
        return round(result, 2)
    else:
        return 0
