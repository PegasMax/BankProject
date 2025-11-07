import pytest

@pytest.fixture
def call_card_number():
    return ['1234567890123456', '1234 56** **** 3456']


@pytest.fixture
def call_account_number():
    return ['12345678901234567890', '**7890']


@pytest.fixture
def call_operations():
    return [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]


@pytest.fixture
def call_empty_operations():
    return [
        {'id': 41428829, 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'date': '2018-10-14T08:21:33.419441'}
    ]