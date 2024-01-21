rows, cols = [int(x) for x in input().split()]

matrix = [[x for x in input().split()] for _ in range(rows)]

while True:
    command = input()
    valid = True
    coordinates = []

    if command == "END":
        break

    cmd = command.split()
    
    for cord in cmd:
        if cord.isdigit():
            coordinates.append(int(cord))

    for r in range(rows):
        for c in range(cols):

            if cmd[0] == "swap" and len(coordinates) == 4 and 0 <= coordinates[r] <= rows and 0 <= coordinates[c] <= cols:
                matrix[coordinates[0]][coordinates[1]]\
                    , matrix[coordinates[2]][coordinates[3]]\
                    = matrix[coordinates[2]][coordinates[3]],\
                      matrix[coordinates[0]][coordinates[1]]
                [print(*r) for r in matrix]
                break

            else:
                valid = False
                print("Invalid input!")
                break

        break
