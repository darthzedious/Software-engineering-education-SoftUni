rows = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(rows)]
cordinates = ((int(x) for x in c.split(",")) for c in input().split())


direction_cord = (
    (-1, 0),# up
    (-1, -1),# up-left
    (-1, +1),# up-right
    (0, -1),#left
    (0, +1),#right
    (+1, -1),#down_left
    (+1, +1), #down-right
    (+1, 0),#down
    (0, 0) #current
)

for row, col in cordinates:
    if matrix[row][col] <= 0:
        continue

    for r, c in direction_cord:
        el_row, el_col = row + r, col + c

        if 0 <= el_row < rows and 0 <= el_col < rows:
            matrix[el_row][el_col] -= matrix[row][col] if matrix[el_row][el_col] > 0 else 0


alive_cells = []
for r in range(rows):
    for c in range(rows):
        if matrix[r][c] > 0:
            alive_cells.append(matrix[r][c])

print(f"Alive cells: {len(alive_cells)}")
print(f"Sum: {sum(alive_cells)}")
[print(*row) for row in matrix]
