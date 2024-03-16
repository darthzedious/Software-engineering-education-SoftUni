# def sustain(self, player_name: str, sustenance_name: str):
#     if player_name not in self.players:
#         return
#     if sustenance_name not in self.VALID_FOODS:
#         return
#
#     player = next(filter(lambda a: a.name == player_name, self.players))
#     if not player.need_sustenance:
#         return f"{player_name} have enough stamina."
#
#     try:
#         current_supply = next(filter(lambda a: a.__class__.__name__ == sustenance_name, reversed(self.supplies)))
#         player.stamina += current_supply.energy
#         self.supplies.remove(current_supply)
#         if player.stamina > 100:
#             player.stamina = 100
#
#     except StopIteration:
#         raise Exception(f"There are no {sustenance_name.lower()} supplies left!")
#
#     return f"{player_name} sustained successfully with {current_supply.name}."