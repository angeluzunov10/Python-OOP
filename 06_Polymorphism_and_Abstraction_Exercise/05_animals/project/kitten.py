from project1.cat import Cat


class Kitten(Cat):
    def __init__(self, name, age):
        Cat.__init__(self, name, age, "Female")

    @staticmethod
    def make_sound():
        return "Meow"
