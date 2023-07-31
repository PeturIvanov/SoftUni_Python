from project.movie_specification.movie import Movie
from project.user import User

class Thriller(Movie):
    def __init__(self, title: str, year: int, owner: User, age_restriction: int=16):
        super().__init__(title, year, owner, age_restriction)

    @property
    def get_minimum_age_restriction(self) -> int:
        return 16
