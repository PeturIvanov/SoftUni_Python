from typing import List

from project.player import Player
from project.supply.supply import Supply


class Controller:
    def __init__(self):
        self.players: List[Player] = []
        self.supplies: List[Supply] = []

    def __str__(self):
        result = []
        [result.append(str(player)) for player in self.players]
        [result.append(supply.details()) for supply in self.supplies]
        return "\n".join(result)

    def add_player(self, *args):
        added_players = []
        for player in args:
            if player not in self.players:
                self.players.append(player)
                added_players.append(player.name)
        return f"Successfully added: {', '.join(added_players)}"

    def add_supply(self, *args):
        [self.supplies.append(supply) for supply in args]

    def sustain(self, player_name: str, sustenance_type: str):
        player = self._find_player_by_name(player_name)

        if player is None or sustenance_type not in self._valid_sustenance_types:
            return

        if not player.need_sustenance:
            return f"{player_name} have enough stamina."


        supply = self._find_supply(sustenance_type)
        if supply is None:
            raise Exception(f"There are no {sustenance_type.lower()} supplies left!")

        if player.stamina + supply.energy > player.MAX_STAMINA:
            player.stamina = player.MAX_STAMINA
        else:
            player.stamina += supply.energy

        self._remove_last_supply(supply)

        return f"{player_name} sustained successfully with {supply.name}."


    def duel(self, first_player: str, second_player: str):
        player_one = self._find_player_by_name(first_player)
        player_two = self._find_player_by_name(second_player)

        valid_hp = self._health_validator(player_one, player_two)
        if valid_hp is not None:
            return valid_hp

        winner = self._fight(player_one, player_two)
        return f"Winner: {winner}"

    def next_day(self):
        for player in self.players:
            player.reduce_stamina_on_new_day()
            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    @property
    def _valid_sustenance_types(self):
        return ["Drink", "Food"]

    def _find_supply(self, sustenance_type):
        supply = [s for s in self.supplies if s.__class__.__name__ == sustenance_type]
        if supply:
            return supply[-1]

        raise Exception(f"There are no {sustenance_type.lower()} supplies left!")


    def _remove_last_supply(self, supply):
        idx = None
        for i, el in enumerate(self.supplies):
            if el == supply:
                idx = i
        self.supplies.pop(idx)


    def _find_player_by_name(self, name):
        player = [p for p in self.players if p.name == name]
        if player:
            return player[0]

    @staticmethod
    def _health_validator(first, second):
        if first.stamina == 0 and second.stamina == 0:
            return f"Player {first.name} does not have enough stamina.\n" \
                   f"Player {second.name} does not have enough stamina."
        elif first.stamina == 0:
            return f"Player {first.name} does not have enough stamina."

        elif second.stamina == 0:
            return f"Player {second.name} does not have enough stamina."

    @staticmethod
    def _fight(player_one, player_two):
        first_player_to_attack = player_one if player_one.stamina < player_two.stamina else player_two
        second_player_to_attack = player_one if first_player_to_attack == player_two else player_two

        for _ in range(2):
            if second_player_to_attack.stamina - first_player_to_attack.stamina / 2 <= 0:
                second_player_to_attack.stamina = 0
                return first_player_to_attack.name
            else:
                second_player_to_attack.stamina -= first_player_to_attack.stamina / 2
            first_player_to_attack, second_player_to_attack = second_player_to_attack, first_player_to_attack

        return player_one.name if player_one.stamina > player_two.stamina else player_two.name



