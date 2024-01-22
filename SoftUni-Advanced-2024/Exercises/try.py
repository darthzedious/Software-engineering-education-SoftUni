if matrix[r][c] == "B":
    if matrix[r][c - 1] in range(len(matrix[r])):
        matrix[r][c - 1] = "B"
    if matrix[r][c + 1] in range(len(matrix[r])):
        matrix[r][c + 1] = "B"
    if matrix[r - 1][c] in range(len(matrix[r])):
        matrix[r - 1][c] = "B"
    if matrix[r + 1][c] in range(len(matrix[r])):
        matrix[r + 1][c] = "B"