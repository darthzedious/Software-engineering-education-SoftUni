from sys import maxsize
row, col = [int(x) for x in input().split(", ")]

matrix = []
for _ in range(row):
    matrix.append([int(x) for x in input().split(", ")])

highest_value = -maxsize
sub_matrix = []
for c in range(col - 1):
    value = 0
    for r in range(row - 1):
        number = matrix[r][c]
        left = matrix[r][c + 1]
        down = matrix[r + 1][c]
        diag = matrix[r + 1][c + 1]
        value = int(number) + int(left) + int(down) + int(diag)
        if value > highest_value:
            highest_value = value
            sub_matrix = [[number, left], [down, diag]]

print(*sub_matrix[0])
print(*sub_matrix[1])
print(highest_value)
