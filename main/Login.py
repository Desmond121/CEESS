"""
@file       : Login.py
@description: For login module.
@date       : 2021/03/22 18:02:25
@author     : Desmond
@email      : dmz990121@outlook.com
@version    : 0.0.1
"""
from PySide2.QtCore import Qt, Signal, Slot
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QLineEdit, QMainWindow, QMessageBox
from ui.generate.Ui_Login import Ui_Login
from utility.DataManager import DataManager

_IMG_PATH = "./resources/img/"


class Login(QMainWindow):
    # signal
    loginType = Signal(tuple)

    def __init__(self):
        super().__init__()
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.ui.pswLineEdit.setEchoMode(QLineEdit.Password)
        # set visible action for lineEdit
        action = self.ui.pswLineEdit.addAction(
            QIcon(_IMG_PATH + "eye.svg"),
            QLineEdit.ActionPosition.TrailingPosition)
        action.setCheckable(True)
        action.toggled.connect(self.test)
        # set the title svg.
        self.ui.titleSvg.load(_IMG_PATH + "title.svg")
        self.ui.titleSvg.setStyleSheet("font-family: Courier New")

    @Slot(bool)
    def test(self, isChecked):
        if isChecked:
            self.ui.pswLineEdit.setEchoMode(QLineEdit.Normal)
        else:
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
