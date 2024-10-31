from project1.person import Person
from project1.employee import Employee


class Teacher(Person, Employee):
    def teach(self):
        return "teaching..."
