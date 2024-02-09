from collections import deque

bows = [int(x) for x in input().split(", ")]
customers = deque([int(x) for x in input().split(", ")])

while bows and customers:
    bow = bows.pop()
    customer = customers.popleft()

    if bow == customer:
        continue

    if bow > customer:
        bow -= customer
        bows.append(bow)

    elif customer > bow:
        customer -= bow
        customers.appendleft(customer)

if not customers:
    print("Great job! You served all the customers.")
    if bows:
        print(f"Bowls of ramen left: {', '.join(str(x) for x in bows)}")

elif not bows:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join(str(x) for x in customers)}")
