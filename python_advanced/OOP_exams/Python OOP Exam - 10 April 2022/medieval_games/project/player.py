class Player:
    players_list = []
    MAX_STAMINA = 100
    MIN_STAMINA = 0
    def __init__(self, name: str, age: int, stamina: int=MAX_STAMINA):
        self.name = name
        self.age = age
        self.stamina = stamina

    def __str__(self) -> str:
        return f"Player: {self.name}, {self.age}, {self.stamina}, {self.need_sustenance}"

    @property
    def need_sustenance(self) -> bool:
        if self.stamina < Player.MAX_STAMINA:
            return True
        return False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name not valid!")
        if value in Player.players_list:
            raise Exception(f"Name {value} is already used!")

        Player.players_list.append(value)
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 12:
            raise ValueError("The player cannot be under 12 years old!")
        self.__age = value

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value):
        if value > Player.MAX_STAMINA or value < Player.MIN_STAMINA:
            raise ValueError("Stamina not valid!")
        self.__stamina = value

    def reduce_stamina_on_new_day(self):
        stamina_reduce = self.age * 2
        if self.stamina - stamina_reduce < Player.MIN_STAMINA:
            self.stamina = Player.MIN_STAMINA
        else:
            self.stamina -= stamina_reduce

