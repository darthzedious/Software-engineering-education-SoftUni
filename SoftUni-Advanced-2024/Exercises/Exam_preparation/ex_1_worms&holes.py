from collections import deque

worms = [int(x) for x in input().split()]
holes = deque([int(x) for x in input().split()])

matches = 0
worm_did_not_fit = 0

while worms and holes:
    worm = worms.pop()
    hole = holes.popleft()

    if worm != hole:
        worm -= 3

        if worm <= 0:
            worm_did_not_fit += 1
            continue
        else:
            worms.append(worm)
    else:
        matches += 1


if matches:
    print(f"Matches: {matches}")
else:
    print("There are no matches.")


if not worms and not worm_did_not_fit:
    print("Every worm found a suitable hole!")
elif not worms and worm_did_not_fit:
    print("Worms left: none")
elif worms:
    print(f'Worms left: {", ".join(str(x) for x in worms)}')


if not holes:
    print("Holes left: none")
else:
    print(f'Holes left: {", ".join(str(x) for x in holes)}')
