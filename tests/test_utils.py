"""Тестирование модуля utils"""

import json
import os
from unittest.mock import Mock

from src.utils import get_data_from_json_file


# Тест функции чтения файла json.
def test_get_data_from_json_file():
    result = get_data_from_json_file(os.path.join("data", "operations.json"))
    assert result[0]["id"] == 441945886


# Тест функции чтения файла json с ошибкой или пустого.
def test_get_data_from_json_file_error():
    mock_json = Mock(side_effect=json.decoder.JSONDecodeError("", "}", 0))
    json.load = mock_json
    result = get_data_from_json_file(os.path.join("data", "operations.json"))
    assert result == []
    mock_json.assert_called_once()


# Тест функции чтения файла json содержащего не список.
def test_get_data_from_json_file_not_list():
    mock_json = Mock(return_value={})
    json.load = mock_json
    result = get_data_from_json_file(os.path.join("data", "operations.json"))
    assert result == []
    mock_json.assert_called_once()


# Тест функции чтения не существующего файла json.
def test_get_data_from_json_file_not_found():
    result = get_data_from_json_file("A file that does not exist")
    assert result == []
