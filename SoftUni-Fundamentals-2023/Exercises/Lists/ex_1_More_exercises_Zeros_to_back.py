lst_input = input().split(", ")
numbers = []
counter = 0
for num in lst_input:
    numbers.append(int(num))
output = [i for i in numbers if i != 0]
for cnt in range(numbers.count(0)):
    output.extend([0])
print(output)
