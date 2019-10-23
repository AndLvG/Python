import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QCheckBox
from PyQt5.QtWidgets import QLCDNumber, QLineEdit


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(400, 400, 400, 400)
        self.setWindowTitle('Мини калькулятор')

        self.suma = QLabel(self)
        self.suma.setText("Сума")
        self.suma.move(100, 215)
        self.rasnost = QLabel(self)
        self.rasnost.setText("Разность")
        self.rasnost.move(100, 245)
        self.chastnoe = QLabel(self)
        self.chastnoe.setText("Частное")
        self.chastnoe.move(100, 275)
        self.proisvedenie = QLabel(self)
        self.proisvedenie.setText("Произведение")
        self.proisvedenie.move(60, 305)
        self.num1 = QLabel(self)
        self.num1.setText("Число 1")
        self.num1.move(100, 155)
        self.num2 = QLabel(self)
        self.num2.setText("Число 2")
        self.num2.move(100, 185)

        self.number1 = QLineEdit(self)
        self.number1.move(150, 150)
        self.number2 = QLineEdit(self)
        self.number2.move(150, 180)

        self.plus = QLCDNumber(self)
        self.plus.move(150, 210)
        self.minus = QLCDNumber(self)
        self.minus.move(150, 240)
        self.delit = QLCDNumber(self)
        self.delit.move(150, 270)
        self.umnojit = QLCDNumber(self)
        self.umnojit.move(150, 300)

        self.btn = QPushButton('Вычислить', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(150, 100)
        self.btn.clicked.connect(self.ras)

    def ras(self):
        number1 = 1
        number2 = 2
        if self.number1.text() != "" and self.number1.text() != "":
            number1 = int(self.number1.text())
            number2 = int(self.number2.text())
        n = number1 + number2
        self.plus.display(n)
        n = number1 - number2
        self.minus.display(n)
        if number2:
            n = number1 / number2
            self.delit.display(n)
        else:
            self.delit.display("Error")
        n = number1 * number2
        self.umnojit.display(n)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())