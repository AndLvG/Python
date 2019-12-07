import sys

from PyQt5.QtWidgets import (QMainWindow, QTextEdit, QAction, QFileDialog, QApplication, QInputDialog, QLineEdit)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.resize(700, 600)

        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)

        newAction = QAction('&Новый', self)
        newAction.triggered.connect(self.newFile)

        openAction = QAction('&Открыть', self)
        openAction.triggered.connect(self.openFile)

        # меню файла - пункт Save As
        saveasAction = QAction('&Сохранить', self)
        saveasAction.triggered.connect(self.saveAs)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&Работа с файлом')
        fileMenu.addAction(newAction)
        fileMenu.addAction(openAction)
        fileMenu.addAction(saveasAction)

        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('Редактор')
        self.fName = ''
        self.show()

    def newFile(self):
        self.fName, okPressed = QInputDialog.getText(self, "Ввод данных", "Введите имя файла:",
                                                     QLineEdit.Normal, "")
        if okPressed:
            self.textEdit.setText("")
            self.setWindowTitle('Редактор - Файл ' + self.fName)

    def openFile(self):
        self.fName, okPressed = QInputDialog.getText(self, "Ввод данных", "Введите имя файла:",
                                                     QLineEdit.Normal, "")
        if okPressed:
            # fname = QFileDialog.getOpenFileName(self, 'Открываем файл')[0]
            openedFile = open(self.fName, 'rt', encoding="utf8")
            txt = openedFile.read()
            openedFile.close()
            self.textEdit.setText(txt)
            self.setWindowTitle('Редактор - Файл ' + self.fName)

    def saveAs(self):
        fname = QFileDialog.getSaveFileName(self)[0]
        openedFile = open(fname, 'w')
        txt = self.textEdit.toPlainText()
        openedFile.write(txt)
        openedFile.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myGUI = MainWindow()
    sys.exit(app.exec_())
