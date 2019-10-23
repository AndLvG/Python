import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QCheckBox, QFrame
from PyQt5.QtWidgets import QLCDNumber, QLineEdit
from PyQt5 import QtCore, QtGui, QtWidgets


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(400, 400, 400, 400)
        self.setWindowTitle('Красивый калькулятор')

        self.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(60, 20, 621, 181))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton4.setObjectName("pushButton4")
        self.gridLayout.addWidget(self.pushButton4, 1, 0, 1, 1)
        self.pushButton2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton2.setObjectName("pushButton2")
        self.gridLayout.addWidget(self.pushButton2, 0, 1, 1, 1)
        self.pushButton_umn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_umn.setObjectName("pushButton_umn")
        self.gridLayout.addWidget(self.pushButton_umn, 1, 5, 1, 1)
        self.pushButton5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton5.setObjectName("pushButton5")
        self.gridLayout.addWidget(self.pushButton5, 1, 1, 1, 1)
        self.pushButton_del = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_del.setObjectName("pushButton_del")
        self.gridLayout.addWidget(self.pushButton_del, 0, 5, 1, 1)
        self.pushButton3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton3.setObjectName("pushButton3")
        self.gridLayout.addWidget(self.pushButton3, 0, 2, 1, 1)
        self.pushButton1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton1.setObjectName("pushButton1")
        self.gridLayout.addWidget(self.pushButton1, 0, 0, 1, 1)
        self.pushButton9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton9.setObjectName("pushButton9")
        self.gridLayout.addWidget(self.pushButton9, 2, 2, 1, 1)
        self.pushButton6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton6.setObjectName("pushButton6")
        self.gridLayout.addWidget(self.pushButton6, 1, 2, 1, 1)
        self.pushButton_minus = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_minus.setObjectName("pushButton_minus")
        self.gridLayout.addWidget(self.pushButton_minus, 1, 4, 1, 1)
        self.pushButton7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton7.setObjectName("pushButton7")
        self.gridLayout.addWidget(self.pushButton7, 2, 0, 1, 1)
        self.pushButton8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton8.setObjectName("pushButton8")
        self.gridLayout.addWidget(self.pushButton8, 2, 1, 1, 1)
        self.pushButton_plus = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_plus.setObjectName("pushButton_plus")
        self.gridLayout.addWidget(self.pushButton_plus, 0, 4, 1, 1)
        self.pushButton0 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton0.setObjectName("pushButton0")
        self.gridLayout.addWidget(self.pushButton0, 3, 0, 1, 1)
        self.pushButton_sbros = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_sbros.setObjectName("pushButton_sbros")
        self.gridLayout.addWidget(self.pushButton_sbros, 3, 1, 1, 1)
        self.pushButton_ravno = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_ravno.setObjectName("pushButton_ravno")
        self.gridLayout.addWidget(self.pushButton_ravno, 3, 2, 1, 1)
        self.pushButton_kor = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_kor.setObjectName("pushButton_kor")
        self.gridLayout.addWidget(self.pushButton_kor, 2, 4, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 4, 0, 1, 3)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "self"))
        self.pushButton4.setText(_translate("self", "4"))
        self.pushButton2.setText(_translate("self", "2"))
        self.pushButton_umn.setText(_translate("self", "*"))
        self.pushButton5.setText(_translate("self", "5"))
        self.pushButton_del.setText(_translate("self", "\\"))
        self.pushButton3.setText(_translate("self", "3"))
        self.pushButton1.setText(_translate("self", "1"))
        self.pushButton9.setText(_translate("self", "9"))
        self.pushButton6.setText(_translate("self", "6"))
        self.pushButton_minus.setText(_translate("self", "-"))
        self.pushButton7.setText(_translate("self", "7"))
        self.pushButton8.setText(_translate("self", "8"))
        self.pushButton_plus.setText(_translate("self", "+"))
        self.pushButton0.setText(_translate("self", "0"))
        self.pushButton_sbros.setText(_translate("self", "C"))
        self.pushButton_ravno.setText(_translate("self", "="))
        self.pushButton_kor.setText(_translate("self", "Корень"))
        self.label.setText(_translate("self", ""))
        self.label.setStyleSheet("background-color: white; inset grey; min-height: 200px;")
        #  'border-style: solid; border-width: 1px; border-color: black;')
        self.label.setFrameShape(QFrame.Panel)
        self.label.setFrameShadow(QFrame.Sunken)
        self.label.setLineWidth(3)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
