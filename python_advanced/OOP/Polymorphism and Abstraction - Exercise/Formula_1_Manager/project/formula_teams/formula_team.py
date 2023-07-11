from abc import ABC, abstractmethod
from typing import Dict


class FormulaTeam(ABC):
    MIN_BUDGET = 1_000_000
    def __init__(self, budget: int):
        self.budget = budget


    @property
    def budget(self) -> int:
        return self.__budget

    @budget.setter
    def budget(self, value):
        if value < FormulaTeam.MIN_BUDGET:
            raise ValueError("F1 is an expensive sport, find more sponsors!")

        self.__budget = value

    @property
    @abstractmethod
    def sponsors(self) -> Dict[str, Dict[int, int]]:
        pass

    @property
    @abstractmethod
    def expenses_for_race(self) -> int:
        pass

    def calculate_revenue_after_race(self, race_pos: int) -> str:
        revenue = 0

        for sponsorship in self.sponsors.values():
            for pos in sponsorship:
                if race_pos <= pos:
                    revenue += sponsorship[pos]
                    break


        revenue -= self.expenses_for_race
        self.budget += revenue

        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"

