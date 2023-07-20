from project.robots.base_robot import BaseRobot

class FemaleRobot(BaseRobot):
    INITIALLY_WEIGHT = 7

    def __init__(self, name: str, kind: str, price: float):
        super().__init__(name, kind, price, self.INITIALLY_WEIGHT)

    @property
    def weight_gained_after_eat(self) -> int:
        return 1

    @property
    def valid_service(self):
        return "SecondaryService"