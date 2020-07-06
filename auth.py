from Design.AuthForm import *
from PyQt5.QtWidgets import QDialog  # Импорт базового диалога
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator


class Auth(QDialog, Ui_AuthForm):
    def __init__(self, main_window, user):
        QDialog.__init__(self)
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.mainwindow = main_window
        self.user = user

        self.comboBox_register_rate.addItems(['BYN', 'RUB', 'USD'])

        self.buttonBox.accepted.connect(self.accept_data)
        self.buttonBox.rejected.connect(self.reject_data)

        reg_ex_email = QRegExp("^[A-Za-z0-9_]+[.][A-Za-z0-9_]+[@][a-z]+[.][a-z]{2,3}$")
        email_validator = QRegExpValidator(reg_ex_email, self.lineEdit_register_email)
        self.lineEdit_register_email.setValidator(email_validator)

        reg_ex_login = QRegExp('^[А-Яа-яA-Za-z0-9_]+$')
        login_validator = QRegExpValidator(reg_ex_login, self.lineEdit_register_login)
        self.lineEdit_register_login.setValidator(login_validator)

        self.buttonBox.button(self.buttonBox.Ok).setEnabled(False)

        self.lineEdit_register_login.textChanged.connect(self.temp)
        self.lineEdit_register_email.textChanged.connect(self.temp)

    def temp(self, text):
        if text == '':
            self.buttonBox.button(self.buttonBox.Ok).setEnabled(False)
        else:
            self.buttonBox.button(self.buttonBox.Ok).setEnabled(True)
        pass

    def validateNoEmpty(self, data):
        error = False
        for name in data:
            if name == 'rate':
                break

            if data[name] == '':
                error = True
                break

        return error

    def reject_data(self):
        print('reject')
        self.show()
        pass

    def accept_data(self):
        if self.toolBox.currentIndex() == 1:
            data = {
                'email': self.lineEdit_register_email.text(),
                'password': self.lineEdit_register_password.text(),
                'login': self.lineEdit_register_login.text(),
                'rate': self.comboBox_register_rate.currentText()
            }
            self.validateNoEmpty(data)
            message = self.user.registerUser(data)
            if message:

                pass

            print('register')
        else:
            print(self.lineEdit_auth_password.text())
            if self.user.checkLogin(self.lineEdit_auth_login.text(), self.lineEdit_auth_password.text()):
                print('login')
            else:
                print('Not login')

        self.show()
        pass
