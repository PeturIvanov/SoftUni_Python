from need_for_speed.vehicle import Vehicle


class Motorcycle(Vehicle):
    fuel_consumption = Vehicle.fuel_consumption
    DEFAULT_FUEL_CONSUMPTION = fuel_consumption
    def __init__(self, fuel: float, horse_power: int):
        super().__init__(fuel, horse_power)
