import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QRadioButton


class Krestiki(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 200)
        self.setWindowTitle('Крестики нолики')

        self.board = [[None for _ in range(3)] for _ in range(3)]

        size_cell = 50

        for i in range(3):
            for j in range(3):
                btn = QPushButton('', self)
                btn.resize(size_cell, size_cell)
                btn.move(i * size_cell, j * size_cell)
                self.board[i][j] = btn
                btn.clicked.connect(self.push_button)

        self.label = QLabel('Играет: Игорок 1 (X)   ', self)
        self.label.move(170, 10)

        self.b1 = QRadioButton("Игорок 1 (X)", self)
        self.b1.setChecked(True)
        self.b1.move(170, 40)
        self.b1.toggled.connect(lambda: self.btnstate(self.b1))
        self.b2 = QRadioButton("Игрок 2 (O)", self)
        self.b2.move(170, 60)
        self.b2.toggled.connect(lambda: self.btnstate(self.b2))

        b_restart = QPushButton('Начать заново', self)
        b_restart.move(170, 100)
        b_restart.clicked.connect(self.restart)

    def btnstate(self, b):
        if b.isChecked() == True:
            self.label.setText('Играет: ' + b.text())

    def push_button(self):
        sender = self.sender()
        if sender.text() == '' and self.label.text()[:7] != 'Победил':
            if self.b1.isChecked():
                sender.setText("X")
                self.b2.setChecked(True)
            else:
                sender.setText("O")
                self.b1.setChecked(True)
            self.check_win()

    def restart(self):
        for i in range(3):
            for j in range(3):
                self.board[i][j].setText("")
        self.label.setText('Играет: Игорок 1 (X)   ')

    def check_win(self):
        win = ''
        if self.board[0][0].text() == self.board[1][1].text() == self.board[2][2].text() and self.board[0][
            0].text() != '':
            win = self.board[0][0].text()
        if self.board[0][2].text() == self.board[1][1].text() == self.board[2][0].text() and self.board[0][
            2].text() != '':
            win = self.board[0][2].text()
        # for i in range(3):
        #     if self.board[i][0].text() == self.board[i][1].text() == self.board[i][2].text():
        #         win = self.board[i][0].text()
        for i in range(3):
            if self.board[0][i].text() == self.board[1][i].text() == self.board[2][i].text() and self.board[0][
                i].text() != '':
                win = self.board[0][i].text()
        for el in self.board:
            a = set(map(lambda x: x.text(), el))
            if len(a) == 1 and el[0].text() != '':
                win = el[0].text()

        aa = []
        for i in range(3):
            for j in range(3):
                aa.append(self.board[i][j].text())
        if '' not in aa:
            win = 'A'

        if win != '':
            if win == 'X':
                self.label.setText('Победил: ' + self.b1.text())
            elif win == "A":
                self.label.setText('Боевая Ничья')
            else:
                self.label.setText('Победил: ' + self.b2.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Krestiki()
    ex.show()
    sys.exit(app.exec())