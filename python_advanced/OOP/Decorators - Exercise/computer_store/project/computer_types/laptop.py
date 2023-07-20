from project.computer_types.computer import Computer
import math




class Laptop(Computer):
    MAX_RAM = 64
    VALID_PROCESSORS = {"AMD Ryzen 9 5950X": 900,
                        "Intel Core i9-11900H": 1050,
                         "Apple M1 Pro": 1200,
                        }

    def _add_processor(self, processor: str):
        if processor not in self.VALID_PROCESSORS:
            raise ValueError(f"{processor} is not compatible with laptop {self.manufacturer} {self.model}!")

        self.processor = processor
        self.price += self.VALID_PROCESSORS[self.processor]

    def _add_ram(self, ram: int):

        if ram > self.MAX_RAM or not self._valid_ram(ram):
            raise ValueError(f"{ram}GB RAM is not compatible with laptop {self.manufacturer} {self.model}!")

        self.ram = ram
        self.price += int(math.log2(ram) * 100)







