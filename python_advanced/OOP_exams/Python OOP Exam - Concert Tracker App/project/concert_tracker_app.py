from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.musician import Musician
from project.band_members.singer import Singer
from project.concert import Concert
from project.band import Band
from typing import List


class ConcertTrackerApp:
    def __init__(self):
        self.bands: List[Band] = []
        self.musicians: List[Musician] = []
        self.concerts: List[Concert] = []

    @property
    def _valid_musician_types(self):
        return {"Guitarist": Guitarist, "Drummer": Drummer, "Singer": Singer}

    @staticmethod
    def _find_musician_by_name(name: str, collection):
        musician = [m for m in collection if m.name == name]
        if musician:
            return musician[0]

    @staticmethod
    def _find_band_by_name(name: str, collection):
        band = [b for b in collection if b.name == name]
        if band:
            return band[0]

    @staticmethod
    def _find_concert_by_place(place: str, collection):
        concert = [c for c in collection if c.place == place]
        if concert:
            return concert[0]

    def create_musician(self, musician_type: str, name: str, age: int) -> str:
        if musician_type not in self._valid_musician_types:
            raise ValueError("Invalid musician type!")

        musician = self._find_musician_by_name(name, self.musicians)

        if musician:
            raise Exception(f"{name} is already a musician!")

        new_musician = self._valid_musician_types[musician_type](name, age)
        self.musicians.append(new_musician)

        return f"{name} is now a {musician_type}."

    def create_band(self, name: str) -> str:
        band = self._find_band_by_name(name, self.bands)

        if band:
            raise Exception(f"{name} band is already created!")

        new_band = Band(name)
        self.bands.append(new_band)

        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str) -> str:
        concert = self._find_concert_by_place(place, self.concerts)

        if concert:
            raise Exception(f"{place} is already registered for {concert.genre} concert!")

        new_concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(new_concert)

        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str) -> str:
        musician = self._find_musician_by_name(musician_name, self.musicians)
        if not musician:
            raise Exception(f"{musician_name} isn't a musician!")

        band = self._find_band_by_name(band_name, self.bands)
        if not band:
            raise Exception(f"{band_name} isn't a band!")

        band.members.append(musician)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str) -> str:
        band = self._find_band_by_name(band_name, self.bands)
        if not band:
            raise Exception(f"{band_name} isn't a band!")

        musician = self._find_musician_by_name(musician_name, band.members)
        if not musician:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        band.members.remove(musician)
        return f"{musician_name} was removed from {band_name}."

    @staticmethod
    def _find_singers(band: Band):
        return [member for member in band.members if member.__class__.__name__ == "Singer"]

    @staticmethod
    def _find_drummers(band: Band):
        return [member for member in band.members if member.__class__.__name__ == "Drummer"]

    @staticmethod
    def _find_guitarists(band: Band):
        return [member for member in band.members if member.__class__.__name__ == "Guitarist"]

    @staticmethod
    def _skill_requirements(singers, drummers, guitarists, concert_genre):
        for drummer in drummers:
            if drummer.skills_needed[concert_genre] not in drummer.skills:
                return False

        for singer in singers:
            for skill in singer.skills_needed[concert_genre]:
                if skill not in singer.skills:
                    return False

        for guitarist in guitarists:
            if guitarist.skills_needed[concert_genre] not in guitarist.skills:
                return False

        return True

    def start_concert(self, concert_place: str, band_name: str) -> str:
        band = self._find_band_by_name(band_name, self.bands)
        concert = self._find_concert_by_place(concert_place, self.concerts)

        singers = self._find_singers(band)
        drummers = self._find_drummers(band)
        guitarists = self._find_guitarists(band)

        if not singers or not drummers or not guitarists:
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        if not self._skill_requirements(singers, drummers, guitarists, concert.genre):
            raise Exception(f"The {band.name} band is not ready to play at the concert!")


        profit = (concert.audience * concert.ticket_price) - concert.expenses

        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}."
