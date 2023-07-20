from src.models.ingredient import Ingredient, Restriction


def test_ingredient():
    ingredient1 = Ingredient("manteiga")
    ingredient2 = Ingredient("manteiga")
    assert hash(ingredient1) == hash(ingredient2)

    ingredient1 = Ingredient("manteiga")
    ingredient2 = Ingredient("farinha")
    assert hash(ingredient1) != hash(ingredient2)

    ingredient1 = Ingredient("queijo mussarela")
    ingredient2 = Ingredient("queijo mussarela")
    assert ingredient1 == ingredient2

    ingredient1 = Ingredient("queijo mussarela")
    ingredient2 = Ingredient("farinha")
    assert ingredient1 != ingredient2

    ingredient = Ingredient("manteiga")
    assert repr(ingredient) == "Ingredient('manteiga')"

    ingredient = Ingredient("manteiga")
    assert ingredient.name == "manteiga"

    ingredient = Ingredient("queijo mussarela")
    expected_restrictions = {Restriction.LACTOSE, Restriction.ANIMAL_DERIVED}
    assert ingredient.restrictions == expected_restrictions
