from abc import ABC, abstractmethod
from project.user import User


class Movie(ABC):
    def __init__(self, title: str, year: int, owner: User, age_restriction: int):
        self.title = title
        self.year = year
        self.owner = owner
        self.age_restriction = age_restriction
        self.likes = 0

    @property
    def age_restriction(self):
        return self.__age_restriction

    @age_restriction.setter
    def age_restriction(self, value):
        if value < self.get_minimum_age_restriction:
            raise ValueError(f"{self.get_genre_name} movies must be restricted for audience under "
                             f"{self.get_minimum_age_restriction} years!")
        self.__age_restriction = value


    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        if not isinstance(value, User):
            raise ValueError("The owner must be an object of type User!")
        self.__owner = value

    @property
    def year(self) -> int:
        return self.__year

    @year.setter
    def year(self, value):
        if value < 1888:
            raise ValueError("Movies weren't made before 1888!")
        self.__year = value

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, value):
        if not value:
            raise ValueError("The title cannot be empty string!")
        self.__title = value


    def details(self) -> str:
        return f"{self.get_genre_name} - Title:{self.__title}, Year:{self.__year}, " \
               f"Age restriction:{self.age_restriction}, Likes:{self.likes}, Owned by:{self.owner.username}"

    @property
    @abstractmethod
    def get_minimum_age_restriction(self) -> int:
        ...

    @property
    def get_genre_name(self) -> str:
        return self.__class__.__name__

