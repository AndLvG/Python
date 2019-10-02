import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtWidgets import QLCDNumber


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Пятая программа')

        self.btn = QPushButton('Кнопка', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(100, 150)
        self.btn.clicked.connect(self.hello)

        self.label = QLabel(self)
        self.label.setText("Количество нажатий на кнопку")
        self.label.move(80, 30)

        self.LCD_number1 = QLCDNumber(self)
        self.LCD_number1.move(110, 80)

        self.LCD_number2 = QLCDNumber(self)
        self.LCD_number2.move(110, 100)

    def hello(self):
        number1 = self.LCD_number1.text()
        number2 = self.LCD_number2.text()
        self.LCD_numer1.display(self.number1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
