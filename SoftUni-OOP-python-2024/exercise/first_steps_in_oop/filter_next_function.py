nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_nums = filter(lambda x: x % 2 == 0, nums)
print(next(filtered_nums))  # when it finds the next match stops and prints it
