row, col = [int(x) for x in input().split()]

matrix = [[int(x) for x in input().split()] for _ in range(row)]

max_sum = float("-inf")
biggest_matrix = []

for r in range(row - 2):
    for c in range(col - 2):

        first_row = matrix[r][c:c+3]
        second_row = matrix[r+1][c:c+3]
        third_row = matrix[r+2][c:c+3]

        current_sum = sum(first_row) + sum(second_row) + sum(third_row)

        if current_sum > max_sum:
            max_sum = current_sum
            biggest_matrix = [first_row, second_row, third_row]

print(f"Sum = {max_sum}")
[print(*r) for r in biggest_matrix]
