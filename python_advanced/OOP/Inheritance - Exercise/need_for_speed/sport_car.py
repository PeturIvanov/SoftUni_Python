from need_for_speed.car import Car


class SportCar(Car):
    fuel_consumption = 10
    DEFAULT_FUEL_CONSUMPTION = fuel_consumption

    def __init__(self, fuel, horse_power):
        super().__init__(fuel, horse_power)