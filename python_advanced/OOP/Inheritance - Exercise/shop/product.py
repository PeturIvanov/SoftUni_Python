class Product:
    def __init__(self, name: str, quantity: int):
        self.name = name
        self.quantity = quantity

    def decrease(self, quantity_to_remove: int) -> None:
        if self.quantity >= quantity_to_remove:
            self.quantity -= quantity_to_remove

    def increase(self, quantity_to_add: int) -> None:
        self.quantity += quantity_to_add

    def __repr__(self):
        return f"{self.name}"

