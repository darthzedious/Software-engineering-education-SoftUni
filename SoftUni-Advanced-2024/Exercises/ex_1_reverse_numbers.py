numbers_as_string = list(input())
reversed_numbers = []

for num in range(len(numbers_as_string)):
    reversed_numbers.append(numbers_as_string.pop())

print("".join(reversed_numbers))
