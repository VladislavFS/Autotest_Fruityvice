import logging
from tests.API.custom_requests import Client
from jsonschema import validate

logger = logging.getLogger("api")


class ApiTest:
    def __init__(self, path):
        self.host = 'https://www.fruityvice.com'
        self.path = path
        self.client = Client()

    def fruts_get(self, valid_schema: dict, **kwargs):
        response = self.client.custom_req(method='GET', url=f'{self.host}{self.path}', **kwargs)
        validate(instance=response.json, schema=valid_schema)
        logger.info(response.json)
        return response

    def fruts_put(self, body: dict):
        response = self.client.custom_req(method='PUT', url=f'{self.host}{self.path}', json=body)
        logger.info(response.json)
        return response
