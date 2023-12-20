from tests.API.api import Api_test
from schemas.Get_fruits import valid_schema
from schemas.Get_fruits import valid_schema_404
from utilities.Fruit_class import random_fruit_class

class TestGetFruts:

    def test_get_fruits_family(self):
        for i in range(3):
            family = random_fruit_class('family')
            response = Api_test(f'/api/fruit/family/{family}').fruts_get(valid_schema)
            assert response.status == 200
            for x in response.json:
                assert x['family']== family

    def test_get_fruits_family_error(self):
        family = random_fruit_class('order')
        response = Api_test(f'/api/fruit/family/{family}').fruts_get(valid_schema_404)
        assert response.status == 404