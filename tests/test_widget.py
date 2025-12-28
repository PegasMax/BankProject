import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "brand",
    [
        "Maestro",
        "MasterCard",
        "Visa Classic",
        "Visa Platinum",
        "Visa Gold",
    ],
)
def test_mask_account_card_for_card(brand: str, call_card_number: list[str]) -> None:
    assert mask_account_card(brand + " " + call_card_number[0]) == brand + " " + call_card_number[1]


@pytest.mark.parametrize("brand", ["Счёт", "Счет", "счет", "счёт", "СЧЁТ", "СЧЕТ", "СчЁт", "СчЕт"])
def test_mask_account_card_for_account(brand: str, call_account_number: list[str]) -> None:
    assert mask_account_card(brand + " " + call_account_number[0]) == "Счет " + call_account_number[1]


@pytest.mark.parametrize(
    "first_part_of_message, number",
    [
        (" ", "12345678901234567890"),
        ("", "12345678901234567890"),
        (" ", "1234567890123456"),
        ("", "1234567890123456"),
    ],
)
def test_mask_account_card_without_type_of_number(first_part_of_message: str, number: str) -> None:
    with pytest.raises(ValueError) as exc_info:
        mask_account_card(first_part_of_message + number)

        assert str(exc_info.value) == 'Введен только номер, впишите тип карты или слово "Счет" в начало сообщения'


@pytest.mark.parametrize(
    "brand",
    [
        "Maesro ",
        "MastaCard ",
        "Счет ",
        "Vista Classic ",
        "Visa Platinum Superior",
        "Visa Gold ",
    ],
)
def test_mask_account_card_without_number(brand: str) -> None:
    with pytest.raises(ValueError) as exc_info:
        mask_account_card(brand + " ")
        assert str(exc_info.value) == "Введите номер карты или счета"


#       Тестирование функции get_date


def test_get_date() -> None:
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"


@pytest.mark.parametrize(
    "source_date, expected_result",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2124-08-11T02:26:18.671407", "11.08.2124"),
        ("21015-03-11T02:26:18.671407", "11.03.21015"),
        ("1015-03-11T02:26:18.671407", "11.03.1015"),
        ("224-03-11T02:26:18.671407", "11.03.224"),
    ],
)
def test_get_date_different_real_dates(source_date: str, expected_result: str) -> None:
    assert get_date(source_date) == expected_result


@pytest.mark.parametrize(
    "source_date",
    [
        "2024-13-11T02:26:18.671407",
        "2124-28-11T02:26:18.671407",
        "21015-33-11T02:26:18.671407",
        "1015-43-11T02:26:18.671407",
        "224-03-51T02:26:18.671407",
    ],
)
def test_get_date_unreal_dates(source_date: str) -> None:
    with pytest.raises(ValueError) as e_info:
        get_date(source_date)
        assert str(e_info.value) == "Введена несуществующая дата"


@pytest.mark.parametrize(
    "source_date",
    [
        "2024-13-1102:26:18.671407",
        "2124-28-T02:26:18.671407",
        "2101511T02:26:18.671407",
        "1015-T02:26:18.671407",
        "224-1T02:26:18.671407",
        "",
        " ",
    ],
)
def test_get_date_no_dates(source_date: str) -> None:
    with pytest.raises(ValueError) as e_info:
        get_date(source_date)
        assert str(e_info.value) == "Дата не введена в корректном формате"
