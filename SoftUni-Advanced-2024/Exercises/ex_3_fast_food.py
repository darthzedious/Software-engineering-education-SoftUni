from collections import deque
quantity_of_food = int(input())
quantity_in_each_order = deque([int(x) for x in input().split()])
print(max(quantity_in_each_order))

while quantity_in_each_order and quantity_in_each_order[0] <= quantity_of_food:
    quantity_of_food -= quantity_in_each_order.popleft()

if quantity_in_each_order:
    print(f"Orders left: {' '.join([str(x) for x in quantity_in_each_order])}")
else:
    print("Orders complete")
