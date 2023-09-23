divisor = int(input())
bound = int(input())

largest = ''

for i in range(1, bound + 1):
    if i % divisor == 0 and i <= bound:
        largest = i

print(largest)
