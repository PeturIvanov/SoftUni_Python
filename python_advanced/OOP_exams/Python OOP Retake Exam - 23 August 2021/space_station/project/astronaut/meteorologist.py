from project.astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):
    INITIAL_OXYGEN = 90

    def __init__(self, name: str):
        super().__init__(name, Meteorologist .INITIAL_OXYGEN)

    @property
    def breathe_units(self) -> int:
        return 15
