rows, cols = [int(x) for x in input().split()]
matrix = []
touched_opponents, moves_made = 0, 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

player_pos = []

for r in range(rows):
    matrix.append(input().split())
    for c in range(cols):
        if matrix[r][c] == "B":
            player_pos = [r, c]
            matrix[r][c] = "-"


enough_opponents = False
command = input()
while command != "Finish":
    row = player_pos[0] + directions[command][0]
    col = player_pos[1] + directions[command][1]

    if not (0 <= row < rows and 0 <= col < cols) or matrix[row][col] == "O":
        command = input()
        continue

    player_pos = [row, col]
    moves_made += 1

    if matrix[row][col] == "P":
        touched_opponents += 1
        matrix[row][col] = "-"

        if touched_opponents == 3:
            enough_opponents = True
            break

    command = input()

print("Game over!")
print(f"Touched opponents: {touched_opponents} Moves made: {moves_made}")
