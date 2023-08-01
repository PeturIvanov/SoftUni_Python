from project.car.car import Car


class MuscleCar(Car):
    @property
    def max_speed(self) -> int:
        return 450

    @property
    def min_speed(self) -> int:
        return 250
