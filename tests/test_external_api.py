"""Тестирование модуля external_api"""

import os
from unittest.mock import patch

from src.external_api import get_sum_transaction_conversion


# Тест функции конвертации валют без обращения к api.
def test_get_sum_transaction_conversion_not_api():
    result = get_sum_transaction_conversion(
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        }
    )
    assert result == 31957.58


# Тест функции конвертации валют с обращением к api.
@patch("requests.get")
def test_get_sum_transaction_conversion(mock_get):
    mock_get.return_value.json.return_value = {
        "success": True,
        "query": {"from": "USD", "to": "RUB", "amount": 9824.07},
        "info": {"timestamp": 1717619584, "rate": 89.04301},
        "date": "2024-06-05",
        "result": 874764.763251,
    }
    result = get_sum_transaction_conversion(
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        }
    )
    assert result == 874764.763251
    mock_get.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/convert",
        headers={"apikey": os.getenv("API_KEY")},
        params={"to": "RUB", "from": "USD", "amount": "9824.07"},
    )
