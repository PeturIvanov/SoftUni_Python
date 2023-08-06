from project.loans.base_loan import BaseLoan


class StudentLoan(BaseLoan):
    INITIAL_INTEREST = 1.5   # Percent
    INITIAL_AMOUNT = 2000.0  # Euro

    def __init__(self):
        super().__init__(StudentLoan.INITIAL_INTEREST, StudentLoan.INITIAL_AMOUNT)

    def increase_interest_rate(self):
        self.interest_rate += 0.2