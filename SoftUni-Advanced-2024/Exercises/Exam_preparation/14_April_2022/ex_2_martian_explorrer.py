ROW, COL = 6, 6
matrix = []

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}
position = []

for r in range(ROW):
    row = input().split()
    matrix.append(row)
    if "E" in row:
        position = [r, row.index("E")]

commands = input().split(", ")
w_deposits = 0
m_deposits = 0
c_deposits = 0

for command in commands:
    row = position[0] + directions[command][0]
    col = position[1] + directions[command][1]

    if not (0 <= row < ROW and 0 <= col < COL):
        if row >= ROW:
            row = ROW - row
        elif row < 0:
            row = ROW + row

        if col >= ROW:
            col = ROW - col
        elif col < 0:
            col = ROW + col

    position = [row, col]

    if matrix[row][col] == "W":
        w_deposits += 1
        print(f"Water deposit found at ({row}, {col})")

    elif matrix[row][col] == "M":
        m_deposits += 1
        print(f"Metal deposit found at ({row}, {col})")

    elif matrix[row][col] == "C":
        c_deposits += 1
        print(f"Concrete deposit found at ({row}, {col})")

    if matrix[row][col] == "R":
        print(f"Rover got broken at ({row}, {col})")
        break

if m_deposits > 0 and w_deposits > 0 and c_deposits > 0:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
