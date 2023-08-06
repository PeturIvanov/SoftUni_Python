from project.clients.adult import Adult
from project.clients.student import Student
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan


class BankApp:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans = []
        self.clients = []
        self.granted_loans = 0

    def add_loan(self, loan_type: str):
        if loan_type not in self.valid_loan_types:
            raise Exception("Invalid loan type!")

        new_loan = self.valid_loan_types[loan_type]()
        self.loans.append(new_loan)
        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if client_type not in self.valid_client_types:
            raise Exception("Invalid client type!")

        if len(self.clients) >= self.capacity:
            return "Not enough bank capacity."

        new_client = self.valid_client_types[client_type](client_name, client_id, income)
        self.clients.append(new_client)
        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):
        client = self._find_client_by_id(client_id)
        loan = self._find_loan_by_type(loan_type)

        if client.type_of_loan != loan_type:
            raise Exception("Inappropriate loan type!")

        self.loans.remove(loan)
        client.loans.append(loan)
        self.granted_loans += 1

        return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."

    def remove_client(self, client_id: str):
        client = self._find_client_by_id(client_id)

        if client is None:
            raise Exception("No such client!")

        if client.loans:
            raise Exception("The client has loans! Removal is impossible!")

        self.clients.remove(client)
        return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):
        number_of_changed_loans = 0

        for loan in self.loans:
            if loan.__class__.__name__ == loan_type:
                loan.increase_interest_rate()
                number_of_changed_loans += 1

        return f"Successfully changed {number_of_changed_loans} loans."

    def increase_clients_interest(self, min_rate: float):
        changed_rates = 0
        for client in self.clients:
            if client.interest < min_rate:
                client.increase_clients_interest()
                changed_rates += 1

        return f"Number of clients affected: {changed_rates}."

    def get_statistics(self):
        income = sum([c.income for c in self.clients])
        granted_loans_total_sum = sum([c.get_total_sum_of_loans for c in self.clients])
        loans_total_sum = sum([l.amount for l in self.loans])
        avg_client_interest_rate = 0

        if len(self.clients) > 0:
            avg_client_interest_rate = sum([c.interest for c in self.clients]) / len(self.clients)


        return f"Active Clients: {len(self.clients)}\n" \
               f"Total Income: {income:.2f}\n" \
               f"Granted Loans: {self.granted_loans}, Total Sum: {granted_loans_total_sum:.2f}\n" \
               f"Available Loans: {len(self.loans)}, Total Sum: {loans_total_sum:.2f}\n" \
               f"Average Client Interest Rate: {avg_client_interest_rate:.2f}"


    def _find_loan_by_type(self, loan_type):
        loan = [l for l in self.loans if l.__class__.__name__ == loan_type]
        if loan:
            return loan[0]

    def _find_client_by_id(self, client_id):
        client = [c for c in self.clients if c.client_id == client_id]
        if client:
            return client[0]

    @property
    def valid_client_types(self):
        return {"Student": Student, "Adult": Adult}

    @property
    def valid_loan_types(self):
        return {"StudentLoan": StudentLoan, "MortgageLoan": MortgageLoan}