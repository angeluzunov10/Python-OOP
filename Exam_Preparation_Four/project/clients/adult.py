from project.clients.base_client import BaseClient


class Adult(BaseClient):
    INITIAL_INTEREST_RATE = 4.0
    ALLOWED_LOAN_TYPES = "MortgageLoan"

    def __init__(self, name, client_id, income):
        super().__init__(name, client_id, income, Adult.INITIAL_INTEREST_RATE)

    def increase_clients_interest(self):
        self.interest += 2
