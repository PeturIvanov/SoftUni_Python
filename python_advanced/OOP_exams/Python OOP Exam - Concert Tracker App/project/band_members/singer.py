from project.band_members.musician import Musician
from typing import List



class Singer(Musician):
    @property
    def _available_skills(self) -> List[str]:
        return ["sing high pitch notes",
                "sing low pitch notes",
                ]

