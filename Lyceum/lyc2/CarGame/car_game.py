import sys, random
from PyQt5.QtWidgets import (QApplication, QLabel, QWidget)
from PyQt5.QtGui import QPainter, QPixmap, QPainter, QPen


class CarGame(QWidget):

    def __init__(self, parent=None):
        super(CarGame, self).__init__(parent=parent)
        self.initUI()
        self.setMouseTracking(True)
        self.target_x_pos = 0
        self.target_y_pos = 0

    def initUI(self):
        self.setGeometry(200, 200, 1000, 500)
        self.setWindowTitle('CarGame')
        self.image = QPixmap("car1.png")
        self.image
        self.show()

    def mouseMoveEvent(self, event):
        self.target_x_pos = event.x()
        self.target_y_pos = event.y()
        self.update()

    def mousePressEvent(self, event):
        new_car = f'car{random.randint(1, 9)}.png'
        self.image = QPixmap(new_car)
        self.update()

    def paintEvent(self, event):
        if self.target_x_pos + self.image.width() > self.width():
            self.target_x_pos = self.width() - self.image.width()
        if self.target_y_pos + self.image.height() > self.height():
            self.target_y_pos = self.height() - self.image.height()
        painter = QPainter(self)
        painter.begin(self)
        painter.drawPixmap(self.target_x_pos, self.target_y_pos, self.image.width(), self.image.height(), self.image)


app = QApplication(sys.argv)
w = CarGame()
sys.exit(app.exec_())
