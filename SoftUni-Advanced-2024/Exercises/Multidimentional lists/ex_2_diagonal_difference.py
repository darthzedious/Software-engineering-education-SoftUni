row = int(input())

matrix = [[int(x) for x in input().split()]for _ in range(row)]

primary_diag = [matrix[r][r]for r in range(row)]
secondary_diag = [matrix[r][row - r - 1] for r in range(row)]

print(abs(sum(primary_diag) - sum(secondary_diag)))
