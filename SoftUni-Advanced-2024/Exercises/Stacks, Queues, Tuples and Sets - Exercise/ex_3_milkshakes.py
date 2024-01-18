from collections import deque
chocolates = deque([int(x) for x in input().split(", ")])
shakes = deque([int(x) for x in input().split(", ")])
shake_counter = 0
while chocolates and shakes and shake_counter != 5:
    chocolate = chocolates.pop()
    shake = shakes.popleft()

    if chocolate == shake:
        shake_counter += 1
    elif shake <= 0:
        chocolates.append(chocolate)
    elif chocolate <= 0:
        shakes.appendleft(shake)
    else:
        chocolate -= 5
        chocolates.append(chocolate)
        shakes.append(shake)

if shake_counter == 5:
    print(f"Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

print(f'Chocolate: {", ".join(str(x) for x in chocolates) or "empty"}')
print(f'Milk: {", ".join(str(x) for x in shakes) or "empty"}')
