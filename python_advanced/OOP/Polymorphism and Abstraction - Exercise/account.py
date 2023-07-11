class Account:
    def __init__(self, owner: str, amount: int=0):
        self.owner = owner
        self.amount = amount
        self.transactions = []
        self.starting_amount = amount

    def __reversed__(self):
        return self.transactions[::-1]

    def __str__(self) -> str:
        return f"Account of {self.owner} with starting amount: {self.amount}"

    def __repr__(self) -> str:
        return f"Account({self.owner}, {self.balance})"

    def __len__(self) -> int:
        return len(self.transactions)

    def __getitem__(self, idx: int):
        return self.transactions[idx]

    def __lt__(self, other) -> bool:
        return self.balance < other.balance

    def __le__(self, other) -> bool:
        return self.balance <= other.balance

    def __eq__(self, other) -> bool:
        return self.balance == other.balance

    def __add__(self, other):
        new_acc = Account(f"{self.owner}&{other.owner}", self.starting_amount + other.starting_amount)
        new_acc.transactions = self.transactions + other.transactions

        return new_acc


    @property
    def balance(self):
        return self.starting_amount + sum(self.transactions)

    @property
    def transactions(self):
        return self._transactions

    @transactions.setter
    def transactions(self, value):
        self._transactions = value

    def handle_transaction(self, transaction_amount: int) -> str:
        if self.balance + transaction_amount < 0:
            raise ValueError("sorry cannot go in debt!")

        self.amount += transaction_amount
        self.transactions.append(transaction_amount)
        return f"New balance: {self.balance}"

    def add_transaction(self, amount: int) -> str:
        if not isinstance(amount, int):
            raise ValueError("please use int for amount")

        return self.handle_transaction(amount)
