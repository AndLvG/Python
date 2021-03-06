import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QCheckBox, QMainWindow
from PyQt5.QtWidgets import QPlainTextEdit
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Заказ в Макдональдсе")
        MainWindow.resize(528, 372)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 40, 500, 268))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lcdNumberGamb = QtWidgets.QLCDNumber(self.horizontalLayoutWidget)
        self.lcdNumberGamb.setProperty("value", 300.0)
        self.lcdNumberGamb.setObjectName("lcdNumberGamb")
        self.gridLayout.addWidget(self.lcdNumberGamb, 1, 1, 1, 1)
        self.lcdNumberMiniKart = QtWidgets.QLCDNumber(self.horizontalLayoutWidget)
        self.lcdNumberMiniKart.setAutoFillBackground(False)
        self.lcdNumberMiniKart.setSmallDecimalPoint(False)
        self.lcdNumberMiniKart.setProperty("value", 50.0)
        self.lcdNumberMiniKart.setObjectName("lcdNumberMiniKart")
        self.gridLayout.addWidget(self.lcdNumberMiniKart, 4, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.spinBoxFanta = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.spinBoxFanta.setObjectName("spinBoxFanta")
        self.gridLayout.addWidget(self.spinBoxFanta, 8, 2, 1, 1)
        self.spinBoxMaxKart = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.spinBoxMaxKart.setObjectName("spinBoxMaxKart")
        self.gridLayout.addWidget(self.spinBoxMaxKart, 5, 2, 1, 1)
        self.checkBFanta = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkBFanta.setObjectName("checkBFanta")
        self.gridLayout.addWidget(self.checkBFanta, 8, 0, 1, 1)
        self.lcdNumberFanta = QtWidgets.QLCDNumber(self.horizontalLayoutWidget)
        self.lcdNumberFanta.setProperty("value", 60.0)
        self.lcdNumberFanta.setObjectName("lcdNumberFanta")
        self.gridLayout.addWidget(self.lcdNumberFanta, 8, 1, 1, 1)
        self.checMiniKart = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checMiniKart.setObjectName("checMiniKart")
        self.gridLayout.addWidget(self.checMiniKart, 4, 0, 1, 1)
        self.lcdNumberCola = QtWidgets.QLCDNumber(self.horizontalLayoutWidget)
        self.lcdNumberCola.setProperty("value", 60.0)
        self.lcdNumberCola.setObjectName("lcdNumberCola")
        self.gridLayout.addWidget(self.lcdNumberCola, 7, 1, 1, 1)
        self.spinBoxCola = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.spinBoxCola.setObjectName("spinBoxCola")
        self.gridLayout.addWidget(self.spinBoxCola, 7, 2, 1, 1)
        self.checkMaxKart = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkMaxKart.setObjectName("checkMaxKart")
        self.gridLayout.addWidget(self.checkMaxKart, 5, 0, 1, 1)
        self.lcdNumberMaxKart = QtWidgets.QLCDNumber(self.horizontalLayoutWidget)
        self.lcdNumberMaxKart.setProperty("value", 80.0)
        self.lcdNumberMaxKart.setObjectName("lcdNumberMaxKart")
        self.gridLayout.addWidget(self.lcdNumberMaxKart, 5, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.spinBoxMiniKart = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.spinBoxMiniKart.setObjectName("spinBoxMiniKart")
        self.gridLayout.addWidget(self.spinBoxMiniKart, 4, 2, 1, 1)
        self.spinBoxGamb = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.spinBoxGamb.setObjectName("spinBoxGamb")
        self.gridLayout.addWidget(self.spinBoxGamb, 1, 2, 1, 1)
        self.checkBGamb = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkBGamb.setObjectName("checkBGamb")
        self.gridLayout.addWidget(self.checkBGamb, 1, 0, 1, 1)
        self.checkBCola = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkBCola.setObjectName("checkBCola")
        self.gridLayout.addWidget(self.checkBCola, 7, 0, 1, 1)
        self.lcdNumberChis = QtWidgets.QLCDNumber(self.horizontalLayoutWidget)
        self.lcdNumberChis.setProperty("value", 250.0)
        self.lcdNumberChis.setObjectName("lcdNumberChis")
        self.gridLayout.addWidget(self.lcdNumberChis, 2, 1, 1, 1)
        self.spinBoxChis = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.spinBoxChis.setObjectName("spinBoxChis")
        self.gridLayout.addWidget(self.spinBoxChis, 2, 2, 1, 1)
        self.checkBChis = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkBChis.setObjectName("checkBChis")
        self.gridLayout.addWidget(self.checkBChis, 2, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.horizontalLayoutWidget)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.horizontalLayout.addWidget(self.plainTextEdit)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(110, 20, 47, 13))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(350, 20, 47, 13))
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(220, 320, 75, 23))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Порций"))
        self.checkBFanta.setText(_translate("MainWindow", "Фанта"))
        self.checMiniKart.setText(_translate("MainWindow", "Мини картошка"))
        self.checkMaxKart.setText(_translate("MainWindow", "Большая картошка"))
        self.label.setText(_translate("MainWindow", "Цена, руб."))
        self.checkBGamb.setText(_translate("MainWindow", "Гамбургер"))
        self.checkBCola.setText(_translate("MainWindow", "Кола"))
        self.checkBChis.setText(_translate("MainWindow", "Чизбургер"))
        self.label_3.setText(_translate("MainWindow", "Меню"))
        self.label_4.setText(_translate("MainWindow", "Заказ"))
        self.pushButton.setText(_translate("MainWindow", "Заказать"))


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.checkBGamb.stateChanged.connect(self.gambu)
        self.checkBFanta.stateChanged.connect(self.fanta)
        self.checMiniKart.stateChanged.connect(self.mikart)
        self.checkMaxKart.stateChanged.connect(self.makart)
        self.checkBCola.stateChanged.connect(self.cola)
        self.checkBChis.stateChanged.connect(self.chis)
        self.pushButton.clicked.connect(self.zakaz)

    def zakaz(self):
        self.plainTextEdit.clear()
        a = 0
        if self.checkBGamb.isChecked():
            a = a + (self.spinBoxGamb.value() * self.lcdNumberGamb.value())
            self.plainTextEdit.appendPlainText(
                f'Гамбургер {self.spinBoxGamb.value()} шт. на сумму {self.spinBoxGamb.value() * self.lcdNumberGamb.value()} руб.')
        if self.checkBFanta.isChecked():
            a = a + (self.spinBoxFanta.value() * self.lcdNumberFanta.value())
            self.plainTextEdit.appendPlainText(
                f'Фанта {self.spinBoxFanta.value()} шт. на сумму {self.spinBoxFanta.value() * self.lcdNumberFanta.value()} руб.')
        if self.checMiniKart.isChecked():
            a = a + (self.spinBoxMiniKart.value() * self.lcdNumberMiniKart.value())
            self.plainTextEdit.appendPlainText(
                f'Мини картошка {self.spinBoxMiniKart.value()} шт. на сумму {self.spinBoxMiniKart.value() * self.lcdNumberMiniKart.value()} руб.')
        if self.checkMaxKart.isChecked():
            a = a + (self.spinBoxMaxKart.value() * self.lcdNumberMaxKart.value())
            self.plainTextEdit.appendPlainText(
                f'Большая картошка {self.spinBoxMaxKart.value()} шт. на сумму {self.spinBoxMaxKart.value() * self.lcdNumberMaxKart.value()} руб.')
        if self.checkBCola.isChecked():
            a = a + (self.spinBoxCola.value() * self.lcdNumberCola.value())
            self.plainTextEdit.appendPlainText(
                f'Кола {self.spinBoxCola.value()} шт. на сумму {self.spinBoxCola.value() * self.lcdNumberCola.value()} руб.')
        if self.checkBChis.isChecked():
            a = a + (self.spinBoxChis.value() * self.lcdNumberChis.value())
            self.plainTextEdit.appendPlainText(
                f'Чизбургер {self.spinBoxChis.value()} шт. на сумму {self.spinBoxChis.value() * self.lcdNumberChis.value()} руб.')

        if a != 0:
            self.plainTextEdit.appendPlainText('------ Конец чека')
            self.plainTextEdit.appendPlainText(f'   Итого {a} руб.')

    def gambu(self):
        if not self.checkBGamb.isChecked():
            self.spinBoxGamb.setValue(0)
        elif self.spinBoxGamb.value() == 0:
            self.spinBoxGamb.setValue(1)

    def fanta(self):
        if not self.checkBFanta.isChecked():
            self.spinBoxFanta.setValue(0)
        elif self.spinBoxFanta.value() == 0:
            self.spinBoxFanta.setValue(1)

    def mikart(self):
        if not self.checMiniKart.isChecked():
            self.spinBoxMiniKart.setValue(0)
        elif self.spinBoxMiniKart.value() == 0:
            self.spinBoxMiniKart.setValue(1)

    def makart(self):
        if not self.checkMaxKart.isChecked():
            self.spinBoxMaxKart.setValue(0)
        elif self.spinBoxMaxKart.value() == 0:
            self.spinBoxMaxKart.setValue(1)

    def cola(self):
        if not self.checkBCola.isChecked():
            self.spinBoxCola.setValue(0)
        elif self.spinBoxCola.value() == 0:
            self.spinBoxCola.setValue(1)

    def chis(self):
        if not self.checkBChis.isChecked():
            self.spinBoxChis.setValue(0)
        elif self.spinBoxChis.value() == 0:
            self.spinBoxChis.setValue(1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
