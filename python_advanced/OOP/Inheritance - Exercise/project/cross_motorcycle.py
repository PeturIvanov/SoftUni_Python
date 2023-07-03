from project.motorcycle import Motorcycle


class CrossMotorcycle(Motorcycle):
    fuel_consumption = Motorcycle.fuel_consumption
    DEFAULT_FUEL_CONSUMPTION = fuel_consumption

    def __init__(self, fuel, horse_power):
        super().__init__(fuel, horse_power)