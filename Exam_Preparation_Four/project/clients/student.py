from project.clients.base_client import BaseClient


class Student(BaseClient):
    INITIAL_INTEREST_RATE = 2
    ALLOWED_LOAN_TYPES = "StudentLoan"

    def __init__(self, name, client_id, income):
        super().__init__(name, client_id, income, Student.INITIAL_INTEREST_RATE)

    def increase_clients_interest(self):
        self.interest += 1
