# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Lvov\Python\Lyceum\lyc2\tovar_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(320, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bLoad = QtWidgets.QPushButton(self.centralwidget)
        self.bLoad.setGeometry(QtCore.QRect(10, 10, 101, 23))
        self.bLoad.setObjectName("bLoad")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 10, 91, 16))
        self.label.setObjectName("label")
        self.lTotal = QtWidgets.QLCDNumber(self.centralwidget)
        self.lTotal.setGeometry(QtCore.QRect(210, 10, 91, 23))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lTotal.setFont(font)
        self.lTotal.setStyleSheet("")
        self.lTotal.setObjectName("lTotal")
        self.tableViewCSV = QtWidgets.QTableView(self.centralwidget)
        self.tableViewCSV.setGeometry(QtCore.QRect(10, 40, 291, 501))
        self.tableViewCSV.setObjectName("tableViewCSV")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 320, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.bLoad.setText(_translate("MainWindow", "Загрузить список"))
        self.label.setText(_translate("MainWindow", "Сумма покупки"))
