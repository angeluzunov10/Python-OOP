from project.clients.adult import Adult
from project.clients.student import Student
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan


class BankApp:
    VALID_LOANS = {
        "StudentLoan": StudentLoan,
        "MortgageLoan": MortgageLoan
    }

    VALID_CLIENTS = {
        "Student": Student,
        "Adult": Adult
    }

    def __init__(self, capacity):
        self.capacity = capacity
        self.loans = []
        self.clients = []

    def add_loan(self, loan_type):
        if loan_type not in self.VALID_LOANS:
            raise Exception("Invalid loan type!")

        loan = self.VALID_LOANS[loan_type]()
        self.loans.append(loan)

        return f"{loan_type} was successfully added."

    def add_client(self, client_type, client_name, client_id, income):
        if client_type not in self.VALID_CLIENTS:
            raise Exception("Invalid client type!")

        if len(self.clients) >= self.capacity:
            return "Not enough bank capacity."

        client = self.VALID_CLIENTS[client_type](client_name, client_id, income)
        self.clients.append(client)

        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type, client_id):
        loan = next(filter(lambda l: l.__class__.__name__ == loan_type, self.loans))
        client = next(filter(lambda c: c.client_id == client_id, self.clients))

        if not loan_type == client.ALLOWED_LOAN_TYPES:
            raise Exception("Inappropriate loan type!")

        self.loans.remove(loan)
        client.loans.append(loan)
        return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."

    def remove_client(self, client_id):
        try:
            client = next(filter(lambda c: c.client_id == client_id, self.clients))
        except StopIteration:
            raise Exception("No such client!")

        if client.loans:
            raise Exception("The client has loans! Removal is impossible!")

        self.clients.remove(client)

        return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type):
        loans_of_given_type = [loan for loan in self.loans if loan.__class__.__name__ == loan_type]

        for loan in loans_of_given_type:
            loan.increase_interest_rate()

        return f"Successfully changed {len(loans_of_given_type)} loans."

    def increase_clients_interest(self, min_rate):
        changed_interests = 0
        for c in self.clients:
            if c.interest < min_rate:
                c.increase_clients_interest()
                changed_interests += 1

        return f"Number of clients affected: {changed_interests}."

    def get_statistics(self):
        total_clients_count = len(self.clients)
        total_clients_income = sum([c.income for c in self.clients])
        loans_count_granted_to_clients = sum([len(c.loans) for c in self.clients])
        loans_count_not_granted = len(self.loans)

        granted_sum = 0
        for client in self.clients:
            for loan in client.loans:
                granted_sum += loan.amount

        not_granted_sum = 0
        for loan in self.loans:
            not_granted_sum += loan.amount

        avg_client_interest_rate = sum([c.interest for c in self.clients]) / len(self.clients) \
            if len(self.clients) != 0 else 0

        return f"Active Clients: {total_clients_count}\n" \
               f"Total Income: {total_clients_income:.2f}\n" \
               f"Granted Loans: {loans_count_granted_to_clients}, Total Sum: {granted_sum:.2f}\n" \
               f"Available Loans: {loans_count_not_granted}, Total Sum: {not_granted_sum:.2f}\n" \
               f"Average Client Interest Rate: {avg_client_interest_rate:.2f}"

