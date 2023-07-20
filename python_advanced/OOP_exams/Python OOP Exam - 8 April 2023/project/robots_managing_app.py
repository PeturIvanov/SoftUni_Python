from typing import List, Dict

from project.robots.base_robot import BaseRobot
from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.base_service import BaseService
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    INVALID_SERVICE_TYPE = "Invalid service type!"
    INVALID_ROBOT_TYPE = "Invalid robot type!"

    def __init__(self):
        self.robots: List[BaseRobot] = []
        self.services: List[BaseService] = []

    @property
    def _valid_services(self):
        return {"MainService": MainService, "SecondaryService": SecondaryService}

    @property
    def _valid_robots(self):
        return {"MaleRobot": MaleRobot, "FemaleRobot": FemaleRobot}

    def add_service(self, service_type: str, name:str) -> str:
        if service_type not in self._valid_services:
            raise Exception(self.INVALID_SERVICE_TYPE)

        new_service = self._valid_services[service_type](name)
        self.services.append(new_service)

        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float) -> str:
        if robot_type not in self._valid_robots:
            raise Exception(self.INVALID_ROBOT_TYPE)

        new_robot = self._valid_robots[robot_type](name, kind, price)
        self.robots.append(new_robot)

        return f"{robot_type} is successfully added."

    @staticmethod
    def _find_robot_by_name(robot_name, collection):
        robots = [r for r in collection if r.name == robot_name]
        if robots:
            return robots[0]

    @staticmethod
    def _find_service_by_name(service_name, collection):
        services = [s for s in collection if s.name == service_name]
        if services:
            return services[0]


    def add_robot_to_service(self, robot_name: str, service_name: str) -> str:
        robot = self._find_robot_by_name(robot_name, self.robots)
        service = self._find_service_by_name(service_name, self.services)

        if robot.valid_service != service.__class__.__name__:
            return "Unsuitable service."

        if len(service.robots) >= service.capacity:
            raise Exception("Not enough capacity for this robot!")

        self.robots.remove(robot)
        service.robots.append(robot)

        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str) -> str:
        service = self._find_service_by_name(service_name, self.services)
        robot = self._find_robot_by_name(robot_name, service.robots)

        if not robot:
            raise Exception("No such robot in this service!")

        service.robots.remove(robot)
        self.robots.append(robot)
        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str) -> str:
        service = self._find_service_by_name(service_name, self.services)

        for robot in service.robots:
            robot.eating()

        return f"Robots fed: {len(service.robots)}."

    def service_price(self, service_name: str) -> str:
        service = self._find_service_by_name(service_name, self.services)

        total_price = sum([r.price for r in service.robots])

        return f"The value of service {service_name} is {total_price:.2f}."

    def __str__(self) -> str:
        return '\n'.join([s.details() for s in self.services])
