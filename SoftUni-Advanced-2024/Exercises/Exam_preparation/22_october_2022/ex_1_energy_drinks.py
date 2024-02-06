from collections import deque

milligrams_of_caffeine = [int(x) for x in input().split(", ")]
energy_drinks = deque([int(x) for x in input().split(", ")])

MAX_CAFFEINE = 300
current_caffeine = 0

while milligrams_of_caffeine and energy_drinks:
    caffeine = milligrams_of_caffeine.pop()
    drink = energy_drinks.popleft()

    caffeine_intake = caffeine * drink

    if current_caffeine < MAX_CAFFEINE:
        if MAX_CAFFEINE < (caffeine_intake + current_caffeine):
            energy_drinks.append(drink)

            current_caffeine -= 30 if current_caffeine - 30 > 0 else current_caffeine
        else:
            current_caffeine += caffeine_intake

if energy_drinks:
    print(f"Drinks left: {', '.join(str(x) for x in energy_drinks)}")
else:
    print(f"At least Stamat wasn't exceeding the maximum caffeine.")
print(f"Stamat is going to sleep with {current_caffeine} mg caffeine.")
