import pytest
from unittest.mock import Mock
from burger import Burger
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


# Мок булочки
@pytest.fixture
def mock_bun():
    mock_bun = Mock()
    mock_bun.get_name.return_value = "red bun"
    mock_bun.get_price.return_value = 300
    return mock_bun

# Мок соуса
@pytest.fixture
def mock_sauce():
    mock_sauce = Mock()
    mock_sauce.get_price.return_value = 200
    mock_sauce.get_name.return_value = "sour cream"
    mock_sauce.get_type.return_value = INGREDIENT_TYPE_SAUCE
    return mock_sauce

# Мок начинки
@pytest.fixture
def mock_filling():
    mock_filling = Mock()
    mock_filling.get_price.return_value = 200
    mock_filling.get_name.return_value = "dinosaur"
    mock_filling.get_type.return_value = INGREDIENT_TYPE_FILLING
    return mock_filling

# Создаем объект бургера
@pytest.fixture
def burger():
    return Burger()
