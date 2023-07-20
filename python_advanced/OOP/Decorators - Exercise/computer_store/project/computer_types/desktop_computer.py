from project.computer_types.computer import Computer
import math


class DesktopComputer(Computer):
    MAX_RAM = 128
    VALID_PROCESSORS = {"AMD Ryzen 7 5700G": 500,
                        "Intel Core i5-12600K": 600,
                        "Apple M1 Max": 1800,
                        }

    def _add_processor(self, processor: str):
        if processor not in self.VALID_PROCESSORS:
            raise ValueError(f"{processor} is not compatible with desktop computer {self.manufacturer} {self.model}!")

        self.processor = processor
        self.price += self.VALID_PROCESSORS[self.processor]

    def _add_ram(self, ram: int):

        if ram > self.MAX_RAM or not self._valid_ram(ram):
            raise ValueError(f"{ram}GB RAM is not compatible with desktop computer {self.manufacturer} {self.model}!")

        self.ram = ram
        self.price += int(math.log2(ram) * 100)

















