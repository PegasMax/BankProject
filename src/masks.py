def get_mask_card_number(card_number: int | str) -> str:
    """Принимает на вход номер карты и возвращает ее маску,
    где все символы кроме первых 6 и последних 4-х заменены на '*'"""
    card_number_str = str(card_number)

    # Очищаем номер карты от разделителей: пробелов и тире
    card_number_str = card_number_str.replace(" ", "")
    card_number_str = card_number_str.replace("-", "")

    # Проверка на посторонние символы
    for char in card_number_str:
        if not ("0" <= char <= "9"):
            raise ValueError("Номер карты может состоять только из цифр")

    # Проверка длины номера карты
    if not 12 < len(card_number_str) < 20:
        raise ValueError(
            "Номер карты может содержать от 13 до 19 цифр, проверьте корректность введенного номера карты"
        )

    mask_card_number = card_number_str[:6] + 6 * "*" + card_number_str[-4:]
    mask_card_number = (
        mask_card_number[:4] + " " + mask_card_number[4:8] + " " + mask_card_number[8:12] + " " + mask_card_number[12:]
    )

    return mask_card_number


def get_mask_account(account_number: int | str) -> str:
    """Принимает на вход номер счета в виде числа и возвращает маску номера,
    где все цифры, кроме последних 4х заменены на '**'"""
    account_number_str = str(account_number)

    # Очищаем номер счета от разделителей: пробелов и тире
    account_number_str = account_number_str.replace(" ", "")
    account_number_str = account_number_str.replace("-", "")

    # Проверка наличия в номере счета хотя бы 4х цифр
    if len(account_number_str) < 4:
        raise ValueError("Обычно номер счета содержит 20 цифр, проверьте корректность введенного номера счета")

    mask_account = "**" + account_number_str[-4:]

    return mask_account
