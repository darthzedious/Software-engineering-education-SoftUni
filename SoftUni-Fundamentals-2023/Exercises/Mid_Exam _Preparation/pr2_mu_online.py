initial_health = 100
bitcoin = 0
dungeon = input().split("|")
room_counter = 0
quest_completed = True
for room in dungeon:
    room_counter += 1
    command, number = room.split()
    if command == "potion":
        temp_health = initial_health
        initial_health += int(number)
        if initial_health > 100:
            initial_health = 100
        amount = initial_health - temp_health
        print(f"You healed for {amount} hp.")
        print(f"Current health: {initial_health} hp.")
    elif command == "chest":
        chest_amount = int(number)
        bitcoin += chest_amount
        print(f"You found {chest_amount} bitcoins.")
    else:
        monster_attack = int(number)
        initial_health -= monster_attack
        if initial_health > 0:
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {room_counter}")
            quest_completed = False
            break
if quest_completed:
    print("You've made it!")
    print(f"Bitcoins: {bitcoin}")
    print(f"Health: {initial_health}")
