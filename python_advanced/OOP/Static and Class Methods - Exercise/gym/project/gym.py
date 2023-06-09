from typing import List

from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers: List[Customer] = []
        self.trainers: List[Trainer] = []
        self.equipment: List[Equipment] = []
        self.plans: List[ExercisePlan] = []
        self.subscriptions: List[Subscription] = []

    @staticmethod
    def __search_by_id(id: int, storage):
        return next(filter(lambda x: x.id == id, storage))


    def add_customer(self, customer: Customer) -> None:
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer) -> None:
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment) -> None:
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan) -> None:
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription) -> None:
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int) -> str:
        subscription = self.__search_by_id(subscription_id, self.subscriptions)

        customer = self.__search_by_id(subscription.customer_id, self.customers)

        trainer = self.__search_by_id(subscription.trainer_id, self.trainers)

        exercise = self.__search_by_id(subscription.exercise_id, self.plans)

        equipment = self.__search_by_id(exercise.equipment_id, self.equipment)


        return f"{subscription}\n{customer}\n{trainer}\n{equipment}\n{exercise}"
