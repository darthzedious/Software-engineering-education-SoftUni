rows, cols = [int(x) for x in input().split()]
matrix = [[x for x in input()]for _ in range(rows)]

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

delivery_boy_pos = []
delivery_starting = []

for r in range(rows):
    for c in range(cols):
        if matrix[r][c] == "B":
            delivery_boy_pos = [r, c]
            delivery_starting = [r, c]

while True:
    command = input()

    row = delivery_boy_pos[0] + directions[command][0]
    col = delivery_boy_pos[1] + directions[command][1]

    if not (0 <= row < rows and 0 <= col < cols):
        matrix[delivery_starting[0]][delivery_starting[1]] = " "
        print("The delivery is late. Order is canceled.")
        break

    if matrix[row][col] == "*":
        delivery_boy_pos = [delivery_boy_pos[0], delivery_boy_pos[1]]
        continue

    delivery_boy_pos = [row, col]

    if not matrix[row][col].isalpha():
        matrix[row][col] = "."

    elif matrix[row][col] == "P":
        matrix[row][col] = "R"
        print("Pizza is collected. 10 minutes for delivery.")

    elif matrix[row][col] == "A":
        matrix[row][col] = "P"
        print("Pizza is delivered on time! Next order...")
        break

[print(*row, sep="") for row in matrix]
