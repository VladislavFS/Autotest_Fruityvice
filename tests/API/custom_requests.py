import requests
from tests.Models.models import ResponseModel


class Client:
    @staticmethod
    def custom_req(method: str, url, **kwargs) -> requests.Response:
        """
            Request method
            method: method for the new Request object: GET, OPTIONS, HEAD, POST, PUT, PATCH, or DELETE. # noqa
            url – URL for the new Request object.
            **kwargs:
                params – (optional) Dictionary, list of tuples or bytes to send in the query string for the Request. # noqa
                json – (optional) A JSON serializable Python object to send in the body of the Request. # noqa
                headers – (optional) Dictionary of HTTP Headers to send with the Request.
        """
        response = (requests.request(method, url, **kwargs))
        return ResponseModel(status=response.status_code, response=response.json())
