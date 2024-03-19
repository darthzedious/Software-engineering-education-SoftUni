from project.supply.supply import Supply
from project.player import Player


class Controller:
    VALID_FOODS = ["Food", "Drink"]

    def __init__(self):
        self.players: list[Player] = []
        self.supplies: list[Supply] = []

    def add_player(self, *args: Player):
        players_added = []

        for player in args:
            if player not in self.players:
                self.players.append(player)
                players_added.append(player)

        return f"Successfully added: {', '.join(x.name for x in players_added)}"

    def add_supply(self, *args: Supply):
        for supply in args:
            self.supplies.append(supply)

    def sustain(self, player_name: str, sustenance_name: str):
        if sustenance_name not in self.VALID_FOODS:
            return

        for player in self.players:
            if player.name == player_name:
                break
        else:
            return

        for i in range(len(self.supplies)-1, -1, -1):
            supply = self.supplies[i]

            if supply.__class__.__name__ == sustenance_name:
                self.supplies.pop(i)
                break
        else:
            raise Exception(f"There are no {sustenance_name.lower()} supplies left!")

        if player.stamina + supply.energy > 100:
            player.stamina = 100
        else:
            player.stamina += supply.energy

        return f"{player_name} sustained successfully with {supply.name}."

    def duel(self, player_name: str, second_player_name: str):
        players = []
        error_message = []
        player_one = next(filter(lambda p: p.name == player_name, self.players))
        player_two = next(filter(lambda pp: pp.name == second_player_name, self.players))

        if player_one.stamina == 0:
            error_message.append(f"Player {player_name} does not have enough stamina.")
        if player_two.stamina == 0:
            error_message.append(f"Player {second_player_name} does not have enough stamina.")
        if len(error_message) > 0:
            return "\n".join(error_message)

        players.append(player_one)
        players.append(player_two)
        players = sorted(players, key=lambda a: a.stamina)

        return self.fight(players)

    def fight(self, players: list[Player]):
        first_player_dmg = players[0].stamina / 2

        if players[1].stamina <= first_player_dmg:
            players[1].stamina = 0
            return f"Winner: {players[0].name}"
        else:
            players[1].stamina -= first_player_dmg

        second_player_dmg = players[1].stamina / 2
        if players[0].stamina <= second_player_dmg:
            players[0].stamina = 0
            return f"Winner: {players[1].name}"
        else:
            players[0].stamina -= second_player_dmg

        if players[0].stamina > players[1].stamina:
            return f"Winner: {players[0].name}"
        else:
            return f"Winner: {players[1].name}"

    def next_day(self):
        for player in self.players:
            reduce_stamina = player.age * 2
            player.stamina = max(player.stamina - reduce_stamina, 0)
            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def __str__(self):
        result = []
        for player in self.players:
            result.append(str(player))

        for supply in self.supplies:
            result.append(supply.details())

        return "\n".join(result)
