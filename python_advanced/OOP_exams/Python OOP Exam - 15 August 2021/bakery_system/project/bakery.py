from typing import List

from project.baked_food.baked_food import BakedFood
from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.drink import Drink
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable
from project.table.table import Table


class Bakery:
    VALID_FOOD_TYPES = {"Bread": Bread, "Cake": Cake}
    VALID_DRINK_TYPES = {"Tea": Tea, "Water": Water}
    VALID_TABLE_TYPES = {"InsideTable": InsideTable, "OutsideTable": OutsideTable}

    def __init__(self, name: str):
        self.name = name
        self.food_menu: List[BakedFood] = []
        self.drinks_menu: List[Drink] = []
        self.tables_repository = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value

    def add_food(self, food_type: str, name: str, price: float):
        if self._find_food_by_name(name) is not None:
            raise Exception(f"{food_type} {name} is already in the menu!")

        if food_type in Bakery.VALID_FOOD_TYPES:
            new_food = Bakery.VALID_FOOD_TYPES[food_type](name, price)
            self.food_menu.append(new_food)
            return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: float, brand):
        if self._find_drink_by_name(name) is not None:
            raise Exception(f"{drink_type} {name} is already in the menu!")

        if drink_type in Bakery.VALID_DRINK_TYPES:
            new_drink = Bakery.VALID_DRINK_TYPES[drink_type](name, portion, brand)
            self.drinks_menu.append(new_drink)
            return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        if self._find_table_by_number(table_number) is not None:
            raise Exception(f"Table {table_number} is already in the bakery!")

        if table_type in Bakery.VALID_TABLE_TYPES:
            new_table = Bakery.VALID_TABLE_TYPES[table_type](table_number, capacity)
            self.tables_repository.append(new_table)
            return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        table = self._find_free_table(number_of_people)

        if table is None:
            return f"No available table for {number_of_people} people"

        table.reserve(number_of_people)
        return f"Table {table.table_number} has been reserved for {number_of_people} people"

    def order_food(self, table_number: int, *food_names):
        table = self._find_table_by_number(table_number)

        if table is None:
            return f"Could not find table {table_number}"

        successful_orders = []
        missing_orders = []
        for food_name in food_names:
            food = self._find_food_by_name(food_name)

            if food is None:
                missing_orders.append(food_name)
                continue

            successful_orders.append(str(food))
            table.food_orders.append(food)

        table_orders = "\n".join(successful_orders)
        bakery_missing = "\n".join(missing_orders)

        return f"Table {table.table_number} ordered:\n" \
               f"{table_orders}\n" \
               f"{self.name} does not have in the menu:\n" \
               f"{bakery_missing}"

    def order_drink(self, table_number: int, *drinks_names):
        table = self._find_table_by_number(table_number)

        if table is None:
            return f"Could not find table {table_number}"

        successful_orders = []
        missing_orders = []
        for drink_name in drinks_names:
            drink = self._find_drink_by_name(drink_name)

            if drink is None:
                missing_orders.append(drink_name)
                continue

            successful_orders.append(str(drink))
            table.drink_orders.append(drink)

        table_orders = "\n".join(successful_orders)
        bakery_missing = "\n".join(missing_orders)

        return f"Table {table.table_number} ordered:\n" \
               f"{table_orders}\n" \
               f"{self.name} does not have in the menu:\n" \
               f"{bakery_missing}"

    def leave_table(self, table_number: int):
        table = self._find_table_by_number(table_number)
        if table in self.tables_repository:
            bill = table.get_bill()
            table.clear()
            self.total_income += bill
            return f"Table: {table.table_number}\nBill: {bill:.2f}"

    def get_free_tables_info(self):
        result = [t.free_table_info() for t in self.tables_repository if not t.is_reserved]
        if result is not None:
            return "\n".join(result)

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"

    def _find_free_table(self, number_of_people):
        for table in self.tables_repository:
            if table.capacity >= number_of_people and not table.is_reserved:
                return table

    def _find_table_by_number(self, number):
        table = [t for t in self.tables_repository if t.table_number == number]
        if table:
            return table[0]

    def _find_drink_by_name(self, name):
        drink = [d for d in self.drinks_menu if d.name == name]
        if drink:
            return drink[0]

    def _find_food_by_name(self, name):
        food = [f for f in self.food_menu if f.name == name]
        if food:
            return food[0]

