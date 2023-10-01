events = input().split("|")
total_energy = 100
initial_coins = 100
day_completed = True
for event in events:
    event_ingredient, number = event.split("-")
    if event_ingredient == "rest":
        current_energy = total_energy
        total_energy += int(number)
        if total_energy > 100:
            total_energy = 100
            print(f"You gained {total_energy - current_energy} energy.")
        else:
            print(f"You gained {number} energy.")
        print(f"Current energy: {total_energy}.")
    elif event_ingredient == "order":
        if total_energy >= 30:
            total_energy -= 30
            initial_coins += int(number)
            print(f"You earned {number} coins.")
        else:
            total_energy += 50
            print(f"You had to rest!")
    else:
        if initial_coins >= int(number):
            initial_coins -= int(number)
            print(f"You bought {event_ingredient}.")
        else:
            print(f"Closed! Cannot afford {event_ingredient}.")
            day_completed = False
            break
if day_completed:
    print(f"Day completed!")
    print(f"Coins: {initial_coins}")
    print(f"Energy: {total_energy}")
