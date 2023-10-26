from math import ceil
budget = float(input())
students = int(input())
flour_price = float(input())
single_egg_price = float(input())
single_apron_price = float(input())
free_package = 0
for i in range(1, students + 1):
    if i % 5 == 0 and i != 1:
        free_package += 1
price_1 = single_apron_price * ceil(students + (students * 0.2))
price_2 = single_egg_price * 10 * students
price_3 = flour_price * (students - free_package)
cost = price_3 + price_2 + price_1

if cost <= budget:
    print(f"Items purchased for {cost:.2f}$.")
else:
    needed_money = cost - budget
    print(f"{needed_money:.2f}$ more needed.")
