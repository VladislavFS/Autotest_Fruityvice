import logging
from tests.API.custom_requests import Client
from jsonschema import validate

logger = logging.getLogger("api")


class ApiTest:
    def __init__(self, path):
        self.host = 'https://www.fruityvice.com'
        self.path = path

    def fruts_get(self, valid_schema: dict, **kwargs):
        """
        Функция производит отправку GET запроса на сервис, валидирует ответ и возвращает ответ и код
        :param valid_schema: Схема JSON по которой будет произведена проверка ответа
        :return: Возврашает кастомный объект с атрибутами: status (Код ответа) и json(Тело ответа)
        """
        # Получаем кастомный объект с кодом и телом ответа
        response = Client.custom_req(method='GET', url=f'{self.host}{self.path}', **kwargs)
        validate(instance=response.json, schema=valid_schema)  # Производим валидацию тела ответа с переданной схемой
        logger.info(response.json)
        return response

    def fruts_put(self, body: dict):
        """
        Функция производит отправку PUT запроса на сервис, и возвращает ответ и код
        :return: Возврашает кастомный объект с атрибутами: status (Код ответа) и json(Тело ответа)
        """
        # Получаем кастомный объект с кодом и телом ответа
        response = Client.custom_req(method='PUT', url=f'{self.host}{self.path}', json=body)
        logger.info(response.json)
        return response
