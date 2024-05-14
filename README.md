# Учебный проект по Python
## Описание
Работа над виджетом банковских операций клиента.
## Модули
* mask
  + Функция маскировки номера счета
  + Функция маскировки номера карты
* widget
  + Фунция форматирования реквезитов 
    с исползованием маскировки
  + Функция форматирования даты
* processing
  + Функция фильтрации операций по состоянию
  + Функция сортировки операций по дате
* generators
  + Функция-генератор фильтрации операций по валюте
  + Функция-генератор дескрипторов операций
  + Функция-генератор номеров банковских карт в заданном диапазоне
## Линтеры
* `flake8`
* `black`
* `mypy`
* `isort`
## Установка
1. Клонировать проект
```
https://github.com/Ramazan-Z/Banking_Widgets.git
```
2. Установить зависимости
```
poetry install
```
## Тестирование
Проект покрыт юнит-тестами
* Запуск теста: `pytest`
* Покрытие кода: `pytest --cov`
