from typing import List

from project.computer_types.computer import Computer
from project.computer_types.desktop_computer import DesktopComputer
from project.computer_types.laptop import Laptop


class ComputerStoreApp:
    VALID_TYPES = {"Laptop": Laptop, "Desktop Computer": DesktopComputer}
    def __init__(self):
        self.warehouse: List[Computer] = []
        self.profits = 0

    def build_computer(self, type_computer, manufacturer, model, processor, ram):
        if type_computer not in self.VALID_TYPES:
            raise ValueError(f"{type_computer} is not a valid type computer!")

        new_computer: Computer = self.VALID_TYPES[type_computer](manufacturer, model)
        self.warehouse.append(new_computer)
        return new_computer.configure_computer(processor, ram)

    def _find_computer(self, budget, processor, ram):
        for pc in self.warehouse:
            if pc.price <= budget and processor == pc.processor and pc.ram >= ram:
                return pc


    def sell_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int):
        wanted_computer = self._find_computer(client_budget, wanted_processor, wanted_ram)

        if not wanted_computer:
            raise Exception("Sorry, we don't have a computer for you.")

        self.profits += (client_budget - wanted_computer.price)
        self.warehouse.remove(wanted_computer)

        return f"{wanted_computer} sold for {client_budget}$."











