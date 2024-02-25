size = int(input())
matrix = []

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

initial_armor = 300
enemy_count = 0
jet_pos = []

for r in range(size):
    row = [x for x in input()]
    enemy_count += row.count("E")
    matrix.append(row)
    if "J" in row:
        jet_pos = [r, row.index("J")]
        matrix[jet_pos[0]][jet_pos[1]] = "-"


command = input()
while enemy_count > 0 and initial_armor > 0:
    row = jet_pos[0] + directions[command][0]
    col = jet_pos[1] + directions[command][1]

    jet_pos = [row, col]
    if matrix[row][col] == "E":
        matrix[row][col] = "-"
        enemy_count -= 1
        if enemy_count == 0:
            break
        elif enemy_count > 0:
            initial_armor -= 100
            if initial_armor <= 0:
                break

    if matrix[row][col] == "R":
        matrix[row][col] = "-"
        initial_armor = 300

    command = input()

matrix[jet_pos[0]][jet_pos[1]] = "J"
if enemy_count == 0:
    print("Mission accomplished, you neutralized the aerial threat!")
if initial_armor <= 0:
    print(f"Mission failed, your jetfighter was shot down! Last coordinates [{jet_pos[0]}, {jet_pos[1]}]!")

[print(*row, sep="") for row in matrix]
