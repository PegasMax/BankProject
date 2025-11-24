import json

def get_transactions_from_json_file(path: str) -> list[dict]:
    '''Принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список'''
    result_list = None

    #Проверки и исключения
    try:
        with open(path) as file:
            try:
                result_list = json.load(file)
            except json.JSONDecodeError:
                return []
    except FileNotFoundError:
        return []

    if type(result_list) != list:
        return []

    return result_list
