import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QRadioButton, QButtonGroup


class Krestiki(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Крестики нолики')

        # Матрица 3 на 3
        self.board = [[None for _ in range(3)] for _ in range(3)]

        # Размер кнопки
        size_cell = 50

        for i in range(3):
            for j in range(3):
                btn = QPushButton('', self)
                btn.resize(size_cell, size_cell)
                btn.move(i * size_cell, j * size_cell)
                self.board[i][j] = btn
                btn.clicked.connect(self.push_button)

        self.label = QLabel('Играет: Игорок 1 (X)', self)
        self.label.move(170, 10)

        self.b1 = QRadioButton("Игорок 1 (X)", self)
        self.b1.setChecked(True)
        self.b1.move(170, 40)
        self.b1.toggled.connect(lambda: self.btnstate(self.b1))
        self.b2 = QRadioButton("Игрок 2 (O)", self)
        self.b2.move(170, 60)
        self.b2.toggled.connect(lambda: self.btnstate(self.b2))

        b_restart = QPushButton('Начать заново', self)
        # btn.resize(size_cell, size_cell)
        b_restart.move(170, 100)
        b_restart.clicked.connect(self.restart)


    def btnstate(self, b):
        if b.isChecked() == True:
            self.label.setText('Играет: ' + b.text())

    def push_button(self):

        sender = self.sender()
        print(sender.text())
        if sender.text() == '':
            if self.b1.isChecked():
                sender.setText("X")
            else:
                sender.setText("O")

    def restart(self):
        for i in range(3):
            for j in range(3):
                self.board[i][j].setText("")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Krestiki()
    ex.show()
    sys.exit(app.exec())
