import sys
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QTableWidget, QTableWidgetItem
from PyQt5.QtSql import QSqlDatabase


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 321, 121))
        self.groupBox.setStyleSheet("")
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName("groupBox")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_3.setGeometry(QtCore.QRect(10, 80, 141, 17))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(10, 50, 82, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(10, 20, 82, 17))
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(180, 60, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(120, 20, 191, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 150, 781, 441))
        self.tableWidget.setObjectName("tableWidget")
        MainWindow.setCentralWidget(self.centralwidget)

        self.bExit = QtWidgets.QPushButton(self)
        self.bExit.setGeometry(QtCore.QRect(350, 60, 75, 23))
        self.bExit.setObjectName("bExit")
        self.bExit.setText("Выход")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Будем искать по"))
        self.radioButton_3.setText(_translate("MainWindow", "Длительности"))
        self.radioButton_2.setText(_translate("MainWindow", "Году"))
        self.radioButton.setText(_translate("MainWindow", "Названию"))
        self.pushButton.setText(_translate("MainWindow", "Полетели"))


class Film_search(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.pushButton.clicked.connect(self.go)
        self.bExit.clicked.connect(self.exit)

    def exit(self):
        sys.exit()

    def go(self):
        # db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        # print(db)
        # db.setDatabaseName("films.db")
        # if not db.open():
        #     print("Database Error")
        #     print(db.lastError().text())
        #     return
        # else:
        #     print("Database open")
        #
        # model = QtSql.QSqlQueryModel(parent=None)
        # model.setQuery("SELECT * FROM films")
        # model.query().exec_()
        # self.tableView.setModel(model)
        # self.tableView.show()
        # # db_connect.close()
        con = sqlite3.connect("films.db")
        cur = con.cursor()
        rows = cur.execute("""SELECT title, year, duration FROM Films
            WHERE genre in (
        SELECT id FROM genres
            WHERE title = "музыка" Or title == "анимация") And year >= 1997""").fetchall()
        for row in rows:
            inx = rows.index(row)
            self.tableWidget.insertRow(inx)
            # add more if there is more columns in the database.
            self.tableWidget.setItem(inx, 0, QTableWidgetItem(row[0]))
            self.tableWidget.setItem(inx, 1, QTableWidgetItem(row[1]))
            self.tableWidget.setItem(inx, 2, QTableWidgetItem(row[2]))

        con.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    print(list(map(str, QSqlDatabase.drivers())))
    ex = Film_search()
    ex.show()
    sys.exit(app.exec())
