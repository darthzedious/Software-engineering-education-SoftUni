rows, cols = [int(x) for x in input().split(",")]

matrix = [[x for x in input()]for _ in range(rows)]

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}
current_cheese = 0
total_cheese = 0

mouse_pos = []

for r in range(rows):
    total_cheese += matrix[r].count("C")
    for c in range(cols):
        if matrix[r][c] == "M":
            mouse_pos = [r, c]
            matrix[r][c] = "*"


while True:
    command = input()

    if command == "danger":
        if current_cheese < total_cheese:
            print("Mouse will come back later!")
        break

    row = mouse_pos[0] + directions[command][0]
    col = mouse_pos[1] + directions[command][1]

    if not (0 <= row < rows and 0 <= col < cols):
        matrix[mouse_pos[0]][mouse_pos[1]] = "M"
        print("No more cheese for tonight!")
        break

    if matrix[row][col] == "@":
        mouse_pos = [mouse_pos[0], mouse_pos[1]]
        continue

    mouse_pos = [row, col]

    if matrix[row][col] == "C":
        current_cheese += 1
        matrix[row][col] = "*"

        if current_cheese >= total_cheese:
            matrix[row][col] = "M"
            print(f"Happy mouse! All the cheese is eaten, good night!")
            break

    if matrix[row][col] == "T":
        matrix[row][col] = "M"
        print("Mouse is trapped!")
        break


matrix[mouse_pos[0]][mouse_pos[1]] = "M"

[print(*row, sep="") for row in matrix]
