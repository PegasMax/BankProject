from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(type_and_number_string: str) -> str:
    """Выделяет из строки номер карты или счета и маскирует его"""
    list_of_data = type_and_number_string.split()
    masked_numbers = ""

    # Проверка наличия только номера
    if len(list_of_data) < 2 and list_of_data[-1][-1].isdigit():
        raise ValueError(
            'Введен только номер, впишите тип карты или слово "Счет" в начало сообщения'
        )

    # Проверка отсутствия в сообщении номера
    if not list_of_data[-1][-1].isdigit():
        raise ValueError("Введите номер карты или счета")

    if list_of_data[0].lower() in ["счет", "счёт"]:
        masked_numbers = get_mask_account(int(list_of_data[-1]))
        list_of_data[0] = "Счет"
    else:
        masked_numbers = get_mask_card_number(int(list_of_data[-1]))

    list_of_data[-1] = masked_numbers

    return " ".join(list_of_data)


def get_date(unformatted_date: str) -> str:
    """Приводит дату к формату 'ДД.ММ.ГГГГ'"""

    last_char = unformatted_date.find("T")

    if last_char == -1:
        raise ValueError("Дата не введена в корректном формате")

    cropped_date = unformatted_date[:last_char]
    cropped_date_in_list = cropped_date.split("-")

    if 0 <= len(cropped_date_in_list) < 3:
        raise ValueError("Дата не введена в корректном формате")

    # Проверка реальности количества месяцев и дней
    if int(cropped_date_in_list[1]) > 12 or int(cropped_date_in_list[2]) > 31:
        raise ValueError("Введена несуществующая дата")

    formatted_date = ".".join(cropped_date_in_list[::-1])

    return formatted_date
