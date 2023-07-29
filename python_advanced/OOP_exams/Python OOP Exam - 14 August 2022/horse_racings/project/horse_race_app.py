from typing import List

from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.horse import Horse
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:
    def __init__(self):
        self.horses: List[Horse] = []
        self.jockeys: List[Jockey] = []
        self.horse_races: List[HorseRace] = []


    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if horse_type not in self.valid_horse_types:
            return
        if self._find_horse_obj_by_name(horse_name) is not None:
            raise Exception(f"Horse {horse_name} has been already added!")

        horse = self.valid_horse_types[horse_type](horse_name, horse_speed)
        self.horses.append(horse)
        return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int) -> str:
        if self._find_jockey_by_name(jockey_name) is not None:
            raise Exception(f"Jockey {jockey_name} has been already added!")

        jockey = Jockey(jockey_name, age)
        self.jockeys.append(jockey)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str) -> str:
        if race_type in self.race_types:
            raise Exception(f"Race {race_type} has been already created!")

        race = HorseRace(race_type)
        self.horse_races.append(race)
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str) -> str:
        jockey = self._find_jockey_by_name(jockey_name)
        horse = self._find_free_horse(horse_type)
        if jockey is None:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if horse is None:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        if jockey.horse is not None:
            return f"Jockey {jockey_name} already has a horse."

        jockey.horse = horse
        horse.is_taken = True
        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str) -> str:
        jockey = self._find_jockey_by_name(jockey_name)
        race = self._find_horse_race_by_type(race_type)

        if race is None:
            raise Exception(f"Race {race_type} could not be found!")
        if jockey is None:
            raise Exception(f"Jockey {jockey_name} could not be found!")
        if jockey.horse is None:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")
        if jockey in race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        race = self._find_horse_race_by_type(race_type)
        if race is None:
            raise Exception(f"Race {race_type} could not be found!")

        if len(race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        winner = self._find_winner(race.jockeys)
        return f"The winner of the {race_type}" \
               f" race, with a speed of {winner.horse.speed}km/h" \
               f" is {winner.name}! Winner's horse: {winner.horse.name}."

    @staticmethod
    def _find_winner(jockeys: List[Jockey]):
        winner = None
        current_max_speed = 0
        for jockey in jockeys:
            if jockey.horse.speed > current_max_speed:
                current_max_speed = jockey.horse.speed
                winner = jockey

        return winner

    def _find_horse_race_by_type(self, race_type):
        race = [r for r in self.horse_races if r.race_type == race_type]
        if race:
            return race[0]

    def _find_free_horse(self, horse_type):
        horses = [h for h in self.horses if h.__class__.__name__ == horse_type and not h.is_taken]
        if horses:
            return horses[-1]

    def _find_jockey_by_name(self, name: str) -> Jockey:
        jockey = [j for j in self.jockeys if j.name == name]
        if jockey:
            return jockey[0]

    def _find_horse_obj_by_name(self, name) -> Horse:
        horse = [h for h in self.horses if h.name == name]
        if horse:
            return horse[0]

    @property
    def valid_horse_types(self):
        return {"Appaloosa": Appaloosa, "Thoroughbred": Thoroughbred}

    @property
    def race_types(self):
        return [r.race_type for r in self.horse_races]
