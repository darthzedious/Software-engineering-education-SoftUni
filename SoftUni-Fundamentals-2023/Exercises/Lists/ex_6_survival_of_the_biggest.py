numbers = input().split(" ")
n = int(input())
numbers_int = []
for i in numbers:
    numbers_int.append(int(i))
for _ in range(n):
    min_number = min(numbers_int)
    numbers_int.remove(min_number)
print(", ".join(str(x) for x in numbers_int))
