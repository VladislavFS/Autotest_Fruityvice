from tests.API.api import Api_test
from schemas.Get_fruits import valid_schema
from schemas.Get_fruits import valid_schema_404
from utilities.Fruit_class import random_fruit_class

class TestGetFruts:

    def test_get_fruits_genus(self):
        for i in range(3):
            genus = random_fruit_class('genus')
            response = Api_test(f'/api/fruit/genus/{genus}').fruts_get(valid_schema)
            assert response.status == 200
            for x in response.json:
                assert x['genus']== genus

    def test_get_fruits_genus_error(self):
        genus = random_fruit_class('order')
        response = Api_test(f'/api/fruit/genus/{genus}').fruts_get(valid_schema_404)
        assert response.status == 404