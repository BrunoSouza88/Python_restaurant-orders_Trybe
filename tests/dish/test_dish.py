import pytest
from src.models.dish import Dish
from src.models.ingredient import Ingredient, Restriction


def test_dish():
    dish = Dish("Spaghetti Carbonara", 15.99)
    assert dish.name == "Spaghetti Carbonara"

    dish1 = Dish("Spaghetti Carbonara", 15.99)
    dish2 = Dish("Spaghetti Carbonara", 15.99)
    assert hash(dish1) == hash(dish2)

    dish1 = Dish("Spaghetti Carbonara", 15.99)
    dish2 = Dish("Pasta Bolognese", 14.99)
    assert hash(dish1) != hash(dish2)

    dish1 = Dish("Spaghetti Carbonara", 15.99)
    dish2 = Dish("Spaghetti Carbonara", 15.99)
    assert dish1 == dish2

    dish1 = Dish("Spaghetti Carbonara", 15.99)
    dish2 = Dish("Pasta Bolognese", 14.99)
    assert dish1 != dish2

    dish = Dish("Spaghetti Carbonara", 15.99)
    assert repr(dish) == "Dish('Spaghetti Carbonara', R$15.99)"

    with pytest.raises(TypeError):
        Dish("Spaghetti Carbonara", "15.99")

    with pytest.raises(ValueError):
        Dish("Spaghetti Carbonara", -10)

    dish = Dish("Spaghetti Carbonara", 15.99)
    ingredient = Ingredient("manteiga")
    dish.add_ingredient_dependency(ingredient, -2)
    assert dish.recipe.get(ingredient) == -2

    ingredient1 = Ingredient("manteiga")
    ingredient2 = Ingredient("queijo mussarela")
    dish.add_ingredient_dependency(ingredient1, 2)
    dish.add_ingredient_dependency(ingredient2, 1)

    restrictions = dish.get_restrictions()
    expected_restrictions = {Restriction.LACTOSE, Restriction.ANIMAL_DERIVED}
    assert restrictions == expected_restrictions

    ingredients = dish.get_ingredients()
    assert ingredient1 in ingredients
    assert ingredient2 in ingredients
