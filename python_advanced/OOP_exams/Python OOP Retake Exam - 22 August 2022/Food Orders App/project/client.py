from typing import List

from project.meals.meal import Meal


class Client:
    def __init__(self, phone_number: str):
        self.phone_number = phone_number
        self.shopping_cart: List[Meal] = []
        self.bill = 0

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value):
        if not self._valid_phone_number(value):
            raise ValueError("Invalid phone number!")

        self.__phone_number = value

    @staticmethod
    def _valid_phone_number(number):
        if number[0] == "0" and len(number) == 10:
            if len([char for char in number if char.isdigit()]) == 10:
                return True

        return False

    def finish_order(self):
        total_bill = self.bill
        self.bill = 0
        self.shopping_cart = []
        return total_bill