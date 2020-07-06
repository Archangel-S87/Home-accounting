# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Design/AuthForm.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AuthForm(object):
    def setupUi(self, AuthForm):
        AuthForm.setObjectName("AuthForm")
        AuthForm.resize(447, 259)
        AuthForm.setMinimumSize(QtCore.QSize(447, 259))
        AuthForm.setMaximumSize(QtCore.QSize(447, 259))
        font = QtGui.QFont()
        font.setPointSize(12)
        AuthForm.setFont(font)
        AuthForm.setAutoFillBackground(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(AuthForm)
        self.verticalLayout.setObjectName("verticalLayout")
        self.toolBox = QtWidgets.QToolBox(AuthForm)
        self.toolBox.setAutoFillBackground(True)
        self.toolBox.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.toolBox.setObjectName("toolBox")
        self.page_auth = QtWidgets.QWidget()
        self.page_auth.setGeometry(QtCore.QRect(0, 0, 158, 74))
        self.page_auth.setObjectName("page_auth")
        self.formLayout = QtWidgets.QFormLayout(self.page_auth)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.formLayout.setHorizontalSpacing(20)
        self.formLayout.setObjectName("formLayout")
        self.label_auth_login = QtWidgets.QLabel(self.page_auth)
        self.label_auth_login.setObjectName("label_auth_login")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_auth_login)
        self.lineEdit_auth_login = QtWidgets.QLineEdit(self.page_auth)
        self.lineEdit_auth_login.setObjectName("lineEdit_auth_login")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_auth_login)
        self.label_auth_password = QtWidgets.QLabel(self.page_auth)
        self.label_auth_password.setObjectName("label_auth_password")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_auth_password)
        self.lineEdit_auth_password = QtWidgets.QLineEdit(self.page_auth)
        self.lineEdit_auth_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_auth_password.setClearButtonEnabled(False)
        self.lineEdit_auth_password.setObjectName("lineEdit_auth_password")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_auth_password)
        self.toolBox.addItem(self.page_auth, "")
        self.page_register = QtWidgets.QWidget()
        self.page_register.setGeometry(QtCore.QRect(0, 0, 429, 142))
        self.page_register.setObjectName("page_register")
        self.formLayout_2 = QtWidgets.QFormLayout(self.page_register)
        self.formLayout_2.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.formLayout_2.setHorizontalSpacing(20)
        self.formLayout_2.setVerticalSpacing(6)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_register_email = QtWidgets.QLabel(self.page_register)
        self.label_register_email.setObjectName("label_register_email")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_register_email)
        self.lineEdit_register_email = QtWidgets.QLineEdit(self.page_register)
        self.lineEdit_register_email.setInputMask("")
        self.lineEdit_register_email.setText("")
        self.lineEdit_register_email.setMaxLength(32767)
        self.lineEdit_register_email.setObjectName("lineEdit_register_email")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_register_email)
        self.label_register_password = QtWidgets.QLabel(self.page_register)
        self.label_register_password.setObjectName("label_register_password")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_register_password)
        self.lineEdit_register_password = QtWidgets.QLineEdit(self.page_register)
        self.lineEdit_register_password.setObjectName("lineEdit_register_password")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_register_password)
        self.label_register_login = QtWidgets.QLabel(self.page_register)
        self.label_register_login.setObjectName("label_register_login")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_register_login)
        self.lineEdit_register_login = QtWidgets.QLineEdit(self.page_register)
        self.lineEdit_register_login.setObjectName("lineEdit_register_login")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_register_login)
        self.label_register_rate = QtWidgets.QLabel(self.page_register)
        self.label_register_rate.setObjectName("label_register_rate")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_register_rate)
        self.comboBox_register_rate = QtWidgets.QComboBox(self.page_register)
        self.comboBox_register_rate.setAcceptDrops(False)
        self.comboBox_register_rate.setEditable(False)
        self.comboBox_register_rate.setInsertPolicy(QtWidgets.QComboBox.InsertAtCurrent)
        self.comboBox_register_rate.setObjectName("comboBox_register_rate")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.comboBox_register_rate)
        self.toolBox.addItem(self.page_register, "")
        self.verticalLayout.addWidget(self.toolBox)
        self.buttonBox = QtWidgets.QDialogButtonBox(AuthForm)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(AuthForm)
        self.toolBox.setCurrentIndex(1)
        self.buttonBox.accepted.connect(AuthForm.accept)
        self.buttonBox.rejected.connect(AuthForm.reject)
        QtCore.QMetaObject.connectSlotsByName(AuthForm)

    def retranslateUi(self, AuthForm):
        _translate = QtCore.QCoreApplication.translate
        AuthForm.setWindowTitle(_translate("AuthForm", "Авnоризация"))
        self.label_auth_login.setText(_translate("AuthForm", "Логин"))
        self.label_auth_password.setText(_translate("AuthForm", "Пароль"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_auth), _translate("AuthForm", "Войти"))
        self.label_register_email.setText(_translate("AuthForm", "Email"))
        self.label_register_password.setText(_translate("AuthForm", "Пароль"))
        self.label_register_login.setText(_translate("AuthForm", "Логин"))
        self.label_register_rate.setText(_translate("AuthForm", "Валюта счёта"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_register), _translate("AuthForm", "Новый пользователь"))