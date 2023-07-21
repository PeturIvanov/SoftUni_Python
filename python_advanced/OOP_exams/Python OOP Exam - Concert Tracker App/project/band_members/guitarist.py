from project.band_members.musician import Musician
from typing import List


class Guitarist(Musician):
    @property
    def _available_skills(self) -> List[str]:
        return ["play metal",
                "play rock",
                "play jazz"
                ]



    @property
    def skills_needed(self):
        return {"Rock": "play rock",
                "Metal": "play metal",
                "Jazz": "play jazz"}