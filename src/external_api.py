"""Модуль конвертации валют"""

import os

import requests
from dotenv import load_dotenv


def get_sum_transaction_conversion(transaction: dict) -> float:
    """Функция принимает транзакцию и возвращает сумму транзакции в рублях (float).
    Если транзакция была в USD или EUR, происходит обращение к внешнему API
    для конвертации суммы операции в рубли."""
    amount = transaction["operationAmount"]["amount"]
    currecy_code = transaction["operationAmount"]["currency"]["code"]
    URL = "https://api.apilayer.com/exchangerates_data/convert"
    params = {"to": "RUB", "from": currecy_code, "amount": amount}
    load_dotenv(".env")
    headers = {"apikey": os.getenv("API_KEY")}

    if currecy_code == "RUB":
        result = amount
    else:
        respone = requests.get(URL, headers=headers, params=params).json()
        result = respone["result"]

    return float(result)
