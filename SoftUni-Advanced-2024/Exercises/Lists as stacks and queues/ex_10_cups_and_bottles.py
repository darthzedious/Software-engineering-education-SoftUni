from collections import deque
cups_capacity = deque([int(cup) for cup in input().split()])
bottles_capacity = deque([int(bottle) for bottle in input().split()])
wasted_litters = 0

while cups_capacity and bottles_capacity:
    cup = cups_capacity.popleft()
    bottle = bottles_capacity.pop()
    if cup - bottle <= 0:
        watter_left = bottle - cup
        wasted_litters += watter_left
    else:
        cup -= bottle
        cups_capacity.appendleft(cup)

        if bottle > cup and cup <= 0:
            watter_left = bottle - cup
            wasted_litters += watter_left

cups_capacity = list(cups_capacity)
bottles_capacity = list(bottles_capacity)

if cups_capacity:
    print(f"Cups: {' '.join(str(x) for x in cups_capacity)}")
    print(f"Wasted litters of water: {wasted_litters}")
else:
    print(f"Bottles: {' '.join(str(x) for x in bottles_capacity)}")
    print(f"Wasted litters of water: {wasted_litters}")
