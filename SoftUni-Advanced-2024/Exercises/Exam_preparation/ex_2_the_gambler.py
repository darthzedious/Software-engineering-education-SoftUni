size = int(input())
matrix = [[x for x in input()] for _ in range(size)]

gambler_money = 100
gambler_pos = []

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for r in range(size):
    for c in range(size):

        if matrix[r][c] == "G":
            gambler_pos = [r, c]
            matrix[r][c] = "-"

command = input()
while command != "end":
    row = gambler_pos[0] + directions[command][0]
    col = gambler_pos[1] + directions[command][1]

    if not (0 <= row < size and 0 <= col <= size):
        print(f"Game over! You lost everything!")
        break

    if matrix[row][col] == "W":
        gambler_money += 100
        matrix[row][col] = "-"
    elif matrix[row][col] == "P":
        gambler_money -= 200
        matrix[row][col] = "-"
    elif matrix[row][col] == "J":
        gambler_money += 100000
        matrix[row][col] = "G"
        gambler_pos = [row, col]
        print(f"You win the Jackpot!\nEnd of the game. Total amount: {gambler_money}$")
        break

    gambler_pos = [row, col]

    if gambler_money <= 0:
        print(f"Game over! You lost everything!")
        break

    command = input()
else:
    print(f"End of the game. Total amount: {gambler_money}$")

matrix[gambler_pos[0]][gambler_pos[1]] = "G"
if gambler_money > 0:
    [print(*row, sep="") for row in matrix]
