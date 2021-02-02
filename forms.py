from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QMessageBox
from PyQt5.QtGui import QIcon
from ui.Ui_Login import Ui_Login
from ui.Ui_Student import Ui_Student
from ui.Ui_Teacher import Ui_Teacher
from dataManager import DBManager


class QWidgetCommon(QWidget):
    def sizeAdapt(self, rate, isFixed):
        desktop = QApplication.desktop()
        if isFixed:
            self.setFixedSize(desktop.width() * rate, desktop.height() * rate)
        else:
            self.resize(desktop.width() * rate, desktop.height() * rate)


class LoginForm(Ui_Login, QWidgetCommon):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.sizeAdapt(0.2, True)
        self.setWindowIcon(QIcon("./source/icon/title.ico"))
        self.subForm = None
        # Signal slots.
        self.loginButtom.clicked.connect(self.loginAndSwitch)

    def loginAndSwitch(self):
        userId = self.LineEdit_Account.text()
        password = self.lineEdit_Password.text()
        data = DBManager("./data/db.sqlite3")
        if data.isPasswordCorrect(userId, password):
            isTeacher = data.getTypeById(userId)
            if isTeacher:
                self.subForm = TeacherForm()
            else:
                self.subForm = StudentForm()
            self.subForm.show()
           # self.close()
        else:
            QMessageBox.information(self, "CEESS-提示", "用户名或密码错误!")


class StudentForm(Ui_Student, QWidgetCommon):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # Signal slots.


class TeacherForm(Ui_Teacher, QWidgetCommon):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # Signal slots.
