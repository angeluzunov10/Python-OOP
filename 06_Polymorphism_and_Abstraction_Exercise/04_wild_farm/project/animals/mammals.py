from project1.animals.animal import Mammal
from project1.food import Meat, Fruit, Vegetable


class Mouse(Mammal):
    @property
    def food_that_eats(self):
        return [Fruit, Vegetable]

    @property
    def gained_weight(self):
        return 0.1

    def make_sound(self):
        return "Squeak"


class Dog(Mammal):
    @property
    def food_that_eats(self):
        return [Meat]

    @property
    def gained_weight(self):
        return 0.40

    def make_sound(self):
        return "Woof!"


class Cat(Mammal):
    @property
    def food_that_eats(self):
        return [Meat, Vegetable]

    @property
    def gained_weight(self):
        return 0.30

    def make_sound(self):
        return "Meow"


class Tiger(Mammal):
    @property
    def food_that_eats(self):
        return [Meat]

    @property
    def gained_weight(self):
        return 1

    def make_sound(self):
        return "ROAR!!!"
