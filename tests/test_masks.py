import pytest

from src.masks import get_mask_account, get_mask_card_number

#       Тестируем функцию get_mask_card_number(card_number)


def test_get_mask_card_number_basic() -> None:
    assert get_mask_card_number("2022568749152356") == "2022 56** **** 2356"


@pytest.mark.parametrize(
    "card_number",
    [
        1234567890123456,
        "1234567890123456",
        "1234 5678 9012 3456",
        "1234561233456",
        "1234567890000123456",
        "1234-5678-9012-3456",
        "1234 5678 90123456",
    ],
)
def test_get_mask_card_number_different_formats(card_number: str | int) -> None:
    assert get_mask_card_number(card_number) == "1234 56** **** 3456"


def test_get_mask_card_number_zero_first() -> None:
    assert get_mask_card_number("0012345678903456") == "0012 34** **** 3456"


@pytest.mark.parametrize(
    "card_number",
    [
        123456789012,
        "123456789012",
        "00123456789012345678",
        "1234 5678 9012 3456 7890",
        "12345612334564532145879549654",
        "1234567890000123456454664",
        "",
        "  ",
        "-",
    ],
)
def test_get_mask_card_number_wrong_length(card_number: str | int) -> None:
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number(card_number)
        assert (
            str(exc_info.value)
            == "Номер карты может содержать от 13 до 19 цифр, проверьте корректность введенного номера карты"
        )


@pytest.mark.parametrize(
    "card_number",
    [
        "1234567890аа3456",
        "1234 5678 9О12 3456",
        "12345612ее456",
        "1234567В90123456",
        "1234*&4890123456",
        "l234567890123456",
        "12345678`0123456",
    ],
)
def test_get_mask_card_number_other_symbols(card_number: str | int) -> None:
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number(card_number)
        assert str(exc_info.value) == "Номер карты может состоять только из цифр"


#       Тестируем функцию get_mask_account(account_number)


@pytest.mark.parametrize(
    "account_number", ["73654108430135874305", 73654108430135874305]
)
def test_get_mask_account_basic(account_number: str | int) -> None:
    assert get_mask_account(account_number) == "**4305"


@pytest.mark.parametrize(
    "account_number",
    [
        12345678901234567890,
        "12345678901234567890",
        "1234 56 78 90 1 2 3456 78 90",
        "1234-567-890-1234-5678-90",
        "12345678900000127890",
        "1234-5678-9012-4589-789 0",
        "123004 567008 90127-890",
    ],
)
def test_get_mask_account_different_formats(account_number: str | int) -> None:
    assert get_mask_account(account_number) == "**7890"


@pytest.mark.parametrize(
    "account_number",
    [
        12345678901234567890,
        "12345678901234567890",
        "12345678901237890",
        "123456789012345678901234567890",
    ],
)
def test_get_mask_account_different_length(account_number: str | int) -> None:
    assert get_mask_account(account_number) == "**7890"


@pytest.mark.parametrize("account_number", [890, "890", " ", ""])
def test_get_mask_account_little_length(account_number: str | int) -> None:
    with pytest.raises(ValueError) as exc_info:
        get_mask_account(account_number)
        assert (
            str(exc_info.value)
            == "Обычно номер счета содержит 20 цифр, проверьте корректность введенного номера счета"
        )


@pytest.mark.parametrize(
    "account_number",
    [
        "12345612347890аа3456",
        "1234 1234 5678 9О12 3456",
        "123412345612ее456",
        "12341234567В90123456",
        "12341234*&4890123456",
        "l2341234567890123456",
        "123412345678`0123456",
    ],
)
def test_get_mask_account_other_symbols(account_number: str | int) -> None:
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number(account_number)
        assert str(exc_info.value) == "Номер карты может состоять только из цифр"
