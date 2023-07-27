from abc import ABC, abstractmethod


class Delicacy(ABC):
    NAME_ERROR = "Name cannot be null or whitespace!"
    PRICE_ERROR = "Price cannot be less or equal to zero!"

    def __init__(self, name: str, portion: int, price: float):
        self.name = name
        self.portion = portion
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError(Delicacy.PRICE_ERROR)
        self.__price = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError(Delicacy.NAME_ERROR)
        self.__name = value

    @abstractmethod
    def details(self):
        ...


