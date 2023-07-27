from typing import List

from project.booths.booth import Booth
from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.delicacy import Delicacy
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    def __init__(self):
        self.booths: List[Booth] = []
        self.delicacies: List[Delicacy] = []
        self.income = 0.0

    def add_delicacy(self, type_delicacy: str, name: str, price: float) -> str:
        if self._find_delicacy_by_name(name):
            raise Exception(f"{name} already exists!")

        if type_delicacy not in self._delicacy_types:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        delicacy = self._delicacy_types[type_delicacy](name, price)
        self.delicacies.append(delicacy)

        return f"Added delicacy {delicacy.name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int) -> str:
        if self._find_booth_by_number(booth_number):
            raise Exception(f"Booth number {booth_number} already exists!")

        if type_booth not in self._booth_types:
            raise Exception(f"{type_booth} is not a valid booth!")

        booth = self._booth_types[type_booth](booth_number, capacity)
        self.booths.append(booth)

        return f"Added booth number {booth.booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int) -> str:
        free_booth = self._find_free_booth(number_of_people)

        if not free_booth:
            raise Exception(f"No available booth for {number_of_people} people!")

        free_booth.reserve(number_of_people)
        return f"Booth {free_booth.booth_number} has been reserved for {number_of_people} people."

    def order_delicacy(self, booth_number: int, delicacy_name: str) -> str:
        booth = self._find_booth_by_number(booth_number)
        delicacy = self._find_delicacy_by_name(delicacy_name)

        if not booth:
            raise Exception(f"Could not find booth {booth_number}!")

        if not delicacy:
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        booth.delicacy_orders.append(delicacy)
        return f"Booth {booth.booth_number} ordered {delicacy.name}."

    def leave_booth(self, booth_number: int) -> str:
        booth = self._find_booth_by_number(booth_number)

        bill = booth.calculate_bill
        booth.clear_table()
        self.income += bill

        return f"Booth {booth.booth_number}:\nBill: {bill:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."

    @property
    def _delicacy_types(self):
        return {"Gingerbread": Gingerbread, "Stolen": Stolen}

    @property
    def _booth_types(self):
        return {"Open Booth": OpenBooth, "Private Booth": PrivateBooth}


    def _find_booth_by_number(self, number):
        booth = [b for b in self.booths if b.booth_number == number]
        if booth:
            return booth[0]

    def _find_delicacy_by_name(self, name):
        delicacy = [d for d in self.delicacies if d.name == name]
        if delicacy:
            return delicacy[0]

    def _find_free_booth(self, number_of_people):
        for booth in self.booths:
            if not booth.is_reserved and booth.capacity >= number_of_people:
                return booth
