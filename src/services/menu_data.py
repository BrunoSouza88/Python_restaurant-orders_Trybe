import csv
from src.models.dish import Dish
from src.models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path):
        self.source_path = source_path
        self.dishes = set()
        self._load_data()

    def _load_data(self):
        with open(self.source_path, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # skip header
            for row in reader:
                dish_name, price, ingredient_name, quantity = row
                dish = self._get_dish(dish_name, price)
                ingredient = Ingredient(ingredient_name)
                dish.add_ingredient_dependency(ingredient, int(quantity))

    def _get_dish(self, name, price):
        for dish in self.dishes:
            if dish.name == name:
                return dish
        dish = Dish(name, float(price))
        self.dishes.add(dish)
        return dish
