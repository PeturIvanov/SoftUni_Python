from project.horse_specification.horse import Horse


class Thoroughbred(Horse):
    @property
    def max_speed(self) -> int:
        return 140

    @property
    def speed_increase_during_train(self) -> int:
        return 3
