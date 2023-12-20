from tests.API.api import Api_test
from tests.Models.models import RegisterFruts

class TestPutFruts:

    def test_put_fruits(self):
        body = RegisterFruts.random_body_fruts()
        response = Api_test('/api/fruit').fruts_put(body)
        assert response.status == 202 or 422
