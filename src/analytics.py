import collections
import re


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """Принимает список словарей с данными о банковских операциях и строку поиска,
    возвращает список словарей, у которых в описании есть данная строка."""
    pattern = rf".*{search},*"
    search_data = [operation for operation in data if "description" in operation]
    result_list = [
        operation for operation in search_data if re.search(pattern, operation["description"], flags=re.IGNORECASE)
    ]
    return result_list


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """Принимает список словарей с данными о банковских операциях и список категорий операций, а возвращает словарь,
    в котором ключи — это названия категорий, а значения — это количество операций в каждой категории."""
    categories_counted = collections.Counter(
        [transaction["description"] for transaction in data if transaction["description"] in categories]
    )

    return categories_counted
