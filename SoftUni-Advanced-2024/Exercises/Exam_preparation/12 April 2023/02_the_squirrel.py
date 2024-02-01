from collections import deque
size = int(input())
commands = deque(input().split(", "))
matrix = [[x for x in input()]for _ in range(size)]

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}
collected_hazlenut = 0
squirrel_pos = []

for r in range(size):
    for c in range(size):
        if matrix[r][c] == "s":
            squirrel_pos = [r, c]
            matrix[r][c] = "*"

while commands:
    command = commands.popleft()

    row = squirrel_pos[0] + directions[command][0]
    col = squirrel_pos[1] + directions[command][1]

    if not (0 <= row < size and 0 <= col < size):
        squirrel_pos = [row, col]
        print("The squirrel is out of the field.")
        break

    squirrel_pos = [row, col]

    if matrix[row][col] == "h":
        collected_hazlenut += 1
        matrix[row][col] = "*"

        if collected_hazlenut == 3:
            print("Good job! You have collected all hazelnuts!")
            break

    if matrix[row][col] == "t":
        print("Unfortunately, the squirrel stepped on a trap...")
        break

if (0 <= squirrel_pos[0] < size and 0 <= squirrel_pos[1] < size) and collected_hazlenut < 3 and matrix[squirrel_pos[0]][squirrel_pos[1]] != "t":
    print("There are more hazelnuts to collect.")
print(f"Hazelnuts collected: {collected_hazlenut}")
