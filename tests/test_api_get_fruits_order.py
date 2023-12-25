from tests.API.api import ApiTest
from schemas.Get_fruits import valid_schema
from schemas.Get_fruits import valid_schema_404
from utilities.Fruit_class import random_fruit_class


class TestGetFruts:

    def test_get_fruits_order(self):
        for i in range(3):
            order = random_fruit_class('order')
            response = ApiTest(f'/api/fruit/order/{order}').fruts_get(valid_schema)
            assert response.status == 200
            for x in response.json:
                assert x['order'] == order

    def test_get_fruits_order_error(self):
        order = random_fruit_class('genus')
        response = ApiTest(f'/api/fruit/order/{order}').fruts_get(valid_schema_404)
        assert response.status == 404
