import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


class Matrica(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        matrix = [[1, 0, 1, 0], [0, 0, 0, 0], [1, 1, 1, 1]]
        size_cell = 50
        self.setGeometry(300, 300, size_cell * len(matrix[0]), size_cell * len(matrix))
        self.setWindowTitle('Матрица')

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                btn = QPushButton(str(matrix[i][j]), self)
                btn.resize(size_cell, size_cell)
                btn.move(j * size_cell, i * size_cell)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Matrica()
    ex.show()
    sys.exit(app.exec())
