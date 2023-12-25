# Autotest_Fruityvice
Проект автоматизирует тестирования API веб-сайта [Fruityvice](https://www.fruityvice.com/). Документацию по API можно найти по [ссылке](https://www.fruityvice.com/doc/index.html#api-GET-GET).

## Установка и запуск
1. Скопировать проект в рабочую среду, по [ссылке](https://www.fruityvice.com/doc/index.html#api-GET-GET)
2. Установить необходимые библиотеки с помощью команды в терминале:
```sh
pip install -r requirements.txt
```
3. Запустить тесты с помощью команды в терминале:
```sh
python -m pytest [...]
```

## Структура проекта 
- API - классы для взаимодействия с api
- logs - логи запросов к серверу
- Models - Модели для работы с API
- schemas - Эталонные файлы json для проверки ответов
- utilities - вспомогательные классы-утилиты (для работы с json и.т.д)
