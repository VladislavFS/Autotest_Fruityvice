# Autotest_Fruityvice
Проект автоматизирует тестирование API веб-сайта [Fruityvice](https://www.fruityvice.com/). Документацию по API можно найти по [ссылке](https://www.fruityvice.com/doc/index.html#api-GET-GET). API веб-сайта [Fruityvice](https://www.fruityvice.com/) позволяет получать в ответе фрукты по заданным параметрам, а так же предлагать на добавление в БД свои фрукты.  

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
[Allure отчет](https://vladislavfs.github.io/Autotest_Fruityvice/)

## Структура проекта 
- API - классы для взаимодействия с api
- logs - логи запросов к серверу
- Models - Модели для работы с API
- schemas - Эталонные файлы json для проверки ответов
- utilities - вспомогательные классы-утилиты (для работы с json и.т.д)

## Описание работы кода
Тесты проверяют данные в теле ответа и коды ответа от тестируемых сервисов. Порядок вызова модулей: test_* -> api -> custom_requests. Код тестов(test_*) обращается к классу ApiTest(api.py) с заданным методом(fruts_get или fruts_get), при этом создается объект с инициализированными атрибутами: host, path, client. Атрибуты host и path формируют URL на который будет отправлен запрос. Атрибут client содержит созданный объект класса Client(custom_requests.py). Методы класса ApiTest вызывают метод класса Client, который возвращает кастомный объект с атрибутами status(Код ответа) и json(Тело ответа). Объект класса Client возвращается в код теста, где производятся проверки. 

## Чек-лист
1. Сервис "Request all Fruits". Получение положительного ответа (код 200). Тест - test_api_get_fruits_all
2. Сервис "Request fruits with given family". Получение положительного ответа (код 200), в котором возвращаются только фрукты с заданным, существующим "family". Тест - test_api_get_fruits_family
3. Сервис "Request fruits with given family". Получение ответа с ошибкой (код 404), в котором не были возвращены фрукты с несуществующим "family". Тест - test_api_get_fruits_family
4. Сервис "Request fruits with given genus". Получение положительного ответа (код 200), в котором возвращаются только фрукты с заданным, существующим "genus". Тест - test_api_get_fruits_genus
5. Сервис "Request fruits with given genus". Получение ответа с ошибкой (код 404), в котором не были возвращены фрукты с несуществующим "genus". Тест - test_api_get_fruits_genus
6. Сервис "Request fruits with given order". Получение положительного ответа (код 200), в котором возвращаются только фрукты с заданным, существующим "order". Тест - test_api_get_fruits_order
7. Сервис "Request fruits with given order". Получение ответа с ошибкой (код 404), в котором не были возвращены фрукты с несуществующим "order". Тест - test_api_get_fruits_order
8. Сервис "Request Fruits information by nutrition value". Получение положительного ответа (код 200), в котором возвращаются только фрукты с заданными параметрами "nutrition". Тест - test_api_get_fruits_nutrition
9. Сервис "Request Fruits information by nutrition value". Получение ответа с ошибкой (код 404), в котором не были возвращены фрукты с несуществующими параметрами "nutrition". Тест - test_api_get_fruits_nutrition
10. Сервис "Add a fruit to the database". Получение положительного ответа (код 200 или 422). Тест - test_api_put_fruits

## Ограничения
Сервис "Add a fruit to the database" при отправке запроса на добавление фрукта, добавляет фрукт в "список на валидацию". Код 200 в ответе возвращается если в "списке на валидацию" нет добавляемого фрукта. Код 422 возвращается если в "списке на валидацию" уже есть добавляемый фрукт. Фрукты из "списка на валидацию" не попадают в возвращаемый результат сервисов GET. Получить доступ к "списку на валидацию" невозможно, из-за чего невозможно отправлять запросы с гарантией получения кода 200 или 422, по этому в тесте test_api_put_fruits идет проверка кода ответа 200 ИЛИ 422. 
