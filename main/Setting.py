"""
@file       : Setting.py
@description: For setting windows.
@date       : 2021/03/22 18:03:32
@author     : Desmond
@email      : dmz990121@outlook.com
@version    : 0.0.1
"""
from utility.DataManager import DataManager
from PySide2.QtCore import Qt, Signal, Slot
from PySide2.QtWidgets import QInputDialog, QLineEdit, QMainWindow, QMessageBox
from ui.generate.Ui_Setting import Ui_Setting


class Setting(QMainWindow):
    switchDisplaySignal = Signal()
    signOutSignal = Signal()
    userId = None

    def __init__(self, userId, parent=None):
        super().__init__(parent)
        self.ui = Ui_Setting()
        self.ui.setupUi(self)

        # get user infomation from database.
        db = DataManager()
        self.ui.userName.setText(db.getNameById(userId))
        self.ui.userAccount.setText(db.getAccountById(userId))
        db.closeConnect()
        # store user id.
        self.userId = userId

    # slot for changing theme.
    @Slot()
    def on_switchDisplayMode_clicked(self):
        self.switchDisplaySignal.emit()

    # slot for sign out.
    @Slot()
    def on_btnSignOut_clicked(self):
        self.signOutSignal.emit()

    @Slot()
    def on_btnChangePsw_clicked(self):
        originalPsw = QInputDialog.getText(
            self, "CEESS-修改密码", "请输入原始密码", QLineEdit.Normal, "",
            Qt.WindowSystemMenuHint | Qt.WindowTitleHint)
        # getText return a tuple in form of (input_text,is_input_successful)
        if originalPsw[1]:  # input successfully
            db = DataManager()  # database open ----------------
            if db.isPasswordCorrectById(self.userId, originalPsw[0]):
                newPsw = QInputDialog.getText(
                    self, "CEESS-修改密码", "请输入新密码", QLineEdit.Normal, "",
                    Qt.WindowSystemMenuHint | Qt.WindowTitleHint)
                if newPsw[1]:  # new password input successfully.
                    db.changePasswordById(self.userId, newPsw[0])
                    QMessageBox.information(self, "CEESS-通知", "密码修改成功！")
                    self.signOutSignal.emit()
            else:
                QMessageBox.warning(self, "CEESS-提醒", "密码输入错误！")
            db.closeConnect()  # database close ----------------

    @Slot()
    def on_rename_clicked(self):
        newName = originalPsw = QInputDialog.getText(
            self, "CEESS-修改姓名", "请输入姓名", QLineEdit.Normal, "",
            Qt.WindowSystemMenuHint | Qt.WindowTitleHint)
        if newName[1]:
            self.ui.userName.setText(newName[0])
            db = DataManager()  # database open ----------------
            db.changeNameById(self.userId, newName[0])
            db.closeConnect()  # database open ----------------
            QMessageBox.information(self, "CEESS-通知", "姓名修改成功！")
