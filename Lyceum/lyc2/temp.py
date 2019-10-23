from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QTableWidget
from PyQt5.QtSql import QSqlDatabase

print(list(map(str, QSqlDatabase.drivers())))

# site_pack_path = site.getsitepackages()[1]
# print(site_pack_path)
# QtGui.QApplication.addLibraryPath('{0}\\PySide\\plugins'.format(site_pack_path))
