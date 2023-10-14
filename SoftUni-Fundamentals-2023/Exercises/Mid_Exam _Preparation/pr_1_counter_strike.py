initial_energy = int(input())
count_won_battles = 0
battle_counter = 0
while True:
    distance = input()
    if distance == "End of battle":
        print(f"Won battles: {count_won_battles}. Energy left: {initial_energy}")
        break
    initial_energy -= int(distance)
    if initial_energy < 0:
        initial_energy = 0
        print(f"Not enough energy! Game ends with {count_won_battles} won battles and {initial_energy} energy")
        break
    count_won_battles += 1
    battle_counter += 1
    if battle_counter != 0 and battle_counter != 1 and battle_counter % 3 == 0:
        initial_energy += count_won_battles

