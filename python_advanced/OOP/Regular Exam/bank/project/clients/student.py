from project.clients.base_client import BaseClient


class Student(BaseClient):
    INITIAL_INTEREST = 2.0      #Percent

    def __init__(self, name: str, client_id: str, income: float):
        super().__init__(name, client_id, income, Student.INITIAL_INTEREST)

    @property
    def type_of_loan(self):
        return "StudentLoan"

    @property
    def get_increase_rate(self):
        return 1.0