class Worker:
    def __init__(self, name, salary, energy):
        self.name = name
        self.energy = energy
        self.salary = salary
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception("Not enough energy.")

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f"{self.name} has saved {self.money} money."
