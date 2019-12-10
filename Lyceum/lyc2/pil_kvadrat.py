import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5.QtWidgets import QLineEdit, QLabel
from PyQt5.QtGui import QPen, QPainter, QPolygon
from PyQt5.QtCore import QPoint, Qt

SCREEN_SIZE = [600, 600]


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, *SCREEN_SIZE)
        self.setWindowTitle('Квадрат-объектив')
        self.Lab1 = QLabel(self)
        self.Lab1.move(20, 440)
        self.Lab1.setText("Сторона квадрата")
        self.Lab2 = QLabel(self)
        self.Lab2.move(20, 470)
        self.Lab2.setText("Коэф. Мастабирования")
        self.Lab3 = QLabel(self)
        self.Lab3.move(20, 500)
        self.Lab3.setText("Кол-во повторений")
        self.line = QLineEdit(self)
        self.line.move(150, 440)
        self.line1 = QLineEdit(self)
        self.line1.move(150, 470)
        self.line2 = QLineEdit(self)
        self.line2.move(150, 500)
        self.button = QPushButton(self)
        self.button.move(400, 500)
        self.button.setText("Полетели")
        self.button.clicked.connect(self.update)
        self.line.setText('400')
        self.line1.setText('0.9')
        self.line2.setText('40')
        self.show()

    def update(self):
        self.repaint()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw(qp)
        qp.end()

    def draw(self, gp):
        gp.setPen(QPen(Qt.black, 1, Qt.SolidLine))
        L = int(self.line.text())
        k = float(self.line1.text())
        N = int(self.line2.text())

        A1 = QPoint(0, 0)
        B1 = QPoint(L, 0)
        C1 = QPoint(L, L)
        D1 = QPoint(0, L)
        # for (i = 0; i < n; i++) {
        #     printf("%f %f\n", x + r * Math.cos(2 * Math.PI * i / n), y + r * Math.sin(2 * Math.PI * i / n));
        # }


        points = QPolygon([A1, B1, C1, D1])
        gp.drawPolygon(points)

        for i in range(N):
            A2 = QPoint(k * A1.x() + (1 - k) * B1.x(), k * A1.y() + (1 - k) * B1.y())
            B2 = QPoint(k * B1.x() + (1 - k) * C1.x(), k * B1.y() + (1 - k) * C1.y())
            C2 = QPoint(k * C1.x() + (1 - k) * D1.x(), k * C1.y() + (1 - k) * D1.y())
            D2 = QPoint(k * D1.x() + (1 - k) * A1.x(), k * D1.y() + (1 - k) * A1.y())

            points = QPolygon([A2, B2, C2, D2])
            gp.drawPolygon(points)
            A1, B1, C1, D1 = A2, B2, C2, D2


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
