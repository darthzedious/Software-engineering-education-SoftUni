rows = int(input())
matrix = [[x for x in input()] for _ in range(rows)]

directions = [
    [-2, -1],  # up- left
    [-2, +1],  # up-right
    [-1, +2],  # right- up
    [+1, +2],  # right-down
    [+2, +1],  # down-right
    [+2, -1],  # down-left
    [+1, -2],  # left-down
    [-1, -2],  # left-up
]
removed_knight = 0

while True:
    knight_with_most_att = []
    max_attacks = 0

    for row in range(rows):
        for col in range(rows):
            attacks = 0
            if matrix[row][col] == "K":

                for pos in directions:
                    move_row = row + pos[0]
                    move_col = col + pos[1]

                    if 0 <= move_row < rows and 0 <= move_col < rows:
                        if matrix[move_row][move_col] == "K":
                            attacks += 1

                            if attacks > max_attacks:
                                max_attacks = attacks
                                knight_with_most_att = [row, col]

    if knight_with_most_att:
        matrix[knight_with_most_att[0]][knight_with_most_att[1]] = "0"
        removed_knight += 1
    else:
        break

print(removed_knight)
