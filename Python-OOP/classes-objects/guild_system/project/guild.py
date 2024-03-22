from player import Player


class Guild:

    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if player in self.players:
            return f"Player {player.name} is already in the guild."
        elif player.guild != "Unaffiliated":
            return f"Player {player.name} is in another guild."
        else:
            self.players.append(player)
            player.guild = self.name
            return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str):
        for player in self.players:
            if player_name == player.name:
                self.players.remove(player)
                return f"Player {player_name} has been removed from the guild."
        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        guild_information = ""
        guild_information += f"Guild: {self.name}\n"
        for player_ in self.players:
            guild_information += player_.player_info() + "\n"
        return guild_information


guild = Guild("GGXrd")
player = Player("Pesho", 90, 90)
guild.assign_player(player)
message = guild.assign_player(player)
print(message)
