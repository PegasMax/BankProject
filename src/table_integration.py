#func for csv. take path to .csv, return list of dicts with transactions

#func for excel take path to .excel,  return list of dicts with transactions

import pandas as pd
import logging

from pandas.core.interchange.dataframe_protocol import DataFrame

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("../logs/table_integration.log")
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)

def get_transactions_from_csv_file(path: str) -> list[dict]:
    """Принимает на вход путь до CSV-файла и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой или не найден, функция возвращает пустой список
    """
    result_list = None
    logger.info("Начинает работу get_transactions_from_csv_file.")

    # Проверки и исключения
    try:
        with open(path) as file:
            data_df = pd.read_csv(file, delimiter=';')
    except FileNotFoundError:
        logger.error(f"Ошибка отсутствия файла {path}.")
        return []

    if data_df.empty:
        logger.error("Ошибка: файл пуст.")
        return []

    standard_df = standardize_df(data_df)
    # Трансформируем DataFrame в список словарей
    result_list = standard_df.to_dict(orient='records')

    logger.info("Список словарей успешно получен из CSV-файла, функция прекращает работу.")
    return result_list


def get_transactions_from_excel_file(path: str) -> list[dict]:
    """Принимает на вход путь до Excel-файла и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой или не найден, функция возвращает пустой список
    """
    result_list = None
    logger.info("Начинает работу get_transactions_from_excel_file.")

    # Проверки и исключения
    try:
        with open(path, encoding='latin-1') as file:
            data_df = pd.read_excel(file)
    except FileNotFoundError:
        logger.error(f"Ошибка отсутствия файла {path}.")
        return []

    if data_df.empty:
        logger.error("Ошибка: файл пуст.")
        return []

    standard_df = standardize_df(data_df)
    # Трансформируем DataFrame в список словарей
    result_list = standard_df.to_dict(orient='records')

    logger.info("Список словарей успешно получен из Excel-файла, функция прекращает работу.")
    return result_list


def standardize_df(df: pd.DataFrame) -> pd.DataFrame:
    """Перевод полученного из excel или csv DataFrame в тип, совпадающий со стандартным"""
    currency = df.loc[:, ['currency_name', 'currency_code']]
    currency.columns = ['name', 'code']
    currency_list = currency.to_dict(orient='records')

    operation_amount = df.loc[:, ['amount']]
    operation_amount.columns = ['amount']
    operation_amount['currency'] = currency_list
    operation_amount_list = operation_amount.to_dict(orient='records')

    new_df = pd.DataFrame(df.loc[:,['id', 'state', 'date']])
    right_df = df.loc[:, ['description', 'from', 'to']]

    new_df['operationAmount'] = operation_amount_list

    new_df = pd.concat([new_df, right_df], axis=1)

    return new_df


print(get_transactions_from_csv_file('../data/transactions.csv'))