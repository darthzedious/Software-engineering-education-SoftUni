row = int(input())

matrix = [[int(x) for x in input().split(", ")]for _ in range(row)]

primary_diagonal = [matrix[r][r] for r in range(row)]
secondary_diagonal = [matrix[r][row - r - 1] for r in range(row)]

print(f"Primary diagonal: {', '.join(str(x) for x in primary_diagonal)}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join(str(x) for x in secondary_diagonal)}. Sum: {sum(secondary_diagonal)}")
