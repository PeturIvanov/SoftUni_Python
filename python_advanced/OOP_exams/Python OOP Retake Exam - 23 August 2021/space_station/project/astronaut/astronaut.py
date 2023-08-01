from abc import ABC, abstractmethod
from typing import List


class Astronaut(ABC):
    def __init__(self, name: str, oxygen: int):
        self.name = name
        self.oxygen = oxygen
        self.backpack: List[str] = []

    def info(self):
        backpack_items = ', '.join(self.backpack) if self.backpack else "none"
        return f"Name: {self.name}\nOxygen: {self.oxygen}\nBackpack items: {backpack_items}"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Astronaut name cannot be empty string or whitespace!")
        self.__name = value

    def increase_oxygen(self, amount: int):
        self.oxygen += amount

    @property
    @abstractmethod
    def breathe_units(self) -> int:
        ...

    def breathe(self):
        self.oxygen -= self.breathe_units

    def collect_item_from_planet(self, item):
        self.backpack.append(item)
        self.breathe()