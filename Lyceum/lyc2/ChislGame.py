import sys
from random import choice

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtWidgets import QLCDNumber

a = []
b = []
for i in range(1, 10):
    a.append(i)
    b.append(i)


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(500, 500, 500, 500)
        self.setWindowTitle('Числовая игра')

        self.a = a
        self.x = choice(self.a)
        self.a.remove(self.x)
        self.y = choice(self.a)
        self.a.remove(self.y)
        self.z = choice(self.a)
        self.a.remove(self.z)
        self.count = 10

        self.btn = QPushButton('Уменьшить', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(150, 100)
        self.btn.clicked.connect(self.minus)
        self.plu = QPushButton('Увеличить', self)
        self.plu.resize(self.btn.sizeHint())
        self.plu.move(150, 70)
        self.plu.clicked.connect(self.plus)

        self.start = QPushButton('Новая игра', self)
        self.start.move(150, 330)
        self.start.clicked.connect(self.generate)

        self.one = QLabel(self)
        self.one.setText("X")
        self.one.move(140, 155)
        self.two = QLabel(self)
        self.two.setText("Y")
        self.two.move(140, 185)
        self.three = QLabel(self)
        self.three.setText("Z")
        self.three.move(140, 215)
        self.popi = QLabel(self)
        self.popi.setText("Попыток")
        self.popi.move(100, 245)
        self.win = QLabel(self)
        self.win.move(150, 270)
        self.lose = QLabel(self)
        self.lose.move(150, 300)

        self.number1 = QLCDNumber(self)
        self.number1.display(self.x)
        self.number1.move(150, 150)
        self.number2 = QLCDNumber(self)
        self.number2.display(self.y)
        self.number2.move(150, 180)
        self.number3 = QLCDNumber(self)
        self.number3.display(self.z)
        self.number3.move(150, 210)
        self.popitok = QLCDNumber(self)
        self.popitok.display(self.count)
        self.popitok.move(150, 240)

    def generate(self):
        self.a = a
        self.x = choice(self.a)
        self.a.remove(self.x)
        self.y = choice(self.a)
        self.a.remove(self.y)
        self.z = choice(self.a)
        self.a.remove(self.z)
        self.count = 10

        self.number1.display(self.x)
        self.number2.display(self.y)
        self.number3.display(self.z)
        self.count = 10
        self.popitok.display(self.count)
        self.win.setText("")
        self.lose.setText("")

    def minus(self):
        if self.count > 0:
            if self.x == 0:
                self.win.setText("Победа")
            elif self.x != 0:
                self.count -= 1
                self.popitok.display(self.count)
                x = self.x - self.z
                self.x = x
                self.number1.display(x)

        else:
            self.lose.setText("Проигрыш")

    def plus(self):
        if self.count > 0:
            if self.x == 0:
                self.win.setText("Победа")
            elif self.x != 0:
                self.count -= 1
                self.popitok.display(self.count)
                x = self.x + self.y
                self.x = x
                self.number1.display(x)
        else:
            self.lose.setText("Проигрыш")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())