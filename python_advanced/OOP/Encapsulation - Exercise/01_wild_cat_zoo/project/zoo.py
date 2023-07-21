from typing import List

from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.budget = budget

        self.animal_capacity = animal_capacity
        self.animals: List[Animal] = []

        self.workers_capacity = workers_capacity
        self.workers: List[Worker] = []

    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, value):
        self.__budget = value

    @property
    def animal_capacity(self):
        return self.__animal_capacity

    @animal_capacity.setter
    def animal_capacity(self, value):
        self.__animal_capacity = value

    @property
    def workers_capacity(self):
        return self.__workers_capacity

    @workers_capacity.setter
    def workers_capacity(self, value):
        self.__workers_capacity = value



    def add_animal(self, animal: Animal, price: int):
        if self.animal_capacity > len(self.animals):
            if self.budget >= price:
                self.animals.append(animal)
                self.budget -= price
                return  f"{animal.name} the {animal.__class__.__name__} added to the zoo"

            return "Not enough budget"

        return "Not enough space for animal"

    def hire_worker(self, worker: Worker) -> str or None:
        if self.workers_capacity == len(self.workers):
            return "Not enough space for test_worker"

        self.workers.append(worker)

        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name: str) -> str:
        try:
            worker: Worker = [w for w in self.workers if w.name == worker_name][0]
        except IndexError:
            return f"There is no {worker_name} in the zoo"

        self.workers.remove(worker)
        self.workers_capacity += 1

        return f"{worker_name} fired successfully"

    def pay_workers(self) -> str:
        total_salaries = sum([w.salary for w in self.workers])

        if self.budget >= total_salaries:
            self.budget -= total_salaries

            return f"You payed your workers. They are happy. Budget left: {self.budget}"

        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self) -> str:
        total_money_for_care = sum([a.money_for_care for a in self.animals])

        if self.budget >= total_money_for_care:
            self.budget -= total_money_for_care

            return f"You tended all the animals. They are happy. Budget left: {self.budget}"

        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount: int) -> None:
        self.budget += amount

    @staticmethod
    def __data(objects_as_str: List[str]) -> str:
        return "\n".join(objects_as_str)

    @staticmethod
    def __filter(list_of_objects: List[Animal or Worker], class_to_find: str) -> List[str]:
        result = []

        for current_object in list_of_objects:
            if current_object.__class__.__name__ == class_to_find:
                result.append(str(current_object))

        return result

    def animals_status(self) -> str:
        lions = self.__filter(self.animals, "Lion")
        tigers = self.__filter(self.animals, "Tiger")
        cheetahs = self.__filter(self.animals, "Cheetah")

        return f"You have {len(self.animals)} animals\n" + \
            f"----- {len(lions)} Lions:\n" + \
            f"{self.__data(lions)}\n" + \
            f"----- {len(tigers)} Tigers:\n" + \
            f"{self.__data(tigers)}\n" + \
            f"----- {len(cheetahs)} Cheetahs:\n" + \
            f"{self.__data(cheetahs)}"

    def workers_status(self) -> str:
        keepers = self.__filter(self.workers, "Keeper")
        caretakers = self.__filter(self.workers, "Caretaker")
        vets = self.__filter(self.workers, "Vet")

        return f"You have {len(self.workers)} workers\n" + \
            f"----- {len(keepers)} Keepers:\n" + \
            f"{self.__data(keepers)}\n" + \
            f"----- {len(caretakers)} Caretakers:\n" + \
            f"{self.__data(caretakers)}\n" + \
            f"----- {len(vets)} Vets:\n" + \
            f"{self.__data(vets)}"
