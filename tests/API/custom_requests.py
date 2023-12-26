import requests
from tests.Models.models import ResponseModel


class Client:
    @staticmethod
    def custom_req(method: str, url, **kwargs) -> requests.Response:
        """
        :param method: Метод HTTP запроса. Принимает значения: GET, OPTIONS, HEAD, POST, PUT, PATCH, или DELETE.
        :param url: Адрес ресурса на который отправляеться запрос
        :param kwargs: params – (Необязательный) Словарь, список кортежей или байтов для отправки в строке запроса.
                       json – (Необязательный) Сериализуемый объект Python в формате JSON для отправки в теле запроса.
                       headers – (Необязательный) Словарь HTTP-заголовков для отправки с запросом.
        :return: Возврашает кастомный объект с атрибутами: status (Код ответа) и json(Тело ответа)
        """
        response = (requests.request(method, url, **kwargs))
        return ResponseModel(status=response.status_code, response=response.json())
