from project.band_members.musician import Musician
from typing import List


class Drummer(Musician):
    @property
    def _available_skills(self) -> List[str]:
        return ["play the drums with drumsticks",
                "play the drums with drum brushes",
                "read sheet music",
                ]