# Учебный проект по Python
## Описание
Работа над виджетом банковских операций клиента.
Программа читает данные и файла. Фильтрует и сортирует
операции по критериям, которые ввел пользователь.
И выводит в консоль результат, отформатированный для
удобного чтения.
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
  + Функция фильтрации по строке в описании
  + Функция подсчета транзакций по выбранным категориям
* generators
  + Функция-генератор фильтрации операций по валюте
  + Функция-генератор дескрипторов операций
  + Функция-генератор номеров банковских карт в заданном диапазоне
* decorators
  + Функция-декоратор для логирования вызова функции
    и ее результата в файл или в консоль.
* utils
  + Функция чтения транзакций из файла json
  + Функция чтения транзакций из файлов Excel и CSV
* external_api
  + Функция конвертации суммы транзакции в рубли с
    использованием запросов на внешний API
* main
  + Функция выбора файла для обработки
  + Функция выбора фильтра по состоянию операции
  + Функция выбора сортировки по дате
  + Функция выбора фильтрации по валюте
  + Функция выбора фильтрации по строке в описании
  + Функция форматирования и печати результатов
## Логирование
Проект имеет логирование с использованием logging
в следующих модулях:
* mask.py
* utils.py
## Линтеры
* `flake8`
* `black`
* `mypy`
* `isort`
* `types-requests`
* `pandas-stubs`
## Зависимости
* `requests`
* `python-dotenv`
* `pandas`
* `openpyxl`
* `xlrd`
## Установка
1. Клонировать проект
```
https://github.com/Ramazan-Z/Banking_Widgets.git
```
2. Установить зависимости
```
poetry install
```
3. Создать файл .env из копии  .env.example и заменить
    значения переменных реальными данными (Токен для APILayer)
## Запуск
main.py
## Тестирование
Проект покрыт юнит-тестами
* Запуск теста: `pytest`
* Покрытие кода: `pytest --cov`
