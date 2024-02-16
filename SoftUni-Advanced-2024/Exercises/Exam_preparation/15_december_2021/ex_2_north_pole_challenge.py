rows, cols = [int(x) for x in input().split(", ")]
matrix = []

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}
all_presents_fount = False
decoration_collected = 0
gifts_collected = 0
cookies_collected = 0

santa_pos = []

all_decoration = 0
all_gifts = 0
all_cookies = 0

for r in range(rows):
    row = input().split()
    matrix.append(row)
    all_decoration += row.count("D")
    all_gifts += row.count("G")
    all_cookies += row.count("C")

    if "Y" in row:
        santa_pos = [r, row.index("Y")]
        matrix[santa_pos[0]][santa_pos[1]] = "x"

command = input()
while "End" not in command:
    direction, steps = command.split("-")
    steps = int(steps)

    for step in range(steps):
        row = santa_pos[0] + directions[direction][0]
        col = santa_pos[1] + directions[direction][1]

        if not (0 <= row < rows and 0 <= col < cols):
            if row >= rows:
                row = rows - row
            elif row < 0:
                row = rows + row
            if col >= cols:
                col = cols - col
            elif col < 0:
                col = cols + col

        santa_pos = [row, col]
        if matrix[row][col] == "D":
            decoration_collected += 1
        elif matrix[row][col] == "G":
            gifts_collected += 1
        elif matrix[row][col] == "C":
            cookies_collected += 1
        matrix[row][col] = "x"

        if decoration_collected == all_decoration and gifts_collected == all_gifts and cookies_collected == all_cookies:
            print("Merry Christmas!")
            all_presents_fount = True
            break

    if all_presents_fount:
        break
    command = input()

matrix[santa_pos[0]][santa_pos[1]] = "Y"

print("You've collected:")
print(f"- {decoration_collected} Christmas decorations")
print(f"- {gifts_collected} Gifts")
print(f"- {cookies_collected} Cookies")

[print(*row, sep=" ") for row in matrix]
