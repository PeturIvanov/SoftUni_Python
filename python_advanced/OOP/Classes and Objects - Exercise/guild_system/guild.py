from guild_system.player import Player

class Guild:
    def __init__(self, name: str):
        self.name = name
        self.players = []

    def assign_player(self, player: Player) -> str:
        if player.guild == self.name:
            return f"Player {player.name} is already in the guild."

        if player.guild != "Unaffiliated":
            return f"Player {player.name} is in another guild."

        self.players.append(player)
        player.guild = self.name

        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str) -> str:
        try:
            player_to_kick = next(filter(lambda p: p.name == player_name, self.players))

        except StopIteration:
            return f"Player {player_name} is not in the guild."

        player_to_kick.guild = "Unaffiliated"

        self.players.remove(player_to_kick)

        return f"Player {player_name} has been removed from the guild."

    def guild_info(self) -> str:
        info = []
        info.append(f"Guild: {self.name}")
        info.append('\n'.join([p.player_info() for p in self.players]))

        return '\n'.join(info)


player = Player("George", 50, 100)

print(player.add_skill("Shield Break", 20))
print(player.player_info())

second_player = Player("Pesho", 100, 100)
print(second_player.add_skill("Bloodlust", 50))
print(second_player.add_skill("Lava Burst", 30))
print(second_player.player_info())

guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.assign_player(second_player))

print(guild.guild_info())












