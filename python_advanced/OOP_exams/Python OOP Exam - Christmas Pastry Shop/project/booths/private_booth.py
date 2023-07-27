from project.booths.booth import Booth


class PrivateBooth(Booth):
    @property
    def _price_per_person(self) -> float:
        return 3.50
