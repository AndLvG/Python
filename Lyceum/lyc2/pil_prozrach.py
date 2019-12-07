import sys
from PIL import Image
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QLabel, QInputDialog, QSlider
from PyQt5.QtGui import QPixmap, QPainter


class Pil1(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(400, 400, 600, 400)
        self.setWindowTitle('Прозрачность')
        self.bLoad = QtWidgets.QPushButton(self)
        self.bLoad.setGeometry(QtCore.QRect(1, 1, 120, 23))
        self.bLoad.setText("Загрузить картинку")
        self.bLoad.clicked.connect(self.Load)

        self.opacity = QtWidgets.QSlider(self)
        self.opacity.setMinimum(0)
        self.opacity.setMaximum(100)
        self.opacity.setOrientation(QtCore.Qt.Horizontal)
        self.opacity.move(300, 6)
        self.opacityLabel = QtWidgets.QLabel(self)
        self.opacityLabel.setText("Непрозрачность")
        self.opacityLabel.setGeometry(QtCore.QRect(150, 1, 120, 23))

        self.opacity.valueChanged.connect(
            lambda: self.opacityLabel.setText("Непрозрачность: {}%".format(self.opacity.value())))
        self.opacity.setValue(50)
        self.opacity.valueChanged.connect(self.on_change)

        self.pixmap = QPixmap()
        self.image = QLabel(self)
        self.image.move(80, 60)
        # self.image.resize(250, 250)

    def on_change(self):
        new_pix = QPixmap(self.pixmap.size())
        new_pix.fill(QtCore.Qt.transparent)
        painter = QPainter(new_pix)
        painter.setOpacity(self.opacity.value() * 0.01)
        painter.drawPixmap(QtCore.QPoint(), self.pixmap)
        painter.end()
        self.image.setPixmap(new_pix)

    def Load(self):
        fname = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '')[0]
        self.pixmap.load(fname)
        im = self.pixmap.toImage()
        self.image.resize(im.width(), im.height())
        self.image.setPixmap(self.pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Pil1()
    ex.show()
    sys.exit(app.exec())
