class Profile:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    @property
    def username(self) -> str:
        return self.__username

    @username.setter
    def username(self, value) -> None:
        if not 5 <= len(value) <= 15:
            raise ValueError("The username must be between 5 and 15 characters.")

        self.__username = value

    @property
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, value) -> None:
        is_long_enough = len(value) >= 8
        is_upper = [c for c in value if c.isupper()]
        is_digit = [c for c in value if c.isdigit()]

        if not is_long_enough or not is_upper or not is_digit:
            raise ValueError("The password must be 8 or more characters with at least 1 digit"
                             " and 1 uppercase letter.")

        self.__password = value

    def __str__(self) -> str:
        return f'You have a profile with username: ' \
        f'"{self.__username}" and password: {"*" * len(self.__username)}'











