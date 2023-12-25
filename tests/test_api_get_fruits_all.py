from tests.API.api import ApiTest
from schemas.Get_fruits import valid_schema


class TestGetAllFruts:

    def test_get_fruits_all(self):
        response = ApiTest('/api/fruit/all').fruts_get(valid_schema)
        assert response.status == 200
