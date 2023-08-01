from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
    CAR_TYPES = {"MuscleCar": MuscleCar, "SportsCar": SportsCar}

    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if car_type not in self.CAR_TYPES:
            return

        if self._find_car_by_model(model) is not None:
            raise Exception(f"Car {model} is already created!")

        new_car = self.CAR_TYPES[car_type](model, speed_limit)
        self.cars.append(new_car)
        return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        if self._find_driver_by_name(driver_name) is not None:
            raise Exception(f"Driver {driver_name} is already created!")

        new_driver = Driver(driver_name)
        self.drivers.append(new_driver)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        if self._find_race_by_name(race_name) is not None:
            raise Exception(f"Race {race_name} is already created!")
        new_race = Race(race_name)
        self.races.append(new_race)
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        driver = self._find_driver_by_name(driver_name)
        car = self._find_free_car(car_type)
        self._is_car_and_driver_available(driver, driver_name, car, car_type)

        if driver.car is not None:
            old_car = driver.car
            old_car.is_taken = False
            driver.car = car
            car.is_taken = True
            return f"Driver {driver.name} changed his car from {old_car.model} to {car.model}."

        driver.car = car
        car.is_taken = True
        return f"Driver {driver.name} chose the car {car.model}."

    def add_driver_to_race(self, race_name, driver_name):
        driver = self._find_driver_by_name(driver_name)
        race = self._find_race_by_name(race_name)
        self._race_and_driver_validator(race_name, race, driver_name, driver)
        if driver in race.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."

        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name):
        race = self._find_race_by_name(race_name)
        self._race_validator(race, race_name)
        result = self._race(race, race_name)
        return "\n".join(result)

    @staticmethod
    def _race(race, race_name):
        result = []
        for driver in sorted(race.drivers, key=lambda x: -x.car.speed_limit):
            result.append(f"Driver {driver.name} wins the {race_name} race with a speed of {driver.car.speed_limit}.")
            driver.number_of_wins += 1
            if len(result) == 3:
                return result


    @staticmethod
    def _race_validator(race, race_name):
        if race is None:
            raise Exception(f"Race {race_name} could not be found!")
        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")


    @staticmethod
    def _race_and_driver_validator(race_name, race, driver_name, driver):
        if race is None:
            raise Exception(f"Race {race_name} could not be found!")
        if driver is None:
            raise Exception(f"Driver {driver_name} could not be found!")
        if driver.car is None:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

    @staticmethod
    def _is_car_and_driver_available(driver, driver_name, car, car_type):
        if driver is None:
            raise Exception(f"Driver {driver_name} could not be found!")

        if car is None:
            raise Exception(f"Car {car_type} could not be found!")

    def _find_free_car(self, car_type):
        for i in range(len(self.cars) - 1, -1, -1):
            if self.cars[i].__class__.__name__ == car_type and not self.cars[i].is_taken:
                return self.cars[i]


    def _find_race_by_name(self, name):
        race = [r for r in self.races if r.name == name]
        if race:
            return race[0]

    def _find_driver_by_name(self, name):
        driver = [d for d in self.drivers if d.name == name]
        if driver:
            return driver[0]


    def _find_car_by_model(self, model):
        car = [c for c in self.cars if c.model == model]
        if car:
            return car[0]
