from project.baked_food.baked_food import BakedFood


class Cake(BakedFood):

    def __init__(self, name: str, price: float):
        super().__init__(name, self.initial_portion, price)

    @property
    def initial_portion(self):
        return 245

