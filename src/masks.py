def get_mask_card_number(card_number: int) -> str:
    """Принимает на вход номер карты и возвращает ее маску,
    где все символы кроме первых 6 и последних 4-х заменены на '*'"""
    card_number_str = str(card_number)

    mask_card_number = card_number_str[:6] + 6 * "*" + card_number_str[-4:]
    mask_card_number = (
        mask_card_number[:4] + " " + mask_card_number[4:8] + " " + mask_card_number[8:12] + " " + mask_card_number[12:]
    )

    return mask_card_number


def get_mask_account(account_number: int) -> str:
    """Принимает на вход номер счета в виде числа и возвращает маску номера,
    где все цифры, кроме последней заменены на '**'"""
    account_number_str = str(account_number)

    mask_account = "**" + account_number_str[-4:]

    return mask_account
