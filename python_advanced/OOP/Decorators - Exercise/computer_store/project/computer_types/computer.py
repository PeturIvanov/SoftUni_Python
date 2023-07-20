from abc import ABC, abstractmethod
from math import ceil, floor, log2

class Computer(ABC):
    MANUFACTURER_ERROR = "Manufacturer name cannot be empty."
    MODEL_ERROR = "Model name cannot be empty."

    def __init__(self, manufacturer: str, model: str):
        self.manufacturer = manufacturer
        self.model = model
        self.processor = None
        self.ram = None
        self.price = 0

    def __repr__(self):
        return f"{self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM"

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if not value.strip():
            raise ValueError(self.MODEL_ERROR)

        self.__model = value

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, value):
        if not value.strip():
            raise ValueError(self.MANUFACTURER_ERROR)

        self.__manufacturer = value


    @staticmethod
    def _valid_ram(ram: int):
        result = log2(ram)
        return ceil(result) == floor(result)


    def configure_computer(self, processor: str, ram: int):
        self._add_processor(processor)
        self._add_ram(ram)

        return f"Created {self.manufacturer} {self.model}" \
               f" with {self.processor} and {self.ram}GB RAM for {self.price}$."


    @abstractmethod
    def _add_processor(self, processor: str):
        pass

    @abstractmethod
    def _add_ram(self, ram: int):
        pass















