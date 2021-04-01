"""
@file       : Login.py
@description: For login module.
@date       : 2021/03/22 18:02:25
@author     : Desmond
@email      : dmz990121@outlook.com
@version    : 0.0.1
"""
from PySide2.QtCore import Signal, Slot
from PySide2.QtWidgets import QMainWindow, QMessageBox
from ui.generate.Ui_Login import Ui_Login
from utility.DataManager import DataManager
from PySide2.QtWidgets import QLineEdit


class Login(QMainWindow):
    # signal
    loginType = Signal(tuple)

    def __init__(self):
        super().__init__()
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.ui.pswLineEdit.setEchoMode(QLineEdit.Password)

    @Slot()
    def on_loginButtom_clicked(self):
        password = self.ui.pswLineEdit.text()
        userAccount = self.ui.accLineEdit.text()

        data = DataManager("./data/db.sqlite3")
        if data.isPasswordCorrectByAccount(userAccount, password):
            result = data.getTypeAndIdByAccount(userAccount)
            # emit the signal to DataManager class
            # for creating Navigator window.
            self.loginType.emit(result)
        else:
            QMessageBox.information(self, "CEESS-提示", "用户名或密码错误!")
            self.ui.accLineEdit.setFocus()
        data.closeConnect()

    @Slot()
    def on_pswLineEdit_returnPressed(self):
        self.on_loginButtom_clicked()

    @Slot()
    def on_accLineEdit_returnPressed(self):
        self.ui.pswLineEdit.setFocus()
