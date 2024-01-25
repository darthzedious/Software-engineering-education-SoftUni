rows = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(rows)]


def add(r, c, value):
    matrix[r][c] += value

    return matrix[r][c]


def subtract(r, c, value):
    matrix[r][c] -= value

    return matrix[r][c]


command = input().split()
while command[0] != "END":
    cmd, row, col, number = command[0], int(command[1]), int(command[2]), int(command[3])

    if not (0 <= row < rows and 0 <= col < rows):
        print("Invalid coordinates")

    elif cmd == "Add":
        add(row, col, number)

    elif cmd == "Subtract":
        subtract(row, col, number)

    command = input().split()

[print(*row) for row in matrix]
