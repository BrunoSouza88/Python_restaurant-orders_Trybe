from src.models.ingredient import Ingredient, Restriction


def test_ingredient():
    # Req 1.1
    ingredient1 = Ingredient("manteiga")
    ingredient2 = Ingredient("manteiga")
    assert hash(ingredient1) == hash(ingredient2)

    # Req 1.2
    ingredient1 = Ingredient("manteiga")
    ingredient2 = Ingredient("farinha")
    assert hash(ingredient1) != hash(ingredient2)

    # Req 1.3
    ingredient1 = Ingredient("queijo mussarela")
    ingredient2 = Ingredient("queijo mussarela")
    assert ingredient1 == ingredient2

    # Req 1.4
    ingredient1 = Ingredient("queijo mussarela")
    ingredient2 = Ingredient("farinha")
    assert ingredient1 != ingredient2

    # Req 1.5
    ingredient = Ingredient("manteiga")
    assert repr(ingredient) == "Ingredient('manteiga')"

    # Req 1.6
    ingredient = Ingredient("manteiga")
    assert ingredient.name == "manteiga"

    # Req 1.7
    ingredient = Ingredient("queijo mussarela")
    expected_restrictions = {Restriction.LACTOSE, Restriction.ANIMAL_DERIVED}
    assert ingredient.restrictions == expected_restrictions
