import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QLabel, QInputDialog
from PyQt5.QtGui import QPixmap, QTransform, QColor


class Pil1(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(400, 400, 600, 400)
        self.setWindowTitle('картинка 1')
        self.bLoad = QtWidgets.QPushButton(self)
        self.bLoad.setGeometry(QtCore.QRect(1, 1, 120, 23))
        self.bLoad.setText("Загрузить картинку")
        self.bLoad.clicked.connect(self.Load)

        self.bRotate_plus = QtWidgets.QPushButton(self)
        self.bRotate_plus.setGeometry(QtCore.QRect(130, 1, 100, 23))
        self.bRotate_plus.setText("повернуь вправо")
        self.bRotate_plus.clicked.connect(self.rotate_plus)

        self.bRotate_minus = QtWidgets.QPushButton(self)
        self.bRotate_minus.setGeometry(QtCore.QRect(240, 1, 100, 23))
        self.bRotate_minus.setText("повернуь влево")
        self.bRotate_minus.clicked.connect(self.rotate_minus)

        self.bChange_RGB = QtWidgets.QPushButton(self)
        self.bChange_RGB.setGeometry(QtCore.QRect(350, 1, 100, 23))
        self.bChange_RGB.setText("Выбрать цвет")
        self.bChange_RGB.clicked.connect(self.change_RGB)

        self.pixmap = QPixmap()
        self.image = QLabel(self)
        self.image.move(80, 60)
        # self.image.resize(250, 250)

    def Load(self):
        fname = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '')[0]
        self.pixmap.load(fname)
        im = self.pixmap.toImage()
        self.image.resize(im.width(), im.height() )
        self.image.setPixmap(self.pixmap)

    def rotate_plus(self):
        self.pixmap = self.pixmap.transformed(QTransform().rotate(90))
        self.image.setPixmap(self.pixmap)

    def rotate_minus(self):
        self.pixmap = self.pixmap.transformed(QTransform().rotate(-90))
        self.image.setPixmap(self.pixmap)

    def change_RGB(self):
        i, okBtnPressed = QInputDialog.getItem(self, "выберите цвет", "Цвет",
                                               ("Red", "Green", "Blue"), 0, False)
        if okBtnPressed:
            if i == "Red":
                im = self.pixmap.toImage()
                for i in range(im.height()):
                    for j in range(im.width()):
                        r, g, b, a = QColor(im.pixel(j, i)).getRgb()
                        im.setPixel(j, i, QColor(r, 0, 0, a).rgb())
                self.image.setPixmap(QPixmap.fromImage(im))
            if i == "Green":
                im = self.pixmap.toImage()
                for i in range(im.height()):
                    for j in range(im.width()):
                        r, g, b, a = QColor(im.pixel(j, i)).getRgb()
                        im.setPixel(j, i, QColor(0, g, 0, a).rgb())
                self.image.setPixmap(QPixmap.fromImage(im))
            if i == "Blue":
                im = self.pixmap.toImage()
                for i in range(im.height()):
                    for j in range(im.width()):
                        r, g, b, a = QColor(im.pixel(j, i)).getRgb()
                        im.setPixel(j, i, QColor(0, 0, b, a).rgb())
                self.image.setPixmap(QPixmap.fromImage(im))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Pil1()
    ex.show()
    sys.exit(app.exec ())
