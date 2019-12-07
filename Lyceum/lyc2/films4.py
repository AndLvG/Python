import sys
from PyQt5 import QtCore, QtWidgets, QtSql
from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox, QLabel
from PyQt5.QtSql import QSqlDatabase


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(10, 150, 781, 441))
        self.tableView.setObjectName("tableView")

        self.combobox = QComboBox(self.centralwidget)
        self.combobox.setGeometry(QtCore.QRect(100, 10, 200, 20))
        self.lGenres = QLabel(self.centralwidget)
        self.lGenres.setBuddy(self.combobox)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lGenres.setText(_translate("MainWindow", "Жанры"))
        db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("films.db")
        db.open()
        model = QtSql.QSqlTableModel(parent=None)
        model.setTable("genres")
        model.select()
        self.combobox.setModel(model)
        self.combobox.setModelColumn(model.fieldIndex("title"))


class Film_genres(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()
        self.go()

    def initUI(self):
        self.combobox.currentIndexChanged.connect(self.go)

    def go(self):
        db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("films.db")
        db.open()
        model = QtSql.QSqlQueryModel(parent=None)
        sql_text = f"select f.title, g.title from films f join genres g on f.genre = g.id where g.title = '{self.combobox.currentText()}'"
        model.setQuery(sql_text)
        model.query().exec_()
        self.tableView.setModel(model)
        self.tableView.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Film_genres()
    ex.show()
    sys.exit(app.exec ())
