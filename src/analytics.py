import collections
import re

def process_bank_search(data:list[dict], search:str)->list[dict]:
    """Принимает список словарей с данными о банковских операциях и строку поиска, 
    возвращает список словарей, у которых в описании есть данная строка."""
    result_list = [operation for operation in data if re.search(search,operation['description'],flags=re.IGNORECASE)]
    return result_list


def process_bank_operations(data:list[dict], categories:list)->dict:
    """Принимает список словарей с данными о банковских операциях и список категорий операций, а возвращает словарь,
    в котором ключи — это названия категорий, а значения — это количество операций в каждой категории."""
    categories_counted = collections.defaultdict(dict)
    for categorie in categories:
        categories_counted[categorie] = len(process_bank_search(data,categorie))

    return categories_counted
