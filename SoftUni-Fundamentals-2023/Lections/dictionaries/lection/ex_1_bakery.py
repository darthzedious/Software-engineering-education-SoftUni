food = {}
given_food = input().split()

for idx in range(0, len(given_food) - 1, 2):
    food_type = given_food[idx]
    food_count = given_food[idx + 1]
    food[food_type] = int(food_count)

print(food)
