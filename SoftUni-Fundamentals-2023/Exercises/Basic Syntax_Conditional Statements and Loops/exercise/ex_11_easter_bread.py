budget = float(input())
flour_price = float(input())
colored_eggs_counter = 0
bread_counter = 0
eggs_price = flour_price * 0.75
milk_price = ((flour_price * 0.25) + flour_price) / 4
price_per_bread = flour_price + eggs_price + milk_price
while price_per_bread <= budget:
    bread_counter += 1
    budget -= price_per_bread
    colored_eggs_counter += 3
    if bread_counter % 3 == 0:
        colored_eggs_counter -= (bread_counter - 2)
print(f"You made {bread_counter} loaves of Easter bread! Now you have {colored_eggs_counter} eggs and {budget:.2f}BGN left.")

