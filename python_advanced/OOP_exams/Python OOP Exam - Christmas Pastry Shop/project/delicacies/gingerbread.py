from project.delicacies.delicacy import Delicacy


class Gingerbread(Delicacy):
    PORTION_SIZE = 200

    def __init__(self, name: str, price: float):
        super().__init__(name, Gingerbread.PORTION_SIZE, price)

    def details(self) -> str:
        return f"{self.__class__.__name__} {self.name}: {Gingerbread.PORTION_SIZE}g - {self.price:.2f}lv."
