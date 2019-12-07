import sys

from file_text_brow import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog


class File_browser(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.bLoad.clicked.connect(self.load_file)

    def load_file(self):
        filename = QFileDialog.getOpenFileName(self, 'Выбрать тексовый файл', '')[0]
        with open(filename, 'rt', encoding="utf8") as f:
            odd_lines = f.readlines()[::2]
        with open(filename, 'rt', encoding="utf8") as f:
            even_lines = f.readlines()[1::2]
        for line in odd_lines:
            self.textEdit.append(line.replace('\n', ''))
        for line in even_lines:
            self.textEdit.append(line.replace('\n', ''))


if __name__ == '__main__':
    app = QApplication(sys.argv)
ex = File_browser()
ex.show()
sys.exit(app.exec())
