"""
@file       : allWindows.py
@description: This file create classes to encapsulate all the QT-uic generated
              files with "Ui_" prefix.
@date       : 2021/02/10 17:22:10
@author     : Desmond
@e-mail     : dmz990121@outlook.com
@version    : 0.0.1
"""

from PySide2.QtWidgets import QApplication, QMainWindow, QWidget
from ui.Ui_Login import Ui_Login
from ui.Ui_Student import Ui_Student
from ui.Ui_Teacher import Ui_Teacher


class CommonMethod(QWidget):
    """
    CommonMethod is a class containing all the public methods
    for all windows, for example, method for adapting size.
    """
    def sizeAdapt(self, rate, isFixed=False):
        desktop = QApplication.desktop()
        if isFixed:
            self.setFixedSize(desktop.width() * rate, desktop.height() * rate)
        else:
            self.resize(desktop.width() * rate, desktop.height() * rate)


class Login(QMainWindow, CommonMethod):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Login()
        self.ui.setupUi(self)

    # def loginAndSwitch(self):
    #     userId = self.accLineEdit.text()
    #     password = self.pswLineEdit.text()
    #     data = DBManager("./data/db.sqlite3")
    #     if data.isPasswordCorrect(userId, password):
    #         isTeacher = data.getTypeById(userId)
    #         if isTeacher:
    #             self.subForm = FramelessWindow(TeacherForm())
    #         else:
    #             self.subForm = FramelessWindow(StudentForm())
    #         self.subForm.show()
    #     else:
    #         QMessageBox.information(self, "CEESS-提示", "用户名或密码错误!")

    # @Slot()
    # def on_loginButtom_clicked(self):
    #     self.loginAndSwitch()


class Student(QMainWindow, CommonMethod):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Student()
        self.ui.setupUi(self)


class Teacher(QMainWindow, CommonMethod):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Teacher()
        self.ui.setupUi(self)
