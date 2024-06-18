"""Тестирование модуля utils"""

import json
import os
from unittest.mock import Mock, patch

import pandas as pd

from src.utils import get_data_from_file, get_data_from_json_file


# Тест функции чтения файла json.
def test_get_data_from_json_file():
    result = get_data_from_json_file(os.path.join("data", "operations.json"))
    assert result[0]["id"] == 441945886


# Тест функции чтения файла json с ошибкой или пустого.
@patch("json.load")
def test_get_data_from_json_file_error(mock_json):
    mock_json.side_effect = json.decoder.JSONDecodeError("", "}", 0)
    result = get_data_from_json_file(os.path.join("data", "operations.json"))
    assert result == []
    mock_json.assert_called_once()


# Тест функции чтения файла json содержащего не список.
@patch("json.load")
def test_get_data_from_json_file_not_list(mock_json):
    mock_json.return_value = {}
    result = get_data_from_json_file(os.path.join("data", "operations.json"))
    assert result == []
    mock_json.assert_called_once()


# Тест функции чтения не существующего файла json.
def test_get_data_from_json_file_not_found():
    result = get_data_from_json_file("A file that does not exist")
    assert result == []


# Тест функции чтения файлов.
def test_get_data_from_file():
    result = get_data_from_file(os.path.join("data", "transactions.csv"))
    assert result[0]["id"] == 650703

    result = get_data_from_file(os.path.join("data", "transactions_excel.xlsx"))
    assert result[0]["id"] == 650703

    result = get_data_from_file(os.path.join("data", "operations.json"))
    assert result[0]["id"] == 441945886


# Тест функции чтения файла с не правильным расширением,
# или не существующего.
def test_get_data_from_file_not_found():
    result = get_data_from_file("transaktions.pdf")
    assert result == []

    result = get_data_from_file("A file that does not exist.xlsx")
    assert result == []


# Тест функции чтения файлов с неверными данными.
# (Нет одного из необходимых столбцов в таблице EXCEL/CSV
# или ошибка декодирования JSON)
def test_get_data_from_file_errors():
    mock_csv = Mock(
        return_value=pd.DataFrame({"id": [0], "amount": [0], "currency_name": [""], "currency_code": [""]})
    )
    mock_excel = Mock(
        return_value=pd.DataFrame({"id": [0], "amount": [0], "currency_name": [""], "currency_code": [""]})
    )
    mock_json = Mock(side_effect=json.decoder.JSONDecodeError("", "}", 0))

    pd.read_csv = mock_csv
    pd.read_excel = mock_excel
    json.load = mock_json

    result = get_data_from_file(os.path.join("data", "transactions.csv"))
    assert result == []
    mock_csv.assert_called_once()

    result = get_data_from_file(os.path.join("data", "transactions_excel.xlsx"))
    assert result == []
    mock_excel.assert_called_once()

    result = get_data_from_file(os.path.join("data", "operations.json"))
    assert result == []
    mock_json.assert_called_once()
