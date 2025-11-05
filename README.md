Описание проекта

Проект автоматизированного тестирования веб-приложения с использованием Selenium WebDriver, Pytest и Allure для генерации детальных отчетов.

Технологии и синтаксис
Основные технологии:
Python 3.8+ - основной язык программирования

Selenium WebDriver - автоматизация веб-браузера

Pytest - фреймворк для написания и запуска тестов

Allure Framework - генерация визуальных отчетов

Page Object Pattern - паттерн проектирования тестов

Форматирование кода:
Код соответствует PEP 8

Используются type hints для указания типов

Docstrings для документирования методов

Allure steps для детализации шагов тестов

Предварительные требования
1. Установка Python
Скачайте Python 3.8+ с официального сайта

Убедитесь, что Python добавлен в PATH

2. Установка зависимостей
bash
pip install -r requirements.txt

3. Установка Allure Framework
Windows:
bash
# Через scoop (рекомендуется)
scoop install allure

# Или скачайте с GitHub и добавьте в PATH
# https://github.com/allure-framework/allure2/releases

Проверка установки:
bash
allure --version

Запуск тестов для формирования отчета Allure
Способ 1: Базовый запуск
bash
# Запуск всех тестов с генерацией Allure результатов
pytest --alluredir=./allure-results

Способ 2: Запуск конкретного теста
bash
pytest tests/test_shop_allure.py --alluredir=./allure-results
Способ 3: С очисткой предыдущих результатов
bash
pytest --alluredir=./allure-results --clean-alluredir
Способ 4: С подробным выводом
bash
pytest --alluredir=./allure-results -v
Способ 5: Параллельный запуск
bash
pytest --alluredir=./allure-results -n 2
Просмотр сформированного отчета Allure
Способ 1: Локальный сервер (рекомендуется)
bash
allure serve ./allure-results
Команда автоматически:

Запустит локальный веб-сервер

Сгенерирует отчет

Откроет браузер с отчетом

Обычно по адресу: http://localhost:8080

Способ 2: Генерация статического HTML отчета
bash
# Генерация отчета
allure generate ./allure-results -o ./allure-report --clean

# Открытие отчета
allure open ./allure-report
Способ 3: Ручное открытие в браузере
bash
# После генерации отчета
allure generate ./allure-results -o ./allure-report --clean

# Открытие напрямую
# Windows:
start ./allure-report/index.html

# Mac:
open ./allure-report/index.html

# Linux:
xdg-open ./allure-report/index.html
