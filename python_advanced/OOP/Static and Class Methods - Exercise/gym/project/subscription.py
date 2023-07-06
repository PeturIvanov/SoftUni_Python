class Subscription:
    id = 1
    def __init__(self, data: str, customer_id: int, trainer_id: int, exercise_id: int):
        self.date = data
        self.customer_id = customer_id
        self.trainer_id = trainer_id
        self.exercise_id = exercise_id
        self.id = Subscription.id
        Subscription.id += 1

    def __repr__(self) -> str:
        return f"Subscription <{self.id}> on {self.date}"

    @staticmethod
    def get_next_id() -> int:
        return Subscription.id
