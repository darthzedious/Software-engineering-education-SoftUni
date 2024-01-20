row = int(input())

matrix = []
for i in range(row):
    matrix.append([x for x in input()])

symbol = input()
for r in range(row):
    for c in range(row):
        if matrix[r][c] == symbol:
            print(f"({r}, {c})")
            exit()
print(f"{symbol} does not occur in the matrix")
