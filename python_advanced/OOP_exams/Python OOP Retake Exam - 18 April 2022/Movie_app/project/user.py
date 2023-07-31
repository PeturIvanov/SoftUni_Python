
class User:
    def __init__(self, username: str, age: int):
        self.username = username
        self.age = age
        self.movies_liked = []
        self.movies_owned = []

    def __str__(self) -> str:
        result = [f"Username: {self.username}, Age: {self.age}",
                  "Liked movies:",
                  "\n".join([m.details() for m in self.movies_liked]) if self.movies_liked else "No movies liked.",
                  "Owned movies:",
                  "\n".join([m.details() for m in self.movies_owned]) if self.movies_owned else "No movies owned."]
        return "\n".join(result)

    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age(self, value):
        if value < 6:
            raise ValueError("Users under the age of 6 are not allowed!")
        self.__age = value

    @property
    def username(self) -> str:
        return self.__username

    @username.setter
    def username(self, value):
        if not value:
            raise ValueError("Invalid username!")
        self.__username = value
