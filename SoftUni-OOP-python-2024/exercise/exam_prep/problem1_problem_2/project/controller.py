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
        if player_name not in self.players:
            return
        if sustenance_name not in self.VALID_FOODS:
            return

        player = next(filter(lambda a: a.name == player_name, self.players))
        if not player.need_sustenance:
            return f"{player_name} have enough stamina."

        try:
            current_supply = next(filter(lambda a: a.__class__.__name__ == sustenance_name, reversed(self.supplies)))
            player.stamina += current_supply.energy
            self.supplies.remove(current_supply)
            if player.stamina > 100:
                player.stamina = 100

        except StopIteration:
            raise Exception(f"There are no {sustenance_name.lower()} supplies left!")

        return f"{player_name} sustained successfully with {current_supply.name}."

    def duel(self, player_name: str, second_player_name: str):
        error_message = []
        player_one = next(filter(lambda p: p.name == player_name, self.players))
        player_two = next(filter(lambda pp: pp.name == second_player_name, self.players))

        if player_one.stamina == 0:
            error_message.append(f"Player {player_name} does not have enough stamina.")
        if player_two.stamina == 0:
            error_message.append(f"Player {second_player_name} does not have enough stamina.")
        if len(error_message) > 0:
            return "\n".join(error_message)

        if player_one.stamina < player_two.stamina:
            player_two.stamina -= player_one.stamina // 2
            if player_two.stamina <= 0:
                player_two.stamina = 0
                return f"Winner: {player_name}"
        else:
            player_one.stamina -= player_two.stamina // 2
            if player_one.stamina <= 0:
                player_one.stamina = 0
                return f"Winner: {second_player_name}"

        if player_one.stamina > player_two.stamina:
            return f"Winner: {player_name}"
        else:
            return f"Winner: {second_player_name}"

    def next_day(self):
        for player in self.players:
            if player.stamina - player.age * 2 > 0:
                player.stamina -= player.age * 2
            else:
                player.stamina = 0
            self.sustain(player.name, "food")
            self.sustain(player.name, "drink")

    def __str__(self):
        result = []
        for player in self.players:
            result.append(f"Player: {player.name}, {player.age}, {player.stamina}, {player.need_sustenance}")

        for supply in self.supplies:
            result.append(f"{supply.__class__.__name__}: {supply.name}, {supply.energy}")

        return "\n".join(result)







