from project.player import Player


class Guild:
    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if player in self.players:
            return f"Player {player.name} is already in the guild."
        if player.guild != "Unaffiliated":
            return f"Player {player.name} is in another guild."

        self.players.append(player)
        player.guild = self.name
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name):
        for player in self.players:
            if player.name == player_name:
                player.guild = "Unaffiliated"
                self.players.remove(player)
                return f"Player {player_name.name} has been removed from the guild."
        return f"Player {player_name.name} is not in the guild."

    def guild_info(self):
        players_info = "\n".join(player.player_info() for player in self.players)
        return f"Guild: {self.name}\n" \
               f"{players_info}"


player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.kick_player(player))
print(guild.assign_player(player))
print(guild.kick_player(player))
print(guild.guild_info())
