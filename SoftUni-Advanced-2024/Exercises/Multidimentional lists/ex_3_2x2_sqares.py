row, col = [int(x) for x in input().split()]

matrix = [input().split() for _ in range(row)]
secondary_matrix = 0

for r in range(row - 1):
    for c in range(col - 1):
        right = matrix[r][c+1]
        down = matrix[r+1][c]
        diag = matrix[r + 1][c + 1]

        if matrix[r][c] == right and matrix[r][c] == down and matrix[r][c] == diag:
            secondary_matrix += 1
if secondary_matrix > 0:
    print(secondary_matrix)
else:
    print(0)
