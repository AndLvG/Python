import numpy as np


class Table(object):

    def __init__(self, rows, cols):
        self.field = [[0 for _ in range(cols)] for _ in range(rows)]
        self.rows = rows
        self.cols = cols

    def get_value(self, row, col):
        if row in range(self.rows) and col in range(self.cols):
            return self.field[row][col]
        return

    def set_value(self, row, col, value):
        self.field[row][col] = value

    def n_rows(self):
        return self.rows

    def n_cols(self):
        return self.cols

    def delete_row(self, row):
        self.field = np.delete(self.field, row, 0)
        self.rows -= 1

    def delete_col(self, col):
        self.field = np.delete(self.field, col, 1)
        self.cols -= 1

    def add_row(self, row):
        if self.cols != 0:
            i = [0 for _ in range(self.cols)]
            self.field = np.insert(self.field, row, i, axis=0)
        else:
            self.field = [[0]]
        self.rows += 1

    def add_col(self, col):
        if self.rows != 0:
            i = [0 for _ in range(self.rows)]
            self.field = np.insert(self.field, col, i, axis=1)
        else:
            self.field = [[0]]
        self.cols += 1


# tab = Table(8, 3)
#
# tab.set_value(0, 0, 10)
# tab.set_value(0, 1, 12)
# tab.set_value(0, 2, 13)
# tab.set_value(1, 2, 14)
# tab.set_value(2, 2, 15)
# tab.set_value(3, 2, 16)
# tab.set_value(4, 2, 17)
# tab.set_value(5, 2, 18)
# tab.set_value(6, 2, 19)
# tab.set_value(7, 2, 20)
# tab.set_value(7, 1, 21)
# tab.set_value(7, 0, 22)
# tab.set_value(6, 0, 23)
# tab.set_value(5, 0, 24)
# tab.set_value(4, 0, 25)
# tab.set_value(3, 0, 26)
# tab.set_value(2, 0, 27)
# tab.set_value(1, 0, 28)
# tab.set_value(1, 1, 29)
# tab.set_value(2, 1, 30)
# tab.set_value(3, 1, 31)
# tab.set_value(4, 1, 32)
# tab.set_value(5, 1, 33)
# tab.set_value(6, 1, 34)
#
# for i in range(tab.n_rows()):
#     for j in range(tab.n_cols()):
#         print(tab.get_value(i, j), end=' ')
#     print()
# print()
#
# for i in range(-1, tab.n_rows() + 1):
#     for j in range(-1, tab.n_cols() + 1):
#         print(tab.get_value(i, j), end=' ')
#     print()
# print()
# 
# tab.delete_row(4)
# tab.delete_row(6)
# tab.delete_col(2)
# tab.add_row(2)
