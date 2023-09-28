numbers_as_str = input().split(" ")
opposite_of_each_number = []
for i in numbers_as_str:
    number_as_int = -int(i)
    opposite_of_each_number.append(number_as_int)

print(opposite_of_each_number)
