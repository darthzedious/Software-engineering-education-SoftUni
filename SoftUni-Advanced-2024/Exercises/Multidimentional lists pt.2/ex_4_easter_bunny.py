rows = int(input())
matrix = []

directions = {
    "up": [-1, 0],
    "down": [+1, 0],
    "left": [0, -1],
    "right": [0, +1],
}

total_number_of_eggs = float("-inf")
bunny_position = []
bunny_best_path = []
final_direction = None

for row in range(rows):
    matrix.append(input().split())
    if "B" in matrix[row]:
        bunny_position = [row, matrix[row].index('B')]

for direction, coordinates in directions.items():
    row = bunny_position[0] + directions[direction][0]
    col = bunny_position[1] + directions[direction][1]

    current_eggs = 0
    current_path = []

    while 0 <= row < rows and 0 <= col < rows:
        if matrix[row][col] == "X":
            break

        current_eggs += int(matrix[row][col])
        current_path.append([row, col])

        row += directions[direction][0]
        col += directions[direction][1]

    if current_eggs >= total_number_of_eggs:
        total_number_of_eggs = current_eggs
        bunny_best_path = current_path
        final_direction = direction

print(final_direction)
print(*bunny_best_path, sep="\n")
print(total_number_of_eggs)
