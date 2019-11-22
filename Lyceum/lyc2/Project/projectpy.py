import sys

from PyQt5 import QtCore, QtWidgets, QtSql
from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog, QLineEdit, QMessageBox, QFileDialog
from PyQt5.QtGui import QPixmap, QTransform
import sqlite3
from project import Ui_MainWindow


class Project(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()
        self.load_genres()

    def initUI(self):
        self.pixmap = QPixmap()
        self.im_name = ''
        self.l_image.setFrameShape(QtWidgets.QFrame.Box)
        self.l_image.setFrameShadow(QtWidgets.QFrame.Plain)
        # событие выбора в комбобокс
        self.cmb_genres.currentIndexChanged.connect(self.refresh_table)
        # событие добавления новой темы
        self.b_new_genre.clicked.connect(self.add_genre)
        # событие клика по таблице
        self.im_table.clicked.connect(self.show_image)
        # поворот против часовой стрелки
        self.left.clicked.connect(self.rotate_minus)
        # поворот по часовой стрелки
        self.right.clicked.connect(self.rotate_plus)
        # сохранить изменения картинки
        self.save.clicked.connect(self.save_image)
        # добавить картинку
        self.new_2.clicked.connect(self.add_image)
        # удалить картинку
        self.dell.clicked.connect(self.del_image)
        # рекдактировать картинку
        self.fix.clicked.connect(self.fix_image)

    # Загрузка данных в список тем
    def load_genres(self):
        db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("image.db")
        db.open()
        model = QtSql.QSqlTableModel(parent=None)
        model.setTable("genres")
        model.select()
        self.cmb_genres.setModel(model)
        self.cmb_genres.setModelColumn(model.fieldIndex("genre"))
        # Добавляем условие для всех тем и ставим его по умолчанию
        self.cmb_genres.insertItem(0, 'Все')
        self.cmb_genres.setCurrentText('Все')
        # Сразу обновляем содержимое таблицы с рисунками
        self.refresh_table()

    # Обновление данных в таблице изображений
    def refresh_table(self):
        db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("image.db")
        db.open()
        model = QtSql.QSqlQueryModel(parent=None)
        # Названия столбцов меняем на русский язык "g.genre as Тематика"
        sql_text = "select i.id, g.genre as Тематика, i.im_name Название, i.im_file Файл, i.data as Добавлен from images i join genres g on i.genre = g.id"
        if self.cmb_genres.currentText() != 'Все':
            sql_text += f" where g.genre = '{self.cmb_genres.currentText()}'"
        model.setQuery(sql_text)
        model.query().exec_()
        self.im_table.setModel(model)
        # Столбец с ID делаем невидимым. Он нам потребуется для удаления строки из таблицы
        self.im_table.setColumnHidden(0, True)
        self.im_table.show()

    # Добавление новой темы
    def add_genre(self):
        new_genre, okPressed = QInputDialog.getText(self, "Ввод данных", "Введите название новой темы:",
                                                    QLineEdit.Normal, "")
        if okPressed and new_genre != '':
            con = sqlite3.connect("image.db")
            cur = con.cursor()
            # Проверяем есть ли уже такая тема. Count(*) взвращает количество строк с данным условие
            # Если 0 значит таких строк нет
            result = cur.execute(f"""SELECT count(*) cc from genres where genre = '{new_genre}'""").fetchall()[0]
            con.close()
            if result[0] == 0:
                db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
                db.setDatabaseName("image.db")
                db.open()
                model = QtSql.QSqlQueryModel(parent=None)
                # Добавляем строку в таблицу
                sql_text = f"INSERT  INTO  genres(genre) VALUES('{new_genre}')"
                model.setQuery(sql_text)
                model.query().exec_()
                # Обновляем данные в TableView
                self.refresh_table()
                db.close()
                QMessageBox.about(self, "Результат", f"Тема <{new_genre}> добавлена")
                # Обновляем содержимое комбобокса с темами
                self.load_genres()
            else:
                # Если такая тема уже есть - сообщаем об ошибке
                QMessageBox().warning(self, "Ошибка", "Такая тема уже есть", QMessageBox.Ok)

        # показываем рисунок

    # размещам рисунок на кнопке
    def show_image(self, signal):
        db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("image.db")
        db.open()
        model = QtSql.QSqlTableModel()
        model.setTable("images")
        model.select()
        # по строке на которую кликнули "signal.row()" берём из таблицы значение в поле 'im_file'
        fname = model.record(signal.row()).value('im_file')
        db.close()
        fname = f"картинки\{fname}"
        # сохраняем имя открытого файла в self переменную чтобы потом при изменении его можно было сохранить
        self.im_name = fname
        self.pixmap.load(fname)
        # получаем размеры картинки
        im = self.pixmap.toImage()
        # и по этим размерам трансформируем изображение чтобы оно влезло в размеры QLabel
        # Свойство QtCore.Qt.KeepAspectRatio сохраняет соотношение сторон
        self.pixmap = self.pixmap.scaled(im.width(), im.height(), QtCore.Qt.KeepAspectRatio)
        self.l_image.setPixmap(self.pixmap)

    # поворачиваем по часовой стрелке
    def rotate_plus(self):
        self.pixmap = self.pixmap.transformed(QTransform().rotate(90))
        self.l_image.setPixmap(self.pixmap)

    # поворачиваем против часовой стрелке
    def rotate_minus(self):
        self.pixmap = self.pixmap.transformed(QTransform().rotate(-90))
        self.l_image.setPixmap(self.pixmap)

    # сохраняем изображение
    def save_image(self):
        self.pixmap.save(self.im_name)

    # добавить картинку в базу
    def add_image(self):
        filename = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '')[0]
        # диалог возвращает полный путь к файлу "D:\.."
        # нам нужно только имя файла - функция filename()
        fname = QtCore.QFileInfo(filename).fileName()
        con = sqlite3.connect("image.db")
        cur = con.cursor()
        # Создаем список жанров чтобы пользователь выбрал к какому жанру будет относится картинка
        result = cur.execute("""SELECT genre from genres""").fetchall()
        genres = []
        for elem in result:
            genres.append(elem[0])
        con.close()

        i, okBtnPressed = QInputDialog.getItem(self, "Выберите тему", "Тема",
                                               genres, 0, False)
        # к индексу в псике добавляем 1 так как ID у жанров в таблице начинаются с 1
        genre_id = genres.index(i) + 1

        if okBtnPressed:
            im_name, okPressed = QInputDialog.getText(self, "Ввод данных", "Введите название картинки:",
                                                      QLineEdit.Normal, "")
            if okPressed:
                db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
                db.setDatabaseName("image.db")
                db.open()
                model = QtSql.QSqlQueryModel(parent=None)
                # добавляем запись в images
                sql_text = f"INSERT INTO images (im_file, genre, im_name) VALUES ('{fname}',{genre_id},'{im_name}')"
                model.setQuery(sql_text)
                model.query().exec_()
                # и обновляем таблицу
                self.refresh_table()
                db.close()

    # удалить картинку
    def del_image(self):
        # по умолчанию в MessageBox ставим Cancel
        buttonReply = QMessageBox.question(self, 'Подтвердите действие', "картинка будет удалена",
                                           QMessageBox.Yes | QMessageBox.Cancel, QMessageBox.Cancel)
        # если пользователь согласен
        if buttonReply == QMessageBox.Yes:
            db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
            db.setDatabaseName("image.db")
            db.open()
            # модель для запроса к базе
            model = QtSql.QSqlQueryModel(parent=None)
            # модель для получения ID записи которую нужно удалить
            model_table = QtSql.QSqlTableModel()
            model_table.setTable("images")
            model_table.select()
            # берем первый индекс из списка выбранных строк.
            # по нему строку с этим индексом в моделе и значение в этой строке value(0) в первом столбце - ID
            id = model_table.record(self.im_table.selectedIndexes()[0].row()).value(0)
            # удаляем
            sql_text = f"DELETE FROM images WHERE id = {id}"
            model.setQuery(sql_text)
            model.query().exec_()
            self.refresh_table()
            db.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
ex = Project()
ex.show()
sys.exit(app.exec())
