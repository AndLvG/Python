# coding=<utf-8>
import sys, csv, random
from PyQt5 import QtGui, QtCore, Qt
from PyQt5.QtWidgets import (QMainWindow, QTextEdit, QAction, QFileDialog, QApplication, qApp, QLabel)
from tovar_ui import Ui_MainWindow


class Tovar_CSV(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.model = QtGui.QStandardItemModel(self)
        self.tableViewCSV.setModel(self.model)
        self.model.dataChanged.connect(self.count_itog)
        self.lTotal.setStyleSheet("""QLCDNumber {background-color: grey;}""")
        self.bLoad.clicked.connect(self.load_csv)

    def load_csv(self):
        filename = QFileDialog.getOpenFileName(self, 'Открываем файл', '', "CSV (*.csv)")[0]
        if filename:
            with open(filename, encoding="utf8") as csvfile:
                reader = sorted(csv.reader(csvfile, delimiter=';'), key=lambda row: int(row[1]), reverse=True)
                self.model.clear()
                for row in reader:
                    items = [QtGui.QStandardItem(field) for field in row]
                    items.append(QtGui.QStandardItem('0'))
                    self.model.appendRow(items)

            self.model.setHorizontalHeaderLabels(['Товар', 'Цена', 'Количество'])

            for j in range(self.model.rowCount()):
                if j < 5:
                    color = QtGui.QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                    for i in range(self.model.columnCount()):
                        self.model.setData(self.model.index(j, i), QtGui.QBrush(color), QtCore.Qt.BackgroundRole)

            self.tableViewCSV.resizeColumnsToContents()
            self.count_itog()

    def count_itog(self):
        result = 0
        for i in range(self.model.rowCount()):
            print(self.model.item(i, 1).text())
            print(self.model.item(i, 2).text())
            print(int(self.model.item(i, 1).text()) * int(self.model.item(i, 2).text()))

            result += int(self.model.item(i, 1).text()) * int(self.model.item(i, 2).text())
        self.lTotal.display(result)


if __name__ == '__main__':
    app = QApplication(sys.argv)
myGUI = Tovar_CSV()
myGUI.setWindowTitle("Список покупок")
myGUI.show()
sys.exit(app.exec_())
