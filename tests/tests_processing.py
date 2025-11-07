import pytest

from src.processing import filter_by_state, sort_by_date
from tests.conftest import call_operations


@pytest.mark.parametrize(
    'state, expected_result',
    [
        (
            'EXECUTED',
            [
                {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
            ]
        ),
        (
            'CANCELED',
            [
                {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
            ]
        ),
    ]
)
def test_filter_by_state(call_operations,state,expected_result):
    assert filter_by_state(call_operations,state) == expected_result


def test_filter_by_state_default_state(call_operations):
    assert filter_by_state(call_operations) == [
                {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
            ]


@pytest.mark.parametrize(
    'state',
    [
        'EXECUTED',
        'CANCELED',
        ''
    ]
)
def test_filter_by_state_without_state(call_empty_operations, state):
    assert filter_by_state(call_empty_operations, state) == []


#       Тестирование функции sort_by_date


@pytest.mark.parametrize(
    'order, expected_result',
    [
        (
            True,
            [
                {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
                {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
            ]
        ),
        (
            False,
            [
                {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
                {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}

            ]
        )
    ]
)
def test_sort_by_date_basic(call_operations,order,expected_result):
    assert sort_by_date(call_operations,order) == expected_result


def test_sort_by_date_not_unique_dates():
    assert sort_by_date([
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2019-07-03T18:35:29.512364'}
    ]) == [
                {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                {'id': 615064591, 'state': 'CANCELED', 'date': '2019-07-03T18:35:29.512364'},
                {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
            ]


@pytest.mark.parametrize(
    'source_data, expected_result',
    [
        ([
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-19-12'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
        ],
        [
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-19-12'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
        ]),
        ([
             {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
             {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
             {'id': 594226727, 'state': 'CANCELED', 'date': '2018.11.12'},
             {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
         ],
         [
             {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
             {'id': 594226727, 'state': 'CANCELED', 'date': '2018.11.12'},
             {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
             {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
         ]),
    ]
)
def test_sort_by_date_wrong_data(source_data,expected_result):
    assert sort_by_date(source_data) == expected_result
