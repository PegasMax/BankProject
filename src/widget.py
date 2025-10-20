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


#if __name__ == "__main__":
#    print(mask_account_or_card("Счет 64686473678894779589"))