import sys, random
from PyQt5.QtWidgets import (QApplication, QLabel, QWidget)
from PyQt5.QtGui import QPainter, QPixmap, QPainter, QPen
from PyQt5.QtCore import Qt


class UFOGame(QWidget):

    def __init__(self, parent=None):
        super(UFOGame, self).__init__(parent=parent)
        self.initUI()

    def initUI(self):
        self.setGeometry(200, 200, 1000, 500)
        self.setWindowTitle('UFOGame')
        self.image = QPixmap("ufo.png")
        self.target_x_pos = 100
        self.target_y_pos = 100
        self.show()
        self.paintEvent(None)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Left:
            self.go_left()
        if event.key() == Qt.Key_Up:
            self.go_up()
        if event.key() == Qt.Key_Right:
            self.go_right()
        if event.key() == Qt.Key_Down:
            self.go_down()

        # self.target_x_pos = event.x()
        # self.target_y_pos = event.y()
        self.update()

    def go_left(self):
        if self.target_x_pos - 10 < 0:
            self.target_x_pos = self.width() - self.image.width()
        else:
            self.target_x_pos -= 10

    def go_up(self):
        if self.target_y_pos - 10 < 0:
            self.target_y_pos = self.height() - self.image.height()
        else:
            self.target_y_pos -= 10

    def go_right(self):
        if self.target_x_pos + 10 > self.width():
            self.target_x_pos = 0
        else:
            self.target_x_pos += 10

    def go_down(self):
        if self.target_y_pos + 10 > self.height():
            self.target_y_pos = 0
        else:
            self.target_y_pos += 10

    def paintEvent(self, event):
        # if self.target_x_pos + self.image.width() > self.width():
        #     self.target_x_pos = self.width() - self.image.width()
        # if self.target_y_pos + self.image.height() > self.height():
        #     self.target_y_pos = self.height() - self.image.height()
        painter = QPainter(self)
        painter.begin(self)
        painter.drawPixmap(self.target_x_pos, self.target_y_pos, self.image.width(), self.image.height(), self.image)


app = QApplication(sys.argv)
w = UFOGame()
sys.exit(app.exec_())
