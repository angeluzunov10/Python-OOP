from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, species):
        self.species = species

    @abstractmethod
    def make_sound(self):
        pass

    def get_species(self):
        return self.__class__.__name__.lower()


class Cat(Animal):
    def make_sound(self):
        return "meow"


class Dog(Animal):
    def make_sound(self):
        return "woof-woof"


def animal_sound(animals_list):
    for animal in animals_list:
        print(animal.make_sound())


animals = [Cat("cat"), Dog("dog")]
animal_sound(animals)
