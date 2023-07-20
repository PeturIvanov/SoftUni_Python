from abc import ABC, abstractmethod
from typing import List

from project.robots.base_robot import BaseRobot


class BaseService(ABC):
    NAME_ERROR = "Service name cannot be empty!"
    CAPACITY_ERROR = "Service capacity cannot be less than or equal to 0!"

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.robots: List[BaseRobot] = []

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value <= 0:
            raise ValueError(self.CAPACITY_ERROR)

        self.__capacity = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError(self.NAME_ERROR)

        self.__name = value

    @property
    @abstractmethod
    def type(self) -> str:
        ...


    def details(self) -> str:
        robots = ' '.join([r.name for r in self.robots]) if self.robots else "none"

        return f"{self.name} {self.type}:\nRobots: {robots}"



