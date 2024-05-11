"""Тестирование модуля processing.py"""

from src.processing import filter_state_operations, sorted_date_operacions


#  Тест функции фильтра, случай пустого списка
def test_filter_state_operations_empty(transaction_empty):
    assert filter_state_operations(transaction_empty) == []


#  Тест функции фильтра по статусу исполнено
def test_filter_state_operations_executed(transaction_total, transaction_executed):
    assert filter_state_operations(transaction_total) == transaction_executed


# Тест функции фильтра по статусу отменено
def test_filter_state_operations_cancaled(transaction_total, transaction_canceled):
    assert filter_state_operations(transaction_total, "CANCELED") == transaction_canceled


# Тест функции сортировки даты по убыванию
def test_sorted_date_operations_decreasing(transaction_total):
    sequence = sorted_date_operacions(transaction_total)
    assert sequence[0]["date"] > sequence[-1]["date"]


# Тест функции сортировки даты по возрастанию
def test_sorted_date_operations(transaction_total):
    sequence = sorted_date_operacions(transaction_total, False)
    assert sequence[0]["date"] < sequence[-1]["date"]
