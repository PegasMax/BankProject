from unittest.mock import patch

from src.external_api import convert_amount_to_rub
from tests.conftest import coll_usd_transaction


def test_convert_amount_to_rub_usd(coll_usd_transaction: dict):
    """Тестирование функции в нормальных условиях
    при получении долларовой операции"""
    with patch("requests.request") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = '{"date": "2018-02-22", "historical": "", "info": {"rate": 148.972231, "timestamp": 1519328414}, "query": {"amount": 25, "from": "GBP", "to": "JPY"}, "result": 3724.305775, "success": true}'
        assert convert_amount_to_rub(coll_usd_transaction) == 3724.305775
        mock_get.assert_called()


def test_convert_amount_to_rub_eur(coll_eur_transaction: dict):
    """Тестирование функции в нормальных условиях
    при получении евро операции"""
    with patch("requests.request") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = '{"date": "2018-02-22", "historical": "", "info": {"rate": 148.972231, "timestamp": 1519328414}, "query": {"amount": 25, "from": "GBP", "to": "JPY"}, "result": 3724.305775, "success": true}'
        assert convert_amount_to_rub(coll_eur_transaction) == 3724.305775
        mock_get.assert_called()


def test_convert_amount_to_rub_bad_response(coll_eur_transaction: dict):
    """Тестирование функции при отказном результате запроса"""
    with patch("requests.request") as mock_get:
        mock_get.return_value.status_code = 400
        mock_get.return_value.text = '{"date": "2018-02-22", "historical": "", "info": {"rate": 148.972231, "timestamp": 1519328414}, "query": {"amount": 25, "from": "GBP", "to": "JPY"}, "result": 3724.305775, "success": true}'
        assert convert_amount_to_rub(coll_eur_transaction) == 0
        mock_get.assert_called()
