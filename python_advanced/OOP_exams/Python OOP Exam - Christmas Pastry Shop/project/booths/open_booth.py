from project.booths.booth import Booth


class OpenBooth(Booth):
    @property
    def _price_per_person(self) -> float:
        return 2.50
