import pytest
from praktikum.burger import Burger


class TestBurger:

    def setup_method(self):
        self.burger = Burger()

    def test_set_buns(self, black_bun_mock):
        self.burger.set_buns(black_bun_mock)
        assert self.burger.bun == black_bun_mock

    def test_add_ingredient(self, ingredient_hot_sause_mock):
        self.burger.add_ingredient(ingredient_hot_sause_mock)
        assert self.burger.ingredients == [ingredient_hot_sause_mock]

    def test_remove_ingredient(self, ingredient_hot_sause_mock, ingredient_cutlet_mock):
        self.burger.add_ingredient(ingredient_hot_sause_mock)
        self.burger.add_ingredient(ingredient_cutlet_mock)
        self.burger.remove_ingredient(0)
        assert self.burger.ingredients == [ingredient_cutlet_mock]

    def test_move_ingredient(self, ingredient_hot_sause_mock, ingredient_cutlet_mock):
        self.burger.add_ingredient(ingredient_hot_sause_mock)
        self.burger.add_ingredient(ingredient_cutlet_mock)
        self.burger.move_ingredient(0,1)
        assert self.burger.ingredients == [ingredient_cutlet_mock, ingredient_hot_sause_mock]

    def test_get_price(self, black_bun_mock, ingredient_cutlet_mock, ingredient_hot_sause_mock):
        self.burger.bun = black_bun_mock
        self.burger.ingredients = [ingredient_cutlet_mock, ingredient_hot_sause_mock]
        black_bun_mock.get_price.return_value = 100
        ingredient_cutlet_mock.get_price.return_value = 100.50
        ingredient_hot_sause_mock.get_price.return_value = 100.51
        assert self.burger.get_price() == 401.01

    def test_get_receipt(self, black_bun_mock, ingredient_cutlet_mock, ingredient_hot_sause_mock):
        self.burger.bun = black_bun_mock
        self.burger.ingredients = [ingredient_cutlet_mock, ingredient_hot_sause_mock]
        black_bun_mock.get_name.return_value = "black bun"
        black_bun_mock.get_price.return_value = 100
        ingredient_cutlet_mock.get_name.return_value = "cutlet"
        ingredient_cutlet_mock.get_type.return_value = 'FILLING'
        ingredient_cutlet_mock.get_price.return_value = 100.50
        ingredient_hot_sause_mock.get_name.return_value = "hot sauce"
        ingredient_hot_sause_mock.get_type.return_value = 'SAUCE'
        ingredient_hot_sause_mock.get_price.return_value = 100.51
        expected_receipt = (
            "(==== black bun ====)\n"
            "= filling cutlet =\n"
            "= sauce hot sauce =\n"
            "(==== black bun ====)\n"
            "\n"
            f"Price: {self.burger.get_price()}"
        )
        assert self.burger.get_receipt() == expected_receipt
