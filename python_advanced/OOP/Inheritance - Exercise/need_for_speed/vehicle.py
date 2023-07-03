class Vehicle:
    fuel_consumption = 1.25
    DEFAULT_FUEL_CONSUMPTION = fuel_consumption
    def __init__(self, fuel: float, horse_power: int):
        self.fuel = fuel
        self.horse_power = horse_power

    def drive(self, kilometers):
        if kilometers * self.fuel_consumption <= self.fuel:
            self.fuel -= kilometers * self.fuel_consumption
