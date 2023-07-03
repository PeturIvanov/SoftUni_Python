from need_for_speed.vehicle import Vehicle


class Car(Vehicle):
    fuel_consumption = 3
    DEFAULT_FUEL_CONSUMPTION = fuel_consumption

    def __init__(self, fuel, horse_power):
        super().__init__(fuel, horse_power)