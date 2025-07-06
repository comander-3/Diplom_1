import pytest
from unittest.mock import Mock

@pytest.fixture
def black_bun_mock():
    mock_bun = Mock()
    mock_bun.name = "black bun"
    mock_bun.price = 100
    return mock_bun

@pytest.fixture
def ingredient_hot_sause_mock():
    mock_ingredient = Mock()
    mock_ingredient.type = 'SAUCE'
    mock_ingredient.name = "hot sauce"
    mock_ingredient.price = 100
    return mock_ingredient

@pytest.fixture
def ingredient_cutlet_mock():
    mock_ingredient = Mock()
    mock_ingredient.type = 'FILLING'
    mock_ingredient.name = "cutlet"
    mock_ingredient.price = 100
    return mock_ingredient
