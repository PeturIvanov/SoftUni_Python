from project.delicacies.delicacy import Delicacy


class Stolen(Delicacy):
    PORTION_SIZE = 250

    def __init__(self, name: str, price: float):
        super().__init__(name, Stolen.PORTION_SIZE, price)

    def details(self) -> str:
        return f"{self.__class__.__name__} {self.name}: {Stolen.PORTION_SIZE}g - {self.price:.2f}lv."