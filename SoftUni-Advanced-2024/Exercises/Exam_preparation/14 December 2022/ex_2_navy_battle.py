size = int(input())
matrix = []

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

marine_pos = []
for r in range(size):
    line = [x for x in input()]
    matrix.append(line)

    if "S" in line:
        marine_pos = [r, line.index("S")]
        matrix[r][marine_pos[1]] = "-"

mine_hits = 0
cruiser_destroyed = 0

while cruiser_destroyed < 3:
    command = input()
    row = marine_pos[0] + directions[command][0]
    col = marine_pos[1] + directions[command][1]

    if not (0 <= row < size and 0 <= col < size):
        continue

    marine_pos = [row, col]

    if matrix[row][col] == "*":
        mine_hits += 1
        matrix[row][col] = "-"
        if mine_hits == 3:
            print(f"Mission failed, U-9 disappeared! Last known coordinates [{row}, {col}]!")
            break

    if matrix[row][col] == "C":
        cruiser_destroyed += 1
        matrix[row][col] = "-"

if cruiser_destroyed == 3:
    print(f"Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")

matrix[marine_pos[0]][marine_pos[1]] = "S"
[print(*row, sep="") for row in matrix]
