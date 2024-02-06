def create(value, row, col):
    if matrix[row][col] == ".":
        matrix[row][col] = value
    return matrix[row][col]


def update(value, row, col):
    if matrix[row][col] != ".":
        matrix[row][col] = value
    return matrix[row][col]


def delete(row, col):
    if matrix[row][col] != ".":
        matrix[row][col] = "."
    return matrix[row][col]


def read(row, col):
    if matrix[row][col] != ".":
        print(matrix[row][col])


ROWS, COLS = 6, 6

matrix = [[x for x in input().split()] for _ in range(ROWS)]

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

given_pos = input()
usable_pos = [int(x) for x in given_pos if x.isdigit()]

command = input()

while "Stop" not in command:
    direction = command.split(", ")[1]
    row = usable_pos[0] + directions[direction][0]
    col = usable_pos[1] + directions[direction][1]

    usable_pos = [row, col]
    if "Create" in command:
        value = command.split(", ")[2]
        create(value, row, col)
    elif "Update" in command:
        value = command.split(", ")[2]
        update(value, row, col)
    elif "Delete" in command:
        delete(row, col)
    elif "Read" in command:
        read(row, col)

    command = input()

[print(*row, sep=" ") for row in matrix]
