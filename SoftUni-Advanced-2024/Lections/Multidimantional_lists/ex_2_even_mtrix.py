row = int(input())

matrix = []
for i in range(row):
    matrix.append([int(x) for x in input().split(", ") if int(x) % 2 == 0])
print(matrix)
