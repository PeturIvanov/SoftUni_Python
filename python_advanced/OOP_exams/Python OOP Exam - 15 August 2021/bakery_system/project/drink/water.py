from project.drink.drink import Drink


class Water(Drink):
    def __init__(self, name: str, portion: float, brand: str):
        super().__init__(name, portion, self.drink_price, brand)

    @property
    def drink_price(self):
        return 1.50