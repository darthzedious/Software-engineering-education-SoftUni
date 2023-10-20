quantity_food_in_kilograms = float(input()) * 1000
quantity_hey_in_kilograms = float(input()) * 1000
quantity_cover_in_kilograms = float(input()) * 1000
guinea_weight_in_kilograms = float(input()) * 1000

for days in range(1, 30 + 1):
    quantity_food_in_kilograms -= 300
    if days % 2 == 0:
        quantity_hey_in_kilograms -= 0.05 * quantity_food_in_kilograms
    if days % 3 == 0:
        quantity_cover_in_kilograms -= guinea_weight_in_kilograms / 3
    if quantity_cover_in_kilograms <= 0 or quantity_hey_in_kilograms <= 0 or quantity_food_in_kilograms <= 0:
        break
if quantity_cover_in_kilograms > 0 and quantity_food_in_kilograms > 0 and quantity_hey_in_kilograms > 0:
    print(f"Everything is fine! Puppy is happy! Food: {quantity_food_in_kilograms / 1000:.2f}, Hay: {quantity_hey_in_kilograms / 1000:.2f}"
          f", Cover: {quantity_cover_in_kilograms / 1000:.2f}.")
else:
    print("Merry must go to the pet store!")
