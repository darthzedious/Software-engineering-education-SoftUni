row, col = [int(x) for x in input().split(", ")]

matrix = []
for i in range(row):
    matrix.append([int(x) for x in input().split()])


for c in range(col):
    value = 0
    for r in range(row):
        value += matrix[r][c]
    print(value)
