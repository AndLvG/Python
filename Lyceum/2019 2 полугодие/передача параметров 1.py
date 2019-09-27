def transpose(trix):
    global matrix
    for row in range(len(trix)):
        for col in range(len(trix[row])):
            matrix[row][col] = trix[col][row]


matrix = [[1, 2], [3, 4]]
transpose(matrix)

for line in matrix:
    print(*line)
