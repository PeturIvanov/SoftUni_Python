from project.horse_specification.horse import Horse


class Appaloosa(Horse):
    @property
    def max_speed(self) -> int:
        return 120

    @property
    def speed_increase_during_train(self) -> int:
        return 2
