import json
import os

import requests
from dotenv import load_dotenv


def convert_amount_to_rub(transaction: dict) -> float:
    """Конвертирует валюту в сумме amount из валюты source в target"""
    load_dotenv()
    API_KEY = os.getenv("EXCHANGE_RATES_DATA_API_KEY")

    amount = transaction[["operationAmount"]["amount"]]
    source = transaction["operationAmount"]["currency"]["code"]

    url = "https://api.apilayer.com/currency_data/convert"

    headers = {"apikey": API_KEY}

    payload = {"amount": amount, "from": source, "to": "RUB"}

    response = requests.get(url, headers=headers, params=payload)

    if response.status_code == 200:
        result_json = json.load(response.json())
        amount = result_json["result"]
        return float(amount)
    else:
        return 0
