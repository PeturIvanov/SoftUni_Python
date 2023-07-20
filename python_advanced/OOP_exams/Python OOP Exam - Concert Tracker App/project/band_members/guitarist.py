from project.band_members.musician import Musician
from typing import List


class Guitarist(Musician):
    @property
    def _available_skills(self) -> List[str]:
        return ["play metal",
                "play rock",
                "play jazz"
                ]