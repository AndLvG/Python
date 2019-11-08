import sys
from PyQt5.QtWidgets import (QMainWindow, QTextEdit, QAction, QFileDialog, QApplication, qApp, QLabel)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.resize(700, 600)

        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)

        ##############################################
        #  Строим меню файла
        ##############################################

        # меню файла - пункт New
        newAction = QAction('&Новый', self)
        newAction.setShortcut('Ctrl+N')
        newAction.setStatusTip('Новый файл')
        newAction.triggered.connect(self.newFile)

        # меню файла - пункт Open
        openAction = QAction('&Открыть', self)
        openAction.setShortcut('Ctrl+O')
        openAction.setStatusTip('Открыть файл')
        openAction.triggered.connect(self.openFile)

        # меню файла - пункт Save As
        saveasAction = QAction('&Сохранить', self)
        saveasAction.setShortcut('Ctrl+S')
        saveasAction.setStatusTip('Сохранить файл')
        saveasAction.triggered.connect(self.saveAs)

        statusBar = self.statusBar()

        # добавляем элементы в меню
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&Работа с файлом')
        fileMenu.addAction(newAction)
        fileMenu.addAction(openAction)
        fileMenu.addAction(saveasAction)

        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('Реадктор')
        self.show()

    def newFile(self):
        self.textEdit.setText("")

    def openFile(self):
        # диалог открытия файла
        fname = QFileDialog.getOpenFileName(self, 'Открываем файл')[0]
        openedFile = open(fname, 'r', encoding="utf8")
        txt = openedFile.read()
        openedFile.close()
        self.textEdit.setText(txt)

    def saveAs(self):
        # диалог сохранения файла
        fname = QFileDialog.getSaveFileName(self)[0]
        openedFile = open(fname, 'w')
        txt = self.textEdit.toPlainText()
        openedFile.write(txt)
        openedFile.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # QApplication.setStyle(QStyleFactory.create('Fusion'))
    myGUI = MainWindow()

    sys.exit(app.exec_())
