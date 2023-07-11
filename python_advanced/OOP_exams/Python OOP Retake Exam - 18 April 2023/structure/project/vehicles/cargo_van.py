from project.vehicles.base_vehicle import BaseVehicle


class CargoVan(BaseVehicle):
    MAX_MILEAGE = 180.00

    def __init__(self, brand: str, model: str, license_plate_number: str):
        super().__init__(brand, model, license_plate_number, CargoVan.MAX_MILEAGE)

    @property
    def load(self):
        return 5

    def drive(self, mileage: float):
        percentages = round((mileage / self.max_mileage) * 100)
        self.battery_level -= (percentages + self.load)
