from tests.API.api import ApiTest
import pytest
import random
from schemas.Get_fruits import valid_schema
from schemas.Get_fruits import valid_schema_404


class TestGetFrutsNutrition:

    @pytest.mark.parametrize('nutrition, ave, max_n', [('carbohydrates', 20, 40),
                                                       ('protein', 10, 20),
                                                       ('fat', 2, 15),
                                                       ('calories', 100, 700),
                                                       ('sugar', 10, 20)
                                                       ])
    def test_get_fruits_nutrition(self, nutrition, ave, max_n):
        min_n = round(random.uniform(0, ave), 1)
        response = ApiTest(f'/api/fruit/{nutrition}').fruts_get(valid_schema, params={'min': min_n, 'max': max_n})
        assert response.status == 200
        for i in response.json:
            assert min_n <= i['nutritions'][nutrition] <= max_n

    @pytest.mark.parametrize('nutrition, min_n, max_n', [('carbohydrates', 200, 400),
                                                         ('protein', 100, 200),
                                                         ('fat', 200, 1500),
                                                         ('calories', 1000, 7000),
                                                         ('sugar', 100, 200)
                                                         ])
    def test_get_fruits_nutrition_error(self, nutrition, min_n, max_n):
        response = ApiTest(f'/api/fruit/{nutrition}').fruts_get(valid_schema_404, params={'min': min_n, 'max': max_n})
        assert response.status == 404
