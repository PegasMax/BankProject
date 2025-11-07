import pytest

@pytest.fixture
def call_card_number():
    return ['1234567890123456', '1234 56** **** 3456']


@pytest.fixture
def call_account_number():
    return ['12345678901234567890', '**7890']