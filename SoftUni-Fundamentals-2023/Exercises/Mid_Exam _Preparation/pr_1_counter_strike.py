initial_energy = int(input())
count_won_battles = 0

while True:
    distance = input()
    current_energy = initial_energy
    if distance == "End of battle":
        break
    count_won_battles += 1
    current_energy -= int(distance)
    if current_energy <= 0:
        print("Not enough energy! Game ends with {count} won battles and {energy} energy".)

