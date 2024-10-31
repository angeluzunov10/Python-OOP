from project.loans.base_loan import BaseLoan


class StudentLoan(BaseLoan):
    INITIAL_INTEREST_RATE = 1.5
    INITIAL_AMOUNT = 2000.0

    def __init__(self):
        super().__init__(StudentLoan.INITIAL_INTEREST_RATE, StudentLoan.INITIAL_AMOUNT)

    def increase_interest_rate(self):
        self.interest_rate += 0.2
