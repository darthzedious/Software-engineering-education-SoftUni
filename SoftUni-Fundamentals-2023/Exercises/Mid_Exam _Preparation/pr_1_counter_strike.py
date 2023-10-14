initial_energy = int(input())
battle_counter = 0
while True:
    distance = input()
    if distance == "End of battle":
        if initial_energy >= 0:
            print(f"Won battles: {battle_counter}. Energy left: {initial_energy}")
        break
    if initial_energy >= int(distance):
        initial_energy -= int(distance)
        battle_counter += 1
    else:
        print(f"Not enough energy! Game ends with {battle_counter} won battles and {initial_energy} energy")
        break
    if battle_counter != 0 and battle_counter != 1 and battle_counter % 3 == 0:
        initial_energy += battle_counter
