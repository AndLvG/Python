# # import sys
# #
# matrix = []
# # for el in sys.stdin:
# #     matrix.append(el.split())
#
# for i in range(10):
#     matrix.append(list(map(int, input().split())))

import sys
matrix = list(map(str.strip, sys.stdin))
print(matrix)
print(any(matrix[k][j] == 0 for k in range(len(matrix)) for j in range(len(matrix))))
