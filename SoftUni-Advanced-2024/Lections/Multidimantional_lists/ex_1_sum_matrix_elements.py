row, col = [int(x) for x in input().split(", ")]

num_value = 0
matrix = []
for i in range(row):
    matrix_element = [int(x) for x in input().split(", ")]
    matrix.append(matrix_element)
    num_value += sum(matrix_element)

print(num_value)
print(matrix)
