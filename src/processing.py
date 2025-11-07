def filter_by_state(list_of_dicts: list[dict], needed_state: str = "EXECUTED") -> list[dict]:
    """Функция, принимающая список словарей и возвращающая новый список словарей,
    состоящий из словарей старого списка, у которых параметр state соответствует полученному
    параметру"""

    list_for_result = []

    for dictionary in list_of_dicts:
        if not "state" in dictionary:
            continue
        if dictionary["state"] == needed_state:
            list_for_result.append(dictionary)

    return list_for_result


def sort_by_date(list_of_dicts: list[dict], order: bool = True) -> list[dict]:
    """Функция, принимающая список словарей и возвращающая новый список словарей,
    состоящий из словарей старого списка, отсортированный по убыванию даты
    (если второй параметр не задан или True и по возрастанию, если - False)"""

    sorted_list = sorted(list_of_dicts, key=lambda d: d["date"], reverse=order)

    return sorted_list
