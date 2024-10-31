from project1.animals.animal import Bird
from project1.food import Meat, Seed, Fruit, Vegetable


class Owl(Bird):
    @property
    def food_that_eats(self):
        return [Meat]

    @property
    def gained_weight(self):
        return 0.25

    def make_sound(self):
        return "Hoot Hoot"


class Hen(Bird):
    @property
    def food_that_eats(self):
        return [Meat, Fruit, Vegetable, Seed]

    @property
    def gained_weight(self):
        return 0.35

    def make_sound(self):
        return "Cluck"
