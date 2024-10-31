from project1.cat import Cat


class Tomcat(Cat):
    def __init__(self, name, age):
        Cat.__init__(self, name, age, "Male")

    @staticmethod
    def make_sound():
        return "Hiss"
