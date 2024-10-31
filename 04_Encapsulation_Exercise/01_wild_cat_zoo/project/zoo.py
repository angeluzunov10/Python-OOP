from project1.animal import Animal
from project1.worker import Worker


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price):
        if self.__animal_capacity > len(self.animals):
            if price <= self.__budget:
                self.animals.append(animal)
                self.__budget -= price

                return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

            return "Not enough budget"

        return "Not enough space for animal"

    def hire_worker(self, worker: Worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"

        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        try:
            worker = [w for w in self.workers if w.name == worker_name][0]
            self.workers.remove(worker)
            return f"{worker_name} fired successfully"
        except IndexError:
            return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        money_to_pay = sum([w.salary for w in self.workers])
        if money_to_pay <= self.__budget:
            self.__budget -= money_to_pay
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        money_to_feed_animals = sum([a.money_for_care for a in self.animals])

        if money_to_feed_animals <= self.__budget:
            self.__budget -= money_to_feed_animals
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return f"You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = f"You have {len(self.animals)} animals\n"

        lions = [a for a in self.animals if a.__class__.__name__ == "Lion"]
        amount_of_lions = len(lions)
        result += f"----- {amount_of_lions} Lions:\n"
        for lion in lions:
            result += f"{lion}\n"

        tigers = [a for a in self.animals if a.__class__.__name__ == "Tiger"]
        amount_of_tigers = len(tigers)
        result += f"----- {amount_of_tigers} Tigers:\n"
        for tiger in tigers:
            result += f"{tiger}\n"

        cheetahs = [a for a in self.animals if a.__class__.__name__ == "Cheetah"]
        amount_of_cheetahs = len(cheetahs)
        result += f"----- {amount_of_cheetahs} Cheetahs:\n"
        for cheetah in cheetahs:
            result += f"{cheetah}\n"

        return result[:-1]

    def workers_status(self):
        result = f"You have {len(self.workers)} workers\n"

        keepers = [w for w in self.workers if w.__class__.__name__ == "Keeper"]
        amount_of_keepers = len(keepers)
        result += f"----- {amount_of_keepers} Keepers:\n"
        for keeper in keepers:
            result += f"{keeper}\n"

        caretakers = [w for w in self.workers if w.__class__.__name__ == "Caretaker"]
        amount_of_caretakers = len(caretakers)
        result += f"----- {amount_of_caretakers} Caretakers:\n"
        for caretaker in caretakers:
            result += f"{caretaker}\n"

        vets = [w for w in self.workers if w.__class__.__name__ == "Vet"]
        amount_of_vets = len(vets)
        result += f"----- {amount_of_vets} Vets:\n"
        for vet in vets:
            result += f"{vet}\n"

        return result[:-1]
