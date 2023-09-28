factor = int(input())
count = int(input())
list_of_numbers = []
for num in range(1, count+1):
    number = num * factor
    list_of_numbers.append(number)
print(list_of_numbers)
