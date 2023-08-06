from project.clients.base_client import BaseClient


class Adult(BaseClient):
    INITIAL_INTEREST = 4.0  # Percent

    def __init__(self, name: str, client_id: str, income: float):
        super().__init__(name, client_id, income, Adult.INITIAL_INTEREST)

    @property
    def get_increase_rate(self):
        return 2.0

    @property
    def type_of_loan(self):
        return "MortgageLoan"