from project.band_members.musician import Musician
from typing import List


class Drummer(Musician):
    @property
    def _available_skills(self) -> List[str]:
        return ["play the drums with drumsticks",
                "play the drums with drum brushes",
                "read sheet music",
                ]

    @property
    def skills_needed(self):
        return {"Rock": "play the drums with drumsticks",
                "Metal": "play the drums with drumsticks",
                "Jazz": "play the drums with drum brushes"}