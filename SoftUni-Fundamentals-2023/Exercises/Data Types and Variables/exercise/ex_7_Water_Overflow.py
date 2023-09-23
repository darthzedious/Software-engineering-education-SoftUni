number_of_lines = int(input())
tank_capacity = 255
water_counter = 0
for i in range(number_of_lines):
    litters_of_watter = int(input())
    if tank_capacity < litters_of_watter:
        print("Insufficient capacity!")
        continue
    tank_capacity -= litters_of_watter
    water_counter += litters_of_watter
print(water_counter)
