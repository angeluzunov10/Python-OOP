from unittest import TestCase, main

from project1.mammal import Mammal


class TestMammal(TestCase):
    def setUp(self):
        self.mammal = Mammal("Steven", "lion", "Roar!")

    def test_init_correct(self):
        self.assertEqual("Steven", self.mammal.name)
        self.assertEqual("lion", self.mammal.type)
        self.assertEqual("Roar!", self.mammal.sound)

    def test_making_sound_returns_string(self):
        self.assertEqual("Steven makes Roar!", self.mammal.make_sound())

    def test_get_kingdom_returns_kingdom(self):
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_get_info_returns_string(self):
        self.assertEqual("Steven is of type lion", self.mammal.info())



if __name__ == '__main__':
    main()