from collections import deque

monsters_armor = deque([int(x) for x in input().split(",")])
soldier_strike = [int(x) for x in input().split(",")]

monsters_killed = 0

while monsters_armor and soldier_strike:
    armor = monsters_armor.popleft()
    strike = soldier_strike.pop()

    if strike >= armor:
        monsters_killed += 1
        strike -= armor

        if soldier_strike:
            soldier_strike[-1] += strike
        else:
            if strike > 0:
                soldier_strike.append(strike)

    else:
        armor -= strike
        monsters_armor.append(armor)

if not monsters_armor:
    print("All monsters have been killed!")
if not soldier_strike:
    print("The soldier has been defeated.")
print(f"Total monsters killed: {monsters_killed}")
