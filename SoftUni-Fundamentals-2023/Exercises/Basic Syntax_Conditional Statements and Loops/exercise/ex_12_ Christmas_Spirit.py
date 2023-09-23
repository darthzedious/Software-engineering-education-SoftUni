decoration_quantity = int(input())
days_left = int(input())

spirit_counter = 0
money_counter = 0
ornament_price = 2
tree_skirt_price = 5
tree_garland = 3
tree_light = 15

for i in range(1, days_left + 1):
    if i % 11 == 0:
        decoration_quantity += 2
    if i % 2 == 0:
        money_counter += ornament_price * decoration_quantity
        spirit_counter += 5
    if i % 3 == 0:
        money_counter += (tree_skirt_price + tree_garland) * decoration_quantity
        spirit_counter += 13
    if i % 5 == 0:
        money_counter += tree_light * decoration_quantity
        spirit_counter += 17
        if i % 3 == 0:
            spirit_counter += 30
    if i % 10 == 0:
        spirit_counter -= 20
        money_counter += tree_skirt_price + tree_garland + tree_light
if days_left % 10 == 0:
    spirit_counter -= 30
print(f'Total cost: {money_counter}')
print(f"Total spirit: {spirit_counter}")
