from project.loans.base_loan import BaseLoan


class MortgageLoan(BaseLoan):
    INITIAL_INTEREST_RATE = 3.5
    INITIAL_AMOUNT = 50000.0

    def __init__(self):
        super().__init__(MortgageLoan.INITIAL_INTEREST_RATE, MortgageLoan.INITIAL_AMOUNT)

    def increase_interest_rate(self):
        self.interest_rate += 0.5
