from project.loans.base_loan import BaseLoan


class MortgageLoan(BaseLoan):
    INITIAL_INTEREST = 3.5   # Percent
    INITIAL_AMOUNT = 50000.0  # Euro

    def __init__(self):
        super().__init__(MortgageLoan.INITIAL_INTEREST, MortgageLoan.INITIAL_AMOUNT)

    def increase_interest_rate(self):
        self.interest_rate += 0.5