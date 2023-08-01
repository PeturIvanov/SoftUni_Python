from project.car.car import Car


class SportsCar(Car):
    @property
    def max_speed(self) -> int:
        return 600

    @property
    def min_speed(self) -> int:
        return 400

