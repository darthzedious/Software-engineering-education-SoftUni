row = int(input())

matrix = []
for i in range(row):
    matrix.append([int(x) for x in input().split(", ")])
flattened = [num for sublist in matrix for num in sublist]
print(flattened)
