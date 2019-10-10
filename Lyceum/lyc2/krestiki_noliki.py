import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QRadioButton, QButtonGroup
from PyQt5.QtWidgets import QLCDNumber, QSlider, QVBoxLayout, QHBoxLayout, QGroupBox, QGridLayout
from PyQt5.QtCore import Qt


class Krestiki(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Крестики нолики')

        # Матрица 3 на 3
        board = [[None for _ in range(3)] for _ in range(3)]

        # Размер кнопки
        size_cell = 50

        for i in range(3):
            for j in range(3):
                btn = QPushButton(f'b{i}{j}')
                btn.resize(size_cell, size_cell)
                btn.move(i * size_cell, j * size_cell)
                board[i][j] = btn
                btn.clicked.connect(self.push_button)

    #
    #     label = QLabel('Текущий игрок')
    #
    #     b1 = QRadioButton("Игорок 1")
    #     b1.setChecked(True)
    #     # b1.toggled.connect(lambda: self.btnstate(self.b1))
    #     b2 = QRadioButton("Игрок 2")
    #     # b2.toggled.connect(lambda: self.btnstate(self.b2))
    #
    #     group = QButtonGroup()
    #     group.addButton(b1)
    #     group.addButton(b2)
    #     group.buttonClicked.connect(self._on_radio_button_clicked)
    #
    #     # layout = QHBoxLayout()
    #     # layout.addWidget(group1)
    #     # layout.addWidget(label)
    #     # layout.addWidget(b1)
    #     # layout.addWidget(b2)
    #     #
    #     # self.setLayout(layout)
    #
    # def _on_radio_button_clicked(self, button):
    #     print(button)
    #     self.label.setText('Current: ' + button.text())

    def push_button(self):
        sender = self.sender()
        sender.setText("Нажали")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Krestiki()
    ex.show()
    sys.exit(app.exec())
