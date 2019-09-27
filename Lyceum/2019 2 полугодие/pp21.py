def transpose(matrix1):
    global matrix
    matrix = [[matrix1[col][row]
               for col in range(0, len(matrix1[row]))]
              for row in range(0, len(matrix1))]
