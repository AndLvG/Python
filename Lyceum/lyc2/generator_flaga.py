import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QCheckBox, QMainWindow, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets


# -*- coding: utf-8 -*-


# Form implementation generated from reading ui file 'gen_flag.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(462, 175)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 441, 151))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.horizontalLayoutWidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 81, 121))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton_1 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_1.setChecked(True)
        self.radioButton_1.setObjectName("radioButton_1")
        self.verticalLayout.addWidget(self.radioButton_1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout.addWidget(self.radioButton_2)
        self.radioButton_3 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_3.setObjectName("radioButton_3")
        self.verticalLayout.addWidget(self.radioButton_3)
        self.horizontalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.horizontalLayoutWidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.groupBox_2)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 20, 81, 121))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.radioButton_7 = QtWidgets.QRadioButton(self.verticalLayoutWidget_3)
        self.radioButton_7.setObjectName("radioButton_7")
        self.verticalLayout_3.addWidget(self.radioButton_7)
        self.radioButton_8 = QtWidgets.QRadioButton(self.verticalLayoutWidget_3)
        self.radioButton_8.setChecked(True)
        self.radioButton_8.setObjectName("radioButton_8")
        self.verticalLayout_3.addWidget(self.radioButton_8)
        self.radioButton_9 = QtWidgets.QRadioButton(self.verticalLayoutWidget_3)
        self.radioButton_9.setObjectName("radioButton_9")
        self.verticalLayout_3.addWidget(self.radioButton_9)
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.horizontalLayoutWidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.groupBox_3)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(10, 20, 81, 121))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.radioButton_10 = QtWidgets.QRadioButton(self.verticalLayoutWidget_4)
        self.radioButton_10.setObjectName("radioButton_10")
        self.verticalLayout_4.addWidget(self.radioButton_10)
        self.radioButton_11 = QtWidgets.QRadioButton(self.verticalLayoutWidget_4)
        self.radioButton_11.setObjectName("radioButton_11")
        self.verticalLayout_4.addWidget(self.radioButton_11)
        self.radioButton_12 = QtWidgets.QRadioButton(self.verticalLayoutWidget_4)
        self.radioButton_12.setChecked(True)
        self.radioButton_12.setObjectName("radioButton_12")
        self.verticalLayout_4.addWidget(self.radioButton_12)
        self.horizontalLayout.addWidget(self.groupBox_3)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Генератор флага"))
        self.groupBox.setTitle(_translate("MainWindow", "Первый цвет"))
        self.radioButton_1.setText(_translate("MainWindow", "Красный"))
        self.radioButton_2.setText(_translate("MainWindow", "Зелёный"))
        self.radioButton_3.setText(_translate("MainWindow", "Белый"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Второй цвет"))
        self.radioButton_7.setText(_translate("MainWindow", "Красный"))
        self.radioButton_8.setText(_translate("MainWindow", "Зелёный"))
        self.radioButton_9.setText(_translate("MainWindow", "Белый"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Третий цвет"))
        self.radioButton_10.setText(_translate("MainWindow", "Красный"))
        self.radioButton_11.setText(_translate("MainWindow", "Зелёный"))
        self.radioButton_12.setText(_translate("MainWindow", "Белый"))
        self.pushButton.setText(_translate("MainWindow", "Флаг"))


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.pushButton.clicked.connect(self.flag)

    def flag(self):
        s = 'Цвета флага: '
        for i in range(1, 13):
            radio = self.findChild(QtWidgets.QRadioButton, "radioButton_" + str(i))
            if not radio == None:
                if radio.isChecked():
                    s += radio.text() + ' '

        QMessageBox.information(self, 'Флаг', s, QMessageBox.Ok)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
