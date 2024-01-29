size = int(input())
matrix = [[x for x in input()] for _ in range(size)]

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

fisherman_pos = []
collected_fish = 0

for row in range(size):
    for col in range(size):

        if matrix[row][col] == "S":
            fisherman_pos = [row, col]
            matrix[row][col] = "-"


command = input()
while command != "collect the nets":

    r = fisherman_pos[0] + directions[command][0]
    c = fisherman_pos[1] + directions[command][1]

    # for row in range(size):  #  mai tova e izlishno shtoto imame duljinata na row v size
    #     for col in range(size):
    #         if r < 0:
    #             r = len(matrix[row]) - r
    #         elif r > 0:
    #             r = r - len(matrix[row])
    #         if c < 0:
    #             c = len(matrix[col]) - c
    #         elif c > 0:
    #             c = c - len(matrix[col])
    if r < 0:
        r = size - abs(r)
    if r >= size:
        r = r - size
    if c < 0:
        c = size - abs(c)
    if c >= size:
        c = c - size

    fisherman_pos = [r, c]

    if matrix[r][c].isdigit():
        collected_fish += int(matrix[r][c])
        fisherman_pos = [r, c]
        matrix[r][c] = "-"

    elif matrix[r][c] == "W":
        fisherman_pos = [r, c]
        print(f"You fell into a whirlpool! "
              f"The ship sank and you lost the fish you caught."
              f" Last coordinates of the ship: [{fisherman_pos[0]},{fisherman_pos[1]}]")
        exit()

    command = input()

matrix[fisherman_pos[0]][fisherman_pos[1]] = "S"

if collected_fish >= 20:
    print(f"Success! You managed to reach the quota!")
    print(f"Amount of fish caught: {collected_fish} tons.")
    [print(*row, sep="") for row in matrix]

else:
    print(f"You didn't catch enough fish and didn't reach the quota! You need {20 - collected_fish} tons of fish more.")

    if collected_fish > 0:
        print(f"Amount of fish caught: {collected_fish} tons.")
    [print(*row, sep="") for row in matrix]
