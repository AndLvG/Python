import sys, random
from PyQt5.QtWidgets import (QApplication, QLabel, QWidget, QPushButton)


class RunningButton(QWidget):

    def __init__(self, parent=None):
        super(RunningButton, self).__init__(parent=parent)
        self.initUI()
        self.setMouseTracking(True)

    def initUI(self):
        self.setGeometry(200, 200, 1000, 500)
        self.btn = QPushButton('Нажми меня', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(150, 100)
        self.setWindowTitle('Running button')
        self.show()

    def mouseMoveEvent(self, event):
        if event.x() > self.btn.x() - 2 and event.x() < self.btn.x() + self.btn.width() + 2:
            if event.y() > self.btn.y() - 2 and event.y() < self.btn.y() + self.btn.height() + 2:
                new_x = random.randint(1, self.width() - self.btn.width())
                new_y = random.randint(1, self.height() - self.btn.height())
                self.btn.move(new_x, new_y)
        self.update()


app = QApplication(sys.argv)
w = RunningButton()
sys.exit(app.exec_())
