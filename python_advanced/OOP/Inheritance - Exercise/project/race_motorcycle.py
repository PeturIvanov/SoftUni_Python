from project.motorcycle import Motorcycle


class RaceMotorcycle(Motorcycle):
    fuel_consumption = 8
    DEFAULT_FUEL_CONSUMPTION = fuel_consumption

    def __init__(self, fuel, horse_power):
        super().__init__(fuel, horse_power)