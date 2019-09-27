import sys

matrix = list(map(str.split, sys.stdin))

print(any(matrix[k][j] == '0' for k in range(len(matrix)) for j in range(len(matrix))))
