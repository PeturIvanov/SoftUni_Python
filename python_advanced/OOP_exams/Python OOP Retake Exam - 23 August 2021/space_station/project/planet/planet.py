from typing import List


class Planet:
    def __init__(self, name: str):
        self.name = name
        self.items: List[str] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Planet name cannot be empty string or whitespace!")
        self.__name = value

    def adding_items(self, items: str):
        self.items.extend(items.split(", "))

