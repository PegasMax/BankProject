def filter_by_state(list_of_dicts: list[dict], needed_state='EXECUTED') -> list[dict]:
    """Функция, принимающая список словарей и возвращающая новый список словарей,
    состоящий из словарей старого списка, у которых параметр state соответствует полученному
    параметру"""

    list_for_result = []

    for dictio in list_of_dicts:
        if dictio['state'] == needed_state:
            list_for_result.append(dictio)

    return list_for_result


def sort_by_date(list_of_dicts: list[dict], order=True) -> list[dict]:
    """Функция, принимающая список словарей и возвращающая новый список словарей,
    состоящий из словарей старого списка, отсортированный по убыванию даты
    (если второй параметр - True и по возрастанию, если - False)"""

    sorted_list = sorted(list_of_dicts, key=lambda d: d['date'], reverse=order)

    return sorted_list

