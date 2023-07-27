from abc import ABC, abstractmethod
from typing import List

from project.delicacies.delicacy import Delicacy


class Booth(ABC):
    CAPACITY_ERROR = "Capacity cannot be a negative number!"


    def __init__(self, booth_number: int, capacity: int):
        self.booth_number = booth_number
        self.capacity = capacity
        self.delicacy_orders: List[Delicacy] = []
        self.price_for_reservation = 0
        self.is_reserved = False

    @property
    def price_for_reservation(self):
        return self.__price_for_reservation

    @price_for_reservation.setter
    def price_for_reservation(self, value):
        self.__price_for_reservation = value

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value < 0:
            raise ValueError(Booth.CAPACITY_ERROR)
        self.__capacity = value

    @property
    @abstractmethod
    def _price_per_person(self):
        ...

    @property
    def calculate_bill(self) -> float:
        return self.price_for_reservation + sum([d.price for d in self.delicacy_orders])

    def clear_table(self):
        self.delicacy_orders = []
        self.is_reserved = False
        self.price_for_reservation = 0

    def reserve(self, number_of_people: int):
        self.price_for_reservation = self._price_per_person * number_of_people
        self.is_reserved = True
