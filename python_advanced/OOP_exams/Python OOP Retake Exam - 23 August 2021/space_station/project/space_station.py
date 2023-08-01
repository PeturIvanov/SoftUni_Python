from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:
    VALID_ASTRONAUT_TYPES = {"Biologist": Biologist,
                             "Geodesist": Geodesist,
                             "Meteorologist": Meteorologist
                             }
    missions_complete = 0
    missions_failed = 0

    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()

    def add_astronaut(self, astronaut_type: str, name: str):
        if self.astronaut_repository.find_by_name(name) is not None:
            return f"{name} is already added."

        if astronaut_type not in SpaceStation.VALID_ASTRONAUT_TYPES:
            raise Exception("Astronaut type is not valid!")

        new_astronaut = SpaceStation.VALID_ASTRONAUT_TYPES[astronaut_type](name)
        self.astronaut_repository.add(new_astronaut)
        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name: str, items: str):
        if self.planet_repository.find_by_name(name) is not None:
            return f"{name} is already added."

        new_planet = Planet(name)
        new_planet.adding_items(items)
        self.planet_repository.add(new_planet)
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str):
        astronaut = self.astronaut_repository.find_by_name(name)
        if astronaut is None:
            raise Exception(f"Astronaut {name} doesn't exist!")

        self.astronaut_repository.remove(astronaut)
        return f"Astronaut {astronaut.name} was retired!"

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.increase_oxygen(10)

    def send_on_mission(self, planet_name: str):
        planet = self.planet_repository.find_by_name(planet_name)
        if planet is None:
            raise Exception("Invalid planet name!")

        astronauts = self.find_astronauts_for_mission()
        mission_result = self.collecting_items(planet, astronauts)
        return mission_result

    @staticmethod
    def collecting_items(planet, astronauts):
        astronauts_counter = 0

        for astronaut in astronauts:
            astronauts_counter += 1

            while astronaut.oxygen > 0:
                current_item = planet.items.pop()
                astronaut.collect_item_from_planet(current_item)

                if not planet.items:
                    SpaceStation.missions_complete += 1

                    return f"Planet: {planet.name} was explored. " \
                           f"{astronauts_counter} astronauts participated in collecting items."

        SpaceStation.missions_failed += 1
        return "Mission is not completed."

    def find_astronauts_for_mission(self):
        list_of_astronauts = []
        for astronaut in sorted(self.astronaut_repository.astronauts, key=lambda x: -x.oxygen):
            if astronaut.oxygen > 30:
                list_of_astronauts.append(astronaut)
            if len(list_of_astronauts) == 5:
                break

        if not list_of_astronauts:
            raise Exception("You need at least one astronaut to explore the planet!")

        return list_of_astronauts

    def report(self):
        astronauts = "\n".join([a.info() for a in self.astronaut_repository.astronauts])
        return f"{SpaceStation.missions_complete} successful missions!\n" \
               f"{SpaceStation.missions_failed} missions were not completed!\n" \
               f"Astronauts' info:\n" \
               f"{astronauts}"
