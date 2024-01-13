numbers = tuple([float(el) for el in input().split()])
numbers_count = {}
for num in numbers:
    if num not in numbers_count:
        numbers_count[num] = numbers.count(num)
for key, value in numbers_count.items():
    print(f"{key} - {value} times")
