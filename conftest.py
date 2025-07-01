import pytest
from unittest.mock import Mock


@pytest.fixture
def bun_mock():
    mock_bun = Mock()
    mock_bun.name = None
    mock_bun.price = None
    return mock_bun

@pytest.fixture
def ingredients_mock():
    mock_ingredient = Mock()
    mock_ingredient.name = None
    mock_ingredient.price = None
    return mock_ingredient
