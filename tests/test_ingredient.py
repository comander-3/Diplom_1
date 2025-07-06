import pytest
from praktikum.ingredient import Ingredient

class TestIngredient:
    # в методах класса Ingredient не реализовано отсечение по типу, поэтому тесты проходят с любыми параметрами
    @pytest.mark.parametrize(
        'type_ingredient, name, price',
        [
            ('SAUCE', 'hot chili', 5),
            ('SAUCE', 'hot chili', -5),
            ('SAUCE', 'hot chili', '5'),
            ('SAUCE', 'hot chili', 5.25)
        ]
    )
    def test_get_price(self, type_ingredient, name, price):
        ingredient = Ingredient(type_ingredient, name, price)
        assert ingredient.get_price() == price


    @pytest.mark.parametrize(
        'type_ingredient, name, price',
        [
            ('SAUCE', 'hot chili', 5),
            ('SAUCE', '', 5),
            ('SAUCE', 0, 5),
            ('SAUCE', None, 5)
        ]
    )
    def test_get_name(self, type_ingredient, name, price):
        ingredient = Ingredient(type_ingredient, name, price)
        assert ingredient.get_name() == name


    @pytest.mark.parametrize(
        'type_ingredient, name, price',
        [
            ('SAUCE', 'hot chili', 5),
            ('', 'hot chili', 5),
            (1.0, 'hot chili', 5),
            (None, 'hot chili', 5)
        ]
    )
    def test_get_type(self, type_ingredient, name, price):
        ingredient = Ingredient(type_ingredient, name, price)
        assert ingredient.get_type() == type_ingredient
