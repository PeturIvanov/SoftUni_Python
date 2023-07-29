from typing import List, Dict, Tuple

from project.client import Client
from project.meals.dessert import Dessert
from project.meals.main_dish import MainDish
from project.meals.meal import Meal
from project.meals.starter import Starter


class FoodOrdersApp:
    receipt_id = 0

    def __init__(self):
        self.menu: List[Meal] = []
        self.clients_list: List[Client] = []

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."

    def register_client(self, phone_number: str):
        if self._find_client_by_number(phone_number):
            raise Exception("The client has already been registered!")

        self.clients_list.append(Client(phone_number))
        return f"Client {phone_number} registered successfully."

    def add_meals_to_menu(self, *meals):
        for meal in meals:
            if meal.__class__.__name__ in self.valid_meals:
                self.menu.append(meal)

    def show_menu(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        return "\n".join([m.details() for m in self.menu])

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities: Dict[str, int]):
        self.show_menu()
        client = self._find_client_by_number(client_phone_number)

        if client is None:
            self.register_client(client_phone_number)

        client = self._find_client_by_number(client_phone_number)
        self._validate_order(**meal_names_and_quantities)

        for meal, quantity in meal_names_and_quantities.items():
            meal_obj = self._find_meal_by_name(meal)
            client_meal_obj = self.valid_meals[meal_obj.__class__.__name__](meal_obj.name, meal_obj.price, quantity)
            client.shopping_cart.append(client_meal_obj)
            client.bill += (meal_obj.price * quantity)
            meal_obj.quantity -= quantity

        return f"Client {client_phone_number} successfully ordered {', '.join([m.name for m in client.shopping_cart])}" \
               f" for {client.bill:.2f}lv."

    def cancel_order(self, client_phone_number: str):
        client = self._find_client_by_number(client_phone_number)
        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

        for meal in client.shopping_cart:
            meal_in_menu = self._find_meal_by_name(meal.name)
            meal_in_menu.quantity += meal.quantity

        client.finish_order()

        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):
        client = self._find_client_by_number(client_phone_number)
        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

        total_bill = client.finish_order()
        self.receipt_id += 1

        return f"Receipt #{self.receipt_id} with total amount of {total_bill:.2f}" \
               f" was successfully paid for {client_phone_number}."

    def _validate_order(self, **kwargs):
        for meal, quantity in kwargs.items():
            meal_obj = self._find_meal_by_name(meal)

            if meal_obj is None:
                raise Exception(f"{meal} is not on the menu!")

            if meal_obj.quantity < quantity:
                raise Exception(f"Not enough quantity of {meal_obj.__class__.__name__}: {meal_obj.name}!")

    def _find_meal_by_name(self, meal_name):
        meal = [m for m in self.menu if m.name == meal_name]

        if meal:
            return meal[0]

    def _find_client_by_number(self, phone_number):
        client = [c for c in self.clients_list if c.phone_number == phone_number]

        if client:
            return client[0]

    @property
    def valid_meals(self):
        return {"Starter": Starter, "MainDish": MainDish, "Dessert": Dessert}
