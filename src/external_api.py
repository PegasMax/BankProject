import json
import os

import requests
from dotenv import load_dotenv


def convert_amount_to_rub(transaction: dict) -> float:
    """Конвертирует валюту операции в словаре"""
    load_dotenv()
    API_KEY = os.getenv("EXCHANGE_RATES_DATA_API_KEY")

    amount = transaction["operationAmount"]["amount"]
    source = transaction["operationAmount"]["currency"]["code"]

    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={source}&amount={amount}"

    payload = {}

    headers = {"apikey": API_KEY}

    response = requests.request("GET", url, headers=headers, data=payload)

    if response.status_code == 200:
        result_json = json.loads(response.text)
        amount = result_json["result"]
        return float(amount)
    else:
        return 0


usd_transaction = {
    "id": 939719570,
    "state": "EXECUTED",
    "date": "2018-06-30T02:08:58.425572",
    "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
    "description": "Перевод организации",
    "from": "Счет 75106830613657916952",
    "to": "Счет 11776614605963066702",
}
print(convert_amount_to_rub(usd_transaction))
