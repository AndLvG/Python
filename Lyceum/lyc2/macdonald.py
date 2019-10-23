import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QCheckBox
from PyQt5.QtWidgets import QPlainTextEdit

a = []


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(400, 400, 400, 400)
        self.setWindowTitle('Мини калькулятор')

        self.gamb = QCheckBox('Гамбургер', self)
        self.gamb.move(100, 150)
        self.gamb.toggle()
        self.gamb.stateChanged.connect(self.gambu)
        self.chis = QCheckBox('Чизбургер', self)
        self.chis.move(100, 180)
        self.chis.toggle()
        self.chis.stateChanged.connect(self.chisb)
        self.mini = QCheckBox('Мини картошка фрии', self)
        self.mini.move(200, 150)
        self.mini.toggle()
        self.mini.stateChanged.connect(self.mifr)
        self.big = QCheckBox('Большая картошка фри', self)
        self.big.move(200, 180)
        self.big.toggle()
        self.big.stateChanged.connect(self.bifr)
        self.cola = QCheckBox('Кола', self)
        self.cola.move(300, 150)
        self.cola.toggle()
        self.cola.stateChanged.connect(self.col)
        self.fanta = QCheckBox('Фанта', self)
        self.fanta.move(300, 180)
        self.fanta.toggle()
        self.fanta.stateChanged.connect(self.fan)

        self.eat = QPlainTextEdit(self)
        self.eat.move(200, 250)
        self.eat.setPlainText('Заказ')

        self.btn = QPushButton('Заказать', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(150, 50)
        self.btn.clicked.connect(self.ras)

    def gambu(self):
        a.append("Гамбургер")

    def chisb(self):
        a.append("Чизбургер")

    def mifr(self):
        a.append("Мини картошка фрии")

    def bifr(self):
        a.append("Большая картошка фри")

    def col(self):
        a.append("Кола")

    def fan(self):
        a.append("Фанта")

    def ras(self):
        b = ""
        for el in a:
            b += el + "\n"
        self.eat.setPlainText(b)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
