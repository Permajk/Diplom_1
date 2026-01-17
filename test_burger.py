import pytest



class TestBurger:

    # Проверка наличия булочки в бургере
    def test_set_buns_in_burger(self, mock_bun, burger):
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    # Проверка добавления ингредиента(соуса) в бургер
    def test_add_ingredient_in_burger(self, mock_sauce, burger):
        burger.add_ingredient(mock_sauce)
        assert burger.ingredients == [mock_sauce]

    # Проверка удаления ингредиента(начинки) из бургера с параметризацией
    @pytest.mark.parametrize("ingredient", ["INGREDIENT_TYPE_SAUCE", "INGREDIENT_TYPE_FILLING"])
    def test_remove_ingredient_in_burger(self, burger, ingredient):
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)
        assert burger.ingredients == []

    # Проверка перемещения ингредиентов в бургере
    def test_move_ingredient_in_burger(self, mock_sauce, mock_filling, burger):
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == mock_filling

    # Проверка стоимости бургера
    def test_get_price_burger(self, mock_bun, mock_sauce, mock_filling, burger):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        assert burger.get_price() == 1000

    # Проверка чека с информацией о бургере
    def test_get_receipt_in_burger(self, mock_bun, mock_sauce, mock_filling, burger):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        receipt = burger.get_receipt()
        expected_receipt = (
            f"(==== {mock_bun.get_name()} ====)\n"
            f"= {str(mock_sauce.get_type()).lower()} {mock_sauce.get_name()} =\n"
            f"= {str(mock_filling.get_type()).lower()} {mock_filling.get_name()} =\n"
            f"(==== {mock_bun.get_name()} ====)\n"
            f"\nPrice: {mock_bun.get_price() * 2 + mock_sauce.get_price() + mock_filling.get_price()}"
        )
        assert receipt == expected_receipt

