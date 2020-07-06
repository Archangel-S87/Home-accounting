# Конвертация дизайна
# pyuic5 Design/AuthForm.ui -o Design/AuthForm.py
# pyuic5 Design/MainWindow.ui -o Design/MainWindow.py --import-from=Design
# pyrcc5 Design/resources.qrc -o Design/resources_rc.py

import sys  # sys нужен для передачи argv в QApplication
from Design.MainWindow import *
from db import DB
from user import User
from services import *
from auth import Auth
from PyQt5 import QtWidgets, QtSql


class HomeAccounting(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна


# Подключение базы данных через QT
def createConnection():
    db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName("data.db")

    if not db.open():
        QtWidgets.QMessageBox.critical(
            None,
            'Ошибка соединения с базой данных',
            'Невозможно установить соединение с базой данных.',
            QtWidgets.QMessageBox.Ok
        )
        return False

    query = QtSql.QSqlQuery()

    query.exec("""CREATE TABLE IF NOT EXISTS users (
        id int primary key,
        'email text',
        'login text',
        'password text',
        'bill double'
    )""")

    query.exec("""CREATE TABLE IF NOT EXISTS categories (
        'id integer PRIMARY KEY',
        'name text',
        'capacity integer',
        'author integer'
    )""")

    query.exec("""CREATE TABLE IF NOT EXISTS events (
        'id integer PRIMARY KEY',
        'type text',
        'amount double',
        'category integer',
        'date numeric',
        'description text',
        'author integer'
    )""")

    return True


def main():
    db = DB()

    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication

    if not createConnection():
        sys.exit(-1)

    window = HomeAccounting()  # Создаём объект класса HomeAccounting
    # window.show()  # Показываем окно

    user = User(db)
    auth = Auth(window, user)
    auth.show()

    app.exec()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
