import json
import logging

from src.external_api import convert_amount_to_rub

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("logs/utils.log")
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_transactions_from_json_file(path: str) -> list[dict]:
    """Принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список
    """
    result_list = None
    logger.info("Начинает работу get_transactions_from_json_file.")

    # Проверки и исключения
    try:
        with open(path) as file:
            try:
                result_list = json.load(file)
                print(result_list[1])
            except json.JSONDecodeError:
                logger.error("Ошибка декодирования JSON формата.")
                return []
    except FileNotFoundError:
        logger.error(f"Ошибка отсутствия файла {path}.")
        return []

    if type(result_list) is not list:
        logger.error("Ошибка: файл содержит не список.")
        return []

    logger.info("Список словарей успешно получен из JSON-файла, функция прекращает работу.")
    return result_list


def get_transaction_amount_rub(transaction: dict) -> float:
    """Принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях, тип данных — float.
    Если транзакция была в USD или EUR, происходит обращение к внешнему API для получения текущего курса валют
    и конвертации суммы операции в рубли"""
    logger.info("Начинает работу get_transaction_amount_rub.")
    result = float(transaction["operationAmount"]["amount"])

    if transaction["operationAmount"]["currency"]["code"] == "RUB":
        result_amount = round(float(result), 2)
        logger.info("Транзакция рублевая, сумма была округлена, функция завершает работу.")
        return result_amount
    elif transaction["operationAmount"]["currency"]["code"] in ["USD", "EUR"]:
        result = convert_amount_to_rub(transaction)
        result_amount = round(result, 2)
        logger.info("Транзакция в долларах или евро, сумма была преобразована, функция завершает работу.")
        return result_amount
    else:
        logger.info("Транзакция не содержит допустимую валюту, Функция завершена, возвращен ноль.")
        return 0
