from project.astronaut.astronaut import Astronaut


class Biologist(Astronaut):
    INITIAL_OXYGEN = 70

    def __init__(self, name: str):
        super().__init__(name, Biologist.INITIAL_OXYGEN)

    @property
    def breathe_units(self) -> int:
        return 5




