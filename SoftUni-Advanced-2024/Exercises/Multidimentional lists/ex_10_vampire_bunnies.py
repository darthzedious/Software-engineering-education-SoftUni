rows, cols = [int(x) for x in input().split()]

directions = {
    "L": [0, -1],
    "R": [0, +1],
    "U": [-1, 0],
    "D": [+1, 0],
}

matrix = [[x for x in input()] for _ in range(rows)]
player_position = []

for r in range(rows):
    for c in range(cols):
        if matrix[r][c] == "P":
            player_position = [r, c]
            matrix[r][c] = "."

commands = [x for x in input()]

for command in commands:  # Main loop for the actual game.
    rol, col = player_position[0] + directions[command][0], player_position[1] + directions[command][1]

    bunny_position = []
    for r in range(rows):  # Loop to spread up the bunny count.
        for c in range(cols):
            if matrix[r][c] == "B":
                bunny_position.append([r, c])

    for bp_row, cp_col in bunny_position:
        for bunny_move in directions.values():
            new_bp_row, new_bp_col = bp_row + bunny_move[0], cp_col + bunny_move[1]

            if 0 <= new_bp_row < rows and 0 <= new_bp_col < cols:
                matrix[new_bp_row][new_bp_col] = "B"

    if not 0 <= rol < rows or not 0 <= col < cols:  # Winning state.
        [print(*x, sep="") for x in matrix]
        print(f"won: {player_position[0]} {player_position[1]}")
        break

    player_position = [rol, col]

    if matrix[rol][col] == "B":
        [print(*x, sep="") for x in matrix]
        print(f"dead: {rol} {col}")
        break
