from masks import get_mask_account, get_mask_card_number


def mask_account_or_card(type_and_number_string: str) -> str:
    """Выделяет из строки номер карты или счета и маскирует его"""
    list_of_data = type_and_number_string.split()
    masked_numbers = ""
    if list_of_data[0] == "Счет":
        masked_numbers = get_mask_account(int(list_of_data[-1]))
    else:
        masked_numbers = get_mask_card_number(int(list_of_data[-1]))

    list_of_data[-1] = masked_numbers
    return " ".join(list_of_data)


def get_date(unformatted_date: str) -> str:
    """Приводит дату к формату 'ДД.ММ.ГГГГ'"""
    cropped_date = unformatted_date[:10]
    cropped_date_in_list = cropped_date.split("-")
    formatted_date = ".".join(cropped_date_in_list[::-1])

    return formatted_date


if __name__ == "__main__":
    print(get_date("2024-03-11T02:26:18.671407"))