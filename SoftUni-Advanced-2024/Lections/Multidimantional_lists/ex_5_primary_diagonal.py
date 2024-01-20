row = int(input())

matrix = []
for i in range(row):
    matrix.append([int(x) for x in input().split()])

diagonal_sum = 0
for r in range(row):
    diagonal_sum += matrix[r][r]
print(diagonal_sum)
