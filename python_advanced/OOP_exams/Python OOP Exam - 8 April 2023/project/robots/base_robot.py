from abc import ABC, abstractmethod


class BaseRobot(ABC):
    NAME_ERROR = "Robot name cannot be empty!"
    KIND_ERROR = "Robot kind cannot be empty!"
    PRICE_ERROR = "Robot price cannot be less than or equal to 0.0!"

    def __init__(self, name: str, kind: str, price: float, weight: int):
        self.name = name
        self.kind = kind
        self.price = price
        self.weight = weight

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError(self.PRICE_ERROR)

        self.__price = value

    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, value):
        if not value.strip():
            raise ValueError(self.KIND_ERROR)

        self.__kind = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError(self.NAME_ERROR)

        self.__name = value

    @property
    @abstractmethod
    def weight_gained_after_eat(self) -> int:
        ...

    def eating(self):
        self.weight += self.weight_gained_after_eat