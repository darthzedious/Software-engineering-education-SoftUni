from collections import deque

money_amount = [int(x) for x in input().split()]
foods_price = deque([int(x) for x in input().split()])

food = 0

while money_amount and foods_price:
    money = money_amount.pop()
    price = foods_price.popleft()

    if money < price:
        continue

    if money == price:
        food += 1
    elif money > price:
        food += 1
        change = money - price
        if money_amount:
            money_amount[-1] += change

if food >= 4:
    print(f"Gluttony of the day! Henry ate {food} foods.")
if 1 < food < 4:
    print(f"Henry ate: {food} foods.")
elif food == 1:
    print(f"Henry ate: {food} food.")
elif food == 0:
    print(f"Henry remained hungry. He will try next weekend again.")
