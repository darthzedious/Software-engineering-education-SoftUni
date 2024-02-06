size = int(input())
racing_number = input()
matrix = []

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}
tunnel_coordinates = []
car_pos = [0, 0]
km = 0

for r in range(size):
    row_to_add = input().split()
    matrix.append(row_to_add)

    if "T" in row_to_add:
        tunnel_coordinates.append([r, row_to_add.index("T")])


while True:
    command = input()
    if command == "End":
        print(f"Racing car {racing_number} DNF.")
        break

    row = car_pos[0] + directions[command][0]
    col = car_pos[1] + directions[command][1]
    car_pos = [row, col]

    if matrix[row][col] == "F":
        km += 10
        print(f"Racing car {racing_number} finished the stage!")
        break

    if matrix[row][col] == "T":
        km += 30
        matrix[row][col] = "."

        car_pos = [tunnel_coordinates[1][0], tunnel_coordinates[1][1]]
        matrix[car_pos[0]][car_pos[1]] = "."
        continue

    km += 10
matrix[car_pos[0]][car_pos[1]] = "C"

print(f"Distance covered {km} km.")
[print(*row, sep="") for row in matrix]
