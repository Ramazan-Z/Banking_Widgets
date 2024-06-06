"""Проверка функции get_sum_transaction_conversion с реальным обращением к API"""

import os

from src.external_api import get_sum_transaction_conversion
from src.generators import filter_by_currency
from src.utils import get_data_from_json_file

transactions = get_data_from_json_file(os.path.join("data", "operations.json"))  # чтение файла
transactions_usd = filter_by_currency(transactions, "USD")  # филтрация по валюте
transaction = next(transactions_usd)  # первая транзакция в $
amount_rub = get_sum_transaction_conversion(transaction)  # конвертация в рубли

print(transaction)
print(amount_rub)
